# Architecture Decision Record Log

## Purpose

This document records the permanent architectural decisions that govern
the design and evolution of the project.

Responsibilities

* Record significant architectural decisions
* Define long-term architectural constraints
* Preserve the history of architectural decisions
* Guide future implementation without recording implementation progress

This document is **not**:

* An implementation log
* A project status report
* A roadmap
* A design discussion

Architectural decisions should be recorded only when a decision:

* Affects future development
* Introduces a long-term architectural constraint
* Changes the architectural direction of the project

Existing ADRs are historical records and must never be modified or
removed.

If an architectural decision changes, append a new ADR that supersedes
the previous decision rather than rewriting history.

This document changes only when a new architectural decision is made.


# ADR-001 — Passwordless-First Authentication

## Decision

The platform will not support password authentication.

Authentication will be implemented using passwordless mechanisms.

## Reason

Passwords introduce credential management complexity, increase attack
surface, and complicate account recovery.

The platform is designed around modern authentication mechanisms from
the outset.

## Consequences

Supported authentication methods include:

* Email OTP
* Passkeys
* OAuth providers

Password reset workflows are not required.


# ADR-002 — Generic Credential Model

## Decision

Authentication credentials are represented by a single Credential
aggregate.

Separate credential aggregates will not be created for individual
authentication mechanisms.

## Reason

Authentication methods share common behaviors and lifecycle
requirements.

A unified credential model simplifies future expansion.

## Consequences

The Credential aggregate must support:

* Email OTP
* OAuth providers
* Passkeys

Future credential types should integrate into the existing model
whenever practical.


# ADR-003 — CredentialSubject Abstraction

## Decision

Credential ownership and identity references are represented through
CredentialSubject.

## Reason

Different authentication providers identify users differently.

CredentialSubject provides a consistent abstraction across
authentication mechanisms.

## Consequences

Credential implementations remain provider-agnostic.

New authentication providers can be introduced without changing
aggregate boundaries.


# ADR-004 — AuthenticationStateMachine Owns Authentication State

## Decision

Authentication workflow state is owned by the
AuthenticationStateMachine.

Authentication state is not stored directly on domain aggregates.

## Reason

Authentication progression is workflow behavior rather than persistent
business identity data.

Separating workflow state from aggregates improves flexibility and
reduces coupling.

## Consequences

User, Credential, and AuthChallenge remain focused on domain
responsibilities.

Authentication workflows can evolve independently.


# ADR-005 — Repository Contracts Before Persistence Implementations

## Decision

Repository contracts are defined before persistence implementations.

## Reason

Domain boundaries should be established before infrastructure concerns.

This preserves a domain-first design and prevents premature persistence
decisions.

## Consequences

Repository interfaces exist before SQLAlchemy implementations.

Persistence remains isolated within the infrastructure layer.


# ADR-006 — Pyright Strict Mode

## Decision

Pyright strict mode is mandatory across the repository.

## Reason

Strong static analysis improves maintainability and detects defects
early.

The project favors explicit typing and long-term maintainability.

## Consequences

All new code must satisfy strict type checking.

Type safety is treated as an architectural requirement rather than an
optional quality improvement.