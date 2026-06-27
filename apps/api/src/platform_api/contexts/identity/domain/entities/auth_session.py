"""Authentication session domain entity."""

from dataclasses import dataclass
from datetime import UTC, datetime

from platform_api.contexts.identity.domain.types import (
    AuthSessionStatus,
    AuthTrustLevel,
)
from platform_api.contexts.identity.domain.value_objects.identifiers import (
    AuthSessionId,
    DeviceId,
    UserId,
)
from platform_api.contexts.identity.domain.value_objects.token_version import TokenVersion


@dataclass(slots=True)
class AuthSession:
    """Authenticated session or device session entity."""

    id: AuthSessionId
    user_id: UserId
    device_id: DeviceId
    status: AuthSessionStatus
    trust_level: AuthTrustLevel
    token_version: TokenVersion
    created_at: datetime
    expires_at: datetime

    def __post_init__(self) -> None:
        if self.created_at.tzinfo is None:
            msg = "AuthSession.created_at must be timezone-aware"
            raise ValueError(msg)

        if self.expires_at.tzinfo is None:
            msg = "AuthSession.expires_at must be timezone-aware"
            raise ValueError(msg)

        created_at = self.created_at.astimezone(UTC)
        expires_at = self.expires_at.astimezone(UTC)

        if expires_at <= created_at:
            msg = "AuthSession.expires_at must be after created_at"
            raise ValueError(msg)

        self.created_at = created_at
        self.expires_at = expires_at
