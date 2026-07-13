# AI-Assisted Software Development Lifecycle (SDLC)

AI Software Development Lifecycle

Version 1.0

## Purpose

This document is the authoritative specification for the Governed AI
Software Development Lifecycle (AI SDLC).

It defines the lifecycle, governance model, authority model, stage
responsibilities, workflow constraints, and quality gates used throughout
the project.

Other documents may summarize this workflow but must not redefine or
duplicate its governance.

Its goals are to:

* Maintain architectural consistency
* Preserve DDD-inspired boundaries
* Preserve modular monolith principles
* Preserve future CQRS adoption
* Preserve future event-driven evolution
* Minimize documentation drift
* Keep implementation and documentation synchronized

Every implementation session follows the same lifecycle.


# Documentation Architecture

README\
──────────────────────────────\
Project vision
Architecture philosophy

↓

Getting Started\
──────────────────────────────\
Project onboarding
Workflow entry

↓

AI SDLC\
──────────────────────────────\
Development governance
Stage responsibilities
Authority model

↓

Prompt Library\
──────────────────────────────\
Executable workflow stages

↓

Stage Reports\
──────────────────────────────\
Working artifacts

↓

Project Documents\
──────────────────────────────\
Roadmap
Snapshot
ADR
Auth Spec
Phase State

↓

Source Code\
──────────────────────────────\
Implementation


# Authoritative Project Documents

Every AI session begins by loading the project context.

Load the following project context:

* `README.md`
* `docs/roadmap.md`
* `docs/snapshot.md`
* `docs/auth-spec.md`
* `docs/adr-log.md`
* `docs/ai/state/phase-state.yaml`

These documents are authoritative only within their defined
responsibilities.

## README.md

Defines the long-term project vision and architectural intent.

Rarely changes.

## roadmap.md

Defines the implementation contract.

Changes only when project scope changes.

## snapshot.md

Defines the current repository implementation.

Updated after implementation sessions.

## auth-spec.md

Defines authentication behavior.

Rarely changes.

## adr-log.md

Defines permanent architectural constraints.

Updated only when a new ADR is required.

## phase-state.yaml

Defines current pipeline position: active roadmap phase, roadmap status,
and the next SDLC stage to run.

Updated by every stage (`sdlc_stage`) and by Stage 6 exclusively
(`current_phase`, `current_phase_name`, `roadmap_status`).


# AI Constitution

Every AI-assisted development session must:

* Preserve architectural boundaries
* Respect project document authority
* Prefer explicit contracts over implicit behavior
* Minimize accidental complexity
* Preserve domain independence from infrastructure
* Avoid inventing implementation details
* Avoid reinterpreting project documentation
* Prefer refinement over redesign
* Leave the repository in a better state than it found it


# Starting a New AI Session

Developers normally enter the workflow through:

`docs/ai/getting-started.md`

That guide explains how to begin a development session and select the appropriate workflow.

This specification defines the required project context that every SDLC
stage assumes has already been loaded.

Before executing any SDLC stage, load:

* `README.md`
* `docs/roadmap.md`
* `docs/snapshot.md`
* `docs/auth-spec.md`
* `docs/adr-log.md`
* `docs/ai/state/phase-state.yaml`

Additionally, you may provide:

* `docs/ai/ai-sdlc.md`

The AI SDLC defines the development process and prompt responsibilities.
Providing it helps establish a consistent workflow but is not required to
understand the current state of the project.

After loading the project context, provide the prompt appropriate for the
current stage of the SDLC.


# Determining the Next Work Item

Before beginning an implementation session, determine the current
implementation state.

Normally this is taken from:

* `docs/ai/state/phase-state.yaml` — current phase and next SDLC stage.
* `docs/snapshot.md` — current repository implementation detail.

If there is any uncertainty about the repository state, first perform a
Review Repository evaluation using:

* `docs/ai/prompts/maintenance/review-repository.md`

If documentation drift is detected:

1. Treat the source code as the source of truth.
2. Reconcile the documentation.
3. Resume the SDLC from Stage 1.

Implementation should never begin while the repository state is uncertain.


# Development Lifecycle

Every roadmap step follows the same SDLC lifecycle.

01 Start Phase

↓

02 Implementation

↓

03 Review Implementation

↓

04 Update Documents

↓

05 Review Architecture Decision Records

↓

06 Complete Phase


# Stage Reports

Each SDLC stage produces a report that becomes the working input for the next stage.

