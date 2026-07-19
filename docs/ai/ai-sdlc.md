# AI-Assisted Software Development Lifecycle (SDLC)

Version 1.1

## Purpose

This document is the authoritative specification for the Governed AI
Software Development Lifecycle (AI SDLC).

It defines the lifecycle, governance model, authority model, stage
authority, workflow constraints, and quality gates used throughout the
project.

Each stage prompt is the authoritative execution contract for that stage.
Detailed responsibilities, inputs, outputs, and restrictions are defined
exclusively in that prompt. This document governs how stages relate to 
each other and to the project's documents — it does not restate any single 
stage's full instructions. Other documents may summarize this workflow but 
must not redefine or duplicate its governance.

Its goals are to:

* Maintain architectural consistency
* Preserve DDD-inspired boundaries
* Preserve modular monolith principles
* Preserve future CQRS adoption
* Preserve future event-driven evolution
* Minimize documentation drift
* Keep implementation and documentation synchronized

Each stage is invoked separately under the Level 0 execution model defined below.


# Workflow Automation Level

This project uses a **Level 0 governed AI workflow**.

Each SDLC stage is invoked separately by a human operator. The stage authorized to run is determined by `docs/ai/state/phase-state.yaml`.

The AI must execute only that stage and must not autonomously continue to another stage.


# AI Constitution

Every AI-assisted development session must:

* Preserve architectural boundaries
* Respect project document authority
* Execute only the stage authorized by `phase-state.yaml`
* Prefer explicit contracts over implicit behavior
* Minimize accidental complexity
* Preserve domain independence from infrastructure
* Avoid inventing implementation details
* Avoid reinterpreting project documentation
* Avoid treating implementation drift as authorization to change project intent
* Prefer refinement over redesign
* Leave the repository in a better state than it found it


# Project Artifact Map

| Artifact group | Artifacts | Purpose |
| --- | --- | --- |
| Project direction | `README.md` | Long-term vision and architectural philosophy |
| Project context | `docs/roadmap.md`, `docs/snapshot.md`, `docs/auth-spec.md`, `docs/adr-log.md` | Scope, implementation state, requirements, and architectural decisions |
| Workflow governance | `docs/ai/ai-sdlc.md` | Lifecycle governance, authority, transitions, and escalation |
| Workflow entry | `docs/ai/getting-started.md` | Onboarding and session guidance |
| Workflow state | `docs/ai/state/phase-state.yaml` | Current phase and authorized next stage |
| Executable workflows | `docs/ai/prompts/` | Development and maintenance execution contracts |
| Working evidence | `docs/reports/` | Stage outputs and handoffs |
| Implementation | Source code and tests | Current implementation facts |

These artifact groups have separate, non-competing responsibilities.
Their order does not represent an authority hierarchy or execution sequence.


# Document Authority

Each artifact is authoritative only within its defined responsibility:

| Artifact | Authority | Updated By | Change Frequency |
| --- | --- | --- | --- |
| Source code | Current implementation facts — ground truth for what exists | Stage 2 | Every implementation |
| `README.md` | Long-term project vision and architectural intent | Manual | Rare |
| `docs/roadmap.md` | Implementation contract — phase goals and deliverables, no status | Manual | Only when project scope changes |
| `docs/snapshot.md` | Current repository implementation | Stage 4; Reconcile Documents when verified drift exists | After approved implementation or reconciliation |
| `docs/auth-spec.md` | Authentication behavior and business requirements | Manual | Rare |
| `docs/adr-log.md` | Permanent architectural constraints (ADRs) | Stage 5 only, append-only | When a new ADR is required |
| `docs/ai/state/phase-state.yaml` | Current phase, authorized next SDLC stage, and whether it may proceed | Every stage (`sdlc_stage`, `sdlc_status`); Stage 6 normally owns phase fields; Reconcile Documents may correct verified state drift | Every successful transition, blocked outcome, or verified reconciliation |
| `docs/ai/ai-sdlc.md` | Governance, stage authority, escalation | Manual | Rare |

