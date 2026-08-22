# DQ-003 Entry-Point Baseline

**Status:** BASELINE — no implementation remediation implied  
**Branch:** `dq/dq-003-audit-record-hash-domain`  
**Purpose:** Record the existing RI-PY and RI-RS cryptographic/audit entry points against the frozen APS-200 / P0-2 contract before any adapter or implementation change.

> This document is a baseline, not a compatibility claim. `chain_hash` is not treated as `audit_record_hash` merely because both use SHA-256.

## 1. Classification

- **EXACT** — existing implementation is the same normative operation and domain required by APS-200/P0-2.
- **ANALOGOUS** — existing implementation serves a related purpose but has a different protocol surface/domain.
- **PARTIAL** — some required semantics exist, but required fields/domain/encoding/verification are incomplete or different.
- **ABSENT** — no corresponding implementation surface was identified.

## 2. Entry-point matrix

| APS-200 requirement | RI-PY symbol/file | RI-RS symbol/file | Exact preimage | Exact encoding | Hash algorithm | Verification semantics | Status |
|---|---|---|---|---|---|---|---|
| Event Payload canonicalization | `compliance/certificate.py::AuraEventCertificate.to_dict/fingerprint` | `conformance/canonical/*`; chain itself uses field-joined preimage | Python hashes serialized certificate, not ENT-007 Event Payload | Python `json.dumps(..., sort_keys=True)`; not established as RFC 8785 JCS | SHA-256 | Certificate fingerprint only | **PARTIAL** / **ANALOGOUS** |
| `event_payload_hash` | No ENT-007 entry point identified | No APS-200 `event_payload_hash` entry point identified | `SHA-256(JCS(event_payload))` required by P0-2 | RFC 8785 JCS + UTF-8 | SHA-256 | Required fixture verification | **ABSENT** |
| Audit Record canonical representation | Certificate serialization is not ENT-007 | `chain_preimage()` constructs a `|`-joined chain string | Rust: `prev_hash|decision|policy_set|policy_hash|context|input_hash|shadow_hash|seq|timestamp` | UTF-8 bytes of joined string | N/A before chain hash | Recomputed from `AuditEntry` | **PARTIAL** |
| `audit_record_hash` | No corresponding function identified | `compute_chain_hash()` | Rust: `SHA-256(chain_preimage)`; differs from frozen P0-2 `SHA-256(0x02 || JCS(R_AR))` | Rust field-joined UTF-8 string, not JCS Audit Record | SHA-256 | Used by Rust chain verification as `chain_hash` | **ANALOGOUS**, not EXACT |
| `integrity_hash` | No corresponding function identified | No corresponding function identified | P0-2 requires `SHA-256(JCS(R_I))` | RFC 8785 JCS + UTF-8 | SHA-256 | Required fixture verification | **ABSENT** |
| `previous_record_hash` | No ENT-007 field identified | `AuditEntry.prev_hash` | Rust links predecessor `chain_hash` | 64-char lowercase hex digest in current chain surface | N/A | `verify_chain()` checks linkage | **PARTIAL** — linkage exists, semantic target is not yet proven equivalent to APS-200 `audit_record_hash` |
| Genesis | Certificate/Merkle surfaces exist, but no ENT-007 genesis field semantics identified | `crypto::genesis_hash()` / `verify_chain()` | Rust genesis is fixed chain anchor | Current Rust chain encoding | SHA-256-derived fixed value | `verify_chain()` checks first `prev_hash` | **ANALOGOUS** |
| Re-computation | `AuraEventCertificate::fingerprint()` recomputes certificate fingerprint | `recompute_for_entry()` | Python certificate serialization vs Rust chain preimage | Python sorted JSON vs Rust joined fields | SHA-256 | Rust recomputes expected chain hash | **PARTIAL** |
| Chain verification | `audit/verify.py` / Merkle verification | `verify_chain()` | Python verifies Merkle proof; Rust recomputes sequential chain | Different audit domains | SHA-256 | Different verification model | **ANALOGOUS** |
| Tamper detection | Merkle proof / certificate audit | `verify_chain()` detects genesis/linkage/hash changes | Different evidence domains | Different encodings | SHA-256 | Different invariants | **ANALOGOUS** |

