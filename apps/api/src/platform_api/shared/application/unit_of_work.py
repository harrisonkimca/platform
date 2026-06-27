"""Application-level Unit of Work contract."""

from __future__ import annotations

from abc import ABC, abstractmethod
from types import TracebackType
from typing import Self


class UnitOfWork(ABC):
    """Abstract async transaction boundary for application use cases.

    Future implementations may collect domain events and persist outbox
    messages during commit, but this contract intentionally exposes only the
    transaction lifecycle required by application services.
    """

    @abstractmethod
    async def __aenter__(self) -> Self:
        """Enter the transactional boundary."""
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        """Exit the transactional boundary."""
        raise NotImplementedError

    @abstractmethod
    async def commit(self) -> None:
        """Commit pending work."""
        raise NotImplementedError

    @abstractmethod
    async def rollback(self) -> None:
        """Roll back pending work."""
        raise NotImplementedError
