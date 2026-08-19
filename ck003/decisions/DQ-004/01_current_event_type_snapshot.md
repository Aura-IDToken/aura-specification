# DQ-004 — Current Event-Type Snapshot

**Classification:** EVIDENCE
**Status:** OPEN
**Review date:** 2026-08-18

## Verified source

`aps/APS-200_CANONICAL_DATA_MODEL.md` on `main`, SHA-1 `c974f59088935883657b1c3b2742bb48a63e52fb`.

## Current definition

ENT-007 Audit Record contains a required field:

`event_type: string — Canonical event type`

The current source does not define a closed vocabulary, exact grammar, registry, namespace, extensibility rule, or version-binding rule for `event_type`.

## Consequence

The field is structurally required but its semantic decision space is incomplete. This is sufficient to establish that DQ-004 remains OPEN; it is not sufficient to choose a new event-type vocabulary without an approved decision.

## Required closure decision

DQ-004 must define at minimum:

1. canonical event-type vocabulary or registry;
2. case and character rules;
3. whether unknown values are rejected in strict conformance mode;
4. whether event types are version-bound;
5. whether event-type meaning affects canonical bytes or hash inputs;
6. compatibility/evolution rules.

## Evidence boundary

No implementation behaviour is promoted to normative semantics by this snapshot.
