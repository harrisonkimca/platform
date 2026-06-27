"""Shared identity domain type definitions."""

from enum import StrEnum


class AuthChallengeKind(StrEnum):
    """Supported authentication challenge categories."""

    EMAIL_OTP = "email_otp"
    OAUTH = "oauth"
    PASSKEY_ASSERTION = "passkey_assertion"
    PASSKEY_REGISTRATION = "passkey_registration"
    STEP_UP = "step_up"
    RECOVERY = "recovery"


class AuthChallengeStatus(StrEnum):
    """Lifecycle states for temporary authentication challenges."""

    PENDING = "pending"
    VERIFIED = "verified"
    FAILED = "failed"
    EXPIRED = "expired"


class AuthenticationState(StrEnum):
    """High-level states used by authentication state machines."""

    UNAUTHENTICATED = "unauthenticated"
    CHALLENGE_PENDING = "challenge_pending"
    AUTHENTICATED = "authenticated"
    STEP_UP_REQUIRED = "step_up_required"
    STEP_UP_VERIFIED = "step_up_verified"
    RECOVERY_PENDING = "recovery_pending"


class AuthenticationTrigger(StrEnum):
    """Triggers that may cause authentication state transitions."""

    EMAIL_SUBMITTED = "email_submitted"
    OTP_VERIFIED = "otp_verified"
    OAUTH_VERIFIED = "oauth_verified"
    PASSKEY_ASSERTED = "passkey_asserted"
    STEP_UP_REQUIRED = "step_up_required"
    STEP_UP_VERIFIED = "step_up_verified"
    RECOVERY_REQUESTED = "recovery_requested"
    RECOVERY_VERIFIED = "recovery_verified"


class AuthSessionStatus(StrEnum):
    """Lifecycle states for authenticated sessions."""

    ACTIVE = "active"
    REVOKED = "revoked"
    EXPIRED = "expired"


class AuthTrustLevel(StrEnum):
    """Trust tier associated with an authenticated session."""

    LOW = "low"
    STANDARD = "standard"
    FRESH_PASSKEY = "fresh_passkey"


class CredentialKind(StrEnum):
    """Supported credential categories for passwordless identity."""

    EMAIL_OTP = "email_otp"
    GOOGLE_OAUTH = "google_oauth"
    APPLE_OAUTH = "apple_oauth"
    PASSKEY = "passkey"
    BACKUP_EMAIL = "backup_email"


class CredentialStatus(StrEnum):
    """Lifecycle states for credentials."""

    PENDING_VERIFICATION = "pending_verification"
    ACTIVE = "active"
    REVOKED = "revoked"


class UserStatus(StrEnum):
    """Lifecycle states for identity users."""

    ACTIVE = "active"
    SUSPENDED = "suspended"
    CLOSED = "closed"
