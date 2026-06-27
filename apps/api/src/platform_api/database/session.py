"""Async SQLAlchemy session setup for PostgreSQL."""

from collections.abc import AsyncIterator
from functools import lru_cache

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from platform_api.database.config import get_database_url


@lru_cache
def get_async_engine() -> AsyncEngine:
    """Create and cache the async SQLAlchemy engine."""

    return create_async_engine(
        get_database_url(),
        pool_pre_ping=True,
    )


@lru_cache
def get_async_session_factory() -> async_sessionmaker[AsyncSession]:
    """Create and cache the async SQLAlchemy session factory."""

    return async_sessionmaker(
        bind=get_async_engine(),
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False,
    )


async def get_async_session() -> AsyncIterator[AsyncSession]:
    """Yield an AsyncSession for FastAPI dependencies."""

    async_session_factory = get_async_session_factory()

    async with async_session_factory() as session:
        yield session


async def dispose_async_engine() -> None:
    """Dispose database connections during application shutdown."""

    if get_async_engine.cache_info().currsize == 0:
        return

    await get_async_engine().dispose()
    get_async_session_factory.cache_clear()
    get_async_engine.cache_clear()