These documents have separate, non-competing areas of authority. If two
appear to disagree, that indicates documentation drift, implementation
drift, state drift, or an architectural violation — never an automatic
change in authority.

Source code is authoritative for implementation facts only.
It does not override project vision, requirements, roadmap scope, or ADRs.

## Resolving Inconsistencies

| Inconsistency | Resolution |
| --- | --- |
| `snapshot.md` differs from source code | Update `snapshot.md` through Stage 4 or Reconcile Documents |
| Source code differs from `phase-state.yaml`'s `current_phase` | Verify whether implementation or pipeline state has drifted, then correct the responsible artifact through the authorized workflow |
| Source code violates an ADR | Correct the implementation unless an intentional architectural change has been approved and recorded through the ADR workflow |
| Source code violates `auth-spec.md` | Correct the implementation unless an authentication requirement change has been explicitly approved |
| Source code no longer reflects the vision in `README.md` | Escalate for an explicit decision; do not treat the implementation as authority over project vision |

`review-repository.md` independently audits these authority relationships
and re-runs the configured quality gates.


# Starting a Session

Developers normally enter the workflow through `docs/ai/getting-started.md`,
which provides onboarding and session guidance.

Before executing any SDLC stage:

1. Load `docs/ai/ai-sdlc.md`.
2. Load `docs/ai/state/phase-state.yaml`.
3. Verify that `schema_version` is supported by this workflow.
4. Confirm the current phase, authorized next stage, and SDLC status.
5. Load the authorized prompt and its required context and reports.
6. Confirm repository implementation facts where required.
7. Execute the authorized prompt only when `sdlc_status: ready`.

If `schema_version` is missing or unsupported, do not execute a
development or maintenance prompt. Escalate for a manual governance
update without modifying pipeline state.

If `sdlc_status: blocked`, review the current stage report and resolve the
recorded conflict before execution resumes.

If repository or documentation state is uncertain, run
`review-repository.md` before continuing.

If drift is verified, use `reconcile-docs.md` only for artifacts within
its authority, then resume at the earliest SDLC stage invalidated by the
finding or correction.


# Lifecycle Overview

Every roadmap phase follows the same six-stage workflow:

| Order | Stage | Purpose |
| --- | --- | --- |
| 01 | Start Phase | Define scope, constraints, risks, and implementation plan |
| 02 | Implementation | Implement the approved phase scope and tests |
| 03 | Review Implementation | Verify architecture, scope, tests, and quality gates |
| 04 | Update Documents | Synchronize implementation documentation |
| 05 | Review ADR | Determine whether a new architectural decision must be recorded |
| 06 | Complete Phase | Verify completion and advance to the next roadmap phase |


# Stage Reference

Full responsibilities, outputs, and restrictions for each stage are
defined exclusively in its prompt file. This table governs only the
cross-cutting facts: what each stage is for, what it may write, and what
it must never touch.

Write permissions do not imply automatic advancement. Stage transitions
are governed by the reported outcome.

| Stage | Prompt | Responsibility | May Write | Must Not Modify | Report |
| --- | --- | --- | --- | --- | --- |
| 01 Start Phase | `01-start.md` | Interpret documentation; define scope, risks, and testing exceptions | `phase-state.yaml` (`sdlc_stage`, `sdlc_status` only) | Source code; any documentation; ADRs | `01-start-report.md` |
| 02 Implementation | `02-build.md` | Implement approved deliverables with tests; run quality gates | Source code; tests; `phase-state.yaml` (`sdlc_stage`, `sdlc_status`) | Documentation; ADRs; scope beyond Start Phase | `02-build-report.md` |
| 03 Review Implementation | `03-review.md` | Verify architecture fitness; re-run gates; verify test coverage | `phase-state.yaml` (`sdlc_stage`, `sdlc_status`) | Source code; documentation | `03-review-report.md` |
| 04 Update Documents | `04-update-docs.md` | Synchronize `snapshot.md`, including verified gate status | `snapshot.md` (implementation-detail sections); `phase-state.yaml` (`sdlc_stage`, `sdlc_status`) | Source code; `README.md`; `auth-spec.md`; `adr-log.md`; `roadmap.md`; `phase-state.yaml` phase fields | `04-update-docs-report.md` |
| 05 Review ADR | `05-review-adr.md` | Determine whether implementation introduced a new permanent architectural decision | `adr-log.md` (only if a new ADR is required, append-only); `phase-state.yaml` (`sdlc_stage`, `sdlc_status`) | Source code; `README.md`; `auth-spec.md`; `roadmap.md`; existing ADRs | `05-review-adr-report.md` |
| 06 Complete Phase | `06-complete.md` | Verify phase completion, including gate and test-coverage confirmation | `phase-state.yaml` (`current_phase`, `current_phase_name`, `roadmap_status`, `sdlc_stage`, `sdlc_status`) | `README.md`; `auth-spec.md`; `adr-log.md`; `roadmap.md`; `snapshot.md` | `06-complete-report.md` |

