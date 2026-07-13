# Getting Started with the Governed AI Software Development Lifecycle

## Purpose

This guide explains how to begin working on the project using the Governed AI Software Development Lifecycle (AI SDLC).

It is intended for developers, reviewers, maintainers, architects, and AI assistants working in the repository.

This guide provides project orientation, explains how to begin a development session, and identifies the appropriate workflow and prompts.

The authoritative definition of the AI SDLC, including stage responsibilities, governance rules, authority models, and workflow constraints, is maintained in:

* `docs/ai/ai-sdlc.md`

---

# Core Idea

Development follows a governed AI-assisted software development lifecycle.

The objective is not simply to generate code.

The objective is to preserve architecture, maintain documentation accuracy, control implementation scope, and keep development aligned with the project roadmap.

Every implementation session follows a defined SDLC stage.

---

# Project Documentation

Before beginning work, load the project's authoritative documentation.

| Document                         | Responsibility                                                 |
| -------------------------------- | -------------------------------------------------------------- |
| `README.md`                      | Project vision and architectural direction                     |
| `docs/roadmap.md`                | Implementation contract — phase goals and deliverables         |
| `docs/snapshot.md`               | Current repository implementation                              |
| `docs/auth-spec.md`              | Authentication behavior and business requirements              |
| `docs/adr-log.md`                | Permanent architectural decisions                              |
| `docs/ai/state/phase-state.yaml` | Current phase, roadmap status, and next SDLC stage |
| `docs/ai/ai-sdlc.md`             | AI SDLC governance, workflow, and stage responsibilities       |

Each document is authoritative only within its defined responsibility.

---

# Reading Order

New contributors should normally read the project documentation in the
following order:

1. README.md
2. docs/ai/getting-started.md
3. docs/ai/ai-sdlc.md
4. The prompt for the current SDLC stage
5. The current stage report (if one exists)

This order establishes project vision before workflow and workflow before
implementation.

---

# Starting a Development Session

Begin every new ChatGPT, Codex, or development session by:

1. Loading the project documentation listed above.
2. Determining the current roadmap phase and next SDLC stage 
   from `docs/ai/state/phase-state.yaml`.
3. Confirming the current repository state from `docs/snapshot.md`.
4. Selecting the appropriate prompt for the work being performed.
5. Executing only that SDLC stage.

If the current repository state is uncertain, perform a repository review before beginning implementation.

---

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

Each stage produces a working report that becomes the input to the next stage.

| Stage Report                 | File                                    |
| ---------------------------- | --------------------------------------- |
| Start Phase Report           | `docs/reports/01-start-report.md`       |
| Implementation Report        | `docs/reports/02-build-report.md`       |
| Review Implementation Report | `docs/reports/03-review-report.md`      |
| Update Documents Report      | `docs/reports/04-update-docs-report.md` |
| Review ADR Report            | `docs/reports/05-review-adr-report.md`  |
| Complete Phase Report        | `docs/reports/06-complete-report.md`    |

Detailed responsibilities, permissions, inputs, outputs, and success criteria for each stage are defined in:

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

Stage responsibilities, governance rules, authority models, quality gates, scope control, escalation procedures, stage reports, and document update permissions are defined exclusively in:

* `docs/ai/ai-sdlc.md`

This guide intentionally summarizes the workflow rather than duplicating the SDLC specification.

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

A single developer or AI assistant may perform multiple roles when appropriate.

---

# Need Help Choosing a Prompt?

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