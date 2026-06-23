"""Health check routes."""

from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from platform_api.core.config import Settings
from platform_api.core.dependencies import get_application_settings

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    app_name: str
    environment: str


@router.get("/health", response_model=HealthResponse)
async def health_check(
    settings: Annotated[Settings, Depends(get_application_settings)],
) -> HealthResponse:
    """Return basic application health."""

    return HealthResponse(
        status="ok",
        app_name=settings.app_name,
        environment=settings.app_env.value,
    )