Each stage may also overwrite only the report assigned to it in the
`Report` column.

A stage prompt governs execution of its stage but does not override
`README.md`, `docs/roadmap.md`, `docs/auth-spec.md`, `docs/adr-log.md`,
`docs/ai/state/phase-state.yaml`, or this document. This is what prevents
architectural drift, scope creep, and documentation drift during AI-assisted
development.

Start Phase plans *what* must be accomplished, not *how* — it must not
prescribe concrete implementation classes, services, persistence models,
or infrastructure patterns unless already required by existing
documentation or ADRs.


# Stage Outcomes and Transitions

Every stage report must record an explicit outcome.

Pipeline state is updated according to that outcome:

* A successful outcome advances to the next stage with
  `sdlc_status: ready`.
* An outcome requiring corrective work routes to the earliest invalidated
  stage with `sdlc_status: ready`.
* An unresolved conflict that prevents further work routes to the earliest
  invalidated stage with `sdlc_status: blocked`.

`changes_required` is not itself a blocked state. Use `blocked` only when
the selected stage cannot proceed until an external conflict, approval,
or repository inconsistency is resolved.

The stage report must be persisted before `phase-state.yaml` is updated.
If the report cannot be persisted, do not change pipeline state.

| Stage | Successful outcome | Successful transition | Corrective transition |
| --- | --- | --- | --- |
| 01 Start Phase | `approved` | `02-build` | Remain at `01-start` with `blocked` |
| 02 Implementation | `completed` | `03-review` | `01-start` if approved scope is invalidated; otherwise remain at `02-build` with `blocked` |
| 03 Review Implementation | `approved` | `04-update-docs` | `02-build` when implementation changes are required |
| 04 Update Documents | `synchronized` | `05-review-adr` | Remain at `04-update-docs` with `blocked` |
| 05 Review ADR | `completed` | `06-complete` | `02-build` to revert implementation drift, or `01-start` when an intentional architecture change requires approval |
| 06 Complete Phase | `phase_complete` | Next phase at `01-start`, or `complete` when the final roadmap phase is completed | Earliest stage invalidated by the completion finding |

If Stage 6 completes the final roadmap phase:

* Keep `current_phase` and `current_phase_name` set to the completed final phase
* Set `roadmap_status: complete`
* Set `sdlc_stage: complete`
* Keep `sdlc_status: ready`

This represents a completed roadmap rather than an authorized new
development stage. Further development requires an intentional roadmap
update.


# Phase Completion Checklist

A roadmap phase is complete only when Stage 6 has confirmed all of the
following:

* Roadmap deliverables are implemented
* Stage 3 outcome is `approved`
* Stage 4 outcome is `synchronized`
* Stage 5 outcome is `completed`
* Quality gates pass, with test coverage confirmed for every non-exempt
  deliverable
* Phase completion is verified against the approved Start Phase scope


# External Architecture Review (Optional)

After Stage 3, the Architecture Review Report may be reviewed externally
— by a human architect, technical lead, or a separate AI session. Typical
review topics include aggregate boundaries, DDD compliance, repository
boundaries, CQRS readiness, event-driven evolution, authentication state
machine design, and service extraction readiness. Possible outcomes:
Approved, Approved with recommendations, Changes required.


# Phase State File

