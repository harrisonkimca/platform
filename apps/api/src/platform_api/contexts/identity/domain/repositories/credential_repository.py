"""Credential repository contract."""

from __future__ import annotations

from typing import Protocol, TypeVar

from platform_api.contexts.identity.domain.value_objects.identifiers import CredentialId, UserId

CredentialT = TypeVar("CredentialT")


class CredentialRepository(Protocol[CredentialT]):
    """Persistence contract for credential aggregates."""

    async def get_by_id(self, credential_id: CredentialId) -> CredentialT | None:
        """Return a credential by identifier, if one exists."""
        ...

    async def list_by_user_id(self, user_id: UserId) -> tuple[CredentialT, ...]:
        """Return credentials owned by a user."""
        ...

    async def add(self, credential: CredentialT) -> None:
        """Add a credential to the repository."""
        ...

    async def remove(self, credential: CredentialT) -> None:
        """Remove a credential from the repository."""
        ...
