# AI Development Workflow

## Purpose

This workflow defines how AI tools are used throughout the project lifecycle.

Goals:

* Maintain architectural consistency
* Preserve DDD-inspired boundaries
* Preserve modular monolith principles
* Preserve future CQRS adoption
* Preserve future event-driven evolution
* Preserve future service extraction

---

# Architecture Context Package

When starting a new Codex or ChatGPT session, provide the latest versions of:

* docs/project-handover.md
* docs/roadmap.md
* docs/authentication-spec.md
* docs/decisions.md

These documents are the authoritative project context.

## Responsibilities

### project-handover.md

Current state of the project.

Contains:

* Current architecture
* Current phase
* Current step
* Implemented concepts
* Repository state
* Known constraints

### roadmap.md

Future project evolution.

Contains:

* Phases
* Goals
* Deliverables
* Evolution path

### authentication-spec.md

Authentication requirements and business behavior.

### decisions.md

Architectural Decision Records (ADRs).

Contains:

* Historical decisions
* Architectural constraints
* Reasons for decisions

---

# Development Workflow

For every roadmap step:

## Step 1 – Start Phase Planning

Provide the Architecture Context Package.

Run:

* Phase Start Prompt

Expected output:

* Goal
* Files expected to change
* Domain concepts affected
* Architectural risks
* Implementation plan

Review the plan before proceeding.

---

## Step 2 – Implement

Run:

* Implementation Prompt

Expected output:

* Code changes only

Documentation should not be updated yet.

---

## Step 3 – Architecture Review

Run:

* Architecture Review Prompt

Expected output:

* Files added
* Files modified
* New concepts
* New entities
* New value objects
* New services
* New repositories
* New events
* Technical debt
* Remaining work
* Recommended next step

---

## Step 4 – External Architecture Evaluation

Provide the Architecture Context Package if necessary.

Paste the Architecture Review Report into ChatGPT.

Request:

"Perform an architecture review."

ChatGPT evaluates:

* DDD boundaries
* Aggregate design
* Repository boundaries
* CQRS readiness
* Event-driven evolution
* State machine placement
* Future service extraction concerns
* ADR implications

Possible outcomes:

* Approved
* Approved with recommendations
* Changes required

---

## Step 5 – ADR Check

If significant architectural decisions were made:

Run:

* ADR Check Prompt

If an ADR is required:

* Append a new ADR to decisions.md

Do not modify historical ADRs.

---

## Step 6 – Documentation Update

After architecture review approval:

Run:

* Documentation Update Prompt

Update:

* project-handover.md
* roadmap.md
* decisions.md (if required)

Do not modify authentication-spec.md unless requirements changed.

---

## Step 7 – Commit

Commit the completed work.

Example:

```shell
git add .
git commit -m "Phase X Step Y complete"
```

---

# Phase Completion Workflow

When an entire phase is completed:

Run:

* Phase Completion Prompt

Review:

* Deliverables completed
* Architectural consistency
* ADR compliance
* Technical debt
* Readiness for next phase

Update project-handover.md if required.

Commit the phase completion.

---

# Starting A New ChatGPT Session

A new ChatGPT session does not automatically know:

* Current architecture
* Current roadmap progress
* Recent implementations
* New ADRs

Provide:

* project-handover.md
* roadmap.md
* authentication-spec.md
* decisions.md

Then provide:

* The current phase
* The current step
* The Codex Architecture Review Report (if requesting review)

This ensures architecture evaluations are based on the latest project state.

---

# Source Of Truth

The following documents are authoritative:

* project-handover.md
* roadmap.md
* authentication-spec.md
* decisions.md

All development decisions should remain consistent with these documents.