Reports are stored under:

* `docs/reports/`

Reports belong to the current roadmap phase.

Each stage overwrites its own report when rerun.

Reports are working artifacts rather than permanent project
documentation.

They preserve the outputs of each SDLC stage and provide the working
context for the next stage.

Terminology:

* Roadmap phase = implementation unit defined in `docs/roadmap.md`
* SDLC stage    = one workflow step executed by a prompt
* Stage report  = working artifact passed between SDLC stages

Report files:

* `docs/reports/01-start-report.md`
* `docs/reports/02-build-report.md`
* `docs/reports/03-review-report.md`
* `docs/reports/04-update-docs-report.md`
* `docs/reports/05-review-adr-report.md`
* `docs/reports/06-complete-report.md`

Stage report flow:

01-start.md\
→ writes docs/reports/01-start-report.md

02-build.md\
→ reads 01-start-report.md\
→ writes 02-build-report.md

03-review.md\
→ reads 02-build-report.md\
→ writes 03-review-report.md

04-update-docs.md\
→ reads 03-review-report.md\
→ writes 04-update-docs-report.md

05-review-adr.md\
→ reads 04-update-docs-report.md\
→ writes 05-review-adr-report.md

06-complete.md\
→ reads 05-review-adr-report.md\
→ writes 06-complete-report.md


# Report Retention

Stage reports are working memory for the pipeline, not a permanent
audit log. Each stage report has exactly one file, and every run of
that stage overwrites the previous version:

* `docs/reports/01-start-report.md`
* `docs/reports/02-build-report.md`
* `docs/reports/03-review-report.md`
* `docs/reports/04-update-docs-report.md`
* `docs/reports/05-review-adr-report.md`
* `docs/reports/06-complete-report.md`

A report reflects only the most recently completed run of that stage.
Once a later phase overwrites a report, the prior phase's version of it
is not recoverable from `docs/reports/`. Durable outcomes of a phase —
what was built, what changed architecturally, what's outstanding — live
in `docs/snapshot.md`, `docs/adr-log.md`, and `docs/ai/state/phase-state.yaml`
instead, all of which persist across phases.

This is a deliberate v1 simplification, not an oversight: it avoids
`docs/reports/` accumulating an ever-growing archive that most sessions
never need to read. It is designed to evolve without restructuring —
a future revision may retain history by writing to a per-phase path
(for example, `docs/reports/phase-09/01-start-report.md`) instead of a
flat one, while keeping every other rule in this document — what each
stage may load, produce, and overwrite — unchanged.


# Phase State File

`docs/ai/state/phase-state.yaml` is the single authoritative record of
pipeline position: the active roadmap phase, its status, and the next SDLC
stage to run.

It has exactly two write zones:

| Field | Writer |
| --- | --- |
| `sdlc_stage` | Every stage (01–06). Each stage sets it to the next stage in sequence immediately after fulfilling its own responsibilities. |
| `current_phase`, `current_phase_name`, `roadmap_status` | Stage 6 (Complete Phase) only — updated only when the phase is verified complete, in the same action that resets `sdlc_stage` to `01-start`. |

No other stage may modify `current_phase`, `current_phase_name`, or
`roadmap_status`. No stage may add narrative content to this file.

This file is read-heavy: every stage loads it at the start of a session to
determine what to run next, without needing to parse `docs/snapshot.md` or
`docs/roadmap.md` in full.


# Stage 1 — Start Phase

Purpose

Prepare the current roadmap phase before implementation begins.

Prompt

* `01-start.md`

Stage Report

Produces:

* `docs/reports/01-start-report.md`

Responsibilities

Load the project context.

Determine:

* Current roadmap phase
* Current repository state
* Current implementation objective
* Current roadmap deliverables
* Implementation scope (in scope and out of scope)
* Architectural risks

Produce a high-level implementation plan.

Outputs

* Current phase
* Current objective
* Deliverables involved
* In scope
* Out of scope
* Repository areas likely to be affected.
* Domain concepts affected
* Architectural constraints
* Architectural risks
* Testing exceptions
* Implementation plan

No source code or documentation is modified.


# Stage 2 — Implementation

Purpose

Implement the approved roadmap phase within the approved Start Phase
scope.

Prompt

* `02-build.md`

Stage Report

Consumes:

* `docs/reports/01-start-report.md`

Produces:

* `docs/reports/02-build-report.md`

Responsibilities

Implement the approved roadmap phase.

