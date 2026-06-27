"""Database configuration helpers."""

from os import environ

DATABASE_URL_ENV = "DATABASE_URL"
POSTGRESQL_SCHEME = "postgresql://"
ASYNC_POSTGRESQL_SCHEME = "postgresql+asyncpg://"


def normalize_database_url(database_url: str) -> str:
    """Return a SQLAlchemy async PostgreSQL database URL."""

    database_url = database_url.strip()

    if database_url.startswith(POSTGRESQL_SCHEME):
        return database_url.replace(POSTGRESQL_SCHEME, ASYNC_POSTGRESQL_SCHEME, 1)

    if not database_url.startswith(ASYNC_POSTGRESQL_SCHEME):
        msg = f"{DATABASE_URL_ENV} must use the {ASYNC_POSTGRESQL_SCHEME} scheme"
        raise RuntimeError(msg)

    return database_url


def get_database_url() -> str:
    """Read and normalize the database URL from the environment."""

    database_url = environ.get(DATABASE_URL_ENV)

    if database_url is None or database_url.strip() == "":
        msg = f"Missing required environment variable: {DATABASE_URL_ENV}"
        raise RuntimeError(msg)

    return normalize_database_url(database_url)
