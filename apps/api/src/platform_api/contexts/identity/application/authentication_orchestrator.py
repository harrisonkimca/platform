"""Application orchestration for authentication provider workflows."""

from dataclasses import dataclass

from platform_api.contexts.identity.application.ports.authentication_providers import (
    EmailOtpChallengeRequest,
    EmailOtpProvider,
    EmailOtpVerificationRequest,
    OAuthIdentityProvider,
    OAuthVerificationRequest,
    PasskeyAssertionProvider,
    PasskeyAssertionVerificationRequest,
    RecoveryProvider,
    RecoveryVerificationRequest,
)
from platform_api.contexts.identity.domain.services.authentication_trust import (
    AuthenticationTrustResolver,
    DefaultAuthenticationTrustResolver,
)
from platform_api.contexts.identity.domain.state_machines.authentication_state_machine import (
    AuthenticationStateMachine,
    DefaultAuthenticationStateMachine,
)
from platform_api.contexts.identity.domain.state_machines.authentication_transition import (
    AuthenticationTransition,
)
from platform_api.contexts.identity.domain.types import (
    AuthenticationState,
    AuthenticationTrigger,
    AuthTrustLevel,
)
from platform_api.contexts.identity.domain.value_objects.credential_subject import CredentialSubject
from platform_api.contexts.identity.domain.value_objects.email_address import EmailAddress
from platform_api.contexts.identity.domain.value_objects.passkey import PasskeyCredentialId
from platform_api.contexts.identity.domain.value_objects.provider_identity import ProviderName
from platform_api.contexts.identity.domain.value_objects.recovery_channel import RecoveryChannel


@dataclass(frozen=True, slots=True)
class AuthenticationWorkflowResult:
    """Result of applying an authentication workflow transition."""

    transition: AuthenticationTransition
    trust_level: AuthTrustLevel | None = None
    credential_subject: CredentialSubject | None = None
    recovery_channel: RecoveryChannel | None = None


class AuthenticationOrchestrator:
    """Coordinates provider verification with domain authentication transitions."""

    def __init__(
        self,
        *,
        email_otp_provider: EmailOtpProvider,
        oauth_identity_provider: OAuthIdentityProvider,
        passkey_assertion_provider: PasskeyAssertionProvider,
        recovery_provider: RecoveryProvider,
        state_machine: AuthenticationStateMachine | None = None,
        trust_resolver: AuthenticationTrustResolver | None = None,
    ) -> None:
        self._email_otp_provider = email_otp_provider
        self._oauth_identity_provider = oauth_identity_provider
        self._passkey_assertion_provider = passkey_assertion_provider
        self._recovery_provider = recovery_provider
        self._state_machine = state_machine or DefaultAuthenticationStateMachine()
        self._trust_resolver = trust_resolver or DefaultAuthenticationTrustResolver()

    async def request_email_otp(
        self,
        current_state: AuthenticationState,
        email: EmailAddress,
    ) -> AuthenticationWorkflowResult:
        """Issue an email OTP challenge and move into challenge-pending state."""
        transition = self._transition_for(
            current_state,
            AuthenticationTrigger.EMAIL_SUBMITTED,
        )
        await self._email_otp_provider.send_challenge(EmailOtpChallengeRequest(email=email))
        return self._result_for(transition)

    async def verify_email_otp(
        self,
        current_state: AuthenticationState,
        email: EmailAddress,
        code: str,
    ) -> AuthenticationWorkflowResult:
        """Verify an email OTP and authenticate at the email-OTP trust tier."""
        transition = self._transition_for(
            current_state,
            AuthenticationTrigger.OTP_VERIFIED,
        )
        verified = await self._email_otp_provider.verify_otp(
            EmailOtpVerificationRequest(email=email, code=code),
        )
        return self._result_for(transition, credential_subject=verified.subject)

    async def verify_oauth_identity(
        self,
        current_state: AuthenticationState,
        provider_name: ProviderName,
        authorization_response: str,
    ) -> AuthenticationWorkflowResult:
        """Verify an OAuth/OIDC response and authenticate the workflow."""
        transition = self._transition_for(
            current_state,
            AuthenticationTrigger.OAUTH_VERIFIED,
        )
        verified = await self._oauth_identity_provider.verify_identity(
            OAuthVerificationRequest(
                provider_name=provider_name,
                authorization_response=authorization_response,
            ),
        )
        return self._result_for(transition, credential_subject=verified.subject)

    async def verify_passkey_assertion(
        self,
        current_state: AuthenticationState,
        passkey_credential_id: PasskeyCredentialId,
        assertion_response: str,
    ) -> AuthenticationWorkflowResult:
        """Verify a passkey assertion for login or fresh step-up."""
        transition = self._transition_for(
            current_state,
            AuthenticationTrigger.PASSKEY_ASSERTED,
        )
        verified = await self._passkey_assertion_provider.verify_assertion(
            PasskeyAssertionVerificationRequest(
                passkey_credential_id=passkey_credential_id,
                assertion_response=assertion_response,
            ),
        )
        return self._result_for(transition, credential_subject=verified.subject)

    def require_step_up(
        self,
        current_state: AuthenticationState,
    ) -> AuthenticationWorkflowResult:
        """Move an authenticated workflow into step-up-required state."""
        transition = self._transition_for(
            current_state,
            AuthenticationTrigger.STEP_UP_REQUIRED,
        )
        return self._result_for(transition)

    def request_recovery(
        self,
        current_state: AuthenticationState,
    ) -> AuthenticationWorkflowResult:
        """Move an eligible workflow into recovery-pending state."""
        transition = self._transition_for(
            current_state,
            AuthenticationTrigger.RECOVERY_REQUESTED,
        )
        return self._result_for(transition)

    async def verify_recovery(
        self,
        current_state: AuthenticationState,
        channel: RecoveryChannel,
        verification_response: str,
    ) -> AuthenticationWorkflowResult:
        """Verify a recovery challenge and return to authenticated state."""
        transition = self._transition_for(
            current_state,
            AuthenticationTrigger.RECOVERY_VERIFIED,
        )
        verified = await self._recovery_provider.verify_recovery(
            RecoveryVerificationRequest(
                channel=channel,
                verification_response=verification_response,
            ),
        )
        return self._result_for(transition, recovery_channel=verified.channel)

    def _transition_for(
        self,
        current_state: AuthenticationState,
        trigger: AuthenticationTrigger,
    ) -> AuthenticationTransition:
        return self._state_machine.transition_for(current_state, trigger)

    def _result_for(
        self,
        transition: AuthenticationTransition,
        *,
        credential_subject: CredentialSubject | None = None,
        recovery_channel: RecoveryChannel | None = None,
    ) -> AuthenticationWorkflowResult:
        return AuthenticationWorkflowResult(
            transition=transition,
            trust_level=self._trust_resolver.trust_level_for(transition.trigger),
            credential_subject=credential_subject,
            recovery_channel=recovery_channel,
        )
