# Stage 6 — Complete Phase

This prompt is the authoritative execution contract for Stage 6 (Complete Phase). 

It operates within the cross-stage governance, document authority, escalation, and ownership rules defined in `docs/ai/ai-sdlc.md`.


## Role

Act as the Phase Gatekeeper for the currently authorized roadmap phase.

This role does not grant authority beyond the permissions defined by
`docs/ai/ai-sdlc.md` and this prompt.


## Purpose

Verify that the approved roadmap phase has been completed successfully.

Confirm that the approved roadmap phase is complete, architecturally compliant,
and ready for the next roadmap phase.

This stage may update pipeline state only.


## References

Load:

* `README.md`
* `docs/roadmap.md`
* `docs/snapshot.md`
* `docs/auth-spec.md`
* `docs/adr-log.md`
* `docs/ai/state/phase-state.yaml`

Confirm before proceeding:

* `sdlc_stage` is `06-complete`
* `sdlc_status` is `ready`

Load the current phase-completion evidence:

* `docs/reports/01-start-report.md`
* `docs/reports/03-review-report.md`
* `docs/reports/04-update-docs-report.md`
* `docs/reports/05-review-adr-report.md`

Verify that all reports record `phase` matching
`phase-state.yaml > current_phase`.

Verify the Start Phase Report records:

* `stage: 01-start`
* `outcome: approved`
* `next_stage: 02-build`

Verify the Architecture Review Report records:

* `stage: 03-review`
* `outcome: approved`
* `next_stage: 04-update-docs`

Verify the Documentation Update Report records:

* `stage: 04-update-docs`
* `outcome: synchronized`
* `next_stage: 05-review-adr`

Verify the ADR Review Report records:

* `stage: 05-review-adr`
* `outcome: completed`
* `next_stage: 06-complete`


## Responsibilities

Verify:

* Completion of the approved Start Phase scope
* Roadmap deliverables
* Acceptance evidence defined in the Start Phase Report
* Authentication specification compliance
* ADR compliance
* Quality gates pass, per Stage 3's verified results
* Each roadmap deliverable has corresponding automated tests, per
  Stage 3's verified coverage confirmation
* Architectural readiness for the next roadmap phase

`docs/snapshot.md` is not modified by this stage. Stage 4 already
synchronized its implementation-detail sections, including `Outstanding
Implementation > Outstanding`, before this stage runs.

Summarize any outstanding risk that remains accepted at phase
completion, including its category, impact, and reason it does not block
the next phase.

Confirm the final disposition of all five risk categories. Record
`None accepted` for any category with no remaining accepted risk.

A risk that prevents safe progression must result in `incomplete` or
`blocked`; it must not be recorded as an accepted outstanding risk.

Determine the stage outcome:

* `phase_complete` — every completion requirement is satisfied
* `incomplete` — corrective work is required in an earlier stage
* `blocked` — completion cannot be determined because required evidence
  or repository state is unavailable or inconsistent

After determining the outcome:

1. Persist the Complete Phase Report with its required metadata.
2. Verify that the report was persisted.
3. Update `phase-state.yaml` according to the outcome.

If the report cannot be persisted, do not modify `phase-state.yaml`.

If the outcome is `phase_complete`:

If another roadmap phase exists:

* Advance `current_phase` and `current_phase_name` to the next roadmap phase
* Set `roadmap_status: current`
* Set `sdlc_stage: 01-start`
* Keep `sdlc_status: ready`

If the completed phase is the final roadmap phase:

* Keep `current_phase` and `current_phase_name` set to the completed final phase
* Set `roadmap_status: complete`
* Set `sdlc_stage: complete`
* Keep `sdlc_status: ready`

If the outcome is `incomplete`, set `sdlc_stage` to the earliest stage
invalidated by the finding:

* `01-start` — approved scope or assumptions must change
* `02-build` — implementation or tests are incomplete
* `03-review` — architecture, gate, or coverage verification must be repeated
* `04-update-docs` — implementation documentation remains unsynchronized
* `05-review-adr` — ADR review remains incomplete

Keep `sdlc_status: ready` so corrective work may proceed.

If the outcome is `blocked`:

* Keep `sdlc_stage: 06-complete`, unless an earlier blocked stage is known
* Set `sdlc_status: blocked`

Record all findings and required resolutions in the report.

Do not modify `phase-state.yaml` except as required by the recorded
outcome.

## Outputs

Provide:

1. Outcome — `phase_complete`, `incomplete`, or `blocked`
2. Phase completion status
3. Evidence each roadmap deliverable is complete
4. Architectural compliance
5. Major concepts introduced
6. Technical debt
7. Accepted outstanding risks:
   * Architectural
   * Operational
   * Migration
   * Maintenance
   * Testing
8. Readiness for the next phase
9. Next authorized action
10. Pipeline state update

Persist this report by overwriting:

* `docs/reports/06-complete-report.md`

Begin the report with the YAML front matter defined in
`docs/ai/ai-sdlc.md > Report Metadata`, using:

* `stage: 06-complete`
* the determined outcome
* the resulting `next_stage`

## Restrictions

Do not:

* Modify `README.md`
* Modify `docs/auth-spec.md`
* Modify `docs/adr-log.md`
* Modify `docs/roadmap.md`
* Modify `docs/snapshot.md`
* Create or modify ADRs
* Mark a phase complete unless all approved Start Phase scope items have
  been completed
* Mark a phase complete while any quality gate is reported failing  
* Mark a phase complete if any deliverable lacks corresponding test
  coverage, unless recorded as a Testing Exception in the Start Phase
  report and confirmed legitimate by Stage 3
* Leave the workflow at `06-complete` when the earliest invalidated
  corrective stage can be identified
* Report Git status, commit status, working tree status, branches, or
  unrelated repository information
* Modify `sdlc_status` except as defined by this prompt
* Set `sdlc_stage: complete` unless the completed phase is the final
  phase defined in `docs/roadmap.md`


## Success Criteria

An outcome of `phase_complete` requires every phase-completion criterion
to be satisfied and either:

* the next roadmap phase to be activated at `01-start`, or
* the roadmap to enter its terminal `complete` state.