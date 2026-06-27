"""Tests for the SQLAlchemy Unit of Work lifecycle."""

from __future__ import annotations

import asyncio
from typing import cast

import pytest

from platform_api.shared.infrastructure.sqlalchemy_unit_of_work import (
    AsyncSessionFactory,
    SqlAlchemyUnitOfWork,
)


class FakeAsyncSession:
    """Small fake for exercising Unit of Work lifecycle behavior."""

    def __init__(self) -> None:
        self.commits = 0
        self.rollbacks = 0
        self.closes = 0
        self.transaction_active = True

    def in_transaction(self) -> bool:
        return self.transaction_active

    async def commit(self) -> None:
        self.commits += 1
        self.transaction_active = False

    async def rollback(self) -> None:
        self.rollbacks += 1
        self.transaction_active = False

    async def close(self) -> None:
        self.closes += 1


class FakeSessionFactory:
    """Callable fake compatible with the Unit of Work's session factory."""

    def __init__(self) -> None:
        self.sessions: list[FakeAsyncSession] = []

    def __call__(self) -> FakeAsyncSession:
        session = FakeAsyncSession()
        self.sessions.append(session)
        return session


def test_unit_of_work_exposes_active_session_and_closes_after_commit() -> None:
    factory = FakeSessionFactory()
    unit_of_work = SqlAlchemyUnitOfWork(cast(AsyncSessionFactory, factory))

    async def run() -> FakeAsyncSession:
        async with unit_of_work as active_unit_of_work:
            session = cast(FakeAsyncSession, active_unit_of_work.session)
            assert active_unit_of_work is unit_of_work
            await active_unit_of_work.commit()
            return session

    session = asyncio.run(run())

    assert session.commits == 1
    assert session.rollbacks == 0
    assert session.closes == 1

    with pytest.raises(RuntimeError, match="Unit of Work is not active"):
        _ = unit_of_work.session


def test_unit_of_work_rolls_back_uncommitted_work_on_exit() -> None:
    factory = FakeSessionFactory()
    unit_of_work = SqlAlchemyUnitOfWork(cast(AsyncSessionFactory, factory))

    async def run() -> FakeAsyncSession:
        async with unit_of_work as active_unit_of_work:
            return cast(FakeAsyncSession, active_unit_of_work.session)

    session = asyncio.run(run())

    assert session.commits == 0
    assert session.rollbacks == 1
    assert session.closes == 1


def test_unit_of_work_rolls_back_and_propagates_exceptions() -> None:
    factory = FakeSessionFactory()
    unit_of_work = SqlAlchemyUnitOfWork(cast(AsyncSessionFactory, factory))

    async def run() -> None:
        async with unit_of_work:
            raise ValueError("boom")

    with pytest.raises(ValueError, match="boom"):
        asyncio.run(run())

    session = factory.sessions[0]
    assert session.commits == 0
    assert session.rollbacks == 1
    assert session.closes == 1


def test_unit_of_work_rejects_reentering_active_context() -> None:
    factory = FakeSessionFactory()
    unit_of_work = SqlAlchemyUnitOfWork(cast(AsyncSessionFactory, factory))

    async def run() -> FakeAsyncSession:
        async with unit_of_work:
            session = cast(FakeAsyncSession, unit_of_work.session)

            with pytest.raises(RuntimeError, match="Unit of Work is already active"):
                await unit_of_work.__aenter__()

            return session

    session = asyncio.run(run())

    assert session.rollbacks == 1
    assert session.closes == 1
