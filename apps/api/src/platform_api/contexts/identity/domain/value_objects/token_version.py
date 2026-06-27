"""Token version value object."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TokenVersion:
    """Monotonic version used for token and session revocation."""

    value: int

    def __post_init__(self) -> None:
        if self.value < 0:
            msg = "TokenVersion must not be negative"
            raise ValueError(msg)
