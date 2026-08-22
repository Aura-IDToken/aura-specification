# DQ-003 — Audit Record Hash Domain Contract (Experimental)

**Status:** EXPERIMENTAL — not normative

## Purpose

Define the protocol-level surface that an implementation must expose before Candidate C can be tested cross-language.

This document does **not** amend APS-200. It is an isolated DQ-003 experiment.

## 1. Audit Record

An Audit Record is the protocol object whose canonical representation is hashed for audit-chain linkage.

The exact field set MUST be taken from the normative Audit Record schema once approved. An implementation MUST NOT add implementation-specific fields to the conformance preimage.

## 2. Canonical representation

The Audit Record MUST first be transformed into the protocol's canonical byte representation.

For DQ-003, the canonicalization function is treated as an input contract inherited from P0-1. DQ-003 MUST NOT redefine canonicalization.

Let:

```text
C(R) = canonical UTF-8 bytes of Audit Record R
```

The canonical bytes MUST be deterministic: identical protocol records produce identical bytes across conforming implementations.

## 3. audit_record_hash

Candidate C proposes a dedicated audit-record hash domain:

```text
H_A(R) = SHA-256( 0x02 || C(R_without_audit_record_hash) )
```

The domain byte `0x02` is experimental and MUST NOT be treated as normative until DQ-003 closes.

The field being derived MUST NOT be included in its own preimage.

## 4. previous_record_hash

For records after the first record in an audit chain:

```text
R[n].previous_record_hash = H_A(R[n-1])
```

The first record uses the protocol-defined genesis/null value. DQ-003 does not redefine the genesis convention.

## 5. Recomputation

A verifier MUST recompute `H_A(R)` from the supplied Audit Record and canonicalization rules. A stored `audit_record_hash` MUST be treated as a value to compare, not as the source of truth.

```text
expected = H_A(R)
PASS iff expected == supplied.audit_record_hash
```

## 6. Chain verification

For a sequence `R[1..n]`, verification MUST establish:

```text
verify(R[1])
verify(R[2]) && R[2].previous_record_hash == H_A(R[1])
...
verify(R[n]) && R[n].previous_record_hash == H_A(R[n-1])
```

Any record mutation that changes its canonical bytes MUST invalidate its own derived hash and, where applicable, the linkage from the following record.

## 7. Domain separation

`audit_record_hash` MUST remain a distinct cryptographic domain from evidence hashes and Merkle leaf/node hashes. DQ-003 will require explicit test evidence that the domains are not silently interchangeable.

## 8. Cross-language conformance surface

Both RI-PY and RI-RS MUST expose equivalent observable operations for the DQ-003 fixture:

```text
canonical_bytes(record)
audit_record_hash(record)
recompute(record)
verify_chain(records)
```

The implementations MAY have different internal APIs and data models. Conformance is established by identical protocol-level outputs, not by runtime coupling.

## 9. Required DQ-003 evidence

The candidate cannot close until all of the following have independently passed:

- canonical bytes equality
- audit-record hash equality
- previous-record linkage
- recomputation
- tamper detection
- domain separation
- Merkle/evidence separation
- RI-PY ↔ RI-RS replay

## Decision rule

If either implementation requires an adapter to invent Audit Record semantics rather than map an already-defined protocol object, DQ-003 remains **BLOCKED** and the specification must be completed before implementation work proceeds.
