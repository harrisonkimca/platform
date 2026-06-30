"""Authentication state-machine guard contracts."""

from collections.abc import Iterable
from typing import Protocol

from platform_api.contexts.identity.domain.state_machines.authentication_state_machine import (
    AuthenticationStateMachine,
)
from platform_api.contexts.identity.domain.state_machines.authentication_transition import (
    AuthenticationTransition,
    InvalidAuthenticationTransition,
)


class AuthenticationGuard(Protocol):
    """Contract for checking whether a transition is currently allowed."""

    def allows(self, transition: AuthenticationTransition) -> bool:
        """Return whether the transition satisfies the guard."""
        ...


class StateMachineAuthenticationGuard:
    """Guard that allows only transitions recognized by a state machine."""

    def __init__(self, state_machine: AuthenticationStateMachine) -> None:
        self._state_machine = state_machine

    def allows(self, transition: AuthenticationTransition) -> bool:
        """Return whether the transition matches the configured state machine."""
        try:
            expected_transition = self._state_machine.transition_for(
                transition.current_state,
                transition.trigger,
            )
        except InvalidAuthenticationTransition:
            return False

        return transition == expected_transition


class CompositeAuthenticationGuard:
    """Guard that requires every nested guard to allow the transition."""

    def __init__(self, guards: Iterable[AuthenticationGuard]) -> None:
        self._guards = tuple(guards)

    def allows(self, transition: AuthenticationTransition) -> bool:
        """Return whether all nested guards allow the transition."""
        return all(guard.allows(transition) for guard in self._guards)
