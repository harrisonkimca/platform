# Stage 1 — Start Phase

This prompt executes Stage 1 (Start Phase) as defined by 
`docs/ai/ai-sdlc.md`.


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

On completion, update `docs/ai/state/phase-state.yaml`:

* Set `sdlc_stage: 02-build`

Do not modify any other field.


## Outputs

Provide:

1. Current phase
2. Current objective
3. Deliverables involved
4. In scope
5. Out of scope
6. Repository areas likely to be affected
7. Domain concepts affected
8. Architectural constraints
9. Architectural risks
10. Testing exceptions — deliverables with no applicable 
    automated tests, and why
11. Implementation plan

Persist this report by overwriting:

* `docs/reports/01-start-report.md`


## Restrictions

Do not:

* Write source code
* Modify documentation
* Create or modify ADRs
* Modify any `phase-state.yaml` field other than `sdlc_stage`


## Success Criteria

The implementation team should understand:

* What will be built
* What will not be built
* Why
* The architectural constraints