"""Environment-based application settings."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from functools import lru_cache
from os import environ


class AppEnvironment(StrEnum):
    """Supported deployment environments."""

    LOCAL = "local"
    DEVELOPMENT = "development"
    TEST = "test"
    STAGING = "staging"
    PRODUCTION = "production"


@dataclass(frozen=True, slots=True)
class Settings:
    """Application settings loaded from environment variables."""

    app_env: AppEnvironment
    app_name: str
    app_debug: bool
    log_level: str
    secret_key: str


def _read_required_env(name: str) -> str:
    value = environ.get(name)

    if value is None or value.strip() == "":
        msg = f"Missing required environment variable: {name}"
        raise RuntimeError(msg)

    return value


def _read_bool_env(name: str, default: bool) -> bool:
    value = environ.get(name)

    if value is None:
        return default

    normalized = value.strip().lower()

    if normalized in {"1", "true", "yes", "on"}:
        return True

    if normalized in {"0", "false", "no", "off"}:
        return False

    msg = f"Environment variable {name} must be a boolean value"
    raise RuntimeError(msg)


def _read_app_environment() -> AppEnvironment:
    value = environ.get("APP_ENV", AppEnvironment.LOCAL.value)

    try:
        return AppEnvironment(value.strip().lower())
    except ValueError as exc:
        allowed_values = ", ".join(environment.value for environment in AppEnvironment)
        msg = f"APP_ENV must be one of: {allowed_values}"
        raise RuntimeError(msg) from exc


@lru_cache
def get_settings() -> Settings:
    """Load and cache application settings from environment variables."""

    app_env = _read_app_environment()
    app_debug = _read_bool_env("APP_DEBUG", default=False)

    if app_env is AppEnvironment.PRODUCTION and app_debug:
        msg = "APP_DEBUG must be false in production"
        raise RuntimeError(msg)

    return Settings(
        app_env=app_env,
        app_name=environ.get("APP_NAME", "Fintech Platform"),
        app_debug=app_debug,
        log_level=environ.get("APP_LOG_LEVEL", "INFO").strip().upper(),
        secret_key=_read_required_env("APP_SECRET_KEY"),
    )
