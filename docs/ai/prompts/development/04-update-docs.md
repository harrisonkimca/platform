# Stage 4 — Update Documents

This prompt is the authoritative execution contract for Stage 4 (Update Documents). 

It operates within the cross-stage governance, document authority, escalation, and ownership rules defined in `docs/ai/ai-sdlc.md`.


## Role

Act as the Documentation Maintainer for the currently authorized roadmap phase.

This role does not grant authority beyond the permissions defined by
`docs/ai/ai-sdlc.md` and this prompt.


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

Confirm before proceeding:

* `sdlc_stage` is `04-update-docs`
* `sdlc_status` is `ready`

Load the current architecture review:

* `docs/reports/03-review-report.md`

Inspect the repository implementation directly before updating
`docs/snapshot.md`.

Verify that its metadata:

* records `phase` matching `phase-state.yaml > current_phase`
* identifies `stage: 03-review`
* records `outcome: approved`
* records `next_stage: 04-update-docs`

## Responsibilities

Update:

* `docs/snapshot.md` — implementation-detail sections only: Implemented
  Contexts, Implemented Layers, Implemented Domain Concepts, Implemented
  Infrastructure, Configured Tooling, Current Risks, and the `Outstanding`
  checklist under `Outstanding Implementation`.

Update `Current Risks` only with material risks confirmed by Stage 3 or
directly evidenced by the implemented repository.

The `Configured Tooling > Current status` section must record Stage 3's
verified result, phase, and report reference — never assumed or left
stale.

During normal lifecycle progression, `current_phase`,
`current_phase_name`, and `roadmap_status` are governed by Stage 6
(Complete Phase). Do not modify them during this stage.

Ensure:

* Documentation reflects the implemented source code
* Documentation responsibilities remain respected
* Documentation drift is removed
* Implementation is not reinterpreted beyond what exists in the repository

Do not advance while authorized `snapshot.md` updates remain incomplete.

Determine the stage outcome:

* `synchronized` — all authorized `snapshot.md` updates are complete
* `blocked` — documentation cannot be synchronized from the available
  implementation and review evidence

After determining the outcome:

1. Persist the Documentation Update Report with its required metadata.
2. Verify that the report was persisted.
3. Update `phase-state.yaml` according to the outcome.

If the report cannot be persisted, do not modify `phase-state.yaml`.

If the outcome is `synchronized`:

* Set `sdlc_stage: 05-review-adr`
* Keep `sdlc_status: ready`

If the outcome is `blocked`:

* Keep `sdlc_stage: 04-update-docs`
* Set `sdlc_status: blocked`
* Record the conflict and required resolution in the report

Do not modify any other field.

## Outputs

Provide:

1. Outcome — `synchronized` or `blocked`
2. Evidence that documentation now matches implementation
3. Summary of changes
4. Reason for each update
5. Current Risks changes — risks added, updated, retained, or removed
6. Remaining documentation drift outside this stage's authority, if any

Persist this report by overwriting:

* `docs/reports/04-update-docs-report.md`

Begin the report with the YAML front matter defined in
`docs/ai/ai-sdlc.md > Report Metadata`, using:

* `stage: 04-update-docs`
* the determined outcome
* the resulting `next_stage`

## Restrictions

Do not:

* Modify source code
* Modify `README.md`
* Modify `docs/auth-spec.md`
* Modify `docs/adr-log.md`
* Modify `docs/roadmap.md`
* Reinterpret implementation beyond the repository
* Create or modify ADRs
* Modify any `phase-state.yaml` field other than `sdlc_stage` and `sdlc_status`


## Success Criteria

An outcome of `synchronized` requires `docs/snapshot.md` to accurately
reflect the repository, including verified quality-gate provenance and
material current risks.