# ADR-CK003-DQ006 — Canonical Serialization Profile

- **Status:** ACCEPTED — bound into APS-200 §8. DQ-006 closure verdict ratified 2026-08-20 (DQ-006 CLOSURE INTEGRATION); see §9.
- **Classification:** DECISION
- **Scope:** Protocol-bound canonical object bytes
- **Normative home:** APS-200 §8 (single authority)
- **Related:** INV-003, INV-006, INV-011, APS-200 §8, APS-300 §5, CONF-003, ADR-CK003-DQ002 (hash domain)
- **Closure record:** [`closures/DQ-006_CLOSURE_PACKAGE.md`](../../closures/DQ-006_CLOSURE_PACKAGE.md)
- **Reconciled:** 2026-08-20 (DQ-006 CLOSURE RECONCILIATION)

## 1. Decision

Aura Protocol uses **JSON Canonicalization Scheme (JCS), RFC 8785**, as the canonical serialization profile for protocol objects whose normative representation is JSON.

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

The canonical byte domain is the exact UTF-8 byte sequence produced by RFC 8785 JCS. A pretty-printed JSON representation, parser-preserving source text, key insertion order, or hexadecimal hash representation is never itself the canonical byte domain.

**This ADR records the decision. It does not restate the normative rule.** The normative rule lives in APS-200 §8 and in APS-300 §5 for the evidence-hash domain. Where this ADR and APS-200 §8 could be read differently, APS-200 §8 governs.

## 2. Normative contract vs. conformance implementation detail

This distinction is the core of the decision and MUST NOT be collapsed.

| Layer | Content | Authority | Changeable by |
|---|---|---|---|
| **NORMATIVE PROTOCOL CONTRACT** | RFC 8785 JCS; UTF-8 `canonical_bytes`; `SHA-256(canonical_bytes)`; RFC 6962 leaf `SHA-256(0x00 \|\| canonical_bytes)`; interior node `SHA-256(0x01 \|\| l \|\| r)` | APS-200 §8, APS-300 §5 | Approved specification change only |
| **CONFORMANCE IMPLEMENTATION DETAIL** | RI-PY engine `rfc8785` 0.1.4; RI-RS engine `serde_json_canonicalizer` 0.3.2; adapter modules; corpus layout; runner scripts | Reference-implementation repositories | Reference implementations, without a protocol change |

The Python and Rust libraries are **not** the protocol. The protocol is RFC 8785 JCS plus the hash/Merkle domain defined in APS-200 §8.5. Pinning an engine version freezes *evidence reproducibility*, not protocol semantics. A different RFC 8785-conformant engine is not thereby non-conformant; an engine that disagrees with RFC 8785 is non-conformant regardless of which repository it lives in.

Naming an engine here does not authorize its introduction into any production runtime dependency graph.

## 3. Normative constraints

These constraints are recorded here for decision traceability. Each is realised normatively in APS-200 §8.

1. Object member ordering is determined by JCS, not implementation insertion order. — APS-200 §8.3
2. No insignificant whitespace occurs in canonical bytes. — APS-200 §8.3
3. Strings use the JCS/JSON UTF-8 representation; non-ASCII is raw UTF-8. — APS-200 §8.3
4. Numbers obey RFC 8785 serialization rules; `NaN`/`Infinity` are rejected, never coerced. — APS-200 §8.3
5. Protocol objects are schema-validated before canonicalization. — APS-200 §8.2(1)
6. Fields excluded from a hash domain are explicitly defined by the applicable object/hash specification; omission is never inferred from implementation behaviour. — APS-200 §4, APS-300 §5.1
7. Hashing consumes canonical bytes directly; hexadecimal digest strings are never substituted for digest bytes. — APS-200 §8.4
8. JCS is the canonical representation profile; alternate wire encodings are transport only and MUST round-trip to the same semantic object and canonical bytes. — APS-200 §8.1
9. Canonical serialization determines representation only — never event semantics, version semantics, identity semantics or Merkle construction semantics. — APS-200 §8.7

## 4. Why this closed the ambiguity

Before this decision, APS-200 §8 permitted JSON, CBOR and Protocol Buffers while requiring deterministic serialization, and left the interoperability serialization format as a `TODO`. INV-003 therefore had no executable byte domain, and CONF-003 could not state a byte-level expectation. The decision selects one language-independent, deterministic JSON canonicalization profile as the protocol's canonical byte boundary, and APS-200 §8 now carries it normatively.

## 5. Compatibility

Binding the canonical serialization profile is a protocol compatibility event. Existing evidence retains its original serialization/hash profile identity. Historical evidence MUST NOT be silently reinterpreted under JCS. — APS-200 §8.8, APS-300 §5.3

## 6. Conformance

CONF-003 is the normative conformance requirement for this decision. It requires byte-level equality between **independently produced** RI-PY and RI-RS canonical bytes, plus independent recomputation of `SHA-256(canonical_bytes)` and `SHA-256(0x00 || canonical_bytes)` on each side, plus discriminating negative controls.

