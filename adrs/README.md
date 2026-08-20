# Architecture Decision Records

This directory contains all Architecture Decision Records (ADRs) for the Aura Protocol.

## What Is an ADR?

An ADR documents a single architectural or protocol decision: **what** was decided, **why**, and what the **consequences** are.

ADRs are permanent records. They are never deleted. A superseded ADR is marked SUPERSEDED with a reference to its replacement.

## Index

| ID | Title | Status | Date |
|----|-------|--------|------|
| [ADR-001](ADR-001_REPOSITORY_STRUCTURE.md) | Canonical Repository Structure | ACCEPTED | 2026-07-23 |
| [ADR-CK003-DQ006](../ck003/dq-006-canonical-serialization/ADR-CK003-DQ006-CANONICAL-SERIALIZATION.md) | Canonical Serialization Profile — RFC 8785 (JCS) | ENACTED | 2026-08-20 |
| [ADR-CK003-DQ002](../ck003/dq-002-hash-domain/ADR-CK003-DQ002-HASH-DOMAIN.md) | Hash Domain — RFC 6962 leaf/node separation | PROPOSED | 2026-08-17 |

The two CK-003 ADRs live under `ck003/` beside the evidence packages that produced
them, and are indexed here so this table remains the entry point. The normative
contract for canonical serialization is **APS-200 §8**, not the ADR; the ADR
records the decision.

## Process

1. Copy [`../templates/ADR_TEMPLATE.md`](../templates/ADR_TEMPLATE.md)
2. Assign next sequential `ADR-NNN`
3. File in this directory
4. Submit pull request
5. Merging = accepting

ADRs for major decisions require a linked RFC.

See [GOVERNANCE.md](../GOVERNANCE.md) §6 for the full process.
