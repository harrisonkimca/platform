"""Credential policy domain service contract."""

from typing import Protocol

from platform_api.contexts.identity.domain.types import CredentialKind, CredentialStatus
from platform_api.contexts.identity.domain.value_objects.credential_subject import CredentialSubject


class CredentialPolicy(Protocol):
    """Contract for credential lifecycle and subject decisions."""

    def can_activate(
        self,
        kind: CredentialKind,
        status: CredentialStatus,
        subject: CredentialSubject,
    ) -> bool:
        """Return whether a credential may become active."""
        ...

    def can_revoke(self, status: CredentialStatus) -> bool:
        """Return whether a credential may be revoked."""
        ...