Discover an implementation that satisfies the approved Start Phase
scope.

Preserve the project's documented architecture.

Include automated tests for each deliverable unless recorded as a
Testing Exception in the Start Phase report.

Run the project's quality gates before reporting completion.

Outputs

* Source code changes
* Tests added
* Quality gate results
* Architectural observations
* Follow-up work

Documentation is intentionally not updated during this stage.


# Stage 3 — Review Implementation

Purpose

Evaluate the completed implementation.

Prompt

* `03-review.md`

Stage Report

Consumes:

* `docs/reports/02-build-report.md`

Produces:

* `docs/reports/03-review-report.md`

Responsibilities

Review the completed implementation.

Evaluate:

* Architecture fitness
* DDD compliance
* Modular monolith boundary compliance
* Authentication specification compliance
* ADR compliance
* CQRS readiness
* Event-driven evolution readiness
* Compliance with the approved Start Phase scope
* Quality gate results reported by Implementation
* Test coverage of the phase's deliverables

Identify:

* Architectural drift
* Documentation drift
* Technical debt
* Scope creep

Recommend the next implementation step.

Outputs

* Architecture summary
* Implementation summary
* Architecture fitness
* DDD compliance
* Quality gate verification
* Test coverage verification
* Architectural drift
* Documentation drift
* Technical debt
* Recommended next implementation step

No files are modified.


# Stage 4 — Update Documents

Purpose

Synchronize implementation documentation with the completed source code.

Prompt

* `04-update-docs.md`

Stage Report

Consumes:

* `docs/reports/03-review-report.md`

Produces:

* `docs/reports/04-update-docs-report.md`

Responsibilities

Update implementation documentation.

Remove documentation drift.

Preserve document responsibilities.

Record the quality gate status verified by Review Implementation into
`docs/snapshot.md > Configured Tooling`.

Outputs

* Updated implementation documentation
* Quality gate status recorded
* Documentation summary
* Remaining documentation drift (if any)

Only implementation documentation is modified during this stage.


# Stage 5 — Review Architecture Decision Records

Purpose

Determine whether the completed implementation introduced a new permanent
architectural decision.

Prompt

* `05-review-adr.md`

Stage Report

Consumes:

* `docs/reports/04-update-docs-report.md`

Produces:

* `docs/reports/05-review-adr-report.md`

Responsibilities

Review the completed implementation.

Determine whether a new permanent architectural decision was introduced.

Create a new ADR only when required.

Otherwise confirm that the existing ADRs remain sufficient.

Outputs

* ADR decision
* Architectural reasoning
* Existing ADR coverage
* Documentation updated (if any)

Restrictions

This is the only stage permitted to modify:

* `docs/adr-log.md`

Existing ADRs are historical records and must never be modified,
reordered, or removed.


# Stage 6 — Complete Phase

Purpose

Verify that the approved roadmap phase has been completed successfully.

Prompt

* `06-complete.md`

Stage Report

Consumes:

* `docs/reports/05-review-adr-report.md`

Produces:

* `docs/reports/06-complete-report.md`

Responsibilities

Verify the completed implementation.

Confirm completion of the approved roadmap phase.

Confirm quality gates pass and test coverage exists for every
non-exempt deliverable, per Review Implementation's verified results.

Confirm readiness for the next roadmap phase.

Update implementation progress when appropriate.

Outputs

* Phase completion status
* Deliverables completed
* Architectural compliance
* Readiness for the next roadmap phase
* Documentation updated (if any)

Update Permissions

May update

* `docs/ai/state/phase-state.yaml`

Must not modify

* `README.md`
* `docs/auth-spec.md`
* `docs/adr-log.md`
* `docs/roadmap.md`
* `docs/snapshot.md`


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


# Review Repository Workflow

A Review Repository evaluation may be performed whenever the current implementation
state is uncertain or periodically to prevent documentation drift.

Prompt

* `review-repository.md`

The audit compares:

* Source code
* `snapshot.md`
* `roadmap.md`
* `docs/ai/state/phase-state.yaml`
* Independently re-run quality gate results

The audit reports:

* Current implementation
* Documentation drift
* Missing implementation
* Incorrect implementation status
* Roadmap alignment
* Phase state alignment
* Quality gate drift
* Test coverage gaps
* Recommended documentation updates

A Review Repository evaluation treats the source code as the source of truth.


# Stage Authority Model

Each SDLC stage has a single responsibility.

