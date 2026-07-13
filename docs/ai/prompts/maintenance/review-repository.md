# Review Repository

This maintenance prompt executes the Review Repository defined by
`docs/ai/ai-sdlc.md`.


## Purpose

Review the current repository implementation.

Identify implementation drift, documentation drift, roadmap alignment,
and repository health.

This prompt produces an audit report only.


## References

Load:

* `README.md`
* `docs/snapshot.md`
* `docs/roadmap.md`
* `docs/auth-spec.md`
* `docs/adr-log.md`
* `docs/ai/state/phase-state.yaml`

Inspect the repository implementation.


## Input Report

None.

This maintenance prompt begins a repository audit.


## Output Report

Persist the audit report to:

`docs/reports/review-repository-report.md`

This report becomes the authoritative working input for:

* `docs/ai/prompts/maintenance/reconcile-docs.md`


## Responsibilities

Compare the repository implementation against:

* Project documentation
* Roadmap deliverables
* Phase-state.yaml pipeline position
* Authentication specification
* ADRs

Identify:

* Implementation drift
* Documentation drift
* Roadmap inconsistencies
* Architectural inconsistencies

Recommend repository maintenance actions where required.


## Outputs

Produce a report containing:

### 1. Repository Summary

Report:

* Current phase (from `docs/ai/state/phase-state.yaml`)
* Current implementation status
* Overall repository health

Repository Health Score:

* Architecture health (1–10)
* Documentation health (1–10)
* Roadmap alignment (1–10)
* Test health (1–10)
* Dependency health (1–10)
* Overall health (1–10)


### 2. Implemented Contexts

Report:

* Implemented bounded contexts
* Placeholder contexts


### 3. Implemented Layers

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


### 4. Implemented Domain Concepts

Report:

* Entities
* Value Objects
* Enumerations
* Domain Services
* Repository Contracts
* Provider Contracts
* Authentication State Machine Contracts
* Domain Events


### 5. Implemented Application Concepts

Report:

* Commands
* Queries
* Handlers
* DTOs
* Application Services
* Workflows


### 6. Implemented Infrastructure

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


### 7. Tooling

Report:

* Tooling configured
* Quality gates
* CI/CD
* Test framework

Independently run the quality gate commands defined 
in `docs/snapshot.md > Configured Tooling`. 
Report the actual result of each, and compare against the status 
currently recorded in `docs/snapshot.md`.

Flag as drift:

* Pyright
* Ruff
* pytest


### 8. Test Coverage

Summarize:

* Areas covered
* Areas not covered

Flag any completed roadmap phase whose deliverables lack corresponding
test coverage — this indicates Stage 3's verification was bypassed or
incorrect in a prior session.

### 9. Roadmap Audit

Compare the implementation against the deliverables of the phase 
identified by `current_phase` in `docs/ai/state/phase-state.yaml`, 
as defined in `docs/roadmap.md`.

Identify:

* Completed deliverables
* Missing deliverables
* Deliverables incorrectly assumed complete


### 10. Phase State Audit

Compare `docs/ai/state/phase-state.yaml` against the verified repository implementation.

Identify:

* Whether `current_phase` matches the phase the implementation actually reflects
* Whether `roadmap_status` matches the verified completion state of that phase
* Whether `sdlc_stage` matches the last SDLC stage actually completed


### 11. Project Handover Audit

Compare the implementation against `docs/snapshot.md`.

Identify:

* Missing implemented concepts
* Incorrect implementation status
* Repository snapshot inaccuracies


### 12. Authentication Specification Audit

Compare the implementation against
`docs/auth-spec.md`.

Identify:

* Implemented requirements
* Missing requirements
* Deviations from the specification


### 13. ADR Compliance

Compare the implementation against
`docs/adr-log.md`.

For each ADR report:

* Implemented
* Partially Implemented
* Not Implemented
* Violated

Identify any implementation that appears to violate an ADR.


### 14. Documentation Drift

Report:

* Drift against `snapshot.md`, including any gap between recorded 
  and actually-verified quality gate status
* Drift against `roadmap.md`
* Drift against `phase-state.yaml`
* Drift against `README.md`
* Drift against `auth-spec.md`
* Drift against `adr-log.md`


### 15. Repository Risks

Summarize:

* Architectural risks
* Documentation risks
* Roadmap risks
* Repository maintenance risks
* Testing risks


### 16. Recommendations

Provide:

* Recommended updates to `snapshot.md`
* Recommended updates to `docs/ai/state/phase-state.yaml`
* Recommended updates to `roadmap.md`, if a phase's stated goal 
  or deliverables are found to be genuinely incorrect
* Whether an Architecture Decision Review should be performed
* Whether a phase completion review is recommended


## Restrictions

Do not:

* Modify source code,
* Modify documentation,
* Reinterpret the implemented architecture,
* Recommend implementation beyond the documented roadmap,
* Propose future architecture beyond the documented roadmap,
* Report Git status unless explicitly requested.