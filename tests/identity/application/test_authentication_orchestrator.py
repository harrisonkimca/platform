"""Tests for authentication application orchestration."""

import asyncio
from dataclasses import dataclass, field

import pytest

from platform_api.contexts.identity.application.authentication_orchestrator import (
    AuthenticationOrchestrator,
)
from platform_api.contexts.identity.application.ports.authentication_providers import (
    EmailOtpChallengeRequest,
    EmailOtpVerificationRequest,
    OAuthVerificationRequest,
    PasskeyAssertionVerificationRequest,
    RecoveryVerificationRequest,
    VerifiedEmailOtp,
    VerifiedOAuthIdentity,
    VerifiedPasskeyAssertion,
    VerifiedRecovery,
)
from platform_api.contexts.identity.domain.state_machines.authentication_transition import (
    InvalidAuthenticationTransition,
)
from platform_api.contexts.identity.domain.types import (
    AuthenticationState,
    AuthTrustLevel,
)
from platform_api.contexts.identity.domain.value_objects.credential_subject import (
    EmailCredentialSubject,
    OAuthCredentialSubject,
    PasskeyCredentialSubject,
)
from platform_api.contexts.identity.domain.value_objects.email_address import EmailAddress
from platform_api.contexts.identity.domain.value_objects.passkey import PasskeyCredentialId
from platform_api.contexts.identity.domain.value_objects.provider_identity import (
    ProviderIdentity,
    ProviderName,
    ProviderSubject,
)
from platform_api.contexts.identity.domain.value_objects.recovery_channel import (
    EmailRecoveryChannel,
)


def _email_otp_challenge_requests() -> list[EmailOtpChallengeRequest]:
    return []


def _email_otp_verification_requests() -> list[EmailOtpVerificationRequest]:
    return []


def _oauth_verification_requests() -> list[OAuthVerificationRequest]:
    return []


def _passkey_assertion_verification_requests() -> list[PasskeyAssertionVerificationRequest]:
    return []


def _recovery_verification_requests() -> list[RecoveryVerificationRequest]:
    return []


@dataclass(slots=True)
class FakeEmailOtpProvider:
    """Fake email OTP provider for orchestration tests."""

    sent_requests: list[EmailOtpChallengeRequest] = field(
        default_factory=_email_otp_challenge_requests,
    )
    verification_requests: list[EmailOtpVerificationRequest] = field(
        default_factory=_email_otp_verification_requests,
    )

    async def send_challenge(self, request: EmailOtpChallengeRequest) -> None:
        self.sent_requests.append(request)

    async def verify_otp(self, request: EmailOtpVerificationRequest) -> VerifiedEmailOtp:
        self.verification_requests.append(request)
        return VerifiedEmailOtp(subject=EmailCredentialSubject(email=request.email))


@dataclass(slots=True)
class FakeOAuthIdentityProvider:
    """Fake OAuth provider for orchestration tests."""

    verification_requests: list[OAuthVerificationRequest] = field(
        default_factory=_oauth_verification_requests,
    )

    async def verify_identity(self, request: OAuthVerificationRequest) -> VerifiedOAuthIdentity:
        self.verification_requests.append(request)
        provider_identity = ProviderIdentity(
            provider_name=request.provider_name,
            subject=ProviderSubject("provider-subject"),
        )
        return VerifiedOAuthIdentity(
            subject=OAuthCredentialSubject(provider_identity=provider_identity),
            email=EmailAddress("oauth@example.com"),
        )


@dataclass(slots=True)
class FakePasskeyAssertionProvider:
    """Fake passkey assertion provider for orchestration tests."""

    verification_requests: list[PasskeyAssertionVerificationRequest] = field(
        default_factory=_passkey_assertion_verification_requests,
    )

    async def verify_assertion(
        self,
        request: PasskeyAssertionVerificationRequest,
    ) -> VerifiedPasskeyAssertion:
        self.verification_requests.append(request)
        return VerifiedPasskeyAssertion(
            subject=PasskeyCredentialSubject(
                passkey_credential_id=request.passkey_credential_id,
            ),
        )


@dataclass(slots=True)
class FakeRecoveryProvider:
    """Fake recovery provider for orchestration tests."""

    verification_requests: list[RecoveryVerificationRequest] = field(
        default_factory=_recovery_verification_requests,
    )

    async def verify_recovery(self, request: RecoveryVerificationRequest) -> VerifiedRecovery:
        self.verification_requests.append(request)
        return VerifiedRecovery(channel=request.channel)


