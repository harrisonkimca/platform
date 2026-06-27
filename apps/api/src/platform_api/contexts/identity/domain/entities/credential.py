"""Credential domain entity."""

from dataclasses import dataclass
from datetime import UTC, datetime

from platform_api.contexts.identity.domain.types import (
    CredentialKind,
    CredentialStatus,
)
from platform_api.contexts.identity.domain.value_objects.credential_subject import CredentialSubject
from platform_api.contexts.identity.domain.value_objects.identifiers import CredentialId, UserId


@dataclass(slots=True)
class Credential:
    """Passwordless authentication credential entity."""

    id: CredentialId
    user_id: UserId
    kind: CredentialKind
    status: CredentialStatus
    subject: CredentialSubject
    created_at: datetime

    def __post_init__(self) -> None:
        if self.created_at.tzinfo is None:
            msg = "Credential.created_at must be timezone-aware"
            raise ValueError(msg)

        self.created_at = self.created_at.astimezone(UTC)
