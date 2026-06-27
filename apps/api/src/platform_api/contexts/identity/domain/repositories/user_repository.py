"""Identity user repository contract."""

from __future__ import annotations

from typing import Protocol, TypeVar

from platform_api.contexts.identity.domain.value_objects.identifiers import UserId

UserT = TypeVar("UserT")


class UserRepository(Protocol[UserT]):
    """Persistence contract for identity users."""

    async def get_by_id(self, user_id: UserId) -> UserT | None:
        """Return a user by identifier, if one exists."""
        ...

    async def add(self, user: UserT) -> None:
        """Add a user to the repository."""
        ...

    async def remove(self, user: UserT) -> None:
        """Remove a user from the repository."""
        ...
