# Roadmap

## Purpose

This document is the implementation contract for the project.

Responsibilities

* Define the implementation phases
* Define the deliverables for each phase
* Define the order in which work is completed

This document defines what the repository should implement next.

It does not describe the current implementation state.

Phase status is governed by `docs/ai/state/phase-state.yaml`.

While `roadmap_status: current`, phases numbered below `current_phase`
are Complete, the matching phase is Current, and phases numbered above
it are Not Started.

When `roadmap_status: complete`, the final phase identified by
`current_phase` is also Complete and no numbered development stage is
authorized.


## Overall Vision

Build a backend-first fintech platform using a modular monolith architecture with clear DDD-inspired boundaries.

The platform is intended to support:

* Passwordless authentication
* Email OTP authentication
* OAuth authentication
* Passkeys
* Tiered account recovery
* Stateless JWT authentication
* Session management and revocation
* CQRS adoption
* Event-driven evolution
* Future multi-service extraction
* AI streaming infrastructure
* Future AI agent support


# Phase 0 - Project Foundation

Goal:

Establish repository structure, documentation, ignore rules, and development standards.

Deliverables:

* Initial repository structure
* README
* Documentation folder structure
* Test folder structure
* Application folder placeholders


# Phase 1 - Core Architecture Foundation

Goal:

Establish modular monolith architecture and bounded-context direction.

Deliverables:

* Modular monolith direction
* Bounded-context folder structure
* DDD-inspired layer boundaries
* Initial context placeholders


# Phase 2 - Shared Building Blocks

Goal:

Create shared application and infrastructure foundations.

Deliverables:

* Shared application layer
* Unit of Work contract
* Shared infrastructure layer
* SQLAlchemy Unit of Work implementation


# Phase 3 - Infrastructure Foundation

Goal:

Create local development and persistence foundations.

Deliverables:

* Dockerfile
* Docker Compose
* PostgreSQL service
* Redis service
* Environment configuration
* SQLAlchemy base
* Async SQLAlchemy session setup
* Alembic configuration


# Phase 4 - API Foundation

Goal:

Create FastAPI entry points and application wiring.

Deliverables:

* FastAPI application factory
* Application lifespan management
* Top-level API router
* Health endpoint
* Settings dependency


# Phase 5 - Security Foundation

Goal:

Establish minimal security-related configuration foundations.

Deliverables:

* Required application secret configuration
* Environment validation
* Production debug-mode guard


# Phase 6 - Authentication Foundations

Goal:

Prepare the project for passwordless authentication modeling.

Deliverables:

* Passwordless authentication requirements documented
* Authentication architecture decisions documented
* Identity context prepared for authentication domain modeling


# Phase 7 - Identity Domain

Goal:

Implement the core Identity domain foundation that supports passwordless authentication methods while remaining independent of transport, persistence, and external identity providers.

Deliverables:

* User aggregate
* Credential entity
* AuthChallenge entity
* AuthSession entity
* Identity value objects
* Repository contracts
* Domain service contracts
* Authentication state machine contracts
* Recovery model foundations


# Phase 8 - Authentication State Machine

Goal:

Implement authentication workflow orchestration.

Deliverables:

* AuthenticationStateMachine implementation
* Authentication triggers
* State transition rules
* Guard implementations
* Provider contracts
* Provider authentication orchestration
* Recovery transitions
* Trust-level transitions


# Phase 9 - Stateless Authentication

Goal:

Implement token-based authentication.

Deliverables:

* Access token issuance
* Refresh token issuance
* Token versioning
* Refresh rotation
* Refresh reuse detection
* Session revocation support


# Phase 10 - Authentication Application Layer

Goal:

Implement authentication use cases.

Deliverables:

* Login workflows
* Registration workflows
* OAuth workflows
* Session workflows
* Recovery workflows


# Phase 11 - Passkeys (WebAuthn)

Goal:

Implement passkey registration and authentication.

Deliverables:

* Registration ceremonies
* Assertion ceremonies
* Credential management
* Multi-device passkeys


# Phase 12 - Recovery System

Goal:

Implement tiered account recovery.

Deliverables:

* Tier 1 recovery
* Tier 2 recovery
* Recovery notifications
* Risk-based recovery controls


# Phase 13 - Domain Events

Goal:

Introduce domain events.

Deliverables:

* Domain event contracts
* Event publication model
* Event dispatch abstractions


# Phase 14 - In-Memory Event Bus

Goal:

Implement internal event dispatching.

Deliverables:

* Event bus
* Event handlers
* Event subscriptions


# Phase 15 - CQRS Foundation

Goal:

Prepare command and query separation.

Deliverables:

* Command contracts
* Query contracts
* Handler contracts


# Phase 16 - Read Models

Goal:

Create dedicated query projections.

Deliverables:

* Read models
* Projection handlers
* Query services


# Phase 17 - Background Jobs

Goal:

Implement asynchronous processing.

Deliverables:

* Job contracts
* Scheduling infrastructure
* Worker execution


# Phase 18 - Outbox Pattern

Goal:

Provide reliable event publication.

Deliverables:

* Outbox table
* Outbox relay
* Retry handling


# Phase 19 - Saga Orchestration

Goal:

Coordinate long-running workflows.

Deliverables:

* Saga contracts
* Saga state management
* Authentication recovery workflows


# Phase 20 - AI Streaming Infrastructure

Goal:

Provide streaming foundations for future AI features.

Deliverables:

* Streaming abstractions
* Token streaming support
* Transport contracts


# Phase 21 - AI Agent Framework

Goal:

Support agent-based workflows.

Deliverables:

* Agent abstractions
* Tool execution framework
* Agent orchestration


# Phase 22 - Multi-Service Extraction

Goal:

Prepare bounded contexts for independent deployment.

Deliverables:

* Context isolation review
* Integration boundaries
* Deployment strategy


# Phase 23 - Kafka Integration

Goal:

Introduce external event streaming.

Deliverables:

* Kafka producers
* Kafka consumers
* Event contracts