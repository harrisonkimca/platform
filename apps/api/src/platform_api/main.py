"""FastAPI application factory."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from platform_api.api.router import api_router
from platform_api.core.config import get_settings
from platform_api.database.session import dispose_async_engine


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    """Manage application startup and shutdown."""

    get_settings()

    try:
        yield
    finally:
        await dispose_async_engine()


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        debug=settings.app_debug,
        lifespan=lifespan,
    )
    app.include_router(api_router)

    return app


app = create_app()
