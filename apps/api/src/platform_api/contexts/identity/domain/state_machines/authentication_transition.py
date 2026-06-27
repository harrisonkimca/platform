"""Authentication state transition value objects."""

from dataclasses import dataclass

from platform_api.contexts.identity.domain.types import AuthenticationState, AuthenticationTrigger


@dataclass(frozen=True, slots=True)
class AuthenticationTransition:
    """A side-effect-free authentication state transition description."""

    current_state: AuthenticationState
    trigger: AuthenticationTrigger
    next_state: AuthenticationState
