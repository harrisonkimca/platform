"""Provider contracts for passwordless authentication workflows."""

from dataclasses import dataclass
from typing import Protocol

from platform_api.contexts.identity.domain.value_objects.credential_subject import (
    EmailCredentialSubject,
    OAuthCredentialSubject,
    PasskeyCredentialSubject,
)
from platform_api.contexts.identity.domain.value_objects.email_address import EmailAddress
from platform_api.contexts.identity.domain.value_objects.passkey import PasskeyCredentialId
from platform_api.contexts.identity.domain.value_objects.provider_identity import ProviderName
from platform_api.contexts.identity.domain.value_objects.recovery_channel import RecoveryChannel


def _ensure_non_empty(value: str, name: str) -> None:
    if value.strip() == "":
        msg = f"{name} must not be empty"
        raise ValueError(msg)


@dataclass(frozen=True, slots=True)
class EmailOtpChallengeRequest:
    """Request to issue an email OTP challenge."""

    email: EmailAddress


@dataclass(frozen=True, slots=True)
class EmailOtpVerificationRequest:
    """Request to verify an email OTP challenge."""

    email: EmailAddress
    code: str

    def __post_init__(self) -> None:
        _ensure_non_empty(self.code, "EmailOtpVerificationRequest.code")


@dataclass(frozen=True, slots=True)
class VerifiedEmailOtp:
    """Verified email OTP provider result."""

    subject: EmailCredentialSubject


@dataclass(frozen=True, slots=True)
class OAuthVerificationRequest:
    """Request to verify an OAuth/OIDC callback response."""

    provider_name: ProviderName
    authorization_response: str

    def __post_init__(self) -> None:
        _ensure_non_empty(
            self.authorization_response,
            "OAuthVerificationRequest.authorization_response",
        )


@dataclass(frozen=True, slots=True)
class VerifiedOAuthIdentity:
    """Verified OAuth provider result with a verified email identity."""

    subject: OAuthCredentialSubject
    email: EmailAddress


@dataclass(frozen=True, slots=True)
class PasskeyAssertionVerificationRequest:
    """Request to verify a WebAuthn passkey assertion."""

    passkey_credential_id: PasskeyCredentialId
    assertion_response: str

    def __post_init__(self) -> None:
        _ensure_non_empty(
            self.assertion_response,
            "PasskeyAssertionVerificationRequest.assertion_response",
        )


@dataclass(frozen=True, slots=True)
class VerifiedPasskeyAssertion:
    """Verified passkey assertion provider result."""

    subject: PasskeyCredentialSubject


@dataclass(frozen=True, slots=True)
class RecoveryVerificationRequest:
    """Request to verify an account recovery challenge."""

    channel: RecoveryChannel
    verification_response: str

    def __post_init__(self) -> None:
        _ensure_non_empty(
            self.verification_response,
            "RecoveryVerificationRequest.verification_response",
        )


@dataclass(frozen=True, slots=True)
class VerifiedRecovery:
    """Verified recovery provider result."""

    channel: RecoveryChannel


class EmailOtpProvider(Protocol):
    """Contract for issuing and verifying email OTP challenges."""

    async def send_challenge(self, request: EmailOtpChallengeRequest) -> None:
        """Issue an OTP challenge for the email address."""
        ...

    async def verify_otp(self, request: EmailOtpVerificationRequest) -> VerifiedEmailOtp:
        """Verify an OTP challenge for the email address."""
        ...


class OAuthIdentityProvider(Protocol):
    """Contract for verifying OAuth/OIDC provider responses."""

    async def verify_identity(self, request: OAuthVerificationRequest) -> VerifiedOAuthIdentity:
        """Verify an OAuth/OIDC response and return a verified identity."""
        ...


class PasskeyAssertionProvider(Protocol):
    """Contract for verifying WebAuthn passkey assertions."""

    async def verify_assertion(
        self,
        request: PasskeyAssertionVerificationRequest,
    ) -> VerifiedPasskeyAssertion:
        """Verify a passkey assertion response."""
        ...


class RecoveryProvider(Protocol):
    """Contract for verifying account recovery challenges."""

    async def verify_recovery(self, request: RecoveryVerificationRequest) -> VerifiedRecovery:
        """Verify a recovery challenge response."""
        ...
