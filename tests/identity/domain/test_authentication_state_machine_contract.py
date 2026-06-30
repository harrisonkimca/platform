"""Authentication state-machine contract tests."""

from dataclasses import FrozenInstanceError

import pytest

from platform_api.contexts.identity.domain.services.authentication_trust import (
    DefaultAuthenticationTrustResolver,
)
from platform_api.contexts.identity.domain.state_machines.authentication_guard import (
    AuthenticationGuard,
    CompositeAuthenticationGuard,
    StateMachineAuthenticationGuard,
)
from platform_api.contexts.identity.domain.state_machines.authentication_state_machine import (
    AuthenticationStateMachine,
    DefaultAuthenticationStateMachine,
)
from platform_api.contexts.identity.domain.state_machines.authentication_transition import (
    AuthenticationTransition,
    InvalidAuthenticationTransition,
)
from platform_api.contexts.identity.domain.types import (
    AuthenticationState,
    AuthenticationTrigger,
    AuthTrustLevel,
)


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


def test_default_authentication_state_machine_supports_passwordless_workflows() -> None:
    state_machine = DefaultAuthenticationStateMachine()
    cases = (
        (
            AuthenticationState.UNAUTHENTICATED,
            AuthenticationTrigger.EMAIL_SUBMITTED,
            AuthenticationState.CHALLENGE_PENDING,
        ),
        (
            AuthenticationState.CHALLENGE_PENDING,
            AuthenticationTrigger.OTP_VERIFIED,
            AuthenticationState.AUTHENTICATED,
        ),
        (
            AuthenticationState.UNAUTHENTICATED,
            AuthenticationTrigger.OAUTH_VERIFIED,
            AuthenticationState.AUTHENTICATED,
        ),
        (
            AuthenticationState.UNAUTHENTICATED,
            AuthenticationTrigger.PASSKEY_ASSERTED,
            AuthenticationState.AUTHENTICATED,
        ),
        (
            AuthenticationState.AUTHENTICATED,
            AuthenticationTrigger.STEP_UP_REQUIRED,
            AuthenticationState.STEP_UP_REQUIRED,
        ),
        (
            AuthenticationState.STEP_UP_REQUIRED,
            AuthenticationTrigger.PASSKEY_ASSERTED,
            AuthenticationState.STEP_UP_VERIFIED,
        ),
        (
            AuthenticationState.UNAUTHENTICATED,
            AuthenticationTrigger.RECOVERY_REQUESTED,
            AuthenticationState.RECOVERY_PENDING,
        ),
        (
            AuthenticationState.RECOVERY_PENDING,
            AuthenticationTrigger.RECOVERY_VERIFIED,
            AuthenticationState.AUTHENTICATED,
        ),
    )

    for current_state, trigger, next_state in cases:
        assert state_machine.can_transition(current_state, trigger) is True
        assert state_machine.next_state_for(current_state, trigger) is next_state
        assert state_machine.transition_for(current_state, trigger) == AuthenticationTransition(
            current_state=current_state,
            trigger=trigger,
            next_state=next_state,
        )


def test_default_authentication_state_machine_rejects_invalid_transition() -> None:
    state_machine = DefaultAuthenticationStateMachine()

    assert (
        state_machine.can_transition(
            AuthenticationState.UNAUTHENTICATED,
            AuthenticationTrigger.OTP_VERIFIED,
        )
        is False
    )

    with pytest.raises(InvalidAuthenticationTransition):
        state_machine.next_state_for(
            AuthenticationState.UNAUTHENTICATED,
            AuthenticationTrigger.OTP_VERIFIED,
        )


def test_state_machine_authentication_guard_requires_exact_transition() -> None:
    state_machine = DefaultAuthenticationStateMachine()
    guard = StateMachineAuthenticationGuard(state_machine)

    assert guard.allows(
        AuthenticationTransition(
            current_state=AuthenticationState.UNAUTHENTICATED,
            trigger=AuthenticationTrigger.EMAIL_SUBMITTED,
            next_state=AuthenticationState.CHALLENGE_PENDING,
        ),
    )
    assert not guard.allows(
        AuthenticationTransition(
            current_state=AuthenticationState.UNAUTHENTICATED,
            trigger=AuthenticationTrigger.EMAIL_SUBMITTED,
            next_state=AuthenticationState.AUTHENTICATED,
        ),
    )


def test_composite_authentication_guard_requires_all_guards() -> None:
    state_machine = DefaultAuthenticationStateMachine()
    guard = CompositeAuthenticationGuard(
        (
            StateMachineAuthenticationGuard(state_machine),
            AllowAllGuard(),
        ),
    )

    assert guard.allows(
        AuthenticationTransition(
            current_state=AuthenticationState.UNAUTHENTICATED,
            trigger=AuthenticationTrigger.EMAIL_SUBMITTED,
            next_state=AuthenticationState.CHALLENGE_PENDING,
        ),
    )


def test_default_authentication_trust_resolver_maps_successful_triggers() -> None:
    trust_resolver = DefaultAuthenticationTrustResolver()

    assert trust_resolver.trust_level_for(AuthenticationTrigger.OTP_VERIFIED) is AuthTrustLevel.LOW
    assert (
        trust_resolver.trust_level_for(AuthenticationTrigger.OAUTH_VERIFIED)
        is AuthTrustLevel.STANDARD
    )
    assert (
        trust_resolver.trust_level_for(AuthenticationTrigger.PASSKEY_ASSERTED)
        is AuthTrustLevel.FRESH_PASSKEY
    )
    assert trust_resolver.trust_level_for(AuthenticationTrigger.EMAIL_SUBMITTED) is None
