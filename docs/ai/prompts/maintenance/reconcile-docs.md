# Reconcile Documents

This maintenance prompt reconciles repository documentation as defined by
`docs/ai/ai-sdlc.md`.


## Purpose

Reconcile repository documentation with the current implementation.

Resolve documentation drift while preserving the responsibility of each
project document.

This maintenance prompt updates documentation only.


## Input Report

Load:

`docs/reports/review-repository-report.md`

This report is produced by:

`docs/ai/prompts/maintenance/review-repository.md`


## References

Load:

* `README.md`
* `docs/snapshot.md`
* `docs/roadmap.md`
* `docs/auth-spec.md`
* `docs/adr-log.md`
* `docs/ai/state/phase-state.yaml`


## Responsibilities

Compare the Review Repository Report against the project
documentation.

Review repository risks identified in the Review Repository Report.

Determine which project documents have drifted.

Update documentation while preserving the authority and responsibility of
each project document.

Recommend additional maintenance prompts where required.


## Outputs

Update documentation only where documentation drift has been identified.

### snapshot.md

Update only:

* Implemented contexts
* Implemented layers
* Implemented domain concepts
* Implemented infrastructure
* Configured tooling — only from the gate results reported in the
  Review Repository Report, never assumed
* Outstanding implementation


### docs/ai/state/phase-state.yaml

Update only when the audited repository state shows `current_phase`,
`roadmap_status`, or `sdlc_stage` no longer match the verified implementation.

Set:

* `current_phase`
* `current_phase_name`
* `roadmap_status`
* `sdlc_stage`

to match the verified repository state.

### roadmap.md

`docs/roadmap.md` defines phase goals and deliverables. 
Phase status is recorded in `docs/ai/state/phase-state.yaml`, not here.

Do not modify unless the Review Repository Report identifies a genuine
error in a phase's stated goal or deliverables.

Preserve:

* Overall project vision
* Phase goals
* Future phases
* Planned deliverables

### README.md

Do not modify unless the Review Repository Report identifies a genuine
inconsistency between the documented vision and the intended
architecture.

### auth-spec.md

Do not modify unless the Review Repository Report identifies an approved
change to the authentication requirements.

Implementation progress alone is never sufficient.

### adr-log.md

Do not modify.

Architectural Decision Records are maintained exclusively through
`05-review-adr.md`.


## Restrictions

Do not:

* Modify source code
* Reinterpret the implemented architecture
* Invent implemented features
* Remove planned roadmap deliverables
* Modify `docs/adr-log.md`
* Report Git status unless explicitly requested