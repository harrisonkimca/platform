"""Authentication policy domain service contract."""

from typing import Protocol

from platform_api.contexts.identity.domain.types import AuthTrustLevel


class AuthenticationPolicy(Protocol):
    """Contract for authentication trust and step-up decisions."""

    def requires_step_up(self, trust_level: AuthTrustLevel, action: str) -> bool:
        """Return whether an action requires step-up authentication."""
        ...