A stage may perform only the work assigned to it.

A stage must not perform work reserved for another stage.

The purpose of this model is to prevent architectural drift, scope creep, and documentation drift during AI-assisted development.

| Stage | May | May Not |
| --- | --- | --- |
| Start Phase | Interpret documentation, determine implementation scope, identify risks | Modify source code, modify documentation, introduce architectural decisions |
| Implementation | Modify source code within the approved Start Phase scope | Modify documentation, redefine roadmap scope, introduce new architectural decisions |
| Review Implementation | Evaluate implementation | Modify source code or documentation |
| Update Documents | Synchronize documentation with implementation | Change implementation or reinterpret architecture |
| Review Architecture Decision Records | Record new architectural decisions | Modify existing ADRs or implementation |
| Complete Phase | Verify roadmap completion and update implementation progress | Redesign architecture or expand implementation scope |

\
If implementation reveals a conflict with the approved scope,
implementation should stop and report the conflict rather than silently
changing scope.


If:

Repository uncertain

↓

Review Repository

If:

Architecture changed

↓

Review Architecture Decision Records

If:

Implementation complete

↓

Review Implementation

↓

Update Documents

↓

Review Architecture Decision Records

↓

Complete Phase


# Planning, Design and Implementation

The SDLC distinguishes planning from design and implementation.

Start Phase plans and defines what must be accomplished.

Implementation determines how to build it while respecting the project's
architecture.

Review Implementation evaluates whether the implementation preserved the
documented architecture.

Update Documents records the implementation exactly as it exists.

Review Architecture Decision Records records permanent architectural decisions introduced during implementation.

Complete Phase verifies that the implemented work satisfies the
approved scope.

Start Phase must not prescribe implementation classes, services, or
patterns unless already required by existing documentation or ADRs.

An implementation plan describes the sequence of work required to satisfy the approved scope. It does not prescribe concrete implementation classes, services, persistence models, or infrastructure patterns unless already required by project documentation or ADRs.


# Scope Control

Every implementation phase has an approved scope.

Start Phase establishes:

* In Scope
* Out of Scope
* Implementation Risks

Implementation must remain within that scope.

If implementation discovers:

* Conflicting requirements
* Architectural inconsistencies
* Missing prerequisites
* Roadmap conflicts

Implementation should stop and report the issue rather than extending
the implementation phase.

If implementation cannot proceed without changing scope:

1. Stop implementation
2. Report the conflict
3. Recommend the minimum documentation or roadmap change required
4. Resume only after the conflict has been resolved

Later-phase roadmap deliverables must not be implemented early unless
the roadmap or ADRs are intentionally updated.

Architectural constraints originate from:

* `README.md`
* `docs/adr-log.md`
* `docs/auth-spec.md`

Implementation constraints originate from:

* `docs/roadmap.md`
* `docs/snapshot.md`
* Current repository state


# Quality Gates

Every implementation phase should conclude by verifying:

* Static analysis
* Formatting/linting
* Automated tests
* All required quality gates defined by the current phase

unless the current roadmap phase explicitly prevents such verification.

Gate commands are defined once, in `docs/snapshot.md > Configured Tooling` 
— no other document restates them.

Responsibility is distributed across four stages:

| Stage | Role |
| --- | --- |
| Implementation | Runs the gates; fixes failures within approved scope |
| Review Implementation | Re-verifies Stage 2's reported results |
| Update Documents | Records the verified result in `snapshot.md` |
| Complete Phase | Refuses completion while any gate is reported failing |

If a roadmap phase genuinely cannot run a gate (for example, no tests
exist yet for a documentation-only phase), Start Phase must record that
exception explicitly in its Out of Scope section. An unrecorded gate
failure is never treated as an intentional exception.

Test Construction

Each roadmap deliverable includes its own automated tests as part of
being implemented — tests are not a separate deliverable and not
optional follow-up work. A passing `pytest` run that adds no tests
covering the phase's deliverables does not satisfy the quality gate,
even though the command exits successfully.

# Success Criteria

Every SDLC stage should define clear success criteria.

A stage is complete only when its required outputs have been produced and
its responsibilities have been fulfilled.

Completion of one stage authorizes progression to the next stage.


# Risk Management

Every implementation phase should explicitly identify and review:

* Architectural risks
* Operational risks
* Migration risks
* Future maintenance risks
* Testing risks

Review Implementation should evaluate whether these risks have changed as
a result of implementation.

