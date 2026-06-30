# Phase Start

## Purpose

Prepare the next implementation step before any code is written.

Responsibilities

* Review the project context documents.
* Determine the current phase and implementation step.
* Identify the requirements for the current step.
* Produce an implementation plan.
* Identify architectural risks before implementation begins.

This prompt performs planning only.

It does not modify source code or documentation.

---

Review:

* README.md
* docs/roadmap.md
* docs/project-handover.md
* docs/authentication-spec.md
* docs/decisions.md

Document responsibilities:

* README.md defines the long-term project vision and architecture intent.
* roadmap.md defines the implementation contract.
* project-handover.md describes the current repository state.
* authentication-spec.md defines authentication behavior.
* decisions.md defines architectural constraints.

Determine:

* Current phase from roadmap.md.
* Current repository state from project-handover.md.
* Current implementation objective.

Requirements:

* Follow the roadmap deliverables.
* Respect all ADRs.
* Follow the authentication specification.
* Preserve modular monolith boundaries.
* Preserve DDD layers.
* Preserve CQRS readiness.
* Preserve event-driven evolution.

Before implementation provide:

1. Current phase
2. Current objective
3. Deliverables involved
4. Repository areas expected to change
5. Domain concepts affected
6. Architectural risks
7. Implementation plan

Do not write code.