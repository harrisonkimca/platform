"""Token service application port."""

from dataclasses import dataclass
from typing import Protocol

from platform_api.contexts.identity.domain.value_objects.identifiers import AuthSessionId, UserId
from platform_api.contexts.identity.domain.value_objects.token_version import TokenVersion


@dataclass(frozen=True, slots=True)
class TokenPair:
    """Access and refresh token pair returned by a token service."""

    access_token: str
    refresh_token: str


class TokenService(Protocol):
    """Port for issuing and verifying authentication tokens."""

    async def issue_token_pair(
        self,
        user_id: UserId,
        session_id: AuthSessionId,
        token_version: TokenVersion,
    ) -> TokenPair:
        """Issue an access and refresh token pair."""
        ...
