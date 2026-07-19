# Snapshot

## Purpose

This document is a snapshot of the current repository implementation.

Responsibilities

* Describe what currently exists in the repository
* Summarize the implemented architecture
* Describe implemented domain concepts
* Describe implemented infrastructure
* Describe outstanding implementation work

This document is updated after implementation work.

It does not define future work or architectural intent.

It records what is currently implemented in the codebase and is intended to support continuation in a new development session.

Source of truth:

* Source code

Supporting documents:

* `README.md`
* `docs/roadmap.md`
* `docs/auth-spec.md`
* `docs/adr-log.md`

Phase and SDLC pipeline position:

* `docs/ai/state/phase-state.yaml`


# Implemented Contexts

## Identity

Implemented:

* Domain layer
* Application layer foundations

Responsibilities currently represented:

* Users
* Credentials
* Authentication sessions
* Authentication challenges
* Authentication state machine contracts
* Authentication state machine implementation
* Authentication workflow orchestration
* Provider authentication contracts
* Trust-level resolution
* Recovery model foundations

## Placeholder Contexts

Directory skeletons only:

* ai_agents
* portfolios
* transactions
* notifications


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
* Authentication state machine implementation
* Authentication guard implementations
* Authentication trust resolver
* Recovery model foundations

## Identity Application

Implemented:

* Authentication provider contracts
* Authentication workflow result model
* Authentication orchestrator

Folder skeleton only:

* commands
* queries

## Identity Infrastructure

Folder skeleton only.

## Identity Presentation

Folder skeleton only.


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
* AuthenticationTrustResolver

Concrete implementations:

* DefaultAuthenticationTrustResolver

Concrete implementations do not yet exist for authentication policy,
credential policy, session policy, challenge policy, or recovery eligibility
policy.

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

Concrete workflow implementation:

* DefaultAuthenticationStateMachine
* StateMachineAuthenticationGuard
* CompositeAuthenticationGuard
* InvalidAuthenticationTransition

Implemented transition coverage:

* Email OTP challenge request
* Email OTP verification
* OAuth verification
* Passkey assertion
* Step-up requirement
* Step-up verification
* Recovery request
* Recovery verification

## Provider Contracts

Implemented:

* EmailOtpProvider
* OAuthIdentityProvider
* PasskeyAssertionProvider
* RecoveryProvider

Provider request and result models exist for email OTP, OAuth, passkey
assertion, and recovery verification.

Provider implementations do not yet exist.

## Application Services

Implemented:

* AuthenticationOrchestrator

Current behavior:

* Coordinates provider verification with authentication state transitions
* Returns workflow results with transition, trust level, credential subject,
  or recovery channel data
* Rejects invalid workflow transitions before provider verification

Persistence-aware authentication use cases do not yet exist.


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
* Verification under the current Stage 3 workflow has not yet been recorded

# Current Risks

Record only material risks that currently affect the implemented
repository.

Current risks:

* None recorded

# Outstanding Implementation

Outstanding:

* Implement access token issuance
* Implement refresh token issuance
* Implement token versioning
* Implement refresh rotation
* Implement refresh reuse detection
* Implement session revocation support