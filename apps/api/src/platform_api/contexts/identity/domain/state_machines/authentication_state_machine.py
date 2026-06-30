"""Authentication state machine contract."""

from collections.abc import Mapping
from typing import Protocol

from platform_api.contexts.identity.domain.state_machines.authentication_transition import (
    AuthenticationTransition,
    InvalidAuthenticationTransition,
)
from platform_api.contexts.identity.domain.types import AuthenticationState, AuthenticationTrigger

type AuthenticationTransitionKey = tuple[AuthenticationState, AuthenticationTrigger]
type AuthenticationTransitionRules = Mapping[AuthenticationTransitionKey, AuthenticationState]

DEFAULT_AUTHENTICATION_TRANSITIONS: dict[AuthenticationTransitionKey, AuthenticationState] = {
    (
        AuthenticationState.UNAUTHENTICATED,
        AuthenticationTrigger.EMAIL_SUBMITTED,
    ): AuthenticationState.CHALLENGE_PENDING,
    (
        AuthenticationState.UNAUTHENTICATED,
        AuthenticationTrigger.OAUTH_VERIFIED,
    ): AuthenticationState.AUTHENTICATED,
    (
        AuthenticationState.UNAUTHENTICATED,
        AuthenticationTrigger.PASSKEY_ASSERTED,
    ): AuthenticationState.AUTHENTICATED,
    (
        AuthenticationState.CHALLENGE_PENDING,
        AuthenticationTrigger.OTP_VERIFIED,
    ): AuthenticationState.AUTHENTICATED,
    (
        AuthenticationState.AUTHENTICATED,
        AuthenticationTrigger.STEP_UP_REQUIRED,
    ): AuthenticationState.STEP_UP_REQUIRED,
    (
        AuthenticationState.STEP_UP_REQUIRED,
        AuthenticationTrigger.PASSKEY_ASSERTED,
    ): AuthenticationState.STEP_UP_VERIFIED,
    (
        AuthenticationState.STEP_UP_REQUIRED,
        AuthenticationTrigger.STEP_UP_VERIFIED,
    ): AuthenticationState.STEP_UP_VERIFIED,
    (
        AuthenticationState.UNAUTHENTICATED,
        AuthenticationTrigger.RECOVERY_REQUESTED,
    ): AuthenticationState.RECOVERY_PENDING,
    (
        AuthenticationState.CHALLENGE_PENDING,
        AuthenticationTrigger.RECOVERY_REQUESTED,
    ): AuthenticationState.RECOVERY_PENDING,
    (
        AuthenticationState.AUTHENTICATED,
        AuthenticationTrigger.RECOVERY_REQUESTED,
    ): AuthenticationState.RECOVERY_PENDING,
    (
        AuthenticationState.STEP_UP_REQUIRED,
        AuthenticationTrigger.RECOVERY_REQUESTED,
    ): AuthenticationState.RECOVERY_PENDING,
    (
        AuthenticationState.RECOVERY_PENDING,
        AuthenticationTrigger.RECOVERY_VERIFIED,
    ): AuthenticationState.AUTHENTICATED,
}


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


class DefaultAuthenticationStateMachine:
    """Table-driven authentication workflow state machine."""

    def __init__(
        self,
        transition_rules: AuthenticationTransitionRules = DEFAULT_AUTHENTICATION_TRANSITIONS,
    ) -> None:
        self._transition_rules = dict(transition_rules)

    def can_transition(
        self,
        current_state: AuthenticationState,
        trigger: AuthenticationTrigger,
    ) -> bool:
        """Return whether a trigger can be applied to the current state."""
        return (current_state, trigger) in self._transition_rules

    def transition_for(
        self,
        current_state: AuthenticationState,
        trigger: AuthenticationTrigger,
    ) -> AuthenticationTransition:
        """Return the transition produced by a trigger."""
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
        """Return the next authentication state for a trigger."""
        try:
            return self._transition_rules[(current_state, trigger)]
        except KeyError as exc:
            msg = f"Cannot apply {trigger.value} while authentication is {current_state.value}"
            raise InvalidAuthenticationTransition(msg) from exc
