# Roadmap

## Vision

Build a backend-first passwordless authentication platform that supports:

* Email OTP authentication
* OAuth authentication (Google, Apple)
* Passkeys (WebAuthn)
* Tiered account recovery
* Stateless JWT authentication
* Session management and revocation
* CQRS adoption
* Event-driven evolution
* Future multi-service extraction

Architecture goals:

* Modular Monolith
* DDD-inspired boundaries
* CQRS-ready
* Event-driven evolution
* Saga orchestration capable
* Strict typing with Pyright
* Container-first deployment

---

# Completed Phases

## Phase 0 - Project Foundation

Goal:
Establish repository structure, tooling, and development standards.

Status:
Complete

---

## Phase 1 - Core Architecture Foundation

Goal:
Establish modular monolith architecture and bounded contexts.

Status:
Complete

---

## Phase 2 - Shared Building Blocks

Goal:
Create shared primitives, identifiers, and common abstractions.

Status:
Complete

---

## Phase 3 - Infrastructure Foundation

Goal:
Create infrastructure patterns and persistence foundations.

Status:
Complete

---

## Phase 4 - API Foundation

Goal:
Create FastAPI entry points and application wiring.

Status:
Complete

---

## Phase 5 - Security Foundation

Goal:
Establish security primitives and authentication infrastructure.

Status:
Complete

---

## Phase 6 - Authentication Foundations

Goal:
Prepare the project for passwordless authentication workflows.

Status:
Complete

---

# Current Phase

## Phase 7 - Identity Domain

Status:
In Progress

Goal:
Implement the core identity model that supports all authentication methods.

Deliverables:

* User aggregate
* Credential entity
* AuthChallenge entity
* AuthSession entity
* Identity value objects
* Repository contracts
* Domain services
* Authentication state machine contracts
* Recovery model foundations

Progress:

Completed:

* User aggregate skeleton
* Credential entity skeleton
* AuthChallenge entity skeleton
* AuthSession entity skeleton
* Identity value objects
* Repository contracts
* Provider contracts
* Authentication state machine contracts
* Pyright strict mode alignment

Remaining:

* Recovery model foundations
* Phase completion review

Future Evolution:

* Supports passkeys
* Supports OAuth identities
* Supports tiered recovery
* Supports CQRS adoption
* Supports event-driven evolution

---

# Future Phases

## Phase 8 - Authentication State Machine

Goal:
Implement authentication workflow orchestration.

Why:
Authentication behavior must be modeled independently from transport and UI concerns.

Deliverables:

* AuthenticationStateMachine implementation
* Triggers
* Transition rules
* Guards
* Recovery transitions
* Trust-level transitions

Future Evolution:

* Can evolve into workflow orchestration
* Can later participate in saga coordination

---

## Phase 9 - Stateless Authentication

Goal:
Implement token-based authentication.

Why:
Provide secure stateless authentication for APIs.

Deliverables:

* Access token issuance
* Refresh token issuance
* Token versioning
* Refresh rotation
* Refresh reuse detection
* Session revocation support

Future Evolution:

* Supports distributed deployments
* Supports service extraction

---

## Phase 10 - Authentication Application Layer

Goal:
Implement authentication use cases.

Why:
Separate domain behavior from application orchestration.

Deliverables:

* Login workflows
* Registration workflows
* OAuth workflows
* Session workflows
* Recovery workflows

Future Evolution:

* Supports CQRS command handlers

---

## Phase 11 - Passkeys (WebAuthn)

Goal:
Implement passkey registration and authentication.

Why:
Passkeys are the primary authentication method.

Deliverables:

* Registration ceremonies
* Assertion ceremonies
* Credential management
* Multi-device passkeys

Future Evolution:

* Hardware security key support
* Enterprise passkey policies

---

## Phase 12 - Recovery System

Goal:
Implement tiered account recovery.

Why:
Users must be able to recover access without passwords.

Deliverables:

* Tier 1 recovery
* Tier 2 recovery
* Recovery notifications
* Risk-based recovery controls

Future Evolution:

* Tier 3 identity verification
* Automated recovery workflows

---

## Phase 13 - Domain Events

Goal:
Introduce domain events.

Deliverables:

* Domain event contracts
* Event publication model
* Event dispatch abstractions

Future Evolution:

* Event-driven architecture

---

## Phase 14 - In-Memory Event Bus

Goal:
Implement internal event dispatching.

Deliverables:

* Event bus
* Event handlers
* Event subscriptions

Future Evolution:

* Outbox integration

---

## Phase 15 - CQRS Foundation

Goal:
Prepare command and query separation.

Deliverables:

* Command contracts
* Query contracts
* Handler contracts

Future Evolution:

* Full CQRS

---

## Phase 16 - Read Models

Goal:
Create dedicated query projections.

Deliverables:

* Read models
* Projection handlers
* Query services

Future Evolution:

* Separate read stores

---

## Phase 17 - Background Jobs

Goal:
Implement asynchronous processing.

Deliverables:

* Job contracts
* Scheduling infrastructure
* Worker execution

Future Evolution:

* Distributed processing

---

## Phase 18 - Outbox Pattern

Goal:
Provide reliable event publication.

Deliverables:

* Outbox table
* Outbox relay
* Retry handling

Future Evolution:

* External messaging

---

## Phase 19 - Saga Orchestration

Goal:
Coordinate long-running workflows.

Deliverables:

* Saga contracts
* Saga state management
* Authentication recovery workflows

Future Evolution:

* Cross-service workflows

---

## Phase 20 - AI Streaming Infrastructure

Goal:
Provide streaming foundations for future AI features.

Deliverables:

* Streaming abstractions
* Token streaming support
* Transport contracts

Future Evolution:

* Agent integrations

---

## Phase 21 - AI Agent Framework

Goal:
Support agent-based workflows.

Deliverables:

* Agent abstractions
* Tool execution framework
* Agent orchestration

Future Evolution:

* Multi-agent systems

---

## Phase 22 - Multi-Service Extraction

Goal:
Prepare bounded contexts for independent deployment.

Deliverables:

* Context isolation review
* Integration boundaries
* Deployment strategy

Future Evolution:

* Service decomposition

---

## Phase 23 - Kafka Integration

Goal:
Introduce external event streaming.

Deliverables:

* Kafka producers
* Kafka consumers
* Event contracts

Future Evolution:

* Full event-driven architecture