## 7. Executed evidence

Fixture **CANONICAL-001** — `{"event_type":"AUDIT_RECORD","payload":{"value":42},"protocol_version":"1.0","schema_version":"1.0"}`

| Property | Value |
|---|---|
| `canonical_bytes` length | 100 |
| `canonical_bytes` (hex) | `7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d` |
| `SHA-256(canonical_bytes)` | `b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6` |
| `SHA-256(0x00 \|\| canonical_bytes)` | `ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039` |

| Implementation | Repository | Execution commit | Engine | Result |
|---|---|---|---|---|
| RI-PY | `Aura-IDToken/aura-poc-a-core-v3.3` | `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f` | `rfc8785` 0.1.4 | PASS |
| RI-RS | `Aura-IDToken/aura-guard-v1.3` | `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2` | `serde_json_canonicalizer` 0.3.2 | PASS |

Canonical-byte equality, SHA-256 equality and RFC 6962 leaf equality: **PASS** (CROSS-LANGUAGE-001). Negative controls (mutated bytes, mutated digest, wrong leaf domain `0x01`): **PASS** — the gate rejected each. Production runtime in both repositories: **unchanged**.

Full evidence ledger: [`closures/DQ-006_CLOSURE_PACKAGE.md`](../../closures/DQ-006_CLOSURE_PACKAGE.md).

## 8. Evidence limitation, and how it was closed

CANONICAL-001 is **JCS-degenerate**: for this object, RFC 8785 and an ordinary sorted-JSON serializer (`json.dumps(sort_keys=True, separators=(",",":"), ensure_ascii=False)`) produce identical bytes, and therefore identical digests. All keys are ASCII, no member ordering depends on UTF-16 code units, the only number is a small integer, and no string requires non-trivial escaping. This was verified by recomputation and is recorded in [`ck003/handover-assessment/10_INDEPENDENT_VERIFICATION.md`](../handover-assessment/10_INDEPENDENT_VERIFICATION.md) §3.2.

Consequence: CROSS-LANGUAGE-001 establishes that RI-PY and RI-RS **agree** on this object. It does not, by itself, establish that both **implement RFC 8785**.

Partial mitigation on the RI-PY side only: the executed `conformance/canonical/test_jcs_behavior.py` suite (13 passed) exercises RFC-8785-discriminating behaviour — ES6 number form (`1.0` → `1`, `1e21` → `1e+21`), rejection of non-finite numbers, minimal escaping, raw UTF-8 for non-ASCII, and member ordering. The RI-RS side has no equivalent executed behavioural suite; its `canonical_001` test covers member ordering, array order, UTF-8 validity, whitespace absence and the leaf domain, none of which distinguish RFC 8785 from sorted JSON.

**Closed 2026-08-20 (DQ-006-R1).** The fixture **CANONICAL-002** was added and
executed on both frozen engines. It is 655 canonical bytes against 716 bytes of
sorted JSON for the same input, exercising UTF-16 code-unit member ordering, raw
UTF-8 output, ECMAScript number form, negative-zero normalisation, exponent form,
recursive canonicalisation, array-order preservation and minimal escaping. RI-PY
and RI-RS produced identical bytes, digest and leaf. A fourth negative control
substitutes sorted-JSON output for one side: it is inert on CANONICAL-001 and is
rejected on CANONICAL-002.

The cross-language evidence therefore now demonstrates conformance to RFC 8785,
not merely agreement, and the DQ-006 closure verdict is no longer constrained by
this limitation. CANONICAL-001 remains in the corpus unchanged; its degeneracy is
a property of that vector, recorded so no future reader over-reads it.

Evidence: [`ck003/dq-006-closure/DQ-006_EVIDENCE.md`](../dq-006-closure/DQ-006_EVIDENCE.md).

## 9. Closure gate

| Condition | State |
|---|---|
| APS-200 §8 updated to bind the profile | **DONE** — APS-200 §8 (DRAFT, mutable per VERSIONING.md §3) |
| APS-300 hash/evidence scope reconciled with canonical bytes | **DONE** — APS-300 §5.1–§5.3 |
| At least one normative cross-language fixture frozen | **DONE** — CANONICAL-001 |
| RI-PY and RI-RS produce identical canonical bytes and expected digests | **DONE** — CROSS-LANGUAGE-001 PASS |
| Version/migration semantics documented | **DONE** — APS-200 §8.8, APS-300 §5.3 |
| Cross-language evidence that discriminates RFC 8785 from sorted JSON | **DONE** — CANONICAL-002; see §8 |
| Chief Architect ratification of the closure verdict | **DONE** — DQ-006 CLOSURE INTEGRATION, 2026-08-20 |
| Evidence merged to the default branch of each RI repository | **CARRIED** — published and reachable by SHA; not on `main`. Closure package §13 item C-1 |

The decision in §1 is accepted and normatively bound, and the DQ-006 gate is
**CLOSED**. The one outstanding row is repository hygiene carried to the release
gate; it does not qualify the decision or the evidence. See the closure package
for the verdict.
