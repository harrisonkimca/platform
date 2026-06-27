"""Tests for identity user repository contracts."""

from __future__ import annotations

import asyncio
import inspect
from dataclasses import dataclass
from uuid import uuid4

from platform_api.contexts.identity.domain.repositories.user_repository import UserRepository
from platform_api.contexts.identity.domain.value_objects.identifiers import UserId


@dataclass(frozen=True, slots=True)
class UserRecord:
    id: UserId


class InMemoryUserRepository(UserRepository[UserRecord]):
    """Contract test double for the identity user repository."""

    def __init__(self) -> None:
        self._users: dict[UserId, UserRecord] = {}

    async def get_by_id(self, user_id: UserId) -> UserRecord | None:
        return self._users.get(user_id)

    async def add(self, user: UserRecord) -> None:
        self._users[user.id] = user

    async def remove(self, user: UserRecord) -> None:
        self._users.pop(user.id, None)


def test_user_repository_contract_is_intentionally_small_and_async() -> None:
    public_methods = {
        name
        for name, value in vars(UserRepository).items()
        if not name.startswith("_") and callable(value)
    }

    assert public_methods == {"get_by_id", "add", "remove"}

    for method_name in public_methods:
        assert inspect.iscoroutinefunction(getattr(UserRepository, method_name))


def test_user_repository_contract_supports_add_get_and_remove() -> None:
    repository = InMemoryUserRepository()
    user = UserRecord(id=UserId(uuid4()))

    async def run() -> None:
        assert await repository.get_by_id(user.id) is None

        await repository.add(user)
        assert await repository.get_by_id(user.id) == user

        await repository.remove(user)
        assert await repository.get_by_id(user.id) is None

    asyncio.run(run())
