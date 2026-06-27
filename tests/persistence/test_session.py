"""Tests for async database session wiring."""

from __future__ import annotations

import asyncio
import importlib
import sys
from collections.abc import AsyncIterator
from types import ModuleType
from typing import Self

import pytest

SESSION_MODULE = "platform_api.database.session"


class FakeSession:
    """Minimal async context manager used by the FastAPI dependency test."""

    def __init__(self) -> None:
        self.entered = False
        self.exited = False

    async def __aenter__(self) -> Self:
        self.entered = True
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: object | None,
    ) -> None:
        self.exited = True


class FakeSessionFactory:
    """Callable fake with the same lifecycle shape as async_sessionmaker."""

    def __init__(self) -> None:
        self.session = FakeSession()

    def __call__(self) -> FakeSession:
        return self.session


def import_session_module(monkeypatch: pytest.MonkeyPatch, database_url: str) -> ModuleType:
    """Import the session module with a controlled database URL."""

    monkeypatch.setenv("DATABASE_URL", database_url)
    sys.modules.pop(SESSION_MODULE, None)
    return importlib.import_module(SESSION_MODULE)


def test_database_url_is_normalized_for_async_postgresql(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = import_session_module(
        monkeypatch,
        "postgresql://platform@localhost/platform",
    )

    try:
        assert module.get_async_engine().url.drivername == "postgresql+asyncpg"
    finally:
        asyncio.run(module.dispose_async_engine())


def test_database_url_rejects_non_async_postgresql_schemes(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("DATABASE_URL", "sqlite:///local.db")
    sys.modules.pop(SESSION_MODULE, None)
    module = importlib.import_module(SESSION_MODULE)

    with pytest.raises(RuntimeError, match="DATABASE_URL must use"):
        module.get_async_engine()


def test_get_async_session_yields_and_exits_session_context(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = import_session_module(
        monkeypatch,
        "postgresql+asyncpg://platform@localhost/platform",
    )
    factory = FakeSessionFactory()
    monkeypatch.setattr(module, "get_async_session_factory", lambda: factory)

    async def consume_session() -> FakeSession:
        dependency: AsyncIterator[FakeSession] = module.get_async_session()
        yielded_session = await anext(dependency)

        with pytest.raises(StopAsyncIteration):
            await anext(dependency)

        return yielded_session

    try:
        session = asyncio.run(consume_session())
    finally:
        asyncio.run(module.dispose_async_engine())

    assert session is factory.session
    assert session.entered is True
    assert session.exited is True
