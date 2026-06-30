# Document Reconciliation

# Purpose

Recover from documentation drift by aligning the project documentation with
the current repository implementation.

This prompt is intended for maintenance use after a repository audit has
identified significant documentation drift.

It updates documentation only.

It does not modify source code.

---

# Inputs

Review:

* Repository Audit Report
* `README.md`
* `docs/project-handover.md`
* `docs/roadmap.md`
* `docs/authentication-spec.md`
* `docs/decisions.md`

---

# Project Authority Model

Use the Project Authority Model when resolving inconsistencies.

| Authority                 | Source                        |
| ------------------------- | ----------------------------- |
| Current implementation    | Source code                   |
| Project vision            | `README.md`                   |
| Authentication behavior   | `docs/authentication-spec.md` |
| Architectural constraints | `docs/decisions.md`           |
| Implementation contract   | `docs/roadmap.md`             |
| Repository snapshot       | `docs/project-handover.md`    |

Determine which artifact has drifted before making any changes.

Do not assume any single document is universally correct.

---

# Responsibilities

Synchronize the documentation with the current repository while preserving
the responsibilities of each document.

---

## project-handover.md

Rewrite as the current repository snapshot.

Update only:

* Repository status
* Current phase
* Current implementation
* Implemented contexts
* Implemented layers
* Implemented domain concepts
* Implemented infrastructure
* Configured tooling
* Outstanding implementation
* Reference documents

Do not include:

* Long-term architectural intent
* Future implementation plans
* Architectural rationale

---

## roadmap.md

Rewrite as the implementation contract.

Update only:

* Phase status
* Deliverable completion
* Current phase progress

Preserve:

* Overall project vision
* Phase goals
* Future phases
* Planned deliverables

Do not include:

* Repository implementation details
* Code-level descriptions
* Architecture rationale

---

## README.md

Do not modify.

The README defines the project's long-term vision and architectural intent.

Only update this document if the Repository Audit Report identifies a
genuine inconsistency between the documented vision and the intended
architecture.

---

## authentication-spec.md

Do not modify.

Only update this document if the Repository Audit Report identifies a
genuine error or approved change in authentication requirements.

Implementation progress alone is never a reason to modify this document.

---

## decisions.md

Do not modify.

Architectural Decision Records are maintained exclusively through
`adr-audit.md`.

Historical ADRs must never be rewritten.

---

# Output

Produce:

* Updated `project-handover.md`
* Updated `roadmap.md`

If the Repository Audit Report identifies genuine inconsistencies in
`README.md` or `authentication-spec.md`, explain them but do not modify
those documents.

If the Repository Audit Report identifies a new architectural decision,
recommend running `adr-audit.md`.

---

# Rules

* Modify documentation only.
* Do not modify source code.
* Preserve the responsibility of every project document.
* Preserve the project vision.
* Preserve authentication behavior.
* Preserve all historical ADRs.
* Do not invent implemented features.
* Do not remove planned roadmap deliverables.
* Distinguish clearly between implementation drift,
  documentation drift, and architectural drift.
* Report any unresolved inconsistencies.

---

# Expected Output

Report:

1. Files updated
2. Summary of changes
3. Files intentionally not modified
4. Remaining documentation drift, if any

Do not report Git status or unrelated repository information.