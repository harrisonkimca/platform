# AI-Assisted Software Development Lifecycle (SDLC)

## Purpose

This workflow defines the standard software development lifecycle for the
project when using AI development tools.

Its goals are to:

* Maintain architectural consistency.
* Preserve DDD-inspired boundaries.
* Preserve modular monolith principles.
* Preserve future CQRS adoption.
* Preserve future event-driven evolution.
* Minimize documentation drift.
* Keep implementation and documentation synchronized.

Every implementation session follows the same lifecycle.

---

# Project Context

Every AI session begins by loading the project context.

Provide:

* `README.md`
* `docs/roadmap.md`
* `docs/project-handover.md`
* `docs/authentication-spec.md`
* `docs/decisions.md`

These documents have distinct responsibilities.

## README.md

Defines the long-term project vision and architectural intent.

Rarely changes.

## roadmap.md

Defines the implementation contract.

Changes only when project scope changes.

## project-handover.md

Defines the current repository implementation.

Updated after implementation sessions.

## authentication-spec.md

Defines authentication behavior.

Rarely changes.

## decisions.md

Defines permanent architectural constraints.

Updated only when a new ADR is required.

---

# Starting a New AI Session

Every new ChatGPT or Codex session begins with the same project context.

Provide:

* `README.md`
* `docs/roadmap.md`
* `docs/project-handover.md`
* `docs/authentication-spec.md`
* `docs/decisions.md`

Additionally, you may provide:

* `docs/ai/ai-sdlc.md`

The AI SDLC defines the development process and prompt responsibilities.
Providing it helps establish a consistent workflow but is not required to
understand the current state of the project.

After loading the project context, provide the prompt appropriate for the
current stage of the SDLC.

---

# Determining the Next Work Item

Before beginning an implementation session, determine the current
implementation state.

Normally this is taken from:

* `docs/project-handover.md`

If there is any uncertainty about the repository state, first perform a
repository audit using:

* `docs/ai/prompts/maintenance/repository-audit.md`

If documentation drift is detected:

1. Treat the source code as the source of truth.
2. Reconcile the documentation.
3. Resume the SDLC from Stage 1.

Implementation should never begin while the repository state is uncertain.

---

# Development Lifecycle

Every roadmap step follows the same lifecycle.

```
Phase Start
      │
      ▼
Implementation
      │
      ▼
Architecture Review
      │
      ▼
Documentation Update
      │
      ▼
ADR Audit
      │
      ▼
Phase Completion
```

---

# Stage 1 — Phase Start

Purpose

Understand the current roadmap step before implementation begins.

Prompt

* `phase-start.md`

Responsibilities

* Review the project context.
* Determine the current roadmap step.
* Identify requirements.
* Produce an implementation plan.
* Identify architectural risks.

Output

* Goal
* Requirements
* Files expected to change
* Domain concepts affected
* Architectural risks
* Implementation plan

No source code or documentation is modified.

---

# Stage 2 — Implementation

Purpose

Implement the current roadmap step.

Prompt

* `implementation.md`

Responsibilities

* Modify source code only.
* Implement only the current roadmap deliverables.
* Respect all ADRs.
* Preserve architectural boundaries.

Output

* Source code changes.

Documentation is intentionally not updated during this stage.

---

# Stage 3 — Architecture Review

Purpose

Evaluate the completed implementation.

Prompt

* `architecture-review.md`

Responsibilities

* Review architecture.
* Review DDD compliance.
* Review ADR compliance.
* Identify documentation drift.
* Identify technical debt.
* Recommend next work.

Output

Architecture Review Report.

No files are modified.

---

# Stage 4 — Documentation Update

Purpose

Synchronize implementation documentation with the repository.

Prompt

* `documentation-update.md`

Responsibilities

* Update `project-handover.md`.
* Update `roadmap.md` only if implementation progress or phase status changed.
* Eliminate documentation drift.

Restrictions

Do not modify:

* `README.md`
* `authentication-spec.md`
* `decisions.md`

---

# Stage 5 — ADR Audit

Purpose

Determine whether the implementation introduced a new architectural
decision.

Prompt

* `adr-audit.md`

Responsibilities

* Review architectural changes.
* Create new ADRs when necessary.
* Preserve ADR history.

Restrictions

This is the only prompt permitted to modify:

* `docs/decisions.md`

Existing ADRs must never be modified.

