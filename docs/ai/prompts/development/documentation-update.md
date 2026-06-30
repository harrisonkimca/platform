# Documentation Update

## Purpose

Synchronize repository documentation with the current implementation.

Responsibilities

* Update the project handover.
* Update the roadmap when implementation status changes.
* Eliminate documentation drift.
* Ensure documentation accurately reflects the repository.

This prompt updates implementation documentation only.

It does not modify architectural documentation, authentication requirements,
or Architecture Decision Records.

---

Update repository documentation.

Reference:

* README.md
* docs/roadmap.md
* docs/project-handover.md
* docs/authentication-spec.md
* docs/decisions.md

Document responsibilities:

README.md

* Defines the long-term project vision and architectural intent.
* **Do not modify.**

roadmap.md

* Defines the implementation contract.
* Update only when implementation progress or roadmap scope changes.

project-handover.md

* Defines the current repository implementation snapshot.
* Update to reflect the current implementation.

authentication-spec.md

* Defines authentication behavior.
* **Do not modify.**

decisions.md

* Defines architectural constraints.
* **Do not modify.**
* New ADRs are handled exclusively by `adr-audit.md`.

Requirements:

* Keep every document aligned with its responsibility.
* Do not duplicate information between documents.
* Remove documentation drift.
* Reflect the source code accurately.
* Do not reinterpret implementation beyond what exists in the repository.

Provide a summary of every document updated and why.