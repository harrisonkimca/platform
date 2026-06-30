# Fintech Platform

## Purpose

This document defines the long-term vision and architectural direction of
the project.

Responsibilities

- Describe the project's purpose and intended capabilities.
- Define the architectural philosophy.
- Describe the intended technology stack.
- Describe the long-term repository structure.
- Communicate the project's guiding principles.

This document intentionally changes very rarely.

It does not track implementation progress, completed work, or the current
state of the repository.

---

## Project Overview

A backend-first passwordless authentication platform designed for long-term maintainability, simplicity, modularity, and future evolution.

The project is intentionally architected so it can evolve from a modular monolith into an event-driven system without requiring fundamental redesign.

The goal is not merely to build authentication, but to establish an architecture capable of supporting web applications, mobile applications, AI agents, and future distributed services while remaining understandable for a single maintainer.

---

# Vision

Build a professional-grade authentication platform that provides:

- Passwordless authentication
- Passkeys (WebAuthn)
- Email OTP
- Google OAuth
- Apple OAuth
- Tiered account recovery
- Stateless authentication
- Session management
- Future CQRS
- Future event-driven architecture

The platform favors long-term maintainability over short-term convenience.

---

# Architecture Philosophy

The architecture is guided by a small number of long-lived principles.

## Modular Monolith First

The system begins as a modular monolith.

This provides clear module boundaries while avoiding the operational complexity of distributed systems.

Individual bounded contexts should be capable of later extraction into independent services without requiring significant redesign.

Microservices are considered an evolutionary outcome—not an initial architectural choice.

---

## Domain-Driven Design

Business capabilities are organized into bounded contexts.

Each context follows layered architecture:

- Domain
- Application
- Infrastructure
- Presentation

The domain remains independent of frameworks.

Frameworks support the domain.

They do not define it.

---

## Authentication Philosophy

Authentication is passwordless-first.

Passwords are intentionally excluded from the architecture.

Supported authentication methods include:

- Email OTP
- Passkeys
- OAuth identities

Authentication behavior is modeled independently from transport and UI.

---

## State Machine Driven Authentication

Authentication workflow is modeled explicitly using state machines.

Workflow state belongs to AuthenticationStateMachine.

It does not belong to:

- User
- Credential
- AuthSession
- AuthChallenge

This keeps workflow behavior independent from domain entities.

---

## Generic Credential Model

Credentials are represented through a generic credential abstraction.

Credential types become value objects rather than separate aggregates.

This allows the platform to support:

- Email identities
- OAuth identities
- Passkeys

without redesigning the domain model.

---

## Repository Strategy

Repository contracts belong to the domain.

Repository implementations belong to infrastructure.

The application depends upon contracts rather than persistence technology.

---

## Unit of Work

Application use cases execute inside a Unit of Work.

The Unit of Work represents the transactional boundary of the system.

---

## CQRS Evolution

The platform is designed to support CQRS.

CQRS is introduced only when it improves the model.

The project intentionally avoids premature command/query separation.

---

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

---

## Technology Direction

Backend

- FastAPI
- Pydantic v2
- SQLAlchemy 2.x
- PostgreSQL
- Redis

Frontend

- React
- TypeScript
- React Router

Infrastructure

- Docker
- Docker Compose

Tooling

- uv
- Ruff
- Pyright
- Alembic
- pytest

---

# Repository Layout

<tree>

---

# Repository Organization

Explain each major folder.

Not implementation.

Purpose.

---

# Documentation

README.md

Vision and architecture.

roadmap.md

Implementation plan.

authentication-spec.md

Authentication requirements.

project-handover.md

Current implementation status.

decisions.md

Architecture Decision Records (ADRs).

---

# Development Philosophy

The project values:

- Maintainability over cleverness
- Explicit contracts over implicit behavior
- Strong typing
- Simple abstractions
- Clear boundaries
- Incremental evolution
- Documentation-driven development