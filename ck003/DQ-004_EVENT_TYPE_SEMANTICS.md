# DQ-004 — Event-Type Semantic Closure

**Status:** PROPOSED CLOSURE — pending incorporation into APS-200/APS-001 approval
**Decision scope:** `ENT-007 Audit Record.event_type`
**Branch:** `ck003/closure-workspace`

## 1. Current normative state

APS-200 defines `ENT-007 — Audit Record` and requires `event_type: string` as a **MUST** field described as the "Canonical event type". It does not currently define a closed vocabulary, event-type grammar, lifecycle semantics, or a machine-readable schema for this field.

APS-001 further requires closed vocabularies defined by an applicable APS/schema to reject unknown values in strict conformance mode. Therefore the current repository state is insufficient to claim DQ-004 CLOSED: the field is structurally required but semantically under-specified.

## 2. Architectural decision

`event_type` SHALL be a protocol-defined semantic discriminator for the kind of auditable protocol event represented by an ENT-007 record.

It SHALL NOT be:

- a free-form human description;
- an implementation class name;
- a policy decision value;
- a severity level;
- an opaque correlation/request identifier;
- a timestamp-derived value.

The value SHALL be deterministic, case-sensitive, ASCII, and represented as a single canonical token.

## 3. Canonical representation

For the current protocol profile:

```text
[A-Z][A-Z0-9_]*
```

The canonical token is UTF-8 encoded as ASCII-compatible bytes with no surrounding whitespace.

No case folding, whitespace normalization, aliases, localization, or implementation-specific spelling is permitted in the digest domain.

## 4. Vocabulary policy

The normative vocabulary SHALL be maintained by APS-200 (or a subordinate approved event-type registry explicitly incorporated by APS-200).

Strict conformance mode SHALL reject an `event_type` not present in the approved vocabulary.

The registry SHALL define, for every value:

1. canonical token;
2. semantic definition;
3. allowed producer/context;
4. required payload contract;
5. whether the event participates in protocol state transition semantics;
6. version introduced;
7. deprecation/replacement status, if applicable.

Adding a new event type is a versioned specification change when it affects validation, canonical bytes, evidence interpretation, or conformance outcomes.

## 5. Initial vocabulary decision

This closure package deliberately does **not** invent an arbitrary final business-event vocabulary from implementation names. Existing source material proves the existence and structural role of `event_type`, but does not provide sufficient normative evidence for a complete approved list.

Therefore the initial approved vocabulary is:

```text
EMPTY SET
```

until the event registry is explicitly populated and approved.

An implementation claiming strict ENT-007 conformance MUST reject unknown/unregistered event types. This avoids silently turning observed implementation strings into protocol semantics.

## 6. Required follow-up to close DQ-004 completely

Create the normative registry:

```text
aps/EVENT_TYPE_REGISTRY.md
```

and a machine-readable form:

```text
fixtures/schemas/event_types.json
```

The registry MUST contain the approved initial event types and their payload contracts. The first fixture SHALL test both an approved value and an unregistered value.

## 7. Conformance mapping

| Requirement | Verification | Fixture | RI-PY | RI-RS |
|---|---|---|---|---|
| `event_type` required on ENT-007 | CONF-012 | FIX-DQ004-001 | Required | Required |
| Canonical token grammar | CONF-012 | FIX-DQ004-002 | Required | Required |
| Unknown value rejected in strict mode | CONF-012 | FIX-DQ004-003 | Required | Required |
| Same event type → same canonical bytes | CONF-012 | FIX-DQ004-004 | Required | Required |
| Cross-language digest equality | CONF-012 | FIX-DQ004-004 | Required | Required |

## 8. Impact

**APS-001:** closes the semantic dependency once the registry is incorporated and approved.

**APS-200:** MUST define or normatively incorporate the event-type registry and validation rule.

**APS-300:** Evidence referring to audit events MUST preserve the canonical event type without semantic reinterpretation.

**APS-400/500:** add DQ-004 conformance cases and fixtures.

**INV-012:** directly affected because the invariant requires an APS-conformant audit trail.

**INV-003 / INV-011:** affected because event type participates in the canonical Audit Record representation and therefore its spelling must be unambiguous before hashing.

**RI-PY / RI-RS:** MUST consume the same vocabulary and produce identical canonical bytes for shared fixtures.

## 9. Verdict

**DQ-004 = OPEN → SEMANTIC CONTRACT DEFINED, VOCABULARY NOT YET APPROVED.**

The correct closure state is therefore **BLOCKED FOR FINAL CLOSURE**, not PASS.

The blocker is deliberately narrow: the repository has not supplied a normative event-type vocabulary and payload registry. This package resolves the semantics of the field without fabricating implementation-derived values.
