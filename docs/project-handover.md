# Project Handover

## Purpose

This document is a snapshot of the current repository implementation.

Responsibilities

- Describe what currently exists in the repository.
- Summarize the implemented architecture.
- Record the current implementation phase.
- Describe implemented domain concepts.
- Describe implemented infrastructure.
- Describe outstanding implementation work.

This document is updated after implementation work.

It does not define future work or architectural intent.

It records what is currently implemented in the codebase and is intended to support continuation in a new development session.

Source of truth:

* Source code

Supporting documents:

* `README.md`
* `docs/roadmap.md`
* `docs/authentication-spec.md`
* `docs/decisions.md`

---

# Repository Status

Current phase:

* Phase 8 – Authentication State Machine

Current step:

* Phase 8 start

Repository status:

* In Progress

---

# Implemented Contexts

## Identity

Implemented:

* Domain layer

Responsibilities currently represented:

* Users
* Credentials
* Authentication sessions
* Authentication challenges
* Authentication state machine contracts
* Recovery model foundations

## Placeholder Contexts

Directory skeletons only:

* ai_agents
* portfolios
* transactions
* notifications

---

# Implemented Layers

## API

* FastAPI application factory
* Top-level API router
* `/health` endpoint

## Core

* Environment settings
* Settings dependency provider

## Database

* SQLAlchemy declarative base
* Metadata naming convention
* Database URL normalization
* Async engine factory
* Async session factory
* FastAPI database dependency

## Shared Application

* UnitOfWork contract

## Shared Infrastructure

* SQLAlchemy UnitOfWork

## Identity Domain

Implemented:

* Entities
* Value objects
* Repository contracts
* Domain policy contracts
* Authentication state machine contracts
* Recovery model foundations

## Identity Application

Folder skeleton only.

## Identity Infrastructure

Folder skeleton only.

## Identity Presentation

Folder skeleton only.

---

# Implemented Domain Concepts

## Entities

* User
* Credential
* AuthSession
* AuthChallenge

Current status:

* Entity skeletons only

## Value Objects

* UserId
* CredentialId
* AuthSessionId
* AuthChallengeId
* DeviceId
* EmailAddress
* ProviderName
* ProviderSubject
* ProviderIdentity
* PasskeyCredentialId
* TokenVersion
* EmailCredentialSubject
* OAuthCredentialSubject
* PasskeyCredentialSubject
* CredentialSubject
* AuthenticationTransition
* EmailRecoveryChannel
* OAuthRecoveryChannel
* BackupEmailRecoveryChannel
* RecoveryChannel

## Domain Enums

* AuthChallengeKind
* AuthChallengeStatus
* AuthenticationState
* AuthenticationTrigger
* AuthSessionStatus
* AuthTrustLevel
* CredentialKind
* CredentialStatus
* RecoveryChannelKind
* RecoveryTier
* UserStatus

## Domain Service Contracts

* AuthenticationPolicy
* CredentialPolicy
* SessionPolicy
* AuthChallengePolicy
* RecoveryEligibilityPolicy

Concrete implementations do not yet exist.

## Repository Contracts

* UserRepository
* CredentialRepository
* AuthSessionRepository
* AuthChallengeRepository

Repository implementations do not yet exist.

## Authentication State Machine Contracts

* AuthenticationStateMachine
* AuthenticationGuard
* AuthenticationTransition
* AuthenticationState
* AuthenticationTrigger

Concrete workflow implementation does not yet exist.

## Provider Contracts

Not yet implemented.

---

# Implemented Infrastructure

## Runtime

* FastAPI
* Docker
* Docker Compose

## Database

Implemented:

* SQLAlchemy async infrastructure
* Alembic configuration
* SQLAlchemy UnitOfWork

Not yet implemented:

* ORM models
* Repository implementations
* Database tables
* Migration revisions

## Environment

* Environment configuration
* Database configuration

---

# Configured Tooling

Configured:

* uv
* Ruff
* Pyright (strict)
* pytest
* Alembic
* Docker
* Docker Compose

Quality gates:

* `uv run pyright`
* `uv run ruff check .`
* `uv run pytest`

Current status:

* All passing

---

# Outstanding Implementation

Current Phase:

* Phase 8 – Authentication State Machine

---

# Reference Documents

* README.md
* docs/roadmap.md
* docs/authentication-spec.md
* docs/decisions.md
