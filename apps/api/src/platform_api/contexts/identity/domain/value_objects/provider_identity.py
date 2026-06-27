"""External provider identity value objects."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProviderName:
    """External identity provider name."""

    value: str

    def __post_init__(self) -> None:
        if self.value.strip() == "":
            msg = "ProviderName must not be empty"
            raise ValueError(msg)


@dataclass(frozen=True, slots=True)
class ProviderSubject:
    """Stable subject identifier assigned by an external provider."""

    value: str

    def __post_init__(self) -> None:
        if self.value.strip() == "":
            msg = "ProviderSubject must not be empty"
            raise ValueError(msg)


@dataclass(frozen=True, slots=True)
class ProviderIdentity:
    """Verified external provider identity reference."""

    provider_name: ProviderName
    subject: ProviderSubject
