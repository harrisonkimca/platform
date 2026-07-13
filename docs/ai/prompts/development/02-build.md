# Stage 2 — Implementation

This prompt executes Stage 2 (Implementation) as defined by 
`docs/ai/ai-sdlc.md`.


## Purpose

Implement the approved roadmap phase within the approved Start Phase
scope.

Discover the implementation that satisfies the approved scope without
expanding project scope or introducing new architectural decisions.

Produce production-quality source code.


## References

Load:

* `README.md`
* `docs/roadmap.md`
* `docs/snapshot.md`
* `docs/auth-spec.md`
* `docs/adr-log.md`
* `docs/ai/state/phase-state.yaml`

Load the current planning report:

* `docs/reports/01-start-report.md`


## Responsibilities

Implement the approved roadmap deliverables.

Keep:

* UnitOfWork as the transactional boundary
* Pyright strict compatibility

Each deliverable includes automated tests covering its behavior as part
of being implemented, unless it was recorded as a Testing Exception in
the Start Phase report. A non-exempt deliverable without tests is not
complete, regardless of whether existing tests still pass.

Before producing this report, run the quality gate commands defined in
`docs/snapshot.md > Configured Tooling`. A failing gate is part of the
approved scope to fix. If a fix would require work outside the approved
Start Phase scope, stop and report the conflict per Scope Control rather
than handing off failing gates as follow-up work.

On completion, update `docs/ai/state/phase-state.yaml`:

* Set `sdlc_stage: 03-review`

Do not modify any other field.


## Outputs

Provide:

1. Files changed
2. Summary
3. Tests added — which deliverables they cover
4. Quality gate results — pass/fail for each gate defined in
   `docs/snapshot.md > Configured Tooling`
5. Architectural observations
6. Follow-up work

Persist this report by overwriting:

* `docs/reports/02-build-report.md`


## Restrictions

Do not:

* Modify project documentation
* Create or modify ADRs
* Expand the approved implementation scope
* Modify any `phase-state.yaml` field other than `sdlc_stage`


## Success Criteria

Implementation satisfies the approved scope without introducing
architectural drift.