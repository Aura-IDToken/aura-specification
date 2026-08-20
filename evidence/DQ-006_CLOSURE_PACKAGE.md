# DQ-006 — Closure Package

> **SUPERSEDED — 2026-08-20.** This record is retained for history only.
> The single authoritative DQ-006 closure record is [`../closures/DQ-006_CLOSURE_PACKAGE.md`](../closures/DQ-006_CLOSURE_PACKAGE.md),
> which reconciles this material against APS-200 §8, APS-300 §5, ADR-CK003-DQ006 and CONF-003.
> Where this document differs from that record — including its status line — that record governs.
> **DQ-006 status of record: CLOSED** (2026-08-20, DQ-006 CLOSURE INTEGRATION).
> The closure now rests on two fixtures: CANONICAL-001 and the JCS-discriminating
> CANONICAL-002. Consolidated evidence:
> [`ck003/dq-006-closure/DQ-006_EVIDENCE.md`](../ck003/dq-006-closure/DQ-006_EVIDENCE.md).

Document ID: DQ-006-CLOSURE-001  
Status: **CLOSED — PASS**  
Authority: DQ-006 / APS-200 / APS-300 / APS-400  
Closure date: 2026-08-19

---

## 1. Decision

DQ-006 — canonical serialization / cross-language canonical equality — is closed as **PASS**.

The closure is based on independently executed RI-PY and RI-RS CANONICAL-001 artifacts and an automated equality gate. The evidence demonstrates equality of the actual canonical byte streams, their SHA-256 digests, and their RFC-6962 leaf hashes.

This closure does **not** modify production hashing, Merkle behavior, event-type semantics, or runtime canonicalization.

---

## 2. Frozen Canonical Contract

| Property | Normative value |
|---|---|
| Canonicalization | RFC 8785 JCS |
| RI-PY conformance engine | `rfc8785==0.1.4` |
| RI-RS conformance engine | `serde_json_canonicalizer==0.3.2` |
| Digest | `SHA-256(canonical_bytes)` |
| RFC-6962 leaf domain | `0x00` |
| Leaf | `SHA-256(0x00 || canonical_bytes)` |
| Production runtime changes | None |

The JCS engines are conformance-only. They are not asserted here as production runtime dependencies.

---

## 3. CANONICAL-001 Input

```json
{
  "event_type": "AUDIT_RECORD",
  "payload": {
    "value": 42
  },
  "protocol_version": "1.0",
  "schema_version": "1.0"
}
```

Canonical output length: **100 bytes**.

Canonical bytes:

```text
7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d
```

SHA-256:

```text
b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
```

RFC-6962 leaf:

```text
ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

---

## 4. Independent RI Evidence

### RI-PY

Repository: `Aura-IDToken/aura-poc-a-core-v3.3`  
Execution commit: `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f`  
Engine: `rfc8785==0.1.4`  
Result: **PASS**

Artifact:
`conformance/corpus/canonical-001/ri-py.json`

### RI-RS

Repository: `Aura-IDToken/aura-guard-v1.3`  
Execution commit: `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2`  
Engine: `serde_json_canonicalizer==0.3.2`  
Result: **PASS**

Artifact origin:
`conformance/corpus/canonical-001/ri-rs.json`

The RI-RS artifact was transported byte-identically into the RI-PY corpus for the bridge comparison. It was not reconstructed or re-keyed.

---

## 5. Cross-Language Equality

The automated bridge independently verified:

| Check | Result |
|---|---|
| RI-PY canonical bytes integrity | PASS |
| RI-RS canonical bytes integrity | PASS |
| Canonical bytes equality | PASS |
| RI-PY SHA recomputation | PASS |
| RI-RS SHA recomputation | PASS |
| SHA equality | PASS |
| RI-PY leaf recomputation | PASS |
| RI-RS leaf recomputation | PASS |
| Leaf equality | PASS |
| Frozen expected-value cross-check | PASS |

CROSS-LANGUAGE-001 verdict: **PASS**.

---

## 6. Negative Controls

The bridge was demonstrated to reject invalid evidence:

- mutated canonical bytes → **FAIL**
- mutated SHA-256 → **FAIL**
- wrong leaf domain → **FAIL** through independent leaf recomputation

All mutations were temporary and were not committed to the canonical corpus.

---

## 7. Production Integrity

The conformance work did not alter production protocol execution paths.

RI-PY:

- `core/` unchanged
- `audit/` unchanged

RI-RS:

- `src/` unchanged
- production `Cargo.toml` unchanged
- production `Cargo.lock` unchanged

Therefore DQ-006 closure is a **conformance/evidence closure**, not a production-runtime change.

---

## 8. Traceability

```text
APS-200 canonical serialization
        ↓
INV-003 Canonical Serialization
        ↓
CONF-003
        ↓
CANONICAL-001
        ↓
RI-PY + RI-RS
        ↓
CROSS-LANGUAGE-001
        ↓
DQ-006 = PASS / CLOSED
```

Version semantics remain governed by the versioning decision space and CONF-008 / INV-009. DQ-006 does not reopen DQ-003.

---

## 9. Evidence Provenance

The execution reports were produced in dedicated conformance branches. Branch-name deviations from the preferred `ck003/*` naming were explicitly declared by the executor and do not affect protocol evidence.

The artifact commit fields identify the clean source commits that produced the artifacts; publication commits are separate to avoid self-reference.

The equality gate is therefore evidence-producing rather than a comparison of two copies of a precomputed constant.

---

## 10. Closure Constraints

This closure does not imply that the entire Aura specification is closed.

Remaining work includes, at minimum:

- DQ-002 final closure;
- INV-001…INV-015 complete closure;
- completion of missing conformance tests;
- canonical fixture corpus completion;
- conformance runner and CI gates;
- release traceability and final specification freeze.

---

## 11. Final Verdict

**DQ-006: CLOSED — PASS**

**CROSS-LANGUAGE-001: PASS**

No production runtime change was required for this closure.
