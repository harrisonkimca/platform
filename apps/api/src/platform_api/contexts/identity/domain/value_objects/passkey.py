"""Passkey value objects."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PasskeyCredentialId:
    """Credential identifier assigned by a WebAuthn passkey ceremony."""

    value: str

    def __post_init__(self) -> None:
        if self.value.strip() == "":
            msg = "PasskeyCredentialId must not be empty"
            raise ValueError(msg)
