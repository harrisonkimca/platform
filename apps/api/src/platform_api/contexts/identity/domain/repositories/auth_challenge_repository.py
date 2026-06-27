"""Authentication challenge repository contract."""

from __future__ import annotations

from typing import Protocol, TypeVar

from platform_api.contexts.identity.domain.value_objects.identifiers import AuthChallengeId

AuthChallengeT = TypeVar("AuthChallengeT")


class AuthChallengeRepository(Protocol[AuthChallengeT]):
    """Persistence contract for authentication challenge aggregates."""

    async def get_by_id(self, challenge_id: AuthChallengeId) -> AuthChallengeT | None:
        """Return a challenge by identifier, if one exists."""
        ...

    async def add(self, challenge: AuthChallengeT) -> None:
        """Add a challenge to the repository."""
        ...

    async def remove(self, challenge: AuthChallengeT) -> None:
        """Remove a challenge from the repository."""
        ...
