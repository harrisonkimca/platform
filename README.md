# Fintech Platform

A modern fintech platform foundation designed for maintainability, simplicity, modularity, future evolution, and developer productivity.

This repository is intentionally at Phase 0. It contains only the initial repository foundation: documentation, ignore rules, and the top-level folder structure. It does not yet contain FastAPI, Docker, PostgreSQL, Redis, authentication, business logic, migrations, or frontend code.

## Architecture Direction

The intended backend architecture is a modular monolith with DDD-inspired boundaries.

The platform is expected to support:

- Web applications
- Mobile applications
- AI agents
- AI streaming responses
- Future event-driven architecture
- Future microservice extraction

The architecture favors a modular monolith first because it keeps development simple for a single maintainer while preserving clear boundaries for later growth. This avoids the operational cost of early microservices while still allowing selected modules to be extracted later if the business need appears.

## Core Principles

1. Maintainability over cleverness
2. Simplicity before abstraction
3. Clear module boundaries
4. Production-minded defaults
5. Twelve-Factor App principles
6. Strict typing and explicit contracts
7. Future evolution without premature infrastructure

## Planned Technology Direction

Backend:

- FastAPI
- Pydantic v2
- SQLAlchemy 2.x
- PostgreSQL
- Redis

Frontend:

- React
- TypeScript
- React Router

Infrastructure:

- Docker
- Docker Compose

Tooling:

- `pyproject.toml`
- `uv`
- Ruff
- Alembic
- Environment-based configuration

These technologies are not implemented in Phase 0. They are listed to document the intended direction.

## Repository Structure

```text
.
├── apps/
│   ├── api/
│   ├── web/
│   ├── mobile/
│   └── agents/
├── docs/
│   ├── ai/
│   │   └── prompts/
│   ├── architecture/
│   └── workflows/
├── infra/
├── scripts/
└── tests/
```

## Folder Responsibilities

### `apps/`

Contains executable applications and user-facing or agent-facing entry points.

### `apps/api/`

Reserved for the future FastAPI backend modular monolith.

This application is expected to hold the core backend runtime, including HTTP APIs, application services, domain modules, persistence, authentication, and future event-publishing integration. It remains empty in Phase 0.

### `apps/web/`

Reserved for the future React and TypeScript web application.

### `apps/mobile/`

Reserved for a future mobile application.

The specific mobile framework is intentionally not selected in Phase 0 because the current phase does not require that decision.

### `apps/agents/`

Reserved for future AI agent entry points.

Agent workflows are separated from the main API surface so they can evolve independently while still integrating with the same backend capabilities.

### `docs/`

Contains repository documentation.

Top-level project documents include the roadmap, architecture decisions,
authentication specification, and project handover notes.

### `docs/ai/prompts/`

Contains reusable AI prompts for phase starts, implementation work,
architecture review, documentation updates, ADR checks, and phase completion.

### `docs/architecture/`

Reserved for architecture notes, diagrams, and future Architecture Decision Records.

### `docs/workflows/`

Contains development and operational workflows, including database migration
workflow documentation.

### `infra/`

Reserved for infrastructure and local development configuration.

Docker and Docker Compose will be introduced in a later phase, not in Phase 0.

### `scripts/`

Reserved for developer and operational helper scripts.

### `tests/`

Reserved for future integration, contract, and cross-application tests.

Unit tests may later live close to the code they test if that improves maintainability.

## Architectural Decisions

### Modular monolith first

A modular monolith is the starting point because it gives the project strong internal boundaries without the complexity of distributed systems.

Microservices are not introduced at the beginning because they add deployment, observability, networking, data consistency, and operational overhead that is not justified before the domain boundaries are proven.

### DDD-inspired boundaries

The project will use DDD-inspired module boundaries to keep business capabilities understandable and independently evolvable.

Full tactical DDD is not forced at this stage because over-modeling early can slow development and create abstractions before the domain is understood.

### CQRS where beneficial

CQRS may be introduced selectively where read and write concerns benefit from separation.

CQRS is not applied globally by default because it can add unnecessary complexity to simple workflows.

### Stateless authentication direction

Authentication is expected to be stateless and OAuth 2.1 / OIDC ready.

It is not implemented in Phase 0 because authentication requires careful modeling, configuration, token strategy, and security review.

### State-machine-driven authentication flow

Authentication flow is expected to use an explicit state-machine approach later.

This is deferred because Phase 0 is only the repository foundation.

### Future event-driven evolution

The platform should be able to evolve toward domain events, an Outbox Pattern, Saga orchestration, and Kafka integration.

These are not created now because premature event infrastructure can obscure the core model and increase maintenance cost.

## Current Phase

Phase 0 creates only:

- Repository documentation
- Ignore rules
- Initial folder structure

Phase 0 intentionally does not create:

- FastAPI application code
- Docker files
- Database configuration
- Redis configuration
- Authentication
- Business logic
- Migrations
- Frontend implementation
