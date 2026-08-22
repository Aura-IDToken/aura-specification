# DQ-003 RI-PY / RI-RS Baseline Conformance Gap Report

**Status:** EXPERIMENTAL / BASELINE ONLY  
**Branch:** `dq/dq-003-audit-record-hash-domain`  
**Contract:** Audit Record Contract v0  
**Fixture:** `DQ-003-AUDIT-CHAIN-001`  
**Purpose:** Record the pre-remediation implementation baseline. This document does not modify RI-PY or RI-RS and does not declare DQ-003 pass/fail.

## 1. Scope

This report records the observed conformance surface before any implementation remediation. The intended chain is:

```text
Contract
  ↓
Fixture
  ↓
RI-PY baseline
  ↓
RI-RS baseline
  ↓
documented gaps
  ↓
implementation remediation
```

The adapters must not introduce or reinterpret Audit Record semantics. A conformance adapter may only expose an existing implementation surface to the DQ-003 fixture.

## 2. DQ-003 reference contract

The experimental Contract v0 requires:

- Audit Record ENT-007 field set.
- Canonical representation by JCS.
- `event_payload_hash = SHA-256(JCS(payload))`.
- `audit_record_hash = SHA-256(0x02 || JCS(record_without_integrity_hash_and_audit_record_hash))`.
- `previous_record_hash` points to the predecessor `audit_record_hash`.
- Genesis sentinel is 32 zero bytes.
- Independent recomputation and verification of the Audit Record hash.
- Chain verification across records.
- Domain separation from the existing Merkle domains.

The fixture `DQ-003-AUDIT-CHAIN-001` is experimental and is not yet frozen as a Golden Fixture.

## 3. RI-RS baseline

### Located surface

`aura-guard-v1.3/src/chain.rs` contains the current chain implementation:

```text
chain_preimage()
compute_chain_hash()
recompute_for_entry()
verify_chain()
```

This is a genuine implementation surface and is suitable for a future adapter without changing `main`.

### Current semantics

The current chain preimage is constructed from AuditEntry fields using a pipe-delimited representation and is then hashed with SHA-256. `recompute_for_entry()` reconstructs the current `chain_hash`; `verify_chain()` validates the stored chain hash and predecessor linkage.

This differs from DQ-003 Contract v0, which requires:

```text
SHA-256(0x02 || JCS(AuditRecord_without_derived_hashes))
```

Therefore the current Rust `chain_hash` must **not** be relabeled as `audit_record_hash` by an adapter.

### RI-RS baseline matrix

| Surface | Baseline |
|---|---|
| Chain preimage | FOUND |
| Chain hash computation | FOUND |
| Recompute | FOUND |
| Chain verification | FOUND |
| DQ-003 JCS Audit Record serialization | NOT FOUND in current chain surface |
| `0x02` Audit Record domain | NOT FOUND in current chain surface |
| DQ-003 `audit_record_hash` | NOT IMPLEMENTED |
| DQ-003 genesis sentinel | NOT VERIFIED as the DQ-003 sentinel |
| DQ-003 event payload hash | NOT VERIFIED |

## 4. RI-PY v3.3 baseline

The `aura-poc-a-core-v3.3` source contains existing certificate and Merkle-related components, but none is an existing DQ-003 Audit Record implementation.

### 4.1 `compliance/certificate.py`

The repository contains `AuraEventCertificate` with `to_dict()` and `fingerprint()`.

Its fingerprint path is conceptually:

```text
AuraEventCertificate
  ↓
to_dict()
  ↓
JSON sort_keys=True
  ↓
UTF-8
  ↓
SHA-256
```

This is not DQ-003 `audit_record_hash`: its certificate object and serialization surface do not expose the ENT-007 Audit Record field set or the required `0x02 || JCS(...)` domain.

### 4.2 `audit/merkle.py`

The repository contains `EventTrustCertificate`, `MerkleTree`, and proof/verification support.

Its existing hash surface uses event hashing and Merkle parent hashing rather than the DQ-003 Audit Record hash domain. Its signature/certificate serialization is also a separate JSON surface.

This is usable as historical audit/Merkle infrastructure but is not a drop-in DQ-003 Audit Record implementation.

### 4.3 `core/merkle.py`

A second Merkle-related surface exists through `MerkleAttestor`. It also hashes JSON-derived data and is not an implementation of the ENT-007 Audit Record Contract v0.

### 4.4 Evaluator path

The RI-PY evaluator path is a mathematical PoCA/ARI evaluation surface. It does not constitute an Audit Record hashing or chain-verification entry point.

### RI-PY baseline matrix

| Surface | Baseline |
|---|---|
| Certificate object | FOUND (`AuraEventCertificate`) |
| Certificate fingerprint | FOUND |
| EventTrustCertificate | FOUND |
| Merkle construction | FOUND |
| Merkle verification | FOUND |
| ENT-007 Audit Record object | NOT FOUND |
| DQ-003 JCS Audit Record serialization | NOT FOUND |
| `0x02` Audit Record domain | NOT FOUND |
| DQ-003 `audit_record_hash` | NOT IMPLEMENTED |
| DQ-003 `previous_record_hash` chain | NOT FOUND as the required semantic surface |
| DQ-003 genesis sentinel | NOT VERIFIED |
| DQ-003 `event_payload_hash` | NOT VERIFIED |
| DQ-003 Audit Record recomputation | NOT FOUND |
| DQ-003 Audit Record chain verification | NOT FOUND |

## 5. Cross-language baseline

| Conformance surface | DQ-003 | RI-PY v3.3 | RI-RS current |
|---|---|---|---|
| ENT-007 field set | REQUIRED | GAP | GAP |
| JCS canonical Audit Record | REQUIRED | GAP | GAP |
| `event_payload_hash` | REQUIRED | GAP | GAP |
| `audit_record_hash` | REQUIRED | GAP | GAP |
| `0x02` domain | REQUIRED | GAP | GAP |
| `previous_record_hash = H_A(prev)` | REQUIRED | GAP | GAP |
| Genesis sentinel | REQUIRED | GAP | NOT VERIFIED |
| Recompute | REQUIRED | GAP | FOUND, different semantics |
| Verify chain | REQUIRED | GAP | FOUND, different semantics |

## 6. Conformance interpretation

The baseline does **not** mean either implementation is defective. It establishes that the current implementations predate or use different audit/hash semantics from Candidate C.

The critical finding is:

> Neither RI-PY v3.3 nor the current RI-RS chain implementation exposes an existing implementation surface that can be mapped to DQ-003 `audit_record_hash` without introducing new semantics.

Therefore an adapter that merely transforms an old hash into the DQ-003 field name would be invalid for conformance purposes.

## 7. Decision / next gate

**DQ-003 remains OPEN.**

No RI-PY or RI-RS implementation files are modified by this baseline report.

Before implementation remediation:

1. Preserve `DQ-003-AUDIT-CHAIN-001` unchanged.
2. Preserve this baseline report as the pre-remediation evidence.
3. Decide the normative relationship between the existing chain/certificate mechanisms and the new Audit Record Contract.
4. Only then implement a dedicated DQ-003 conformance surface if required.
5. Re-run RI-PY and RI-RS against the unchanged fixture.
6. Freeze the fixture as Golden only after cross-language, replay, tamper, and domain-separation checks pass.

**Conclusion:** baseline established; implementation remediation intentionally deferred.