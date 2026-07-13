# Stage 5 — Review Architecture Decision Records

This prompt executes Stage 5 (Review Architecture Decision Records) as defined by
`docs/ai/ai-sdlc.md`.


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

Load the current documentation update report:

* `docs/reports/04-update-docs-report.md`


## Responsibilities

Determine whether implementation introduced a new permanent
architectural decision.

If a new permanent architectural decision was introduced:

* Create a new ADR

Otherwise:

* Confirm that the existing ADRs remain sufficient

The burden of proof is to demonstrate that implementation introduced a
new permanent architectural decision. If sufficient evidence cannot be 
demonstrated, no new ADR should be created.

On completion, update `docs/ai/state/phase-state.yaml`:

* Set `sdlc_stage: 06-complete`

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

Decision:
...

Reason:
...

Consequences:
...


## Outputs

Report:

1. Decision — new ADR required, or existing ADRs remain sufficient
2. Reasoning — summarize architectural reasoning that led to the decision
3. Existing ADR coverage — ADRs already covering implementation if no new ADR required
4. Documentation modified (if any)
5. Non-ADR decisions noted (if any)

Persist this report by overwriting:

* `docs/reports/05-review-adr-report.md`


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
* Modify any `phase-state.yaml` field other than `sdlc_stage`


## Success Criteria

A new ADR exists only when implementation introduced a genuine permanent
architectural decision; otherwise the existing ADR log is confirmed
sufficient.