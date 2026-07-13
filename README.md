# Fintech Platform

## Purpose

This document defines the long-term vision and architectural direction of the project.

Responsibilities

* Describe the project's purpose and intended capabilities
* Define the architectural philosophy
* Describe the intended technology stack
* Describe the long-term repository structure
* Communicate the project's guiding principles

This document intentionally changes very rarely.

It does not track implementation progress, completed work, or the current
state of the repository.

To contribute to this project, begin with:

* `docs/ai/getting-started.md`


## Project Overview

A backend-first passwordless authentication platform designed for long-term maintainability, simplicity, modularity, and future evolution.

The project is intentionally architected so it can evolve from a modular monolith into an event-driven system without requiring fundamental redesign.

The goal is not merely to build authentication, but to establish an architecture capable of supporting web applications, mobile applications, AI agents, and future distributed services while remaining understandable for a single maintainer.


# Vision

Build a professional-grade authentication platform that provides:

* Passwordless authentication
* Passkeys (WebAuthn)
* Email OTP
* Google OAuth
* Apple OAuth
* Tiered account recovery
* Stateless authentication
* Session management
* Future CQRS
* Future event-driven architecture

The platform favors long-term maintainability over short-term convenience.


# Architecture Philosophy

The architecture is guided by a small number of long-lived principles.

## Modular Monolith First

The system begins as a modular monolith.

This provides clear module boundaries while avoiding the operational complexity of distributed systems.

Individual bounded contexts should be capable of later extraction into independent services without requiring significant redesign.

Microservices are considered an evolutionary outcome—not an initial architectural choice.


## Domain-Driven Design

Business capabilities are organized into bounded contexts.

Each context follows layered architecture:

* Domain
* Application
* Infrastructure
* Presentation

The domain remains independent of frameworks.

Frameworks support the domain.

They do not define it.


## Authentication Philosophy

Authentication is passwordless-first.

Passwords are intentionally excluded from the architecture.

Supported authentication methods include:

* Email OTP
* Passkeys
* OAuth identities

Authentication behavior is modeled independently from transport and UI.


## State Machine Driven Authentication

Authentication workflow is modeled explicitly using state machines.

Workflow state belongs to AuthenticationStateMachine.

It does not belong to:

* User
* Credential
* AuthSession
* AuthChallenge

This keeps workflow behavior independent from domain entities.


## Generic Credential Model

Credentials are represented through a generic credential abstraction.

Credential types become value objects rather than separate aggregates.

This allows the platform to support:

* Email identities
* OAuth identities
* Passkeys

without redesigning the domain model.


## Repository Strategy

Repository contracts belong to the domain.

Repository implementations belong to infrastructure.

The application depends upon contracts rather than persistence technology.


## Unit of Work

Application use cases execute inside a Unit of Work.

The Unit of Work represents the transactional boundary of the system.


## CQRS Evolution

The platform is designed to support CQRS.

CQRS is introduced only when it improves the model.

The project intentionally avoids premature command/query separation.


## Event-Driven Evolution

The architecture is designed for incremental evolution.

The intended progression is:

Modular Monolith

↓

Domain Events

↓

In-Memory Event Bus

↓

Outbox Pattern

↓

Saga Orchestration

↓

Kafka

↓

Selective Service Extraction

Each stage builds upon the previous one.


## Technology Direction

Backend

* FastAPI
* Pydantic v2
* SQLAlchemy 2.x
* PostgreSQL
* Redis

Frontend

* React
* TypeScript
* React Router

Infrastructure

* Docker
* Docker Compose

Tooling

* uv
* Ruff
* Pyright
* Alembic
* pytest


# Repository Layout

The repository is organized by architectural responsibility rather than
technical framework.

```
apps/
    api/
        src/
            platform_api/
                contexts/
                shared/
                core/

docs/

tests/

docker/
```

The exact contents of each directory may evolve over time while
preserving the overall architectural organization.


# Repository Organization

## apps/

Contains the application source code.

### contexts/

Business capabilities organized as bounded contexts.

Each context owns its own:

* Domain
* Application
* Infrastructure
* Presentation

### shared/

Shared abstractions that are intentionally reusable across bounded
contexts.

### core/

Cross-cutting application configuration and bootstrapping.


## docs/

Project documentation.

Includes:

* Project vision
* Authentication specification
* Roadmap
* Project snapshot
* Architecture Decision Records
* AI SDLC


## tests/

Automated tests organized to mirror the application architecture.


## docker/

Local development infrastructure.


# Documentation

The project documentation is organized so that each document has a single
responsibility.

| Document                         | Purpose                                  |
|--------------------------------- |------------------------------------------|
| `README.md`                      | Project vision and architecture          |
| `docs/auth-spec.md`              | Authentication requirements              |
| `docs/roadmap.md`                | Implementation roadmap                   |
| `docs/snapshot.md`               | Current repository state                 |
| `docs/adr-log.md`                | Permanent architectural decisions        |
| `docs/ai/state/phase-state.yaml` | Current phase and SDLC pipeline position |
| `docs/ai/getting-started.md`     | How to begin working on the project      |
| `docs/ai/ai-sdlc.md`             | Development lifecycle and governance     |


# Development Philosophy

Project values:

* Maintainability over cleverness
* Explicit contracts over implicit behavior
* Strong typing
* Simple abstractions
* Clear boundaries
* Incremental evolution
* Documentation-driven development

Repository principles:

* Every implementation should reduce ambiguity
* Every abstraction should have a clear responsibility
* Every dependency should justify its long-term maintenance cost
* Every workflow should preserve architectural boundaries
* Every completed phase should improve implementation, documentation, consistency, and maintainability