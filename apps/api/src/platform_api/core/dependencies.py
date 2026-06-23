"""Application dependency providers."""

from platform_api.core.config import Settings, get_settings


def get_application_settings() -> Settings:
    """Provide cached application settings to request handlers."""

    return get_settings()