`docs/ai/state/phase-state.yaml` is the single authoritative record of
pipeline state: the active roadmap phase, the next SDLC stage to run,
whether that stage may proceed, or whether the roadmap has reached its
terminal completed state.

Field ownership is divided as follows:

| Field | Writer |
| --- | --- |
| `schema_version` | Manual governance change only |
| `sdlc_stage` | Every stage (01–06). Each stage sets it according to its recorded outcome and the transition rules above. |
| `sdlc_status` | Every stage (01–06). Set to `ready` when the selected stage may proceed and `blocked` when a conflict prevents progress. |
| `current_phase`, `current_phase_name`, `roadmap_status` | Stage 6 during normal lifecycle progression; Reconcile Documents only when verified state drift exists |

`schema_version` identifies the structure of the state file. Numbered
stages and maintenance prompts must not modify it.

## Phase-State Invariants

| Condition | Required state |
| --- | --- |
| Active roadmap phase | `roadmap_status: current` |
| Executable numbered stage | `sdlc_stage: 01-start` through `06-complete` |
| Stage may execute | `sdlc_status: ready` |
| Unresolved conflict | `sdlc_status: blocked` |
| Roadmap completed | `roadmap_status: complete`, `sdlc_stage: complete`, `sdlc_status: ready` |

Any other combination must be treated as state drift and audited before
normal execution continues.

When a stage is blocked:

* Retain the stage that must resume in `sdlc_stage`.
* Set `sdlc_status: blocked`.
* Record the reason and required resolution in the current stage report.

When `sdlc_stage: complete`:

* No numbered development stage is authorized.
* `roadmap_status` must be `complete`.
* `sdlc_status` must be `ready`.
* Further development requires an intentional roadmap update followed by
  authorization of a new `01-start` stage.

When the conflict is resolved, set `sdlc_status: ready` and resume at the
earliest stage invalidated by the finding or correction.

No numbered stage other than Stage 6 may modify `current_phase`,
`current_phase_name`, or `roadmap_status`. Reconcile Documents is the
sole maintenance-recovery exception. No workflow may add block reasons or other narrative content to this file.

This file is read-heavy: every stage loads it at the start of a session
to determine what to run next, without needing to parse `docs/snapshot.md`
or `docs/roadmap.md` in full.


# Stage Reports & Retention

Each SDLC stage produces a report that becomes handoff evidence for one
or more later stages, as defined by the report-dependency table below.
Reports are stored under `docs/reports/` and belong to the current
roadmap phase.

Terminology:

* Roadmap phase = implementation unit defined in `docs/roadmap.md`
* SDLC stage = one workflow step executed by a prompt
* Stage report = working artifact passed between SDLC stages

## Report Metadata

Every numbered stage report must begin with YAML front matter:

```yaml
---
phase:
phase_name:
stage:
outcome:
next_stage:
---
```

Metadata values must reflect the current roadmap phase, the producing
stage, its recorded outcome, and the resulting `sdlc_stage`.

Before consuming a report, a stage must verify that:

* `phase` matches `phase-state.yaml > current_phase`
* `stage` matches the expected producing stage
* `outcome` authorizes the current stage
* `next_stage` matches the expected transition from the producing stage

The immediate predecessor report must also record `next_stage` matching
`phase-state.yaml > sdlc_stage`.

A report that fails validation must not be used.

Maintenance reports must begin with YAML front matter containing:

```yaml
---
phase:
phase_name:
workflow:
outcome:
next_action:
---
```

Maintenance prompts use `workflow` and `next_action` rather than `stage`
and `next_stage`.

## Report Write Order

Stages must apply writes in this order:

1. Complete the stage work.
2. Determine the outcome and resulting next stage.
3. Persist the stage report with its metadata.
4. Verify that the report was persisted.
5. Update `phase-state.yaml`.

If the report cannot be persisted, do not update `phase-state.yaml`.

When replacing an existing report, a stage must complete the new report
before overwriting the prior valid report. It must not truncate, delete,
or partially replace the existing report before the replacement is ready
to persist.

Report dependencies:

