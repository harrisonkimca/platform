Implement the current step identified in the project documentation.

Reference:

* docs/project-handover.md
* docs/roadmap.md
* docs/authentication-spec.md
* docs/decisions.md

Requirements:

* Follow the documented architecture.
* Follow all ADRs.
* Preserve modular monolith boundaries.
* Preserve DDD layers.
* Preserve future CQRS adoption.
* Preserve future event-driven evolution.

Constraints:

* Do not introduce shortcuts.
* Do not introduce infrastructure leakage into the domain layer.
* Do not violate repository contracts.
* Keep UnitOfWork as the transactional boundary.
* Maintain strict Pyright compatibility.
* Keep future service extraction feasible.

Implementation Rules:

* Update code only.
* Do not update documentation.
* Do not modify roadmap status.
* Do not modify project progress tracking.
* Minimize changes outside the scope of the current step.

After implementation provide:

1. Files changed
2. Summary of implementation
3. Architectural considerations
4. Potential follow-up work