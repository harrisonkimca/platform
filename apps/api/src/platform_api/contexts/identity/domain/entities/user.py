"""User domain entity."""

from dataclasses import dataclass
from datetime import UTC, datetime

from platform_api.contexts.identity.domain.types import UserStatus
from platform_api.contexts.identity.domain.value_objects.identifiers import UserId
from platform_api.contexts.identity.domain.value_objects.token_version import TokenVersion


@dataclass(slots=True)
class User:
    """Passwordless identity user aggregate root."""

    id: UserId
    status: UserStatus
    token_version: TokenVersion
    created_at: datetime

    def __post_init__(self) -> None:
        if self.created_at.tzinfo is None:
            msg = "User.created_at must be timezone-aware"
            raise ValueError(msg)

        self.created_at = self.created_at.astimezone(UTC)
