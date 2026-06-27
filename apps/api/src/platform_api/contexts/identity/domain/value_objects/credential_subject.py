"""Credential subject value objects."""

from dataclasses import dataclass

from platform_api.contexts.identity.domain.value_objects.email_address import EmailAddress
from platform_api.contexts.identity.domain.value_objects.passkey import PasskeyCredentialId
from platform_api.contexts.identity.domain.value_objects.provider_identity import ProviderIdentity


@dataclass(frozen=True, slots=True)
class EmailCredentialSubject:
    """Subject for an email-based credential."""

    email: EmailAddress


@dataclass(frozen=True, slots=True)
class OAuthCredentialSubject:
    """Subject for an OAuth/OIDC credential."""

    provider_identity: ProviderIdentity


@dataclass(frozen=True, slots=True)
class PasskeyCredentialSubject:
    """Subject for a passkey credential."""

    passkey_credential_id: PasskeyCredentialId


type CredentialSubject = EmailCredentialSubject | OAuthCredentialSubject | PasskeyCredentialSubject
