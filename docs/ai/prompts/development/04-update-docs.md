# Stage 4 — Update Documents

This prompt executes Stage 4 (Update Documents) as defined by
`docs/ai/ai-sdlc.md`.


## Purpose

Synchronize implementation documentation with the completed source code.

Ensure the repository documentation accurately reflects the current
implementation while preserving the responsibilities of each project
document.

This stage updates implementation documentation only.


## References

Load:

* `README.md`
* `docs/roadmap.md`
* `docs/snapshot.md`
* `docs/auth-spec.md`
* `docs/adr-log.md`
* `docs/ai/state/phase-state.yaml`

Load the current architecture review:

* `docs/reports/03-review-report.md`


## Responsibilities

Update:

* `docs/snapshot.md` — implementation-detail sections only: Implemented
  Contexts, Implemented Layers, Implemented Domain Concepts, Implemented
  Infrastructure, Configured Tooling, and the `Outstanding` checklist
  under `Outstanding Implementation`.

The `Configured Tooling > Current status` line must be set from Stage 3's
verified quality gate results — never assumed or left stale.

`current_phase`, `current_phase_name`, and `roadmap_status` in
`docs/ai/state/phase-state.yaml` are governed exclusively by Stage 6
(Complete Phase). Do not modify them during this stage.

Ensure:

* Documentation reflects the implemented source code
* Documentation responsibilities remain respected
* Documentation drift is removed
* Implementation is not reinterpreted beyond what exists in the repository

On completion, update `docs/ai/state/phase-state.yaml`:

* Set `sdlc_stage: 05-review-adr`

Do not modify any other field.


## Outputs

Provide:

1. Evidence that documentation now matches implementation
2. Summary of changes
3. Reason for each update
4. Remaining documentation drift (if any)

Persist this report by overwriting:

* `docs/reports/04-update-docs-report.md`


## Restrictions

Do not:

* Modify source code
* Modify `README.md`
* Modify `docs/auth-spec.md`
* Modify `docs/adr-log.md`
* Modify `docs/roadmap.md`
* Reinterpret implementation beyond the repository
* Create or modify ADRs
* Modify any `phase-state.yaml` field other than `sdlc_stage`


## Success Criteria

Documentation accurately reflects the repository.