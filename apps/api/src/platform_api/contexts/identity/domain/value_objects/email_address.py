"""Email address value object."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EmailAddress:
    """Normalized email address used by passwordless identity."""

    value: str

    def __post_init__(self) -> None:
        normalized = self.value.strip().lower()

        if "@" not in normalized:
            msg = "EmailAddress must contain @"
            raise ValueError(msg)

        if normalized.startswith("@") or normalized.endswith("@"):
            msg = "EmailAddress must include local and domain parts"
            raise ValueError(msg)

        object.__setattr__(self, "value", normalized)
