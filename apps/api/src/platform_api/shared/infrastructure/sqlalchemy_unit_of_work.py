"""SQLAlchemy-backed Unit of Work implementation."""

from __future__ import annotations

from types import TracebackType
from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from platform_api.shared.application.unit_of_work import UnitOfWork

AsyncSessionFactory = async_sessionmaker[AsyncSession]


class SqlAlchemyUnitOfWork(UnitOfWork):
    """Async Unit of Work backed by a SQLAlchemy AsyncSession."""

    def __init__(self, session_factory: AsyncSessionFactory) -> None:
        self._session_factory = session_factory
        self._session: AsyncSession | None = None

    @property
    def session(self) -> AsyncSession:
        """Return the active SQLAlchemy session."""

        if self._session is None:
            msg = "Unit of Work is not active"
            raise RuntimeError(msg)

        return self._session

    async def __aenter__(self) -> Self:
        """Open a new SQLAlchemy session for this unit of work."""

        if self._session is not None:
            msg = "Unit of Work is already active"
            raise RuntimeError(msg)

        self._session = self._session_factory()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        """Roll back uncommitted work and close the session."""

        try:
            if self._session is not None and self._session.in_transaction():
                await self.rollback()
        finally:
            if self._session is not None:
                await self._session.close()
                self._session = None

        return None

    async def commit(self) -> None:
        """Commit pending work."""

        await self.session.commit()

    async def rollback(self) -> None:
        """Roll back pending work."""

        await self.session.rollback()
