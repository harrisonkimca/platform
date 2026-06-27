"""Identity identifier value objects."""

from dataclasses import dataclass
from uuid import UUID


def _ensure_non_empty_uuid(value: UUID, name: str) -> None:
    if value.int == 0:
        msg = f"{name} must not be the nil UUID"
        raise ValueError(msg)


@dataclass(frozen=True, slots=True)
class UserId:
    """Stable identity for a user aggregate."""

    value: UUID

    def __post_init__(self) -> None:
        _ensure_non_empty_uuid(self.value, "UserId")


@dataclass(frozen=True, slots=True)
class CredentialId:
    """Stable identity for a credential aggregate."""

    value: UUID

    def __post_init__(self) -> None:
        _ensure_non_empty_uuid(self.value, "CredentialId")


@dataclass(frozen=True, slots=True)
class AuthSessionId:
    """Stable identity for an authentication session aggregate."""

    value: UUID

    def __post_init__(self) -> None:
        _ensure_non_empty_uuid(self.value, "AuthSessionId")


@dataclass(frozen=True, slots=True)
class AuthChallengeId:
    """Stable identity for an authentication challenge aggregate."""

    value: UUID

    def __post_init__(self) -> None:
        _ensure_non_empty_uuid(self.value, "AuthChallengeId")


@dataclass(frozen=True, slots=True)
class DeviceId:
    """Stable identity for a device associated with an auth session."""

    value: UUID

    def __post_init__(self) -> None:
        _ensure_non_empty_uuid(self.value, "DeviceId")
