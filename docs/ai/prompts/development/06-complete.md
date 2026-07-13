# Stage 6 — Complete Phase

This prompt executes Stage 6 (Complete Phase) as defined by
`docs/ai/ai-sdlc.md`.


## Purpose

Verify that the approved roadmap phase has been completed successfully.

Confirm that the approved roadmap phase is complete, architecturally compliant,
and ready for the next roadmap phase.

This stage may update phase-status documentation only.


## References

Load:

* `README.md`
* `docs/roadmap.md`
* `docs/snapshot.md`
* `docs/auth-spec.md`
* `docs/adr-log.md`
* `docs/ai/state/phase-state.yaml`

Load the current ADR review report:

* `docs/reports/05-review-adr-report.md`


## Responsibilities

Verify:

* Completion of the approved Start Phase scope
* Roadmap deliverables
* Authentication specification compliance
* ADR compliance
* Quality gates pass, per Stage 3's verified results
* Each roadmap deliverable has corresponding automated tests, per
  Stage 3's verified coverage confirmation
* Architectural readiness for the next roadmap phase

If the phase is complete, update:

* `docs/ai/state/phase-state.yaml` — set `current_phase`,
  `current_phase_name`, and `roadmap_status: current` to the next phase,
  and reset `sdlc_stage: 01-start`.

`docs/snapshot.md` is not modified by this stage. Stage 4 already
synchronized its implementation-detail sections, including `Outstanding
Implementation > Outstanding`, before this stage runs.

If the phase is not complete, do not modify `docs/ai/state/phase-state.yaml`.
Report the outstanding deliverables instead and leave
`sdlc_stage: 06-complete` so the next session knows a completion check is
still pending.


## Outputs

Provide:

1. Phase completion status
2. Evidence each roadmap deliverable is complete
3. Architectural compliance
4. Major concepts introduced
5. Technical debt
6. Readiness for the next phase
7. Recommended first step of the next phase
8. Documentation updated (if any)

Persist this report by overwriting:

* `docs/reports/06-complete-report.md`


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
* Report Git status, commit status, working tree status, branches, or
  unrelated repository information


## Success Criteria

The roadmap phase is objectively complete.