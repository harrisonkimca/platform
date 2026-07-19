# Stage 2 — Implementation

This prompt is the authoritative execution contract for Stage 2 (Implementation).

It operates within the cross-stage governance, document authority, escalation, and ownership rules defined in `docs/ai/ai-sdlc.md`.


## Role

Act as the Implementer for the currently authorized roadmap phase.

This role does not grant authority beyond the permissions defined by
`docs/ai/ai-sdlc.md` and this prompt.


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

Confirm before proceeding:

* `sdlc_stage` is `02-build`
* `sdlc_status` is `ready`

Load the current planning report:

* `docs/reports/01-start-report.md`

Verify that its metadata:

* records `phase` matching `phase-state.yaml > current_phase`
* identifies `stage: 01-start`
* records `outcome: approved`
* records `next_stage: 02-build`


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

Identify any risk that was newly discovered, resolved, increased, or
reduced during implementation.

Classify each risk change as architectural, operational, migration,
maintenance, or testing.

Do not reinterpret the approved risk assessment; report only changes
supported by implementation evidence.

Determine the stage outcome:

* `completed` — all approved non-exempt deliverables, tests, and quality
  gates are complete
* `blocked` — implementation cannot continue within the approved scope

After determining the outcome:

1. Persist the Implementation Report with its required metadata.
2. Verify that the report was persisted.
3. Update `phase-state.yaml` according to the outcome.

If the report cannot be persisted, do not modify `phase-state.yaml`.

If the outcome is `completed`:

* Set `sdlc_stage: 03-review`
* Keep `sdlc_status: ready`

If the outcome is `blocked` because the approved scope remains valid:

* Keep `sdlc_stage: 02-build`
* Set `sdlc_status: blocked`

If the outcome is `blocked` because scope, requirements, roadmap
deliverables, or architectural assumptions must change:

* Set `sdlc_stage: 01-start`
* Set `sdlc_status: blocked`

Record the conflict and required resolution in the report.

Do not modify any other field.


## Outputs

Provide:

1. Outcome — `completed` or `blocked`
2. Files changed
3. Summary
4. Tests added — which deliverables they cover
5. Quality gate results — pass/fail for each gate defined in
   `docs/snapshot.md > Configured Tooling`
6. Architectural observations
7. Risk changes:
   * Architectural
   * Operational
   * Migration
   * Maintenance
   * Testing
8. Non-blocking future work

Record `None` for any risk category with no implementation-supported
change.

Unfinished current-phase deliverables, missing tests, and failing quality
gates must not be recorded as non-blocking future work.

Persist this report by overwriting:

* `docs/reports/02-build-report.md`

Begin the report with the YAML front matter defined in
`docs/ai/ai-sdlc.md > Report Metadata`, using:

* `stage: 02-build`
* the determined outcome
* the resulting `next_stage`


## Restrictions

Do not:

* Modify project documentation
* Create or modify ADRs
* Expand the approved implementation scope
* Modify any `phase-state.yaml` field other than `sdlc_stage` and `sdlc_status`


## Success Criteria

An outcome of `completed` requires the approved scope, tests, and quality
gates to be complete without architectural drift.