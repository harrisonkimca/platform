# Dependency Audit

## Purpose

Audit the project's dependencies to ensure they remain necessary,
consistent with the architecture, and aligned with the project's long-term
design goals.

This prompt is intended for periodic maintenance.

It produces an audit report only.

It does not modify source code or project documentation.

---

# Reference Documents

Review:

* `README.md`
* `docs/roadmap.md`
* `docs/decisions.md`

Inspect:

* `pyproject.toml`
* `uv.lock`
* `Dockerfile`
* `docker-compose.yml`
* `.env.example`

Then inspect the repository.

---

# Responsibilities

Review all runtime and development dependencies.

Identify:

* Unused packages
* Duplicate packages
* Conflicting packages
* Obsolete packages
* Missing packages
* Tooling inconsistencies
* Architecture violations introduced through dependencies

---

# Project Authority Model

Use the Project Authority Model.

| Authority                 | Source              |
| ------------------------- | ------------------- |
| Project vision            | `README.md`         |
| Architectural constraints | `docs/decisions.md` |
| Planned technology        | `docs/roadmap.md`   |
| Current implementation    | Source code         |

Dependencies should support these authorities.

---

# Audit Report

Produce:

## 1. Runtime Dependencies

List all runtime packages.

Identify:

* Required
* Possibly unused
* Unused

---

## 2. Development Dependencies

Review:

* Ruff
* Pyright
* pytest
* Alembic
* uv

Identify:

* Missing tooling
* Redundant tooling

---

## 3. Infrastructure Dependencies

Review:

* PostgreSQL
* Redis
* Docker
* Docker Compose

Verify consistency with the documented architecture.

---

## 4. Dependency Quality

Identify:

* Duplicate functionality
* Conflicting libraries
* Deprecated libraries
* Large dependencies that provide little value

---

## 5. Architecture Alignment

Verify dependencies remain consistent with:

* Modular monolith
* DDD-inspired boundaries
* Future CQRS adoption
* Future event-driven evolution

Report any dependency that appears inconsistent with the project's
architectural direction.

---

## 6. Recommendations

Provide:

* Packages that can be removed
* Packages that should be added
* Packages that should be updated
* Tooling improvements

---

# Rules

* Do not modify any files.
* Do not recommend additional frameworks unless they support the documented architecture.
* Prefer simplicity over additional dependencies.
* Report only evidence found in the repository.

---

# Expected Output

Produce a Dependency Audit Report containing:

1. Dependency summary
2. New dependencies introduced
3. Removed dependencies
4. Runtime dependencies
5. Development dependencies
6. Architecture impact
7. Dependency justification
8. Unused or redundant dependencies
9. Versioning concerns
10. Security or maintenance concerns
11. Recommendations

For each new dependency, report:

* Purpose
* Where it is used
* Whether it aligns with the project architecture
* Whether an existing dependency could have been used instead

Do not recommend dependencies that are unrelated to the documented
roadmap or architectural direction.

Do not modify source code or documentation.

Do not report Git status, commit history, or unrelated repository
information.