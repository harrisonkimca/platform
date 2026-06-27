"""One-time passcode sender application port."""

from typing import Protocol

from platform_api.contexts.identity.domain.value_objects.email_address import EmailAddress


class OtpSender(Protocol):
    """Port for sending one-time passcodes."""

    async def send_otp(self, email: EmailAddress, code: str) -> None:
        """Send a one-time passcode to an email address."""
        ...
