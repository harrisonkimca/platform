# Review Dependency

This prompt is the authoritative execution contract for the Review Dependency maintenance workflow.

It operates within the governance, document authority, escalation, and ownership rules defined in `docs/ai/ai-sdlc.md`.


## Role

Act as the Dependency Auditor for the current repository and roadmap phase.

This role does not grant authority beyond the permissions defined by
`docs/ai/ai-sdlc.md` and this prompt.


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

Begin the report with the maintenance YAML front matter defined in
`docs/ai/ai-sdlc.md > Report Metadata`, using:

* `workflow: review-dependency`
* the determined audit outcome
* the recommended `next_action`


## Responsibilities

Review runtime and development dependencies.

Determine the audit outcome:

* `aligned` — no dependency changes are recommended
* `changes_recommended` — non-critical dependency maintenance should be
  scoped
* `critical_finding` — an urgent security, operational, or compatibility
  dependency risk requires remediation
* `blocked` — the audit cannot be completed from available evidence

Set `next_action` according to the outcome:

* `aligned` → `none`
* `changes_recommended` → `01-start`
* `critical_finding` → `01-start`
* `blocked` → `manual-review`

Support version, obsolescence, deprecation, and security findings with
available repository or authoritative external evidence.

For a critical security finding:

* Record the affected dependency and evidence
* Identify the minimum safe remediation
* Recommend an immediately scoped Stage 1 and Stage 2 cycle
* Do not modify dependencies directly

Record `Not assessed` when required external evidence is unavailable.

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

### Audit Outcome

Record:

* Outcome
* Evidence basis
* Recommended `next_action`

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


## Success Criteria

The report provides evidence-based dependency findings, clearly marks
unassessed areas, and routes any required dependency modification through
the normal governed development workflow.