| Stage | Reports loaded | Report written |
| --- | --- | --- |
| `01-start.md` | None | `01-start-report.md` |
| `02-build.md` | `01-start-report.md` | `02-build-report.md` |
| `03-review.md` | `01-start-report.md`, `02-build-report.md` | `03-review-report.md` |
| `04-update-docs.md` | `03-review-report.md` | `04-update-docs-report.md` |
| `05-review-adr.md` | `02-build-report.md`, `03-review-report.md`, `04-update-docs-report.md` | `05-review-adr-report.md` |
| `06-complete.md` | `01-start-report.md`, `03-review-report.md`, `04-update-docs-report.md`, `05-review-adr-report.md` | `06-complete-report.md` |

**Retention.** Each stage report has exactly one file, and every run of
that stage overwrites the previous version. A report reflects only the
most recently completed run of that stage — once a later phase overwrites
it, the prior version is not recoverable from `docs/reports/`. Reports
are working memory for the pipeline, not a permanent audit log. Durable
outcomes of a phase live in `docs/snapshot.md`, `docs/adr-log.md`, and
`docs/ai/state/phase-state.yaml` instead, all of which persist across
phases.

This is a deliberate v1 simplification, not an oversight: it avoids
`docs/reports/` accumulating an archive most sessions never need to read.
It is designed to evolve without restructuring — a future revision may
retain history by writing to a per-phase path (for example,
`docs/reports/phase-09/01-start-report.md`) instead of a flat one, while
every other rule in this document stays unchanged.


# Scope Control

Every implementation phase has an approved scope. Start Phase establishes:

* In Scope
* Out of Scope
* Architectural, operational, migration, maintenance, and testing risks
* Testing Exceptions

Implementation must remain within that scope. If Implementation discovers
conflicting requirements, architectural inconsistencies, missing
prerequisites, or roadmap conflicts, it should stop and report the issue
rather than silently extending the phase:

1. Stop implementation.
2. Report the conflict.
3. Identify the earliest SDLC stage invalidated by the conflict.
4. Recommend the minimum authorized change required.
5. Resume only after the conflict has been resolved through the appropriate workflow.

While the conflict remains unresolved, retain the appropriate
`sdlc_stage` and set `sdlc_status: blocked`.

Later-phase roadmap deliverables must not be implemented early unless the
roadmap has been intentionally updated first.

Architectural constraints originate from `README.md`, `docs/adr-log.md`,
and the architectural requirements in `docs/auth-spec.md`.

Behavioral requirements originate from `docs/auth-spec.md`.

Implementation scope originates from `docs/roadmap.md` and the approved
Start Phase report.

`docs/snapshot.md` and the current repository state describe existing
implementation conditions and constraints; they do not authorize scope
expansion.


# Quality Gates

Every implementation phase concludes by verifying static analysis,
formatting/linting, and automated tests, unless the current roadmap phase
explicitly prevents such verification. Gate commands are defined once, in
`docs/snapshot.md > Configured Tooling` — no other document restates
them. Stage-by-stage gate responsibility is defined in Stage Reference.

**Test Construction.** Each roadmap deliverable includes its own
automated tests as part of being implemented — tests are not a separate
deliverable and not optional follow-up work. A passing test run that adds
no tests covering the phase's deliverables does not satisfy the quality
gate, even though the command exits successfully.

**Testing Exceptions.** If a deliverable genuinely has no executable
behavior to test (for example, documentation or folder scaffolding),
Start Phase must record that explicitly as a Testing Exception, with a
one-line reason. Review Implementation confirms each claimed exception is
legitimate. An unrecorded gate or coverage failure is never treated as an
intentional exception.


# Risk Management

Every implementation phase must explicitly identify and review:

* Architectural risks
* Operational risks
* Migration risks
* Maintenance risks
* Testing risks

Risk responsibility is distributed across the lifecycle:

| Stage | Risk responsibility |
| --- | --- |
| Start Phase | Identify the initial risks in all five categories |
| Implementation | Report risks newly discovered, resolved, increased, or reduced during implementation |
| Review Implementation | Independently reassess all five categories and identify material current risks |
| Update Documents | Record only material risks that currently affect the implemented repository |
| Review ADR | Identify risks introduced or changed by any newly recorded permanent architectural decision |
| Complete Phase | Summarize accepted outstanding risks and confirm that none blocks phase completion |

