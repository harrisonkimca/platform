# Stage 3 — Review Implementation

This prompt executes Stage 3 (Review Implementation) as defined by 
`docs/ai/ai-sdlc.md`.


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

Load the current implementation report:

* `docs/reports/02-build-report.md`


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
* Quality gate results reported by Stage 2
* Test coverage of the phase's deliverables — a passing `pytest` run is
  not sufficient evidence on its own; confirm each deliverable claimed
  in Stage 2's report has corresponding tests, except deliverables
  recorded as a Testing Exception in the Start Phase report

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

On completion, update `docs/ai/state/phase-state.yaml`:

* Set `sdlc_stage: 04-update-docs`

Do not modify any other field.


## Outputs

Produce an Architecture Review Report containing:

1. Architecture summary
2. Implementation summary
3. Evidence of DDD compliance
4. Modular monolith boundary compliance
5. Authentication specification compliance
6. ADR compliance
7. CQRS readiness
8. Event-driven evolution readiness
9. Architecture fitness — assess whether the implementation improved,
   preserved, or weakened the long-term maintainability and evolvability
   of the architecture
10. Quality gate verification — confirmed pass/fail per gate, and any
    discrepancy against Stage 2's reported results
11. Test coverage verification — confirmed tests exist for each
    non-exempt deliverable, not merely that the test suite passes, and
    confirmation that any claimed Testing Exception is legitimate
12. Scope compliance
13. Documentation drift
14. Technical debt
15. Remaining work
16. Recommended next step

For each relevant ADR, report:

* Implemented
* Partially implemented
* Not implemented

Persist this report by overwriting:

* `docs/reports/03-review-report.md`


## Restrictions

Do not:

* Modify source code
* Modify documentation
* Create or modify ADRs
* Report Git status, commit status, working tree status, branches, or
  unrelated repository information
* Modify any `phase-state.yaml` field other than `sdlc_stage`


## Success Criteria

Architectural health is understood before documentation is updated.