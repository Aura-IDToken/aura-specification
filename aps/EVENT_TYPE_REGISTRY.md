# Aura Event-Type Registry

**Document:** Event-Type Registry  
**Status:** DRAFT — DQ-004 closure artifact  
**Authority:** APS-001 / APS-200 / APS-100  
**Purpose:** Define the normative contract for `ENT-007.event_type` without inventing event vocabulary that is not supported by the current specification corpus.

## 1. Scope

`event_type` is the semantic discriminator of an `ENT-007 — Audit Record`. APS-200 currently requires the field and calls it a “Canonical event type”, but does not yet define a closed vocabulary. This registry therefore establishes the binding rules first; individual event tokens become normative only when explicitly registered below.

## 2. Canonical token contract

A registered `event_type` MUST:

- be a UTF-8 string;
- use ASCII characters only for the canonical token;
- match `^[A-Z][A-Z0-9_]*$`;
- be case-sensitive;
- contain no whitespace;
- contain no aliases or implementation-specific spellings;
- identify one protocol-defined audit-event semantic;
- be explicitly registered before it may be emitted in strict conformance mode.

An implementation MUST NOT silently normalize an unknown token into a known token.

## 3. Validation semantics

```text
registered token  -> ACCEPT
unknown token     -> REJECT in strict conformance mode
malformed token   -> REJECT
alias             -> REJECT
implementation-local token -> REJECT as normative event_type
```

The registry itself is not an authorization mechanism. It defines protocol vocabulary and semantic identity.

## 4. Event definition record

Every normative registry entry MUST define:

| Property | Requirement |
|---|---|
| `event_type` | Canonical token |
| `description` | Normative semantic meaning |
| `producer` | Protocol component/profile permitted to emit it |
| `payload_schema` | Canonical payload contract |
| `introduced_protocol_version` | Version in which the token became valid |
| `deprecated` | Boolean/status |
| `replacement` | Required when deprecated |

## 5. Current vocabulary posture

### 5.1 Release-grade normative vocabulary

The full release-grade event vocabulary is **not yet complete**. The current APS corpus still lacks the broader approved list needed for final DQ-004 closure across all audit-event semantics.

### 5.2 Repository-local draft gate vocabulary

The repository now registers one controlled draft token for the local `CONF-012` gate:

| event_type | Scope | Source |
|---|---|---|
| `AUDIT_RECORD` | repository-local draft auditability gate only | `ck003/decisions/DQ-004/CURRENT_EVENT_TYPE_REGISTRY.md` |

This token is sufficient for the current local draft gate because it is now explicitly registered and bound to `FIX-INV-012`. It does **not** imply that the complete protocol event vocabulary is finished or release-ready.

Strict conformance implementations MUST reject an `event_type` value that is not present in the applicable approved versioned registry.

## 6. Version binding

The event-type registry is protocol-version bound. A token MAY be introduced, deprecated or retired only through an approved specification change with explicit compatibility analysis.

Changing the semantic meaning of an existing token is a breaking normative change and MUST NOT be performed in place.

## 7. Canonicalization

`event_type` participates in canonical object serialization exactly as defined by APS-200's approved serialization profile. This registry does not define an alternative hash or serialization domain.

The token's canonical byte representation is therefore the UTF-8 encoding of the exact registered token after validation; no case folding, whitespace normalization or alias expansion is permitted.

## 8. Conformance mapping

| Requirement | Verification |
|---|---|
| token syntax | DQ-004 fixture |
| closed vocabulary | registry membership fixture |
| unknown-token rejection | negative fixture |
| alias rejection | negative fixture |
| version binding | version fixture |
| canonical byte identity | shared RI-PY / RI-RS fixture |

## 9. Closure status

**DQ-004:** `READY AT REPOSITORY-LOCAL DRAFT LEVEL / FINAL VOCABULARY STILL OPEN`.

This document MUST NOT be used to claim release-grade DQ-004 PASS until the broader approved event vocabulary and corresponding implementation evidence exist.

## 10. Source constraint

This registry intentionally preserves the distinction between source evidence and normative decision. APS-200 defines `ENT-007.event_type` as a required canonical event-type string but does not provide the closed vocabulary. APS-001 identifies DQ-004 event-type semantics as an explicit closure dependency. The missing vocabulary therefore remains an open specification decision.
