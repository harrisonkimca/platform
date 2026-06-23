FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV PATH="/app/.venv/bin:${PATH}"
ENV PYTHONPATH="/app/apps/api/src"

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.11.23 /uv /uvx /bin/

COPY pyproject.toml uv.lock .python-version README.md ./

RUN uv sync --frozen --no-dev

COPY apps/api/src ./apps/api/src

CMD ["python", "-c", "from platform_api.core.config import get_settings; settings = get_settings(); print(f'{settings.app_name} container ready. No API server is configured in Phase 3.')"]
