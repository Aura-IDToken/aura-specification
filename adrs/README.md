# Architecture Decision Records

This directory contains all Architecture Decision Records (ADRs) for the Aura Protocol.

## What Is an ADR?

An ADR documents a single architectural or protocol decision: **what** was decided, **why**, and what the **consequences** are.

ADRs are permanent records. They are never deleted. A superseded ADR is marked SUPERSEDED with a reference to its replacement.

## Index

| ID | Title | Status | Date |
|----|-------|--------|------|
| [ADR-001](ADR-001_REPOSITORY_STRUCTURE.md) | Canonical Repository Structure | ACCEPTED | 2026-07-23 |

Only ADRs listed in this index are active records for current repository policy.
Archived drafts or duplicate historical representations may remain in the repository for traceability, but they are non-active unless reintroduced through the normal ADR process.

## Process

1. Copy [`../templates/ADR_TEMPLATE.md`](../templates/ADR_TEMPLATE.md)
2. Assign next sequential `ADR-NNN`
3. File in this directory
4. Submit pull request
5. Merging = accepting

ADRs for major decisions require a linked RFC.

See [GOVERNANCE.md](../GOVERNANCE.md) §6 for the full process.
