"""Authentication state machine contract."""

from typing import Protocol

from platform_api.contexts.identity.domain.state_machines.authentication_transition import (
    AuthenticationTransition,
)
from platform_api.contexts.identity.domain.types import AuthenticationState, AuthenticationTrigger


class AuthenticationStateMachine(Protocol):
    """Contract for side-effect-free authentication state transitions."""

    def can_transition(
        self,
        current_state: AuthenticationState,
        trigger: AuthenticationTrigger,
    ) -> bool:
        """Return whether a trigger can be applied to the current state."""
        ...

    def transition_for(
        self,
        current_state: AuthenticationState,
        trigger: AuthenticationTrigger,
    ) -> AuthenticationTransition:
        """Return the transition produced by a trigger."""
        ...

    def next_state_for(
        self,
        current_state: AuthenticationState,
        trigger: AuthenticationTrigger,
    ) -> AuthenticationState:
        """Return the next authentication state for a trigger."""
        ...
