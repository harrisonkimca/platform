"""Authentication challenge policy domain service contract."""

from typing import Protocol

from platform_api.contexts.identity.domain.types import AuthChallengeKind, AuthChallengeStatus


class AuthChallengePolicy(Protocol):
    """Contract for challenge attempt and verification decisions."""

    def can_attempt(
        self,
        kind: AuthChallengeKind,
        status: AuthChallengeStatus,
        attempt_count: int,
    ) -> bool:
        """Return whether another challenge attempt is allowed."""
        ...

    def can_verify(
        self,
        kind: AuthChallengeKind,
        status: AuthChallengeStatus,
        attempt_count: int,
    ) -> bool:
        """Return whether a challenge is eligible for verification."""
        ...
