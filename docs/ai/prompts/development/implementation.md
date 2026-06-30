# Implementation

## Purpose

Implement the current roadmap step.

Responsibilities

* Implement only the current roadmap deliverables.
* Follow the documented architecture.
* Respect all ADRs.
* Preserve architectural boundaries.
* Produce production-quality code.

This prompt modifies source code only.

It does not update project documentation or project status.

---

Implement the current roadmap deliverable.

Reference:

* README.md
* docs/roadmap.md
* docs/project-handover.md
* docs/authentication-spec.md
* docs/decisions.md

Document responsibilities:

* README.md provides architectural intent.
* roadmap.md defines what is being implemented.
* project-handover.md describes the current repository state.
* authentication-spec.md defines authentication behavior.
* decisions.md defines architectural constraints.

Constraints:

* Do not modify documentation.
* Modify source code only.
* Implement only the current roadmap deliverable.
* Preserve DDD boundaries.
* Preserve modular monolith boundaries.
* Preserve CQRS readiness.
* Preserve future event-driven evolution.
* Preserve repository contracts.
* Keep UnitOfWork as the transactional boundary.
* Maintain Pyright strict compatibility.

After implementation provide:

1. Files changed
2. Summary
3. Architectural impact
4. Follow-up work