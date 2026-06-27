"""Authentication session repository contract."""

from __future__ import annotations

from typing import Protocol, TypeVar

from platform_api.contexts.identity.domain.value_objects.identifiers import AuthSessionId, UserId

AuthSessionT = TypeVar("AuthSessionT")


class AuthSessionRepository(Protocol[AuthSessionT]):
    """Persistence contract for authentication session aggregates."""

    async def get_by_id(self, session_id: AuthSessionId) -> AuthSessionT | None:
        """Return a session by identifier, if one exists."""
        ...

    async def list_active_by_user_id(self, user_id: UserId) -> tuple[AuthSessionT, ...]:
        """Return active sessions owned by a user."""
        ...

    async def add(self, session: AuthSessionT) -> None:
        """Add a session to the repository."""
        ...

    async def remove(self, session: AuthSessionT) -> None:
        """Remove a session from the repository."""
        ...
