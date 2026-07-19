# Stage 1 — Start Phase

This prompt is the authoritative execution contract for Stage 1 (Start Phase).

It operates within the cross-stage governance, document authority, escalation, and ownership rules defined in `docs/ai/ai-sdlc.md`.


## Role

Act as the Phase Planner for the currently authorized roadmap phase.

This role does not grant authority beyond the permissions defined by
`docs/ai/ai-sdlc.md` and this prompt.


## Purpose

Prepare the current roadmap phase before implementation begins.

Determine the implementation scope, constraints, risks, and a high-level
implementation plan.

This stage performs planning only.


## References

Load:

* `README.md`
* `docs/roadmap.md`
* `docs/snapshot.md`
* `docs/auth-spec.md`
* `docs/adr-log.md`
* `docs/ai/state/phase-state.yaml`

Confirm before proceeding:

* `sdlc_stage` is `01-start`
* `sdlc_status` is `ready`


## Responsibilities

Determine:

* Current implementation phase
* Current repository state
* Current implementation objective
* Current roadmap deliverables
* Dependencies between roadmap deliverables
* In-scope work
* Out-of-scope work

Distinguish clearly between:

* Requirements
* Architectural constraints
* Implementation considerations

Identify phase risks in all five categories defined by
`docs/ai/ai-sdlc.md > Risk Management`:

* Architectural
* Operational
* Migration
* Maintenance
* Testing

The implementation plan should describe what must be accomplished rather
than prescribe concrete implementation classes, services, persistence
models, or infrastructure patterns unless already required by project
documentation or ADRs.

For each deliverable, determine whether it has executable behavior that
automated tests can cover. If a deliverable is not testable — for
example, documentation, folder scaffolding, or configuration with no
executable behavior — record it explicitly as a Testing Exception, with
a one-line reason. Any deliverable not recorded as an exception is
expected to carry automated tests when implemented in Stage 2.

For each roadmap deliverable, define the evidence Stage 6 will use to
verify completion.

Acceptance evidence should identify observable proof that the deliverable
has been implemented without prescribing unnecessary implementation
details.

Determine the stage outcome:

* `approved` — the phase scope, constraints, risks, testing exceptions,
  acceptance evidence, and implementation plan are complete
* `blocked` — a conflict prevents an approved plan from being produced

After determining the outcome:

1. Persist the Start Phase Report with its required metadata.
2. Verify that the report was persisted.
3. Update `phase-state.yaml` according to the outcome.

If the report cannot be persisted, do not modify `phase-state.yaml`.

If the outcome is `approved`:

* Set `sdlc_stage: 02-build`
* Keep `sdlc_status: ready`

If the outcome is `blocked`:

* Keep `sdlc_stage: 01-start`
* Set `sdlc_status: blocked`
* Record the conflict and required resolution in the report

Do not modify any other field.


## Outputs

Provide:

1. Outcome — `approved` or `blocked`
2. Current phase
3. Current objective
4. Deliverables involved
5. Acceptance evidence for each deliverable
6. In scope
7. Out of scope
8. Repository areas likely to be affected
9. Domain concepts affected
10. Architectural constraints
11. Risks:
    * Architectural
    * Operational
    * Migration
    * Maintenance
    * Testing
12. Testing exceptions — deliverables with no applicable
    automated tests, and why
13. Implementation plan

Persist this report by overwriting:

* `docs/reports/01-start-report.md`

Begin the report with the YAML front matter defined in
`docs/ai/ai-sdlc.md > Report Metadata`, using:

* `stage: 01-start`
* the determined outcome
* the resulting `next_stage`

## Restrictions

Do not:

* Write source code
* Modify documentation
* Create or modify ADRs
* Modify any `phase-state.yaml` field other than `sdlc_stage` and `sdlc_status`


## Success Criteria

The implementation team should understand:

* What will be built
* What will not be built
* Why
* The architectural constraints

An `approved` outcome requires a complete and internally consistent plan.