Update Documents should document only risks that materially affect the
current repository implementation.

Complete Phase should summarize outstanding risks before the next
implementation phase begins.


# Decision Escalation

If implementation cannot proceed because of:

* Scope conflicts
* Architectural conflicts
* Repository inconsistencies
* Documentation drift

The SDLC pauses implementation and follows this escalation path:

Implementation

↓

Review Implementation

↓

Review Repository (if required)

↓

Reconcile Documents (if required)

↓

Resume Implementation

Escalation exists to preserve architectural integrity rather than allow
implementation to silently redefine project scope.


# Project Authority Model

Each project document has a single responsibility and is authoritative
only within that responsibility.

| Document                         | Authority                                   |
| -------------------------------- | ------------------------------------------- |
| Source code                      | Current implementation                      |
| `README.md`                      | Project vision and architectural intent     |
| `docs/auth-spec.md`              | Authentication behavior and business requirements |
| `docs/adr-log.md`                | Permanent architectural constraints (ADRs)  |
| `docs/roadmap.md`                | Implementation contract                     |
| `docs/snapshot.md`               | Current repository snapshot                 |
| `docs/ai/state/phase-state.yaml` | Current pipeline position (active phase, roadmap status, next SDLC stage) |
| `docs/ai/ai-sdlc.md`             | AI software development lifecycle specification, governance model, stage responsibilities, workflow constraints, quality gates, and escalation procedures. |

\
These documents complement one another rather than competing.

If inconsistencies are discovered, they indicate documentation drift,
implementation drift, or an architectural violation rather than a change
in authority.

Review Repository evaluations are used to identify and resolve these inconsistencies.


# Resolving Inconsistencies

When inconsistencies are discovered, determine which responsibility has
been violated.

| Inconsistency | Resolution |
| --- | --- |
| Source code differs from `snapshot.md` | Update `snapshot.md` |
| Source code differs from `phase-state.yaml` current phase | Correct `phase-state.yaml` via Stage 6, or complete the missing implementation if the roadmap contract has not yet been fulfilled |
| Source code violates an ADR | Correct the implementation or create a new ADR if the architecture has intentionally changed |
| Source code violates `auth-spec.md` | Correct the implementation unless the authentication requirements have intentionally changed |
| Source code no longer reflects the architectural vision in `README.md` | Review whether the implementation or the architectural vision should change. Architectural changes should normally be accompanied by a new ADR |

\
Review Repository evaluations are performed periodically to detect and eliminate drift between the implementation and the project documentation.


# Maintenance Prompts

The following prompts support long-term repository maintenance.

| Prompt | Purpose |
| --- | --- |
| `review-repository.md` | Audit the repository and detect implementation/documentation drift |
| `review-dependency.md` | Audit the repository and detect architecturally misaligned dependencies |
| `reconcile-docs.md` | Synchronize documentation with the audited repository state |

\
These prompts are not part of the normal implementation lifecycle.

They are used only when repository maintenance or architectural review is
required.


# Prompt Selection Guide

Use the following prompts depending on the work being performed.

| Situation | Prompt |
| --- | --- |
| Beginning implementation | `01-start.md` |
| Implementing the current roadmap step | `02-build.md` |
| Reviewing completed code | `03-review.md` |
| Updating implementation documentation | `04-update-docs.md` |
| Determining whether a new ADR is required | `05-review-adr.md` |
| Completing an entire roadmap phase | `06-complete.md` |
| Unsure whether documentation matches the repository | `review-repository.md` |
| Unsure whether dependencies match the repository | `review-dependency.md` |
| Repository documentation has drifted from the implementation | `reconcile-docs.md` |

\
The implementation prompts form the normal SDLC.

The maintenance prompts are used only when repository maintenance or
documentation reconciliation is required.


# Guiding Principle

Implementation always follows the documented architecture.

Documentation always follows the implementation.

Architecture changes only through new ADRs.

Each SDLC stage has a single responsibility and limited authority.

Start Phase defines scope.

Implementation produces working software.

Review Implementation evaluates implementation.

Update Documents records implementation.

Review Repository keeps all project artifacts aligned.

The source code remains the authoritative representation of the current
implementation.


Definition of Done

A roadmap phase is complete only when:

□ Roadmap deliverables are implemented
□ Architecture review passes
□ Documentation is synchronized
□ Architecture Decision Review completed
□ Quality gates pass (verified by Review Implementation, 
  gated by Complete Phase)
□ Phase completion verified