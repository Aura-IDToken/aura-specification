# DQ-003 — Audit Record Hash Domain

**Status:** EXPERIMENTAL / NOT NORMATIVE  
**Branch:** `dq/dq-003-audit-record-hash-domain`  
**Purpose:** resolve the hash domain of APS-200 `ENT-007.previous_record_hash` without modifying `main`.

## Scope

This experiment evaluates candidate C: a dedicated Audit Record hash domain.

Candidate C is **not yet a normative Aura requirement**. The experiment MUST NOT update APS-200, close DQ-003, or freeze Golden Fixtures as normative evidence.

## Candidate C

For an Audit Record `R`, define the experimental function:

```text
canonical_record_bytes(R)
    = RFC 8785 JCS UTF-8 bytes of R with `integrity_hash` excluded

H_A(R)
    = SHA-256(0x02 || canonical_record_bytes(R))
```

The experimental chain rule is:

```text
R[n].previous_record_hash = H_A(R[n-1])
```

`0x02` is an **experimental domain-separation octet only**. It has no normative status until DQ-003 is accepted.

## Why candidate C is being tested

APS-200 defines `integrity_hash` as `SHA-256(canonical_bytes)` excluding `integrity_hash` itself, while `ENT-007.previous_record_hash` is currently described only as the hash of the previous Audit Record. The specification does not presently provide the exact hash equation for that field.

APS-300 separately defines the Evidence chain as `previous_evidence_hash = evidence_hash(previous Evidence)`. The Evidence chain MUST NOT be silently reused as the Audit Record chain.

Candidate C therefore tests whether the Audit Record chain can have an explicit, independently domain-separated cryptographic identity.

## Required tests

### C-01 — deterministic construction

For the same frozen Audit Record, RI-PY and RI-RS MUST produce byte-identical canonical bytes and identical `H_A`.

### C-02 — chain linkage

For `R1 -> R2 -> R3`:

```text
R2.previous_record_hash == H_A(R1)
R3.previous_record_hash == H_A(R2)
```

### C-03 — tamper cascade

Changing any covered field in `R2` MUST invalidate `R2`'s computed hash and MUST invalidate the stored `R3.previous_record_hash` linkage.

### C-04 — integrity-domain separation

For the same record:

```text
integrity_hash(R) != H_A(R)
```

must hold for the test vector. The two functions MUST use distinct domains, not merely different field names.

### C-05 — Evidence-domain separation

The Audit Record chain MUST NOT validate an Evidence-chain link and vice versa.

### C-06 — Merkle separation

The Audit Record hash MUST NOT be treated as a Merkle leaf. Merkle leaf construction remains independently governed by APS-300.

### C-07 — cross-language replay

The verifier MUST independently recompute `H_A` from canonical bytes. Stored `previous_record_hash` and stored digest values are comparison targets, not trust anchors.

## PASS rule

DQ-003 Candidate C is eligible for normative consideration only if C-01 through C-07 pass in both RI-PY and RI-RS, with independently produced artifacts and reproducible provenance.

A PASS here does **not** itself change APS-200. Normative acceptance requires a separate specification update and review.

## Evidence outputs

The execution harness MUST produce, for each implementation:

- fixture input SHA-256;
- canonical bytes as hex and length;
- `integrity_hash` recomputation;
- experimental `audit_record_hash` recomputation;
- chain-link checks;
- tamper-control result;
- implementation identity/version;
- repository and source commit;
- toolchain/platform;
- clean-worktree state.

The cross-language gate MUST independently recompute the cryptographic values rather than trusting values emitted by either implementation.
