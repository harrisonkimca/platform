# ADR Audit

## Purpose

Determine whether the completed implementation introduced a new permanent
architectural decision that must be recorded as an Architecture Decision
Record (ADR).

Responsibilities

* Review architectural changes.
* Compare them against existing ADRs.
* Identify new long-term architectural constraints.
* Create new ADRs only when required.
* Preserve ADR history.

This is the only prompt permitted to modify `docs/decisions.md`.

Existing ADRs are historical records and must never be modified,
reordered, or removed.

---

Review the completed implementation.

Determine whether a new Architecture Decision Record (ADR) is required.

A new ADR should be created only if **all** of the following are true:

* A significant architectural decision was made.
* The decision introduces a permanent architectural constraint.
* The decision will influence future implementation.
* The decision is not already documented by:
  * `README.md`
  * `docs/authentication-spec.md`
  * an existing ADR
  * the project's established architectural principles.
* The decision represents a change or addition to the project's
  architecture rather than simply implementing the existing architecture.

Do **not** create ADRs for:

* Normal implementation work.
* DDD best practices.
* Layering rules already established by the project.
* Coding conventions.
* Refactoring.
* Repository organization.
* Technology already chosen by previous ADRs.
* Completing roadmap deliverables.

When in doubt, do **not** create a new ADR.

Architectural decisions should be rare and represent intentional changes
to the project's long-term architecture rather than the implementation of
existing architectural decisions.

If no new ADR is required:

* Report that the existing ADRs remain sufficient.
* Explain briefly why no new ADR is necessary.
* Do not modify `docs/decisions.md`.

If a new ADR is required:

* Append it to `docs/decisions.md`.
* Never modify, reorder, or remove existing ADRs.

Format:

## ADR-XXX

Decision:
...

Reason:
...

Consequences:
...

Do not update any other documentation.

---

# Expected Output

Report:

1. ADR decision
   * New ADR required, or
   * Existing ADRs remain sufficient.

2. Reasoning

Summarize the architectural reasoning that led to the decision.

3. Existing ADR coverage

If no ADR is required, identify which existing ADRs already cover the
implementation.

4. Files modified

List any documentation files modified during this audit.

Do not report Git status, commit status, working tree status, branches,
or unrelated repository information.