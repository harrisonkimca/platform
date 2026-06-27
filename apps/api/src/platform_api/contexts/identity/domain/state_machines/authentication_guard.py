"""Authentication state-machine guard contracts."""

from typing import Protocol

from platform_api.contexts.identity.domain.state_machines.authentication_transition import (
    AuthenticationTransition,
)


class AuthenticationGuard(Protocol):
    """Contract for checking whether a transition is currently allowed."""

    def allows(self, transition: AuthenticationTransition) -> bool:
        """Return whether the transition satisfies the guard."""
        ...
