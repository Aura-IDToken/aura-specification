# DQ-006 — Canonical Serialization / Cross-Language Conformance

## 1. Decision identity

- **Decision:** DQ-006 — Canonical Serialization / Cross-Language Conformance
- **Workstream:** CK-003 Remediation
- **Gate:** CROSS-LANGUAGE-001 ARTIFACT BRIDGE
- **Decision status:** **CLOSED**
- **Closure package:** `ck003/dq-006-closure`

## 2. Closure statement

DQ-006 concerns the canonical serialization boundary and cross-language conformance.

The verified protocol contract is:

```text
Object
  ↓
RFC 8785 JCS
  ↓
canonical UTF-8 bytes
  ↓
SHA-256
  ↓
RFC-6962 leaf domain 0x00
```

The contract is independently implemented by RI-PY and RI-RS and was demonstrated equal by CROSS-LANGUAGE-001 using independently generated implementation artifacts.

DQ-006 is closed on the basis of the executed evidence recorded in this package: canonical byte equality, SHA-256 equality, RFC-6962 leaf equality, independent recomputation, negative controls, and production-integrity checks.

This closure establishes the verified canonical serialization/hash-input boundary. It does not imply closure of DQ-002, APS-001, or unrelated protocol invariants.

## 3. Normative contract

### 3.1 Canonical serialization

The normative serialization profile is **RFC 8785 JSON Canonicalization Scheme (JCS)**.

The following are conformance implementation dependencies, not the protocol semantic definition:

- RI-PY: `rfc8785==0.1.4`
- RI-RS: `serde_json_canonicalizer==0.3.2`

Neither implementation version defines or replaces the RFC 8785 protocol requirement.

### 3.2 Digest domain

For canonical byte sequence `B`:

`digest(B) = SHA-256(B)`

### 3.3 Merkle leaf domain

For canonical byte sequence `B`:

`leaf(B) = SHA-256(0x00 || B)`

where `0x00` is one raw octet.

The interior Merkle-node domain remains governed by the existing Merkle specification. DQ-006 does not redefine the complete Merkle architecture.

### 3.4 Version semantics

DQ-006 does not create or modify versioning rules. The existing specification semantics for `protocol_version` and `schema_version` remain authoritative.

CANONICAL-001 contains both fields as evidence at the canonical serialization boundary.

## 4. CANONICAL-001 — normative fixture record

**Fixture:** `CANONICAL-001`

**Canonicalization profile:** RFC 8785 JCS

**Input object:**

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

**Canonical byte length:** `100`

**Canonical bytes (hex):**

```text
7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d
```

**SHA-256:**

```text
b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
```

**Leaf domain:** `0x00`

**RFC-6962 leaf:**

