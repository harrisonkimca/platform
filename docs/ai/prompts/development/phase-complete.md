# Phase Complete

## Purpose

Verify that the current roadmap phase has been completed successfully.

Responsibilities

* Verify all roadmap deliverables.
* Confirm implementation readiness.
* Validate architectural compliance.
* Confirm readiness for the next phase.
* Update implementation progress when appropriate.

This prompt may update only implementation progress documentation.

It must not modify architectural documentation, authentication
requirements, or Architecture Decision Records.

---

Review:

* docs/roadmap.md
* docs/project-handover.md
* docs/authentication-spec.md
* docs/decisions.md

---

# Verify

Confirm that:

* All roadmap deliverables for the current phase are complete.
* The implementation satisfies the authentication specification.
* All active ADRs remain respected.
* No architectural drift has been introduced.

---

# Produce

Provide:

1. Phase completion summary
2. Deliverables completed
3. Major concepts introduced
4. Technical debt remaining
5. Readiness for the next phase
6. Recommended first step of the next phase

---

# Documentation Updates

If the phase is complete:

Update only:

* docs/roadmap.md
  * Change the current phase status to **Complete**
  * Mark the next phase as **Current**

* docs/project-handover.md
  * Update current phase
  * Update repository status if necessary

---

# Restrictions

Do NOT modify:

* README.md
* docs/authentication-spec.md
* docs/decisions.md

Do NOT create new ADRs.

ADR creation is handled exclusively by:

* docs/ai/prompts/maintenance/adr-audit.md

Only update roadmap.md and project-handover.md if the phase has actually
completed.

---

# Expected Output

Report:

1. Phase completion status
2. Deliverables completed
3. Architectural compliance
4. ADR summary
5. Technical debt
6. Readiness for the next phase
7. Documentation updated

Do not report Git status or unrelated repository information.