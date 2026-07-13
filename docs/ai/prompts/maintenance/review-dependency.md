# Review Dependency

This maintenance prompt audits project dependencies as defined by
`docs/ai/ai-sdlc.md`.


## Purpose

Review the project's dependencies.

Identify unnecessary, inconsistent, obsolete, or architecturally
misaligned dependencies.

This maintenance prompt produces an audit report only.


## References

Load:

* `README.md`
* `docs/snapshot.md`
* `docs/roadmap.md`
* `docs/auth-spec.md`
* `docs/adr-log.md`
* `docs/ai/state/phase-state.yaml`

Inspect:

* `pyproject.toml`
* `uv.lock`
* `Dockerfile`
* `docker-compose.yml`
* `.env.example`

Inspect the repository implementation.


## Input Report

None.

This maintenance prompt performs an independent dependency audit.


## Output Report

Persist the audit report to:

`docs/reports/review-dependency-report.md`

This report is an informational maintenance artifact.

It does not become part of the normal SDLC workflow.


## Responsibilities

Review runtime and development dependencies.

Identify:

* Unused dependencies
* Duplicate dependencies
* Conflicting dependencies
* Obsolete dependencies
* Missing dependencies
* Tooling inconsistencies
* Architectural inconsistencies introduced by dependencies

Recommend dependency maintenance where required.


## Outputs

Produce a report containing:

### 1. Runtime Dependencies

Report:

* Required
* Possibly unused
* Unused

### 2. Development Dependencies

Review:

* Ruff
* Pyright
* pytest
* Alembic
* uv

Identify:

* Missing tooling
* Redundant tooling

### 3. Infrastructure Dependencies

Review:

* PostgreSQL
* Redis
* Docker
* Docker Compose

Verify alignment with the documented architecture.

### 4. Dependency Quality

Identify:

* Duplicate functionality
* Conflicting libraries
* Deprecated libraries
* Large dependencies with little value

### 5. Architecture Alignment

Verify dependency alignment with:

* Modular monolith
* DDD boundaries
* CQRS evolution
* Event-driven evolution

Identify dependencies that appear inconsistent with the documented
architecture.

### 6. Dependency Risks

Summarize:

* Architectural risks
* Maintenance risks
* Versioning risks
* Security risks

### 7. Recommendations

Provide:

* Dependencies to remove
* Dependencies to add
* Dependencies to update
* Tooling improvements


## Restrictions

Do not:

* Modify source code
* Modify documentation
* Recommend frameworks beyond the documented roadmap
* Recommend unnecessary dependencies
* Report Git status unless explicitly requested