```text
ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

CANONICAL-001 is evidence of the canonical serialization boundary. It is not, by itself, a claim of complete RFC 8785 behavioral coverage. The broader JCS-B01…B06 conformance tests provide the broader behavioral coverage.

## 5. Evidence provenance

### 5.1 RI-PY

Repository: `Aura-IDToken/aura-poc-a-core-v3.3`

Execution/source commit:
`49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f`

Evidence/artifact commit:
`3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e`

Engine: `rfc8785==0.1.4`

Artifact:
`conformance/corpus/canonical-001/ri-py.json`

### 5.2 RI-RS

Repository: `Aura-IDToken/aura-guard-v1.3`

Execution/source commit:
`4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2`

Evidence/artifact commit:
`420653e232cb0ff1e365edd2e4a5eb294d2bb2a0`

Engine: `serde_json_canonicalizer==0.3.2`

Artifact:
`conformance/corpus/canonical-001/ri-rs.json`

The two implementation evidence commits are the execution evidence cited by CROSS-LANGUAGE-001. They are not replaced by reconstructed values in this specification record.

## 6. CROSS-LANGUAGE-001 — Artifact Bridge

CROSS-LANGUAGE-001 is based on independently generated RI-PY and RI-RS artifacts, not merely equality against a frozen expected digest.

| Check | Result |
|---|---|
| RI-PY actual execution | PASS |
| RI-RS actual execution | PASS |
| canonical bytes equality | PASS |
| SHA equality | PASS |
| leaf equality | PASS |
| independent recomputation | PASS |
| modified canonical bytes negative control | PASS |
| modified SHA-256 negative control | PASS |
| incorrect leaf domain negative control | PASS |
| RI-PY production integrity | PASS |
| RI-RS production integrity | PASS |

The detailed execution ledger is `ck003/dq-006-closure/CROSS-LANGUAGE-001-EVIDENCE.md`.

## 7. Evidence matrix

| ID | Requirement | Evidence | RI-PY | RI-RS | Cross-language | Result |
|---|---|---|---|---|---|---|
| DQ-006-01 | Canonical serialization profile | CANONICAL-001; RFC 8785 JCS; `canonical-001-evidence-manifest.json` | `rfc8785==0.1.4` | `serde_json_canonicalizer==0.3.2` | PASS | PASS |
| DQ-006-02 | Canonical byte determinism | CANONICAL-001 actual artifacts | PASS | PASS | byte equality PASS | PASS |
| DQ-006-03 | SHA-256 domain | `SHA-256(canonical_bytes)`; independent recomputation in CROSS-LANGUAGE-001 | PASS | PASS | SHA equality PASS | PASS |
| DQ-006-04 | RFC-6962 leaf domain | `SHA-256(0x00 || canonical_bytes)`; independent leaf recomputation | PASS | PASS | leaf equality PASS | PASS |
| DQ-006-05 | RI-PY implementation | RI-PY execution/evidence commits above | PASS | N/A | artifact accepted | PASS |
| DQ-006-06 | RI-RS implementation | RI-RS execution/evidence commits above | N/A | PASS | artifact accepted | PASS |
| DQ-006-07 | Cross-language equality | CROSS-LANGUAGE-001 execution ledger | PASS | PASS | bytes/SHA/leaf equality PASS | PASS |
| DQ-006-08 | Negative controls | Modified bytes, modified SHA, incorrect leaf domain rejected | PASS | PASS | all three gate failures asserted | PASS |
| DQ-006-09 | Production isolation | Production-integrity checks recorded in CROSS-LANGUAGE-001 | core/audit unchanged | src/Cargo unchanged | no production modification | PASS |

The matrix is a traceability summary of existing evidence; it does not create new execution evidence.

## 8. Negative controls

The bridge correctly rejected the following controlled mutations:

1. modified canonical bytes;
2. modified SHA-256 metadata;
3. incorrect leaf domain (`0x01` instead of `0x00`).

All three controls produced gate failure as expected. Mutated artifacts are not part of the committed specification corpus.

## 9. Production boundary

No production runtime modification was required to establish DQ-006.

Recorded production-integrity results:

- RI-PY `core/` unchanged;
- RI-PY `audit/` unchanged;
- RI-RS `src/` unchanged;
- RI-RS production `Cargo.toml` unchanged;
- RI-RS production `Cargo.lock` unchanged.

JCS implementation dependencies remain conformance-layer infrastructure.

This closure does **not** authorize production runtime canonicalization. Any future runtime integration requires a separate architectural decision.

## 10. Traceability

```text
DQ-006
  ↓
CANONICAL-001
  ↓
RI-PY ───────────────┐
                     ├── CROSS-LANGUAGE-001
RI-RS ───────────────┘
  ↓
byte / SHA / leaf equality
  ↓
evidence artifacts
  ↓
DQ-006 CLOSED
```

Relevant invariant linkage is limited to traceability; no invariant status is changed by this package:

- INV-003 — Canonical Serialization
- INV-005 — Evidence Traceability
- INV-011 — Cryptographic Integrity
- INV-014 — Reference Compatibility

The invariant registry remains authoritative for invariant definitions and statuses. DQ-006 does not mark any of these invariants CLOSED.

## 11. Scope discipline

This closure does **not**:

- close DQ-002;
- close APS-001;
- close INV-001…INV-015;
- establish complete APS-500 fixture corpus conformance;
- establish CI or release gates;
- authorize a production JCS dependency;
- redefine version semantics;
- redefine the complete Merkle architecture;
- constitute `aura-specification v1.0` release approval.

## 12. Closure authority

**Architectural verdict: PASS.**

**DQ-006: CLOSED.**

This record is a specification/evidence consolidation artifact. It does not alter the canonical serialization values, implementation behavior, or production runtime.
