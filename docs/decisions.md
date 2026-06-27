# Architecture Decision Records

This document records major architectural decisions that shape the system.

Architectural constraints should not be changed without updating the relevant ADR.

---

# ADR-001 — Passwordless-First Authentication

## Decision

The platform will not support password authentication.

Authentication will be implemented using passwordless mechanisms.

## Reason

Passwords introduce credential management complexity, increase attack surface, and create recovery challenges.

The platform is being designed around modern authentication mechanisms from the beginning.

## Consequences

Supported authentication methods include:

* Email OTP
* Passkeys
* OAuth providers

Password reset workflows are not required.

---

# ADR-002 — Generic Credential Model

## Decision

Authentication credentials are represented by a single Credential aggregate.

Separate credential aggregates will not be created for individual authentication mechanisms.

## Reason

Authentication methods share many common behaviors and lifecycle requirements.

A unified credential model simplifies future expansion.

## Consequences

The credential model must support:

* Email OTP
* OAuth providers
* Passkeys

Future credential types should integrate into the existing model whenever practical.

---

# ADR-003 — CredentialSubject Abstraction

## Decision

Credential ownership and identity references are represented through CredentialSubject.

## Reason

Different credential providers identify users differently.

CredentialSubject provides a consistent abstraction across authentication methods.

## Consequences

Credential implementations remain provider-agnostic.

New authentication providers can be added without changing aggregate boundaries.

---

# ADR-004 — AuthenticationStateMachine Owns Authentication State

## Decision

Authentication workflow state is owned by AuthenticationStateMachine.

Authentication state is not stored directly on domain aggregates.

## Reason

Authentication flow progression is workflow behavior rather than business identity data.

Separating workflow state from aggregates improves flexibility and reduces coupling.

## Consequences

User, Credential, and AuthChallenge remain focused on domain responsibilities.

Authentication workflows can evolve independently.

---

# ADR-005 — Repository Contracts Before Persistence Implementations

## Decision

Repository contracts are defined before persistence implementations.

## Reason

Domain boundaries should be established before infrastructure concerns.

This preserves domain-first design and avoids premature persistence decisions.

## Consequences

Repository interfaces exist before SQLAlchemy implementations.

Persistence details remain isolated within infrastructure layers.

---

# ADR-006 — Pyright Strict Mode

## Decision

Pyright strict mode is required for the entire project.

## Reason

Strong static analysis improves maintainability and catches defects early.

The project favors explicit typing and long-term maintainability.

## Consequences

New code must satisfy strict type checking.

Type safety is treated as an architectural requirement rather than an optional quality improvement.


Looking at roadmap, some future ADRs:

ADR-007 CQRS Read/Write Separation
ADR-008 Domain Events as Integration Boundary
ADR-009 Outbox Pattern for Reliable Event Publication
ADR-010 Saga Orchestration for Distributed Workflows
ADR-011 Kafka as Event Backbone