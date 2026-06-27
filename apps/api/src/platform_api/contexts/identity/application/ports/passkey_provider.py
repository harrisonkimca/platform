"""Passkey provider application port."""

from dataclasses import dataclass
from typing import Protocol

from platform_api.contexts.identity.domain.value_objects.identifiers import UserId
from platform_api.contexts.identity.domain.value_objects.passkey import PasskeyCredentialId


@dataclass(frozen=True, slots=True)
class PasskeyAssertion:
    """Verified passkey assertion returned by a passkey provider."""

    credential_id: PasskeyCredentialId
    user_id: UserId


class PasskeyProvider(Protocol):
    """Port for verifying passkey ceremonies."""

    async def verify_assertion(self, assertion_response: str) -> PasskeyAssertion:
        """Verify a passkey assertion response."""
        ...
