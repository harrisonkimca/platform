# Reconcile Documents

This prompt is the authoritative execution contract for the Reconcile Documents maintenance workflow.

It operates within the governance, document authority, escalation, and ownership rules defined in `docs/ai/ai-sdlc.md`.


## Role

Act as the Documentation Reconciler for the current repository and roadmap phase.

This role does not grant authority beyond the permissions defined by
`docs/ai/ai-sdlc.md` and this prompt.


## Purpose

Reconcile repository documentation with the current implementation.

Resolve documentation drift while preserving the responsibility of each
project document.

This maintenance prompt corrects verified implementation-documentation
drift and, when explicitly supported by the Repository Review Report,
verified pipeline-state drift.


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

Verify that the Review Repository Report metadata:

* records `phase` matching `phase-state.yaml > current_phase`
* identifies `workflow: review-repository`
* records `outcome: findings_detected`
* records `next_action: reconcile-docs`


## Responsibilities

Compare the Review Repository Report against the project documentation.

Review repository risks identified in the Review Repository Report.

Determine which project documents have drifted.

Determine which verified corrections fall within this workflow's authority.

Determine the reconciliation outcome:

* `reconciled` — all verified drift within this workflow's authority was
  corrected
* `no_authorized_changes` — findings exist, but none fall within this
  workflow's write authority
* `blocked` — reconciliation cannot be completed because evidence is
  incomplete or inconsistent

Determine the resulting `next_action` according to the earliest stage
invalidated by the verified finding or correction.

Apply these routing rules:

* If only `snapshot.md` was corrected, resume the previously interrupted
  numbered stage. Determine that stage from the verified pre-reconciliation
  `phase-state.yaml` value and the Repository Review Report, not from
  repository contents alone.
* If only `phase-state.yaml` was corrected, use the corrected `sdlc_stage`.
* If a protected normative document requires an approved change, set
  `next_action: manual-governance`; after that change, resume at `01-start`.
* If implementation correction is required, resume at `02-build`.
* If review evidence must be repeated, resume at the corresponding review stage.
* When multiple findings apply, select the earliest invalidated numbered stage.

Apply writes in this order:

1. Update authorized sections of `docs/snapshot.md`, if required.
2. Persist and verify `docs/reports/reconcile-docs-report.md`.
3. Update drifted fields in `phase-state.yaml`, if required.

If the reconciliation report cannot be persisted, do not modify
`phase-state.yaml`.

Preserve the authority and responsibility of each project document.

Recommend additional maintenance prompts where required.


## Outputs

Update documentation only where documentation drift has been identified.

The reconciliation report must contain:

1. Outcome — `reconciled`, `no_authorized_changes`, or `blocked`
2. Verified findings received from Review Repository
3. Snapshot corrections applied
4. Phase-state corrections applied
5. Findings outside reconciliation authority
6. Resulting `next_action`
7. Remaining blocked conflicts, if any

Persist the reconciliation report by overwriting:

* `docs/reports/reconcile-docs-report.md`

Begin the report with the maintenance YAML front matter defined in
`docs/ai/ai-sdlc.md > Report Metadata`, using:

* `workflow: reconcile-docs`
* the determined reconciliation outcome
* the resulting `next_action`

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
`roadmap_status`, `sdlc_stage`, or `sdlc_status` no longer match the
verified repository and workflow state.

Correct only the drifted fields to match the verified repository state:

* `current_phase`
* `current_phase_name`
* `roadmap_status`
* `sdlc_stage`
* `sdlc_status`

When correcting pipeline state, resume at the earliest SDLC stage
invalidated by the verified drift.

Set `sdlc_status: blocked` only when that stage cannot proceed until an
unresolved conflict is resolved. Otherwise set `sdlc_status: ready`.

### roadmap.md

`docs/roadmap.md` defines phase goals and deliverables. 
Phase status is recorded in `docs/ai/state/phase-state.yaml`, not here.

Do not modify.

If the Review Repository Report identifies a genuine error in a phase
goal or deliverable, recommend an approved manual roadmap update.

### README.md

Do not modify.

If the Review Repository Report identifies an inconsistency, recommend
an approved manual update.

### auth-spec.md

Do not modify.

If the Review Repository Report identifies an approved authentication
requirement change, recommend an authorized manual update.

### adr-log.md

Do not modify.

Architectural Decision Records are maintained exclusively through
`05-review-adr.md`.


## Restrictions

Do not:

* Modify source code
* Modify `README.md`
* Modify `docs/roadmap.md`
* Modify `docs/auth-spec.md`
* Reinterpret the implemented architecture
* Invent implemented features
* Remove planned roadmap deliverables
* Modify `docs/adr-log.md`
* Report Git status unless explicitly requested


## Success Criteria

All verified drift within this workflow's authority is corrected,
protected normative documents remain unchanged, the reconciliation
report records the applied evidence, and pipeline state points to the
earliest valid next action.