# Architecture Review

## Purpose

Review the completed implementation for architectural correctness.

Responsibilities

* Review architecture compliance.
* Review DDD compliance.
* Review modular monolith boundaries.
* Review ADR compliance.
* Identify documentation drift.
* Identify technical debt.
* Recommend the next implementation step.

This prompt produces an architecture review report only.

It does not modify source code or documentation.

---

Review the implementation.

Reference:

* README.md
* docs/roadmap.md
* docs/project-handover.md
* docs/authentication-spec.md
* docs/decisions.md

Do not modify files.

Produce an architecture review covering:

1. Repository changes
2. New domain concepts
3. New entities
4. New value objects
5. New domain services
6. New repositories
7. New application services
8. New infrastructure
9. New state machines
10. New events

Review:

* DDD compliance
* Modular monolith compliance
* Authentication-spec compliance
* ADR compliance
* CQRS readiness
* Event-driven readiness

Identify:

* Documentation drift
* Architectural drift
* Technical debt
* Recommended next implementation step

For each ADR report:

* Implemented
* Partially Implemented
* Not Implemented

Expected Output:

Produce an Architecture Review Report containing:

1. Architecture summary
2. DDD compliance
3. Modular monolith boundary compliance
4. ADR compliance
5. CQRS readiness
6. Event-driven evolution readiness
7. Documentation drift
8. Technical debt
9. Remaining work
10. Recommended next step

Do not modify source code or documentation.
Do not report Git status or repository housekeeping information.