"""OAuth provider application port."""

from dataclasses import dataclass
from typing import Protocol

from platform_api.contexts.identity.domain.value_objects.email_address import EmailAddress
from platform_api.contexts.identity.domain.value_objects.provider_identity import ProviderSubject


@dataclass(frozen=True, slots=True)
class OAuthIdentity:
    """Verified OAuth identity returned by an OAuth provider."""

    subject: ProviderSubject
    email: EmailAddress
    email_verified: bool


class OAuthProvider(Protocol):
    """Port for verifying OAuth/OIDC provider responses."""

    async def verify_authorization_response(self, authorization_response: str) -> OAuthIdentity:
        """Verify an OAuth authorization response."""
        ...
