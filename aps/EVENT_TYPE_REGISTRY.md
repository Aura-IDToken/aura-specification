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

## 5. Current normative vocabulary

**No individual event token is promoted to final normative status by this document yet.**

Reason: the current APS corpus establishes the existence and role of `ENT-007.event_type`, but does not provide sufficient normative evidence for a complete closed vocabulary. Adding tokens from implementation code alone would convert implementation behaviour into protocol authority.

Until entries are registered, strict conformance implementations MUST reject an `event_type` value that is not present in an approved versioned registry.

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

**DQ-004:** `SEMANTIC CONTRACT DEFINED / VOCABULARY REGISTRY PENDING NORMATIVE ENTRIES`.

This document MUST NOT be used to claim DQ-004 PASS until the approved event vocabulary and corresponding fixtures exist.

## 10. Source constraint

This registry intentionally preserves the distinction between source evidence and normative decision. APS-200 defines `ENT-007.event_type` as a required canonical event-type string but does not provide the closed vocabulary. APS-001 identifies DQ-004 event-type semantics as an explicit closure dependency. The missing vocabulary therefore remains an open specification decision.
