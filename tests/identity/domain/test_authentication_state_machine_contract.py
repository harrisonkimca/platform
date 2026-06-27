"""Authentication state-machine contract tests."""

from dataclasses import FrozenInstanceError

import pytest

from platform_api.contexts.identity.domain.state_machines.authentication_guard import (
    AuthenticationGuard,
)
from platform_api.contexts.identity.domain.state_machines.authentication_state_machine import (
    AuthenticationStateMachine,
)
from platform_api.contexts.identity.domain.state_machines.authentication_transition import (
    AuthenticationTransition,
)
from platform_api.contexts.identity.domain.types import AuthenticationState, AuthenticationTrigger


class AllowAllGuard:
    """Test double for the authentication guard contract."""

    def allows(self, transition: AuthenticationTransition) -> bool:
        return transition.current_state is not transition.next_state


class StaticAuthenticationStateMachine:
    """Test double for the authentication state-machine contract."""

    def can_transition(
        self,
        current_state: AuthenticationState,
        trigger: AuthenticationTrigger,
    ) -> bool:
        return trigger is AuthenticationTrigger.EMAIL_SUBMITTED

    def transition_for(
        self,
        current_state: AuthenticationState,
        trigger: AuthenticationTrigger,
    ) -> AuthenticationTransition:
        return AuthenticationTransition(
            current_state=current_state,
            trigger=trigger,
            next_state=self.next_state_for(current_state, trigger),
        )

    def next_state_for(
        self,
        current_state: AuthenticationState,
        trigger: AuthenticationTrigger,
    ) -> AuthenticationState:
        if trigger is AuthenticationTrigger.EMAIL_SUBMITTED:
            return AuthenticationState.CHALLENGE_PENDING

        return current_state


def test_authentication_transition_is_immutable() -> None:
    transition = AuthenticationTransition(
        current_state=AuthenticationState.UNAUTHENTICATED,
        trigger=AuthenticationTrigger.EMAIL_SUBMITTED,
        next_state=AuthenticationState.CHALLENGE_PENDING,
    )

    with pytest.raises(FrozenInstanceError):
        transition.__setattr__("next_state", AuthenticationState.AUTHENTICATED)


def test_authentication_guard_contract_accepts_transition() -> None:
    guard: AuthenticationGuard = AllowAllGuard()
    transition = AuthenticationTransition(
        current_state=AuthenticationState.UNAUTHENTICATED,
        trigger=AuthenticationTrigger.EMAIL_SUBMITTED,
        next_state=AuthenticationState.CHALLENGE_PENDING,
    )

    assert guard.allows(transition) is True


def test_authentication_state_machine_contract_uses_triggers() -> None:
    state_machine: AuthenticationStateMachine = StaticAuthenticationStateMachine()

    assert (
        state_machine.can_transition(
            AuthenticationState.UNAUTHENTICATED,
            AuthenticationTrigger.EMAIL_SUBMITTED,
        )
        is True
    )
    assert (
        state_machine.next_state_for(
            AuthenticationState.UNAUTHENTICATED,
            AuthenticationTrigger.EMAIL_SUBMITTED,
        )
        is AuthenticationState.CHALLENGE_PENDING
    )
    assert state_machine.transition_for(
        AuthenticationState.UNAUTHENTICATED,
        AuthenticationTrigger.EMAIL_SUBMITTED,
    ) == AuthenticationTransition(
        current_state=AuthenticationState.UNAUTHENTICATED,
        trigger=AuthenticationTrigger.EMAIL_SUBMITTED,
        next_state=AuthenticationState.CHALLENGE_PENDING,
    )
