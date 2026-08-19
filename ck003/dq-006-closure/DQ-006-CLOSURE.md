# DQ-006 Closure Record

## 1. Decision identity

- **Decision:** DQ-006 — JCS / canonical serialization cross-language conformance
- **Workstream:** CK-003 Remediation
- **Gate:** CROSS-LANGUAGE-001 ARTIFACT BRIDGE
- **Decision status:** **PASS / CLOSED**
- **Closure package:** `ck003/dq-006-closure`

## 2. Closure statement

DQ-006 is closed because the Aura reference implementations RI-PY and RI-RS have independently executed the frozen CANONICAL-001 fixture and produced byte-identical canonical serialization, identical SHA-256 digests, and identical RFC 6962 leaf digests. The equality gate independently re-verifies each artifact and rejects controlled mutations.

This closure establishes implementation conformance for the tested canonicalization/hash boundary. It does not imply that the entire Aura Protocol specification, all invariants, or DQ-002 are closed.

## 3. Normative contract closed by this decision

### Canonical serialization

The canonical serialization profile is **RFC 8785 JSON Canonicalization Scheme (JCS)**.

Conformance engines:

- RI-PY: `rfc8785==0.1.4`
- RI-RS: `serde_json_canonicalizer==0.3.2`

These dependencies are conformance-scoped. This decision does not require either dependency to enter production runtime.

### Digest domain

For a canonical byte sequence `B`:

`digest(B) = SHA-256(B)`

### Merkle leaf domain

For a canonical byte sequence `B`:

`leaf(B) = SHA-256(0x00 || B)`

where `0x00` is one raw octet, not an ASCII representation.

### CANONICAL-001 fixture

Input object:

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

Observed canonical byte length: `100`.

Observed canonical bytes:

```text
7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d
```

SHA-256:

```text
b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
```

RFC 6962 leaf SHA-256:

```text
ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

## 4. Evidence provenance

### RI-PY

Repository: `Aura-IDToken/aura-poc-a-core-v3.3`

Execution/source commit:
`49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f`

Evidence/artifact commit:
`3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e`

Engine: `rfc8785==0.1.4`

The evidence commit records the actual CANONICAL-001 execution, generated artifacts, equality result, negative controls and production-integrity checks. The commit is GitHub-verified.

### RI-RS

Repository: `Aura-IDToken/aura-guard-v1.3`

Execution/source commit:
`4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2`

Evidence/artifact commit:
`420653e232cb0ff1e365edd2e4a5eb294d2bb2a0`

Engine: `serde_json_canonicalizer==0.3.2`

The evidence commit records independent Rust execution and the generated RI-RS artifact. The commit is GitHub-verified.

## 5. CROSS-LANGUAGE-001 verdict

| Check | Result |
|---|---|
| RI-PY actual execution | PASS |
| RI-RS actual execution | PASS |
| RI-PY artifact provenance | PASS |
| RI-RS artifact provenance | PASS |
| canonical bytes equality | PASS |
| RI-PY SHA independent verification | PASS |
| RI-RS SHA independent verification | PASS |
| SHA equality | PASS |
| RI-PY leaf independent verification | PASS |
| RI-RS leaf independent verification | PASS |
| leaf equality | PASS |
| frozen expected cross-check | PASS |
| modified-bytes negative control | PASS |
| modified-SHA negative control | PASS |
| wrong-leaf-domain negative control | PASS |
| RI-PY production integrity | PASS |
| RI-RS production integrity | PASS |
| cross-language equality runner | PASS |

## 6. Negative-control significance

The equality runner was demonstrated to reject:

1. modified canonical bytes;
2. modified SHA-256 metadata;
3. a wrong leaf domain (`0x01` instead of `0x00`) through independent leaf recomputation.

The third control is intentionally not reduced to leaf-to-leaf equality: independently recomputing the leaf domain is required to detect a consistent but wrong mutation on both sides.

## 7. Production boundary

No production Core or Guard hashing/Merkle implementation was changed by the CROSS-LANGUAGE-001 work.

Specifically, the reported checks showed:

- RI-PY `core/` unchanged;
- RI-PY `audit/` unchanged;
- RI-RS `src/` unchanged;
- RI-RS production `Cargo.toml` unchanged;
- RI-RS production `Cargo.lock` unchanged.

JCS engines remain conformance-only.

## 8. Accepted deviations

### Branch naming

The execution branches were session-designated Claude branches rather than `ck003/cross-language-canonical-001`. This is accepted as an execution-environment deviation and has no protocol-semantic impact.

### Evidence artifact commit identity

Execution artifacts identify the clean source commit that produced them; the artifact publication commit is separate. This avoids self-referential commit identity.

### Corpus transport

The RI-RS artifact was generated in `aura-guard-v1.3` and transported byte-identically into the RI-PY corpus used by the equality runner. The artifact was not reconstructed or re-keyed. The source artifact digest was preserved.

## 9. Consequences

The following may now be treated as evidence-backed decisions for subsequent conformance work:

- RFC 8785 JCS is the canonical serialization profile under test.
- canonical bytes, rather than semantic JSON equivalence, are the equality boundary;
- SHA-256 is applied to the canonical byte sequence;
- RFC 6962 leaf domain `0x00` is applied to raw canonical bytes;
- cross-language equality must be evaluated on independently produced artifacts;
- conformance evidence is separate from production runtime changes.

## 10. Non-consequences

This closure does **not** by itself:

- close DQ-002;
- close APS-001;
- establish full INV-001…INV-015 conformance;
- establish full APS-500 fixture corpus conformance;
- establish CI/release gates;
- authorize a production JCS dependency;
- constitute `aura-specification v1.0` release approval.

## 11. Traceability

```text
APS-200 canonical data model
        ↓
RFC 8785 JCS boundary
        ↓
CANONICAL-001
        ↓
RI-PY actual execution ─────┐
                            ├── CROSS-LANGUAGE-001
RI-RS actual execution ─────┘
        ↓
byte / SHA / leaf equality
        ↓
DQ-006 CLOSED
```

APS-300 requires Evidence to be immutable, deterministic, traceable and independently verifiable, and its traceability model connects APS requirement → invariant → evaluation → evidence → conformance test → release. This closure package is structured to preserve that chain.

## 12. Closure authority

**Architectural verdict: PASS.**

**DQ-006: CLOSED.**

The next gate is DQ-002 final closure, subject to its own evidence and decision record.
