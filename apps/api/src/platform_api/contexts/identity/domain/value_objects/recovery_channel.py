"""Recovery channel value objects."""

from dataclasses import dataclass
from typing import ClassVar

from platform_api.contexts.identity.domain.types import RecoveryChannelKind
from platform_api.contexts.identity.domain.value_objects.email_address import EmailAddress
from platform_api.contexts.identity.domain.value_objects.identifiers import CredentialId
from platform_api.contexts.identity.domain.value_objects.provider_identity import ProviderIdentity


@dataclass(frozen=True, slots=True)
class EmailRecoveryChannel:
    """Primary email channel available for account recovery decisions."""

    email: EmailAddress
    kind: ClassVar[RecoveryChannelKind] = RecoveryChannelKind.EMAIL


@dataclass(frozen=True, slots=True)
class OAuthRecoveryChannel:
    """OAuth identity channel available for account recovery decisions."""

    provider_identity: ProviderIdentity
    kind: ClassVar[RecoveryChannelKind] = RecoveryChannelKind.OAUTH


@dataclass(frozen=True, slots=True)
class BackupEmailRecoveryChannel:
    """Backup email credential reference available for recovery decisions."""

    credential_id: CredentialId
    kind: ClassVar[RecoveryChannelKind] = RecoveryChannelKind.BACKUP_EMAIL


type RecoveryChannel = EmailRecoveryChannel | OAuthRecoveryChannel | BackupEmailRecoveryChannel