def test_authentication_orchestrator_coordinates_email_otp_workflow() -> None:
    email_provider = FakeEmailOtpProvider()
    orchestrator = _orchestrator(email_provider=email_provider)
    email = EmailAddress("User@Example.com")

    async def run() -> None:
        challenge_result = await orchestrator.request_email_otp(
            AuthenticationState.UNAUTHENTICATED,
            email,
        )

        assert challenge_result.transition.next_state is AuthenticationState.CHALLENGE_PENDING
        assert challenge_result.trust_level is None
        assert email_provider.sent_requests == [EmailOtpChallengeRequest(email=email)]

        verification_result = await orchestrator.verify_email_otp(
            AuthenticationState.CHALLENGE_PENDING,
            email,
            "123456",
        )

        assert verification_result.transition.next_state is AuthenticationState.AUTHENTICATED
        assert verification_result.trust_level is AuthTrustLevel.LOW
        assert verification_result.credential_subject == EmailCredentialSubject(email=email)

    asyncio.run(run())


def test_authentication_orchestrator_coordinates_oauth_and_passkey_workflows() -> None:
    oauth_provider = FakeOAuthIdentityProvider()
    passkey_provider = FakePasskeyAssertionProvider()
    orchestrator = _orchestrator(
        oauth_provider=oauth_provider,
        passkey_provider=passkey_provider,
    )
    provider_name = ProviderName("google")
    passkey_credential_id = PasskeyCredentialId("passkey-id")

    async def run() -> None:
        oauth_result = await orchestrator.verify_oauth_identity(
            AuthenticationState.UNAUTHENTICATED,
            provider_name,
            "authorization-response",
        )

        assert oauth_result.transition.next_state is AuthenticationState.AUTHENTICATED
        assert oauth_result.trust_level is AuthTrustLevel.STANDARD
        assert len(oauth_provider.verification_requests) == 1

        passkey_login_result = await orchestrator.verify_passkey_assertion(
            AuthenticationState.UNAUTHENTICATED,
            passkey_credential_id,
            "assertion-response",
        )

        assert passkey_login_result.transition.next_state is AuthenticationState.AUTHENTICATED
        assert passkey_login_result.trust_level is AuthTrustLevel.FRESH_PASSKEY

        step_up_result = orchestrator.require_step_up(AuthenticationState.AUTHENTICATED)
        assert step_up_result.transition.next_state is AuthenticationState.STEP_UP_REQUIRED

        passkey_step_up_result = await orchestrator.verify_passkey_assertion(
            AuthenticationState.STEP_UP_REQUIRED,
            passkey_credential_id,
            "fresh-assertion-response",
        )

        assert passkey_step_up_result.transition.next_state is AuthenticationState.STEP_UP_VERIFIED
        assert passkey_step_up_result.trust_level is AuthTrustLevel.FRESH_PASSKEY
        assert len(passkey_provider.verification_requests) == 2

    asyncio.run(run())


def test_authentication_orchestrator_coordinates_recovery_workflow() -> None:
    recovery_provider = FakeRecoveryProvider()
    orchestrator = _orchestrator(recovery_provider=recovery_provider)
    channel = EmailRecoveryChannel(email=EmailAddress("recovery@example.com"))

    async def run() -> None:
        recovery_request_result = orchestrator.request_recovery(
            AuthenticationState.UNAUTHENTICATED,
        )

        assert recovery_request_result.transition.next_state is AuthenticationState.RECOVERY_PENDING

        recovery_result = await orchestrator.verify_recovery(
            AuthenticationState.RECOVERY_PENDING,
            channel,
            "recovery-response",
        )

        assert recovery_result.transition.next_state is AuthenticationState.AUTHENTICATED
        assert recovery_result.trust_level is AuthTrustLevel.STANDARD
        assert recovery_result.recovery_channel == channel
        assert len(recovery_provider.verification_requests) == 1

    asyncio.run(run())


def test_authentication_orchestrator_rejects_invalid_workflow_before_provider_call() -> None:
    email_provider = FakeEmailOtpProvider()
    orchestrator = _orchestrator(email_provider=email_provider)

    async def run() -> None:
        with pytest.raises(InvalidAuthenticationTransition):
            await orchestrator.verify_email_otp(
                AuthenticationState.UNAUTHENTICATED,
                EmailAddress("user@example.com"),
                "123456",
            )

    asyncio.run(run())

    assert email_provider.verification_requests == []


def _orchestrator(
    *,
    email_provider: FakeEmailOtpProvider | None = None,
    oauth_provider: FakeOAuthIdentityProvider | None = None,
    passkey_provider: FakePasskeyAssertionProvider | None = None,
    recovery_provider: FakeRecoveryProvider | None = None,
) -> AuthenticationOrchestrator:
    return AuthenticationOrchestrator(
        email_otp_provider=email_provider or FakeEmailOtpProvider(),
        oauth_identity_provider=oauth_provider or FakeOAuthIdentityProvider(),
        passkey_assertion_provider=passkey_provider or FakePasskeyAssertionProvider(),
        recovery_provider=recovery_provider or FakeRecoveryProvider(),
    )
