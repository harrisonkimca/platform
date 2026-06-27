"""Authentication challenge domain entity."""

from dataclasses import dataclass
from datetime import UTC, datetime

from platform_api.contexts.identity.domain.types import (
    AuthChallengeKind,
    AuthChallengeStatus,
)
from platform_api.contexts.identity.domain.value_objects.identifiers import AuthChallengeId, UserId


@dataclass(slots=True)
class AuthChallenge:
    """Temporary authentication challenge entity."""

    id: AuthChallengeId
    kind: AuthChallengeKind
    status: AuthChallengeStatus
    expires_at: datetime
    attempt_count: int = 0
    user_id: UserId | None = None

    def __post_init__(self) -> None:
        if self.expires_at.tzinfo is None:
            msg = "AuthChallenge.expires_at must be timezone-aware"
            raise ValueError(msg)

        if self.attempt_count < 0:
            msg = "AuthChallenge.attempt_count must not be negative"
            raise ValueError(msg)

        self.expires_at = self.expires_at.astimezone(UTC)