## 3. RI-PY baseline

### `compliance/certificate.py`

The identified certificate surface is `AuraEventCertificate`. Its `fingerprint()` serializes `to_dict()` using Python JSON with `sort_keys=True` and hashes the UTF-8 representation with SHA-256. The represented object contains certificate fields such as `schema_version`, `agent_id`, `timestamp`, `ari`, and an `audit` object containing `leaf_hash` and `merkle_root`.

This is **not** the frozen ENT-007 Audit Record domain and is therefore not accepted as an `audit_record_hash` implementation.

### `audit/merkle.py`

The identified audit surface provides SHA-256 leaves, Merkle-tree construction, proof generation/verification, and an event trust certificate. Its signing payload is a separate deterministic JSON structure containing `event_hash`, `merkle_root`, and `timestamp`.

This is an **ANALOGOUS** audit/evidence mechanism, not an ENT-007 sequential Audit Record chain.

### `audit/verify.py`

Provides verification wrappers for the Merkle/audit surface. No `previous_record_hash` / `audit_record_hash` / `integrity_hash` conformance entry point was identified.

### `core/`

The core evaluator is the measurement/ARI surface. It is not the ENT-007 audit-record hashing surface.

## 4. RI-RS baseline

### `src/chain.rs`

The current Rust chain implementation exposes:

- `chain_preimage()` — builds the current chain preimage from the nine chain fields.
- `compute_chain_hash()` — hashes that preimage with SHA-256.
- `recompute_for_entry()` — derives the expected chain hash from an `AuditEntry`.
- `verify_chain()` — verifies genesis, predecessor linkage, and recomputed chain hashes.

These functions provide a strong existing **chain conformance surface**, but the current chain domain is not automatically equivalent to APS-200/P0-2 `audit_record_hash`.

The current Rust preimage is a pipe-delimited UTF-8 string of chain fields, whereas frozen P0-2 requires:

```text
0x02 || JCS(R_AR)
        ↓
      SHA-256
        ↓
 audit_record_hash
```

Therefore `compute_chain_hash()` is classified **ANALOGOUS**, not **EXACT**, until a DQ-003 execution proves otherwise.

## 5. Frozen DQ-003 comparison target

The Golden Fixture is the source of truth. Implementations MUST be evaluated against it; the fixture MUST NOT be modified to accommodate an implementation.

Required comparison layers:

1. Event Payload bytes.
2. RFC 8785 JCS Event Payload bytes.
3. `event_payload_hash`.
4. ENT-007 Audit Record object.
5. `0x02 || JCS(R_AR)` preimage.
6. `audit_record_hash`.
7. Integrity object/preimage.
8. `integrity_hash`.
9. `previous_record_hash` linkage.
10. Verification result and rejection semantics.

## 6. Current DQ-003 conclusion

The baseline establishes a real architectural gap rather than a mere adapter naming problem:

```text
RI-PY
  certificate + Merkle audit
          ≠ ENT-007 Audit Record Chain

RI-RS
  sequential Audit Chain
          ≠ frozen P0-2 Audit Record hash domain
```

Accordingly, no implementation remediation is authorized by this baseline. The next DQ-003 action is a **read-only execution attempt** against the frozen Golden Fixture wherever an existing entry point can be invoked without semantic adaptation. Any missing surface is recorded as a gap rather than synthesized by an adapter.

## 7. Decision vocabulary

`EXACT` / `ANALOGOUS` / `PARTIAL` / `ABSENT` are evidence classifications only. They do not imply pass/fail by themselves. DQ-003 conformance is decided only after fixture execution and byte/hash comparison.
