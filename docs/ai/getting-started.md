# Getting Started with the Governed AI Software Development Lifecycle

## Purpose

This guide explains how developers, reviewers, maintainers, architects,
and AI assistants enter and navigate the Governed AI Software Development
Lifecycle.

It provides onboarding and workflow-routing guidance only.

Workflow authority, document ownership, stage transitions, and escalation
rules are defined in:

* `docs/ai/ai-sdlc.md`


# Core Idea

Development follows a governed AI-assisted software development lifecycle.

The objective is not simply to generate code.

The objective is to preserve architecture, maintain documentation accuracy, control implementation scope, and keep development aligned with the project roadmap.

Every implementation session follows a defined SDLC stage.


# Workflow Execution

The project uses a **Level 0 governed AI workflow**.

Read `docs/ai/state/phase-state.yaml`, execute only the authorized stage prompt, and stop when that stage is complete.

Workflow authority and transition rules are defined in:

* `docs/ai/ai-sdlc.md`


# Project Documentation

Load these every session, before executing any SDLC stage:

| Document | Responsibility |
| --- | --- |
| `README.md` | Project vision and architectural direction |
| `docs/roadmap.md` | Implementation contract — phase goals and deliverables |
| `docs/snapshot.md` | Current repository implementation |
| `docs/auth-spec.md` | Authentication behavior and business requirements |
| `docs/adr-log.md` | Permanent architectural decisions |
| `docs/ai/state/phase-state.yaml` | Current phase, roadmap status, and next SDLC stage |

`docs/ai/ai-sdlc.md` governs authority, transitions, escalation, and
document ownership across stages. It must be loaded before executing
any development stage.

Each document and prompt is authoritative only within its defined responsibility.
Stage prompts govern stage execution but do not override project documentation or `docs/ai/ai-sdlc.md`.


# Reading Order

Onboarding, read once:

1. README.md
2. docs/ai/getting-started.md
3. docs/ai/ai-sdlc.md

This establishes project vision, then workflow, then governance, before
touching any stage-specific content.

Every session:

1. `docs/ai/ai-sdlc.md` — workflow governance and authority
2. `docs/ai/state/phase-state.yaml` — current phase, authorized stage,
   and SDLC status
3. The prompt authorized by `phase-state.yaml`
4. The project context required by that prompt
5. Any reports required by that prompt


# Starting a Development Session

Begin every new ChatGPT, Codex, or development session by:

1. Load `docs/ai/ai-sdlc.md`.
2. Load `docs/ai/state/phase-state.yaml`.
3. Verify that `schema_version` is supported.
4. Confirm the current phase, authorized stage, and `sdlc_status`.
5. Load the authorized prompt and its required context and reports.
6. Execute only that stage when `sdlc_status: ready`.

If `sdlc_status: blocked`, review the current stage report and resolve the
recorded conflict before resuming the workflow.

If repository or documentation state is uncertain, run `review-repository.md` 
before continuing.


# Standard Development Workflow

Every roadmap phase follows the same six-stage workflow.

| Stage                                | Prompt                                          |
| ------------------------------------ | ----------------------------------------------- |
| Start Phase                          | `docs/ai/prompts/development/01-start.md`       |
| Implementation                       | `docs/ai/prompts/development/02-build.md`       |
| Review Implementation                | `docs/ai/prompts/development/03-review.md`      |
| Update Documents                     | `docs/ai/prompts/development/04-update-docs.md` |
| Review Architecture Decision Records | `docs/ai/prompts/development/05-review-adr.md`  |
| Complete Phase                       | `docs/ai/prompts/development/06-complete.md`    |

Each stage produces a working report that becomes handoff evidence for
one or more later stages, as defined in `docs/ai/ai-sdlc.md`.

| Stage Report                 | File                                    |
| ---------------------------- | --------------------------------------- |
| Start Phase Report           | `docs/reports/01-start-report.md`       |
| Implementation Report        | `docs/reports/02-build-report.md`       |
| Review Implementation Report | `docs/reports/03-review-report.md`      |
| Update Documents Report      | `docs/reports/04-update-docs-report.md` |
| Review ADR Report            | `docs/reports/05-review-adr-report.md`  |
| Complete Phase Report        | `docs/reports/06-complete-report.md`    |

Detailed responsibilities, inputs, outputs, and success criteria for
each stage are defined in its own prompt file, listed above. Cross-stage
governance — authority, escalation, and document ownership — is defined
in:

* `docs/ai/ai-sdlc.md`

---

# Repository Maintenance Workflow

Maintenance prompts are used when repository state is uncertain or periodic maintenance is required.

| Situation                     | Prompt                                             |
| ----------------------------- | -------------------------------------------------- |
| Review repository state       | `docs/ai/prompts/maintenance/review-repository.md` |
| Reconcile documentation drift | `docs/ai/prompts/maintenance/reconcile-docs.md`    |
| Review dependency health      | `docs/ai/prompts/maintenance/review-dependency.md` |

Associated reports:

| Report                              | File                                       |
| ----------------------------------- | ------------------------------------------ |
| Repository Review Report            | `docs/reports/review-repository-report.md` |
| Documentation Reconciliation Report | `docs/reports/reconcile-docs-report.md`    |
| Dependency Review Report            | `docs/reports/review-dependency-report.md` |

Maintenance prompts supplement the normal SDLC and do not replace it.

---

# Stage Responsibilities

The AI SDLC intentionally assigns a single responsibility to each stage.

Each stage's detailed responsibilities, inputs, and outputs are defined
exclusively in its own prompt file, under `docs/ai/prompts/`. Governance
rules, authority models, quality gates, scope control, escalation
procedures, and document update permissions are defined exclusively in:

* `docs/ai/ai-sdlc.md`

This guide intentionally summarizes the workflow rather than duplicating
either the SDLC specification or any individual prompt's instructions.

---

# Team Adoption

The workflow supports both individual and team-based development.

Typical responsibilities are:

| Role                        | Typical Stages                       |
| --------------------------- | ------------------------------------ |
| Developer                   | Start Phase, Implementation          |
| Reviewer                    | Review Implementation                |
| Maintainer                  | Update Documents                     |
| Architect or Technical Lead | Review Architecture Decision Records |
| Project Owner               | Complete Phase                       |

A single developer or AI assistant may perform multiple roles across
separate stage invocations.


# Need Help Choosing a Prompt?

This table provides navigation guidance only. During the normal SDLC,
`phase-state.yaml` determines which numbered prompt is authorized to run.

| If you need to...                       | Use...                 |
| --------------------------------------- | ---------------------- |
| Begin a roadmap phase                   | `01-start.md`          |
| Implement approved work                 | `02-build.md`          |
| Review completed implementation         | `03-review.md`         |
| Synchronize documentation               | `04-update-docs.md`    |
| Determine whether a new ADR is required | `05-review-adr.md`     |
| Complete a roadmap phase                | `06-complete.md`       |
| Audit repository state                  | `review-repository.md` |
| Reconcile documentation                 | `reconcile-docs.md`    |
| Review project dependencies             | `review-dependency.md` |

---

# Guiding Principle

The repository should always be left in a better state than it was found.

Every completed roadmap phase should improve:

* Implementation
* Documentation
* Architectural consistency
* Maintainability

The SDLC provides the governance that preserves those goals throughout the lifetime of the project.