A risk category may record `None identified`, but it must not be omitted.


# Decision Escalation

If implementation cannot proceed because of scope conflicts,
architectural conflicts, repository inconsistencies, or documentation
drift, the SDLC pauses and resumes at the earliest stage invalidated by
the finding or correction.

Run `review-repository.md` when repository state is uncertain and
`reconcile-docs.md` when verified drift falls within its authority.

| Finding | Resume at |
| --- | --- |
| Only `snapshot.md` implementation details were corrected | The previously interrupted numbered stage |
| Only `phase-state.yaml` drift was corrected | The stage identified by the corrected `sdlc_stage` |
| An approved manual change was made to `README.md`, `roadmap.md`, or `auth-spec.md` | `01-start` |
| Scope, roadmap, requirements, or architectural assumptions changed | `01-start` |
| Implementation changes are required | `02-build` |
| Architecture review must be repeated | `03-review` |
| Implementation documentation remains unsynchronized | `04-update-docs` |
| ADR review remains incomplete | `05-review-adr` |

When multiple findings invalidate different stages, resume at the
earliest invalidated numbered stage.

Maintenance prompts do not replace that numbered stage. They correct or
classify drift and then route the workflow back to the appropriate
development stage.

Escalation exists to preserve architectural integrity rather than allow
implementation to silently redefine project scope.

Set `sdlc_status: blocked` only while an unresolved conflict prevents the
selected corrective stage from proceeding.

When corrective work is already identified and may proceed, set
`sdlc_status: ready` and resume at the earliest invalidated stage.


# Prompt Selection Guide

The six numbered prompts form the normal SDLC. The three maintenance
prompts supplement it — used only when repository maintenance or
documentation reconciliation is required — and do not replace it.

## Maintenance Prompt Authority

| Prompt | May Write | Must Not Modify | Report |
| --- | --- | --- | --- |
| `review-repository.md` | `review-repository-report.md` only | Source code; project documentation; `phase-state.yaml` | `review-repository-report.md` |
| `review-dependency.md` | `review-dependency-report.md` only | Source code; project documentation; `phase-state.yaml` | `review-dependency-report.md` |
| `reconcile-docs.md` | `snapshot.md` (implementation-detail sections); `phase-state.yaml`, including `sdlc_status`, only when verified state drift exists; `reconcile-docs-report.md` | Source code; `README.md`; `roadmap.md`; `auth-spec.md`; `adr-log.md` | `reconcile-docs-report.md` |

Stage 6 is the sole normal lifecycle writer of `current_phase`,
`current_phase_name`, and `roadmap_status`.

`reconcile-docs.md` is the sole maintenance-recovery exception and may
modify `phase-state.yaml` only when `review-repository.md` has verified
that the state file itself has drifted.

Changes to `README.md`, `roadmap.md`, or `auth-spec.md` must be approved
and performed outside the Reconcile Documents workflow.

| Situation | Prompt |
| --- | --- |
| Beginning a roadmap phase | `01-start.md` |
| Implementing the current roadmap phase | `02-build.md` |
| Reviewing completed implementation | `03-review.md` |
| Synchronizing documentation | `04-update-docs.md` |
| Determining whether a new ADR is required | `05-review-adr.md` |
| Completing a roadmap phase | `06-complete.md` |
| Unsure whether documentation matches the repository | `review-repository.md` |
| `snapshot.md` or `phase-state.yaml` has verified documentation or state drift | `reconcile-docs.md` |
| Unsure whether dependencies match the documented architecture | `review-dependency.md` |


# Guiding Principle

Implementation must conform to the approved documented architecture.

Implementation documentation follows the implementation.

Normative documentation changes only through its authorized governance
process.

Approved permanent architecture changes are recorded through new ADRs.

Each SDLC stage has a single responsibility and limited authority.

Source code is authoritative only for current implementation facts.

The repository should always be left in a better state than it was
found.