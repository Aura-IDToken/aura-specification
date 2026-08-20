# ADR-CK003-DQ006 — Canonical Serialization Profile

- **Status:** ENACTED — the decision is written into APS-200 §8; approval is the merge act (GOVERNANCE.md §2)
- **Enacted:** 2026-08-20 (CK-003)
- **Normative text:** `aps/APS-200_CANONICAL_DATA_MODEL.md` §8 — **this ADR records the decision; APS-200 §8 states the contract**
- **Scope:** Protocol-bound canonical object bytes
- **Related:** INV-003, INV-006, INV-011, APS-200 §8, APS-300 §5.1, APS-500, CONF-003

> **Read APS-200 §8 for the contract.** This ADR is the decision record — the
> *why*. Where its wording differs from APS-200 §8, APS-200 §8 governs. Two
> constraints proposed below were refined during enactment; see "Enactment
> notes".

## Decision

Aura Protocol SHALL use **JSON Canonicalization Scheme (JCS), RFC 8785**, as the canonical serialization profile for protocol objects whose normative representation is JSON.

The canonicalization pipeline is:

```text
validated protocol object
        ↓
semantic object model
        ↓
JCS / RFC 8785
        ↓
UTF-8 canonical bytes
        ↓
hash domain
```

The canonical byte domain is therefore the exact UTF-8 byte sequence produced by RFC 8785 JCS. A pretty-printed JSON representation, parser-preserving source text, key insertion order, or hexadecimal hash representation is never itself the canonical byte domain.

## Normative constraints (as proposed)

1. Object member ordering SHALL be determined by JCS, not implementation insertion order.
2. No insignificant whitespace SHALL occur in canonical bytes.
3. Strings SHALL use the JCS/JSON UTF-8 representation.
4. Numbers SHALL obey RFC 8785 serialization rules; implementations MUST NOT introduce non-JSON numeric values such as NaN or Infinity.
5. Protocol objects SHALL be schema-validated before canonicalization.
6. Fields excluded from a hash domain MUST be explicitly defined by the applicable object/hash specification; omission MUST NOT be inferred from implementation behaviour.
7. Hashing SHALL consume canonical bytes directly. Hexadecimal digest strings SHALL never be substituted for digest bytes in the cryptographic domain.
8. JCS is the canonical representation profile; alternate wire encodings MAY exist only as transport representations and MUST round-trip to the same semantic object and canonical bytes.

## Why this closes the current ambiguity

APS-200 currently permits JSON, CBOR and Protocol Buffers while requiring deterministic serialization, but §8 leaves the interoperability serialization format TODO. This proposal selects one language-independent, deterministic JSON canonicalization profile for the protocol's canonical byte boundary.

## Compatibility

Changing canonical serialization is a protocol compatibility event. Existing evidence MUST retain its original serialization/hash profile identity. Historical evidence MUST NOT be silently reinterpreted under JCS.

## Conformance

CONF-003 SHALL verify that two independent serializations of the same validated object produce byte-identical JCS output. The canonical fixture corpus SHALL store canonical bytes (or an unambiguous byte encoding) and expected digests.

## Enactment notes

Two proposed constraints changed shape when written into APS-200 §8. Recorded here
so the difference is visible rather than silent:

1. **"Protocol objects SHALL be schema-validated before canonicalization"**
   (constraint 5) became two separate rules in APS-200 §8.2. Canonicalization is
   *total over the JSON data model* — it is a pure function of a JSON value and
   asserts nothing about schema validity. Validation-before-canonicalization is
   retained as a requirement on **protocol operations**, not as a precondition of
   the canonicalization function. Without this split, the canonicalization contract
   would inherit every open entity-model and event-registry question, and the
   CANONICAL-001 vector could not be scoped.

2. **Unicode normalization** was not addressed by the proposal. APS-200 §8.3 now
   prohibits it explicitly, in either direction, rather than leaving it unstated.

## Closure gate

| Condition | State |
|---|---|
| APS-200 §8 updated to bind the profile | **DONE** — enacted 2026-08-20 |
| APS-300 hash/evidence scope reconciled with canonical bytes | **DONE** — APS-300 §5.1 |
| At least one normative cross-language fixture frozen | **DONE** — CANONICAL-001, FROZEN |
| RI-PY and RI-RS produce identical canonical bytes and digests | **DONE** — CROSS-LANGUAGE-001 PASS; re-executed 2026-08-20 |
| Version/migration semantics documented | **DONE** — APS-200 §8.6 |
| Chief Architect approval recorded | **PENDING** — merge act under GOVERNANCE.md §2; AI assistants may propose, never approve or freeze |

The APS documents this ADR amends remain `1.0-DRAFT`. Enactment means the contract
is written and self-consistent, not that APS-200 is frozen. Freezing is the Chief
Architect's act.
