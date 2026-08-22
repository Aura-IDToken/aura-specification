# DQ-003 Audit Surface Integration Decision

**Status:** EXPERIMENTAL / ARCHITECTURAL DECISION  
**Branch:** `dq/dq-003-audit-record-hash-domain`  
**Scope:** Integration of Audit Record Contract v0 with existing certificate, Merkle, and chain mechanisms.  
**Rule:** No RI-PY or RI-RS implementation changes are made by this document.

## 1. Decision

The normative Audit Record Contract becomes the **single semantic authority** for the protocol audit record and its record-level integrity chain.

Existing certificate, Merkle, and chain mechanisms are retained as **derived, supporting, or legacy verification surfaces**. They must not independently redefine the meaning of an Audit Record or introduce a second record hash domain.

The integration model is:

```text
                    Audit Record Contract v0
                              │
              ┌───────────────┼────────────────┐
              │               │                │
              ▼               ▼                ▼
       record canonical   payload hash   audit_record_hash
       representation                     (domain 0x02)
                              │                │
                              └───────┬────────┘
                                      ▼
                             previous_record_hash
                                      │
                                      ▼
                               record chain
                                      │
                 ┌────────────────────┼─────────────────────┐
                 ▼                    ▼                     ▼
             certificate            Merkle             chain verifier
             (derived)              (derived)           (derived)
```

The key architectural constraint is:

> **One normative Audit Record semantics; multiple derived evidence/verification views.**

## 2. Existing mechanisms and their roles

### 2.1 RI-RS `chain.rs`

Current `chain_preimage()`, `compute_chain_hash()`, `recompute_for_entry()`, and `verify_chain()` are an existing chain implementation. Their current pipe-delimited hash preimage is **not** the DQ-003 Audit Record hash domain.

Therefore:

- the existing implementation is preserved as baseline evidence;
- it must not be relabeled as `audit_record_hash`;
- future remediation should make the normative Audit Record hash surface explicit;
- `verify_chain()` may become the implementation of Audit Record chain verification only after its preimage/domain semantics conform to the contract.

### 2.2 RI-PY `AuraEventCertificate`

`AuraEventCertificate.fingerprint()` is retained as a certificate fingerprint mechanism unless and until a separate compatibility decision is made.

It is **not** the Audit Record hash.

The certificate should consume/reference the normative Audit Record evidence rather than independently manufacture a competing record identity. If compatibility requires the historical fingerprint, it must be explicitly named and domain-separated from `audit_record_hash`.

### 2.3 RI-PY `EventTrustCertificate` / Merkle

`EventTrustCertificate` and `MerkleTree` remain proof/aggregation infrastructure.

They should operate over explicitly defined leaf material derived from the normative Audit Record/evidence model. Their Merkle parent hash remains a Merkle-domain operation and must not be treated as `audit_record_hash`.

The Merkle layer therefore provides:

```text
Audit Records
   ↓
explicit leaf material
   ↓
Merkle aggregation
   ↓
proof / root
```

not:

```text
Audit Record
   ↓
Merkle hash
   ↓
audit_record_hash
```

### 2.4 `integrity_hash`

`integrity_hash` remains a separate derived integrity field. It must not become an implicit dependency of `audit_record_hash` unless the normative contract explicitly says so.

For Candidate C / Contract v0, the dependency direction is:

```text
canonical source fields
      ├───────────────┐
      ▼               ▼
 audit_record_hash  integrity_hash
      │
      ▼
 previous_record_hash (for the next record)
```

This avoids circularity and keeps the record hash domain stable.

## 3. Compatibility rule

Existing mechanisms may coexist with the new contract only if each has a distinct semantic name and domain.

Forbidden compatibility shortcuts:

- renaming `chain_hash` to `audit_record_hash` without changing its preimage semantics;
- using a certificate `fingerprint()` as the Audit Record hash;
- using a Merkle leaf/root as the Audit Record hash;
- making `audit_record_hash` depend on `integrity_hash` when the contract excludes that dependency;
- allowing an adapter to synthesize a DQ-003 result from a non-conforming legacy hash.

## 4. Proposed normative layering

### Layer A — Audit Record

Normative protocol object:

```text
ENT-007 Audit Record
```

This layer owns field definitions, canonical inclusion/exclusion, `event_payload_hash`, `audit_record_hash`, `previous_record_hash`, genesis, recomputation, and verification semantics.

### Layer B — Evidence

Derived evidence attached to or associated with the Audit Record. Evidence may include canonical bytes, hashes, signatures, or provenance required by the specification.

### Layer C — Certificate

A certificate is a presentation/attestation object over already-defined protocol evidence. It must not redefine record hashing.

### Layer D — Merkle / aggregation

Merkle structures aggregate explicitly defined leaves or evidence. They provide aggregation/proof semantics, not Audit Record identity semantics.

### Layer E — Implementation chain verifier

RI-PY and RI-RS implementations expose conformance entry points against the normative contract. Existing chain implementations are adapted only after their semantics are mapped and gaps are documented.

## 5. Conformance implications

The first implementation remediation should target a **dedicated Audit Record conformance surface**, not mutate legacy certificate/Merkle semantics merely to make DQ-003 pass.

The adapter/conformance API should conceptually expose:

```text
canonicalize_audit_record(record)
compute_event_payload_hash(payload)
compute_audit_record_hash(record)
recompute_audit_record(record)
verify_audit_record(record)
verify_audit_chain(records)
```

The exact API names are implementation-specific and are not normative until separately specified.

The conformance surface must consume the same fixture and return the exact domain/bytes/hashes required by Contract v0.

## 6. Migration rule

Migration is additive and evidence-preserving:

1. Freeze the current RI-PY / RI-RS baseline.
2. Keep existing certificate/Merkle/chain mechanisms operational where required for compatibility.
3. Introduce the normative Audit Record surface separately.
4. Produce DQ-003 results from the normative surface.
5. Add compatibility projections from Audit Record to legacy certificate/Merkle/chain structures only where required.
6. Deprecate or rename ambiguous legacy hash fields after compatibility evidence exists.

No destructive rewrite of historical evidence is implied by this decision.

## 7. Required follow-up before implementation

Before changing RI-PY or RI-RS, the specification should explicitly settle:

- exact ENT-007 field set;
- canonical inclusion/exclusion list;
- exact `event_payload_hash` input;
- exact `audit_record_hash` preimage;
- whether `integrity_hash` is excluded from the record-hash domain;
- genesis representation;
- exact previous-record dependency;
- Merkle leaf input and domain, if the Merkle layer is retained;
- certificate fingerprint compatibility and naming.

## 8. Decision status

**PROPOSED / EXPERIMENTAL.**

This document resolves the architectural direction for DQ-003 but does not close DQ-003, freeze the Golden Fixture, or authorize implementation remediation by itself.

The governing principle is:

> **Do not make the new contract conform to legacy hashes. Make legacy mechanisms consume or project the one normative Audit Record contract.**