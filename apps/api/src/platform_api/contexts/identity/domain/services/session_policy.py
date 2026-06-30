"""Authentication session policy domain service contract."""

from typing import Protocol

from platform_api.contexts.identity.domain.types import AuthSessionStatus, AuthTrustLevel


class SessionPolicy(Protocol):
    """Contract for session lifecycle and trust decisions."""

    def can_refresh(self, status: AuthSessionStatus, trust_level: AuthTrustLevel) -> bool:
        """Return whether a session may be refreshed."""
        ...

    def can_revoke(self, status: AuthSessionStatus) -> bool:
        """Return whether a session may be revoked."""
        ...
