# Requests for Comments

This directory contains all RFCs (Requests for Comments) for the Aura Protocol.

## What Is an RFC?

An RFC is a formal proposal for a protocol change. It is the mandatory process for any change that affects:
- Protocol behavior
- Protocol Invariants
- Conformance Tests
- Evidence structure
- Constitutional principles

## Index

| ID | Title | Status | Date |
|----|-------|--------|------|
| [RFC-001](RFC-001_APS001_MILESTONE1_EXECUTION_SCOPE.md) | APS-001 Milestone 1 Execution Scope | DRAFT | 2026-09-26 |

## RFC Lifecycle

```
DRAFT (open PR)
    ↓
COMMENT PERIOD (minimum 14 days)
    ↓
REVIEW (Architecture Review Board)
    ↓
ACCEPTED or REJECTED
    ↓
(if ACCEPTED) Implementation PR referencing RFC
```

Both ACCEPTED and REJECTED RFCs are permanently preserved.

## Process

1. Copy [`../templates/RFC_TEMPLATE.md`](../templates/RFC_TEMPLATE.md)
2. Assign next sequential `RFC-NNN`
3. File in this directory
4. Open pull request — this starts the comment period
5. Respond to feedback by updating the RFC in the PR
6. Do not merge your own RFC

See [GOVERNANCE.md](../GOVERNANCE.md) §7 for the full process.
