# Stage 3 — Review Implementation

This prompt is the authoritative execution contract for Stage 3 (Review Implementation). 

It operates within the cross-stage governance, document authority, escalation, and ownership rules defined in `docs/ai/ai-sdlc.md`.


## Role

Act as the Independent Architecture Reviewer for the currently authorized roadmap phase.

This role does not grant authority beyond the permissions defined by
`docs/ai/ai-sdlc.md` and this prompt.


## Purpose

Review the completed implementation for architectural correctness.

This prompt produces an architecture review report only. It does not 
modify source code or documentation.


## References

Load:

* `README.md`
* `docs/roadmap.md`
* `docs/snapshot.md`
* `docs/auth-spec.md`
* `docs/adr-log.md`
* `docs/ai/state/phase-state.yaml`

Confirm before proceeding:

* `sdlc_stage` is `03-review`
* `sdlc_status` is `ready`

Inspect the implemented repository changes directly.

Load the current phase reports:

* `docs/reports/01-start-report.md`
* `docs/reports/02-build-report.md`

Verify that both reports record `phase` matching
`phase-state.yaml > current_phase`.

Verify the Start Phase Report records:

* `stage: 01-start`
* `outcome: approved`
* `next_stage: 02-build`

Verify the Implementation Report records:

* `stage: 02-build`
* `outcome: completed`
* `next_stage: 03-review`


## Responsibilities

Review:

* Repository changes
* Architecture fitness
* DDD compliance
* Modular monolith boundary compliance
* Authentication specification compliance
* ADR compliance
* CQRS readiness
* Event-driven evolution readiness
* Compliance with the approved Start Phase scope
* Satisfaction of the acceptance evidence defined for each deliverable
* Quality gate results reported by Stage 2
* Test coverage of the phase's deliverables — a passing `pytest` run is
  not sufficient evidence on its own; confirm each deliverable claimed
  in Stage 2's report has corresponding tests, except deliverables
  recorded as a Testing Exception in the Start Phase report
* The five risk categories recorded in the Start Phase Report

Re-run the quality gate commands defined in
`docs/snapshot.md > Configured Tooling` to confirm Stage 2's reported
results are accurate. This is read-only verification — do not modify
source code to fix a discrepancy; report it instead.

Identify:

* Scope creep
* Architectural drift
* Documentation drift
* Technical debt
* Remaining work
* Recommended next step
* Risks that were introduced, resolved, increased, reduced, or remain unchanged

Determine the review outcome:

* `approved` — the implementation satisfies the approved scope,
  architecture, acceptance evidence, test coverage, and quality gates
* `changes_required` — implementation changes are required before the
  phase may continue
* `blocked` — the review cannot be completed because required evidence or
  repository state is unavailable or inconsistent

After determining the outcome:

1. Persist the Architecture Review Report with its required metadata.
2. Verify that the report was persisted.
3. Update `phase-state.yaml` according to the outcome.

If the report cannot be persisted, do not modify `phase-state.yaml`.

If the outcome is `approved`:

* Set `sdlc_stage: 04-update-docs`
* Keep `sdlc_status: ready`

If the outcome is `changes_required`:

* Set `sdlc_stage: 02-build`
* Keep `sdlc_status: ready`
* Identify the required implementation corrections in the report

If the outcome is `blocked`:

* Keep `sdlc_stage: 03-review`
* Set `sdlc_status: blocked`
* Record the conflict and required resolution in the report

Do not modify any other field.


## Outputs

Produce an Architecture Review Report containing:

1. Outcome — `approved`, `changes_required`, or `blocked`
2. Architecture summary
3. Implementation summary
4. Evidence of DDD compliance
5. Modular monolith boundary compliance
6. Authentication specification compliance
7. ADR compliance
8. CQRS readiness
9. Event-driven evolution readiness
10. Architecture fitness — assess whether the implementation improved,
   preserved, or weakened the long-term maintainability and evolvability
   of the architecture
11. Quality gate verification — confirmed pass/fail per gate, and any
    discrepancy against Stage 2's reported results
12. Test coverage verification — confirmed tests exist for each
    non-exempt deliverable, not merely that the test suite passes, and
    confirmation that any claimed Testing Exception is legitimate
13. Acceptance evidence verification
14. Scope compliance
15. Documentation drift
16. Technical debt
17. Risk reassessment:
    * Architectural
    * Operational
    * Migration
    * Maintenance
    * Testing
18. Material current risks that Stage 4 should record in
    `docs/snapshot.md`
19. Remaining work
20. Recommended next step

For each relevant ADR, report:

* Implemented
* Partially implemented
* Not implemented
* Violated

Persist this report by overwriting:

* `docs/reports/03-review-report.md`

Begin the report with the YAML front matter defined in
`docs/ai/ai-sdlc.md > Report Metadata`, using:

* `stage: 03-review`
* the determined outcome
* the resulting `next_stage`

## Restrictions

Do not:

* Modify source code
* Modify documentation
* Create or modify ADRs
* Report Git status, commit status, working tree status, branches, or
  unrelated repository information
* Modify any `phase-state.yaml` field other than `sdlc_stage` and `sdlc_status`


## Success Criteria

An `approved` outcome requires the implementation to satisfy the approved
scope, architecture, acceptance evidence, test coverage, and quality gates.