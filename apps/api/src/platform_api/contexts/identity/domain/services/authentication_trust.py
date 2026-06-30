"""Authentication trust-level resolution."""

from typing import Protocol

from platform_api.contexts.identity.domain.types import AuthenticationTrigger, AuthTrustLevel


class AuthenticationTrustResolver(Protocol):
    """Contract for resolving trust level from successful authentication triggers."""

    def trust_level_for(self, trigger: AuthenticationTrigger) -> AuthTrustLevel | None:
        """Return the trust level established by a trigger, when one exists."""
        ...


class DefaultAuthenticationTrustResolver:
    """Default trust-level mapping for passwordless authentication workflows."""

    def trust_level_for(self, trigger: AuthenticationTrigger) -> AuthTrustLevel | None:
        """Return the trust level established by a trigger, when one exists."""
        match trigger:
            case AuthenticationTrigger.OTP_VERIFIED:
                return AuthTrustLevel.LOW
            case AuthenticationTrigger.OAUTH_VERIFIED | AuthenticationTrigger.RECOVERY_VERIFIED:
                return AuthTrustLevel.STANDARD
            case AuthenticationTrigger.PASSKEY_ASSERTED | AuthenticationTrigger.STEP_UP_VERIFIED:
                return AuthTrustLevel.FRESH_PASSKEY
            case _:
                return None
