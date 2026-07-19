# Stage 5 — Review Architecture Decision Records

This prompt is the authoritative execution contract for Stage 5 (Review Architecture Decision Records). 

It operates within the cross-stage governance, document authority, escalation, and ownership rules defined in `docs/ai/ai-sdlc.md`.


## Role

Act as the Architecture Decision Custodian for the currently authorized roadmap phase.

This role does not grant authority beyond the permissions defined by
`docs/ai/ai-sdlc.md` and this prompt.


## Purpose

Review the completed implementation to determine whether it introduced a
new permanent architectural decision that requires a new Architecture
Decision Record (ADR).

Architectural decisions should remain rare. This stage exists to record 
changes to the project's long-term architecture rather than the 
implementation of existing architectural principles.

This is the only stage permitted to modify `docs/adr-log.md`. Existing 
ADRs are historical records and must never be modified, reordered, or 
removed.


## References

Load:

* `README.md`
* `docs/roadmap.md`
* `docs/snapshot.md`
* `docs/auth-spec.md`
* `docs/adr-log.md`
* `docs/ai/state/phase-state.yaml`

Confirm before proceeding:

* `sdlc_stage` is `05-review-adr`
* `sdlc_status` is `ready`

Load the current implementation and review reports:

* `docs/reports/02-build-report.md`
* `docs/reports/03-review-report.md`
* `docs/reports/04-update-docs-report.md`

Inspect the implemented repository changes directly.

Verify that all reports record `phase` matching
`phase-state.yaml > current_phase`.

Verify the Implementation Report records:

* `stage: 02-build`
* `outcome: completed`
* `next_stage: 03-review`

Verify the Architecture Review Report records:

* `stage: 03-review`
* `outcome: approved`
* `next_stage: 04-update-docs`

Verify the Documentation Update Report records:

* `stage: 04-update-docs`
* `outcome: synchronized`
* `next_stage: 05-review-adr`


## Responsibilities

Determine whether the implementation introduced a new permanent
architectural decision.

If an approved new permanent architectural decision was introduced:

* Create a new ADR

If a new ADR is appended, identify the architectural, operational,
migration, maintenance, and testing risks introduced or changed by the
decision.

Otherwise:

* Confirm that the existing ADRs remain sufficient

The burden of proof is to demonstrate that implementation introduced a
new permanent architectural decision. If sufficient evidence cannot be 
demonstrated, no new ADR should be created.

Determine the stage outcome:

* `completed` — existing ADRs remain sufficient, or an approved permanent
  architectural decision has been recorded in a new ADR
* `changes_required` — implementation introduced an unapproved
  architectural change that must be corrected or formally approved
* `blocked` — the ADR review cannot be completed from the available
  evidence

After determining the outcome:

1. Persist the ADR Review Report with its required metadata.
2. Verify that the report was persisted.
3. Update `phase-state.yaml` according to the outcome.

If the report cannot be persisted, do not modify `phase-state.yaml`.

If the outcome is `completed`:

* Set `sdlc_stage: 06-complete`
* Keep `sdlc_status: ready`

If the outcome is `changes_required` and implementation must be corrected:

* Set `sdlc_stage: 02-build`
* Keep `sdlc_status: ready`

If the outcome is `changes_required` and an intentional architecture
change requires approval:

* Set `sdlc_stage: 01-start`
* Set `sdlc_status: blocked`

If the outcome is `blocked`:

* Keep `sdlc_stage: 05-review-adr`
* Set `sdlc_status: blocked`

Record the finding and required resolution in the report.

Do not modify any other field.


## ADR Decision Criteria

Create a new ADR only when **all** of the following conditions are met:

* A significant architectural decision was made
* The decision introduces a permanent architectural constraint
* The decision will influence future implementation
* The decision is not already documented by:
  * `README.md`
  * `docs/auth-spec.md`
  * an existing ADR
  * the project's established architectural principles
* The decision represents a change or addition to the project's
  architecture rather than simply implementing the existing architecture

Do **not** create ADRs for:

* Normal implementation work
* DDD best practices
* Layering rules already established by the project
* Coding conventions
* Refactoring
* Repository organization
* Technology already chosen by previous ADRs
* Completing roadmap deliverables

When in doubt, do **not** create a new ADR.

Architectural decisions should be rare and represent intentional changes
to the project's long-term architecture rather than the implementation of
existing architectural decisions.

If no new ADR is required:

* Report that the existing ADRs remain sufficient
* Explain briefly why no new ADR is necessary
* Do not modify `docs/adr-log.md`

If a new ADR is required:

* Append it to `docs/adr-log.md`
* Never modify, reorder, or remove existing ADRs


### ADR Format

ADR-XXX

Status:
...

Date:
...

Decision:
...

Reason:
...

Consequences:
...

Supersedes:
...

Superseded by:
...


## Outputs

Report:

1. Outcome — `completed`, `changes_required`, or `blocked`
2. Decision — new ADR required, or existing ADRs remain sufficient
3. Reasoning — summarize architectural reasoning that led to the decision
4. Existing ADR coverage — ADRs already covering implementation 
   if no new ADR required
5. Documentation modified (if any)
6. Non-ADR decisions noted (if any)
7. Architectural-decision risk assessment:
   * Risks introduced or changed by a newly recorded ADR, classified as
     architectural, operational, migration, maintenance, or testing
   * `None` when no new ADR was recorded

Persist this report by overwriting:

* `docs/reports/05-review-adr-report.md`

Begin the report with the YAML front matter defined in
`docs/ai/ai-sdlc.md > Report Metadata`, using:

* `stage: 05-review-adr`
* the determined outcome
* the resulting `next_stage`

## Restrictions

Do not:

* Modify source code
* Modify `README.md`
* Modify `docs/auth-spec.md`
* Modify `docs/roadmap.md`
* Modify existing ADRs
* Reorder ADRs
* Remove ADRs
* Modify any documentation other than `docs/adr-log.md` when a new ADR
  is required
* Report Git status, commit status, working tree status, branches, or 
  unrelated repository information
* Modify any `phase-state.yaml` field other than `sdlc_stage` and `sdlc_status`
* Create an ADR solely to legitimize unapproved implementation drift


## Success Criteria

An outcome of `completed` requires either confirmation that existing ADRs
remain sufficient or a new ADR recording an approved genuine permanent
architectural decision.