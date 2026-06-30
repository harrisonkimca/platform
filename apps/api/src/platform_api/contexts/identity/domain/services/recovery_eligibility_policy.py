"""Recovery eligibility policy domain service contract."""

from typing import Protocol

from platform_api.contexts.identity.domain.types import RecoveryTier, UserStatus
from platform_api.contexts.identity.domain.value_objects.recovery_channel import RecoveryChannel


class RecoveryEligibilityPolicy(Protocol):
    """Contract for account recovery eligibility decisions."""

    def is_eligible(
        self,
        user_status: UserStatus,
        tier: RecoveryTier,
        channel: RecoveryChannel,
    ) -> bool:
        """Return whether recovery is allowed for the user, tier, and channel."""
        ...

    def requires_step_up(self, tier: RecoveryTier, channel: RecoveryChannel) -> bool:
        """Return whether recovery through the channel requires step-up checks."""
        ...
