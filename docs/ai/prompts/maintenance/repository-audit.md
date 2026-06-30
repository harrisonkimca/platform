# Repository Audit

## Purpose

Audit the current repository implementation and identify any drift between
the implementation and the project documentation.

Responsibilities

* Inspect the entire repository.
* Compare the implementation against the project context documents.
* Verify roadmap progress.
* Verify the project handover.
* Detect implementation drift.
* Detect documentation drift.
* Recommend documentation updates where required.

This prompt produces an audit report only.

It does not modify source code or documentation.

---

# Reference Documents

Review:

* `README.md`
* `docs/project-handover.md`
* `docs/roadmap.md`
* `docs/authentication-spec.md`
* `docs/decisions.md`

Then inspect the entire repository.

---

# Project Authority Model

Use the following authority model during the audit.

| Authority                 | Source                        |
| ------------------------- | ----------------------------- |
| Current implementation    | Source code                   |
| Project vision            | `README.md`                   |
| Authentication behavior   | `docs/authentication-spec.md` |
| Architectural constraints | `docs/decisions.md`           |
| Implementation contract   | `docs/roadmap.md`             |
| Repository snapshot       | `docs/project-handover.md`    |

When inconsistencies are found, identify which responsibility has drifted.

Do not automatically assume the source code or documentation is correct.

---

# Audit Report

Produce a report containing:

## 1. Repository Summary

* Current phase
* Current implementation status
* Overall repository health

---

## 2. Implemented Contexts

Report:

* Implemented bounded contexts
* Placeholder contexts

---

## 3. Implemented Layers

For each implemented context report:

* Domain
* Application
* Infrastructure
* Presentation

Identify whether each layer is:

* Implemented
* Partial
* Skeleton only
* Not implemented

---

## 4. Implemented Domain Concepts

Report:

* Entities
* Value Objects
* Enumerations
* Domain Services
* Repository Contracts
* Provider Contracts
* Authentication State Machine Contracts
* Domain Events

---

## 5. Implemented Application Concepts

Report:

* Commands
* Queries
* Handlers
* DTOs
* Application Services
* Workflows

---

## 6. Implemented Infrastructure

Report:

* Persistence
* Repository implementations
* Database models
* Migrations
* External providers
* Event infrastructure
* Messaging
* Docker
* Environment configuration

---

## 7. Tooling

Report:

* Tooling configured
* Quality gates
* CI/CD
* Test framework

Include the current status of:

* Pyright
* Ruff
* pytest

---

## 8. Test Coverage

Summarize:

* Areas covered
* Areas not covered

---

## 9. Roadmap Audit

Compare the implementation against `docs/roadmap.md`.

Identify:

* Completed deliverables
* Missing deliverables
* Incorrect implementation status
* Phase completion status

---

## 10. Project Handover Audit

Compare the implementation against `docs/project-handover.md`.

Identify:

* Missing implemented concepts
* Incorrect implementation status
* Repository snapshot inaccuracies

---

## 11. Authentication Specification Audit

Compare the implementation against
`docs/authentication-spec.md`.

Identify:

* Implemented requirements
* Missing requirements
* Deviations from the specification

---

## 12. ADR Audit

Compare the implementation against
`docs/decisions.md`.

For each ADR report:

* Implemented
* Partially Implemented
* Not Implemented
* Violated

Identify any implementation that appears to violate an ADR.

---

## 13. Documentation Drift

Report:

* Drift against `project-handover.md`
* Drift against `roadmap.md`
* Drift against `README.md`
* Drift against `authentication-spec.md`
* Drift against `decisions.md`

---

## 14. Recommendations

Provide:

* Recommended updates to `project-handover.md`
* Recommended updates to `roadmap.md`
* Whether an ADR audit should be performed
* Whether a phase completion review is recommended

---

# Rules

* Inspect the entire repository.
* Treat the repository as the current implementation.
* Do not modify any files.
* Do not propose architecture beyond the documented roadmap.
* Do not recommend changing `README.md`,
  `authentication-spec.md`, or `decisions.md` unless a genuine
  inconsistency is discovered.
* Distinguish clearly between implementation drift and documentation drift.
* Report only the current repository state.

---

# Expected Output

Produce a repository audit report containing only:

1. Repository summary
2. Implemented contexts
3. Implemented layers
4. Implemented domain concepts
5. Implemented application concepts
6. Implemented infrastructure
7. Tooling
8. Test coverage
9. Roadmap audit
10. Project handover audit
11. Authentication specification audit
12. ADR audit
13. Documentation drift
14. Recommendations

Do not propose future architecture beyond the documented roadmap.
Do not report Git status unless explicitly requested.