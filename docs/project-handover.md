# Project Handover

## Project Overview

Backend-first passwordless authentication platform designed for future CQRS adoption and event-driven evolution.

Primary goals:

* Passwordless authentication
* Stateless authentication
* Passkey-first user experience
* Strong domain boundaries
* Future CQRS support
* Future Saga orchestration support
* Future multi-service extraction

---

# Technology Stack

## Runtime

* Python 3.12

## API

* FastAPI

## Database

* PostgreSQL

## Cache / Ephemeral Storage

* Redis

## Infrastructure

* Docker

## Tooling

* uv
* Ruff
* Pyright strict mode

---

# Architecture

## Style

* Modular Monolith
* Bounded Contexts
* DDD Layers
* CQRS-ready
* Event-driven evolution planned

## Current Contexts

### Identity

Responsible for:

* Authentication
* Credentials
* Sessions
* Recovery
* Identity Providers

Future contexts may be introduced as the platform evolves.

---

# Architectural Structure

The project follows a modular monolith architecture organized by bounded context.

Each context is structured using DDD layers:

context/
├── domain/
├── application/
├── infrastructure/
└── presentation/

## Layer Responsibilities

### Domain

* Aggregates
* Entities
* Value Objects
* Domain Services
* Domain Events
* Repository Contracts

### Application

* Commands
* Queries
* Handlers
* DTOs

### Infrastructure

* Persistence
* External Integrations
* Messaging

### Presentation

* HTTP APIs
* Request/Response Models

Some layers may be introduced incrementally as the project evolves.

---

# Authentication Strategy

## Core Principles

* No password authentication
* Passwordless-first
* Stateless authentication
* State-machine-driven authentication

## Authentication Methods

### Tier 1

Email OTP

### Tier 2

Passkeys (WebAuthn)

### Tier 3

Account Recovery

Status:
Deferred pending additional research.

## Additional Authentication Sources

* Google OAuth
* Apple OAuth

Supported through the credential model.

---

# Identity Domain

## Current Aggregates

* User
* Credential
* AuthSession
* AuthChallenge

## Current Value Objects

* CredentialSubject
* AuthenticationTransition
* AuthenticationState
* AuthenticationTrigger

Additional domain concepts may be introduced as the system evolves.

---

# Credential Strategy

## Credential Model

Generic credential model.

Credential types are represented through abstractions rather than separate aggregates.

## CredentialSubject

Supports:

* Email identities
* OAuth identities
* Passkeys

---

# Authentication State Strategy

Authentication state is not stored on:

* User
* Credential
* AuthChallenge

Authentication workflow state is owned by:

* AuthenticationStateMachine

Authentication transitions are represented as:

* Current state
* Trigger
* Next state

Transition guards are represented through domain contracts and are not yet implemented as concrete policies.

This allows authentication behavior to evolve independently from domain entities.

---

# Repository Strategy

## Repository Design

Repository contracts only.

Current repositories define persistence boundaries but do not contain implementation details.

## Unit of Work

Retained as the transactional boundary.

---

# Architectural Constraints

The following constraints must not be violated without updating the ADRs:

* No password authentication
* No framework dependencies in the domain layer
* No persistence logic inside domain entities
* Authentication state owned by AuthenticationStateMachine
* Repository contracts before repository implementations
* UnitOfWork remains the transactional boundary

---

# Current Implementation Status

## Implemented

### Foundation

* Repository structure
* Dependency management
* Environment configuration
* Docker foundation

### Tooling

* Ruff
* Pyright strict mode configuration
* Pyright strict mode verification

### API

* FastAPI bootstrap

### Identity Domain

* Identity contracts
* Domain entity skeletons
* Value objects
* Repository contracts
* Provider contracts
* Authentication state machine contracts
* Authentication transition value object
* Authentication guard contract

---

## Not Yet Implemented

### Persistence

* SQLAlchemy models
* Database repositories
* Migrations

### Authentication

* Authentication workflows
* OTP verification
* OAuth integrations
* Passkey implementation

### Application Layer

* Commands
* Queries
* Handlers

### Eventing

* Domain events
* Event bus
* Outbox pattern

### Distributed Workflows

* Saga orchestration

### CQRS

* Read models
* Projections
* Query infrastructure

---

# Deferred Decisions

The following decisions are intentionally postponed:

* Account recovery design
* Passkey recovery strategy
* Event bus implementation
* Outbox implementation
* Saga implementation
* Service extraction boundaries
* Kafka adoption strategy

---

# Current Progress

Current Phase:
Phase 7 – Identity Domain

Current Step:
Step 6 – Phase 7 Completion Review

Status:
Ready

Completed Steps:

* Step 1
* Step 2
* Step 3
* Step 4
* Step 5

Recent Quality Checks:

* uv run pyright
* uv run ruff check .
* uv run pytest

---

# Active ADRs

* ADR-001 Passwordless-first Authentication
* ADR-002 Generic Credential Model
* ADR-003 CredentialSubject Abstraction
* ADR-004 AuthenticationStateMachine Owns Authentication State
* ADR-005 Repository Contracts Before Persistence Implementations
* ADR-006 Pyright Strict Mode

Full details:

See `decisions.md`

---

# Reference Documents

* roadmap.md
* authentication-spec.md
* decisions.md