---

# Stage 6 — Phase Completion

Purpose

Verify that the roadmap phase has been completed successfully.

Prompt

* `phase-complete.md`

Responsibilities

* Verify roadmap completion.
* Confirm architectural compliance.
* Confirm readiness for the next phase.
* Update implementation progress when appropriate.

May update

* `project-handover.md`
* `roadmap.md`

Must not modify

* `README.md`
* `authentication-spec.md`
* `decisions.md`

---

# External Architecture Review (Optional)

After Stage 3, the Architecture Review Report may be reviewed externally.

Typical review topics include:

* Aggregate boundaries
* DDD compliance
* Repository boundaries
* CQRS readiness
* Event-driven evolution
* Authentication state machine design
* Service extraction readiness

Possible outcomes

* Approved
* Approved with recommendations
* Changes required

---

# Repository Audit Workflow

A repository audit may be performed whenever the current implementation
state is uncertain or periodically to prevent documentation drift.

Prompt

* `repository-audit.md`

The audit compares:

* Source code
* `project-handover.md`
* `roadmap.md`

The audit reports:

* Current implementation
* Documentation drift
* Missing implementation
* Incorrect implementation status
* Roadmap alignment
* Recommended documentation updates

The source code is always treated as the source of truth.

---

# Project Authority Model

Each project document has a single responsibility and is authoritative
only within that responsibility.

| Document                      | Authority                                         |
| ----------------------------- | ------------------------------------------------- |
| Source code                   | Current implementation                            |
| `README.md`                   | Project vision and architectural intent           |
| `docs/authentication-spec.md` | Authentication behavior and business requirements |
| `docs/decisions.md`           | Permanent architectural constraints (ADRs)        |
| `docs/roadmap.md`             | Implementation contract                           |
| `docs/project-handover.md`    | Current repository snapshot                       |

These documents complement one another rather than competing.

If inconsistencies are discovered, they indicate documentation drift,
implementation drift, or an architectural violation rather than a change
in authority.

Repository audits are used to identify and resolve these inconsistencies.

# Resolving Inconsistencies

When inconsistencies are discovered, determine which responsibility has
been violated.

| Inconsistency                                                          | Resolution                                                                                                                                      |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Source code differs from `project-handover.md`                         | Update `project-handover.md`.                                                                                                                   |
| Source code differs from `roadmap.md` implementation status            | Update `roadmap.md` if progress changed, or complete the missing implementation if the roadmap contract has not yet been fulfilled.             |
| Source code violates an ADR                                            | Correct the implementation or create a new ADR if the architecture has intentionally changed.                                                   |
| Source code violates `authentication-spec.md`                          | Correct the implementation unless the authentication requirements have intentionally changed.                                                   |
| Source code no longer reflects the architectural vision in `README.md` | Review whether the implementation or the architectural vision should change. Architectural changes should normally be accompanied by a new ADR. |

Repository audits are performed periodically to detect and eliminate
drift between the implementation and the project documentation.

---

# Maintenance Prompts

The following prompts support long-term repository maintenance.

| Prompt | Purpose |
|---------|---------|
| `repository-audit.md` | Audit the repository and detect implementation/documentation drift. |
| `documentation-reconciliation.md` | Synchronize documentation with the audited repository state. |
| `adr-audit.md` | Determine whether a new Architecture Decision Record is required. |

These prompts are not part of the normal implementation lifecycle.

They are used only when repository maintenance or architectural review is
required.

---

# Prompt Selection Guide

Use the following prompts depending on the work being performed.

| Situation | Prompt |
|-----------|--------|
| Beginning implementation | `phase-start.md` |
| Implementing the current roadmap step | `implementation.md` |
| Reviewing completed code | `architecture-review.md` |
| Updating implementation documentation | `documentation-update.md` |
| Determining whether a new ADR is required | `adr-audit.md` |
| Completing an entire roadmap phase | `phase-complete.md` |
| Unsure whether documentation matches the repository | `repository-audit.md` |
| Repository documentation has drifted from the implementation | `documentation-reconciliation.md` |

The implementation prompts form the normal SDLC.

The maintenance prompts are used only when repository maintenance or
documentation reconciliation is required.

---

# Guiding Principle

Implementation always follows the documented architecture.

Documentation always follows the implementation.

Architecture changes only through new ADRs.

Repository audits exist to keep all three aligned.