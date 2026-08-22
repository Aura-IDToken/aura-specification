# DQ-003 — Audit Record Contract v0 / Hash Domain Contract (Experimental)

**Status:** EXPERIMENTAL — not normative

## Purpose

Define the minimum protocol-level Audit Record contract required before Candidate C can be implemented and tested cross-language.

This document does **not** amend APS-200. It is an isolated DQ-003 experiment. Any rule that differs from or extends APS-200 remains provisional until DQ-003 closes and the corresponding normative specification change is approved.

## 1. Audit Record — exact field set

For DQ-003 Contract v0, an Audit Record `R` consists exactly of:

### Common Object Contract fields inherited from APS-200 ENT-007

- `object_id`
- `object_type`
- `protocol_version`
- `schema_version`
- `created_at`
- `integrity_hash`

### ENT-007 audit fields

- `event_type`
- `sequence_number`
- `previous_record_hash`
- `event_payload_hash`
- `audit_record_hash`

No implementation-specific fields MAY participate in the DQ-003 conformance preimage.

`audit_record_hash` is a **derived DQ-003 field** and is not currently normative in APS-200.

## 2. Canonical representation

The Audit Record MUST first be transformed into the protocol canonical byte representation inherited from P0-1 / APS-200 §8.

Let:

```text
C(R) = RFC 8785 JCS canonical UTF-8 bytes of Audit Record R
```

For purposes of computing `audit_record_hash`, both derived digest fields are excluded from the preimage:

```text
R_A = R without:
      - integrity_hash
      - audit_record_hash
```

Therefore:

```text
C_A(R) = JCS(R_A)
```

This explicit exclusion prevents a circular dependency between the APS-200 `integrity_hash` and the DQ-003 `audit_record_hash`.

The canonical bytes MUST be deterministic: identical protocol records produce identical bytes across conforming implementations.

## 3. audit_record_hash

Candidate C defines a dedicated audit-record hash domain:

```text
H_A(R) = SHA-256( 0x02 || C_A(R) )
```

where `0x02` is one raw octet and MUST NOT be represented as ASCII text or a hexadecimal string in the preimage.

The `0x02` domain byte is experimental and MUST NOT be treated as normative until DQ-003 closes.

The derived `audit_record_hash` MUST NOT be included in its own preimage.

The inherited `integrity_hash` MUST also be excluded from the `audit_record_hash` preimage; its own APS-200 self-exclusion rule is insufficient to avoid a cross-digest dependency.

## 4. previous_record_hash

For records after the first record in an audit chain:

```text
R[n].previous_record_hash = H_A(R[n-1])
```

The first record is the chain genesis record and MUST use the DQ-003 Contract v0 genesis sentinel:

```text
previous_record_hash = 0000000000000000000000000000000000000000000000000000000000000000
```

This 32-byte zero value is **experimental** and becomes normative only if DQ-003 closes with Candidate C accepted.

A chain MUST NOT silently mix genesis conventions.

## 5. event_payload_hash

`event_payload_hash` commits to the event payload independently from the Audit Record chain hash.

For a payload object `P`:

```text
C_P(P) = JCS(P)
H_P(P) = SHA-256(C_P(P))
```

and:

```text
R.event_payload_hash = H_P(P)
```

The payload hash domain is therefore distinct from `audit_record_hash`:

```text
event_payload_hash = SHA-256(JCS(payload))
audit_record_hash   = SHA-256(0x02 || JCS(record_without_digest_fields))
```

The payload itself is not implicitly inserted into the Audit Record hash preimage unless the normative Audit Record schema explicitly includes it as a field. DQ-003 Contract v0 uses the hash-only reference already present in APS-200 ENT-007.

## 6. integrity_hash interaction

APS-200 already defines:

```text
integrity_hash = SHA-256(JCS(object_without_integrity_hash))
```

DQ-003 does not redefine `integrity_hash`.

For Contract v0, `integrity_hash` and `audit_record_hash` are separate derived values over separate declared domains:

```text
integrity_hash     = SHA-256(JCS(R_without_integrity_hash))
audit_record_hash  = SHA-256(0x02 || JCS(R_without_integrity_hash, audit_record_hash))
```

The second expression is shorthand for the explicit exclusion rule in §2: `audit_record_hash` is excluded, and `integrity_hash` is also excluded.

The two digests MUST NOT be treated as interchangeable.

## 7. Recomputation

A verifier MUST recompute `audit_record_hash` from the supplied Audit Record, excluding both derived digest fields as defined in §2.

The stored value is evidence to compare, not the source of truth.

```text
expected = H_A(R)
PASS iff expected == R.audit_record_hash
```

The verifier MUST also independently validate `integrity_hash` according to APS-200.

A DQ-003 implementation MUST be able to report these checks independently so that a passing integrity check cannot mask a failing audit-record hash check, or vice versa.

## 8. Chain verification

For a sequence `R[1..n]`, verification MUST establish:

```text
verify_record(R[1])
AND R[1].previous_record_hash == GENESIS

verify_record(R[2])
AND R[2].previous_record_hash == H_A(R[1])

...

verify_record(R[n])
AND R[n].previous_record_hash == H_A(R[n-1])
```

where `verify_record(R)` includes at minimum:

```text
- structural validation
- canonicalization
- audit_record_hash recomputation
- integrity_hash validation
- event_payload_hash validation when the payload fixture is supplied
```

Any record mutation that changes its canonical bytes MUST invalidate its own derived hash and, where applicable, the linkage from the following record.

Reordering, deletion, duplication, or substitution of a record MUST cause chain verification to fail unless the resulting sequence is independently valid under the same contract.

## 9. Domain separation

The following domains MUST remain distinct:

```text
0x00 || B              Merkle leaf domain (APS-200)
0x01 || L || R         Merkle interior-node domain (APS-200)
0x02 || C_A(R)         Audit Record hash domain (DQ-003 candidate)
C_P(P)                  Event payload hash input
C_A(R)                 Audit Record canonical input
```

`audit_record_hash`, `integrity_hash`, `event_payload_hash`, and Merkle digests MUST NOT be silently substituted for one another.

DQ-003 MUST include negative tests proving that cross-domain substitution changes the resulting digest and causes verification failure where applicable.

## 10. Cross-language conformance surface

Both RI-PY and RI-RS MUST expose equivalent observable operations for the DQ-003 fixture:

```text
canonical_bytes(record)
audit_record_hash(record)
recompute(record)
verify_chain(records)
```

For the payload fixture, implementations MUST additionally expose an observable result equivalent to:

```text
event_payload_hash(payload)
```

The implementations MAY have different internal APIs and data models. Conformance is established by identical protocol-level outputs, not by runtime coupling.

## 11. Required DQ-003 evidence

Candidate C cannot close until all of the following have independently passed:

- exact Audit Record field-set agreement
- canonical bytes equality
- audit-record hash equality
- genesis equality
- previous-record linkage
- integrity-hash independence
- event-payload hash equality
- recomputation
- tamper detection
- record reorder/delete/duplicate detection
- domain separation
- Merkle/evidence separation
- RI-PY ↔ RI-RS replay

## 12. Golden Fixture requirements

The Golden Fixture MUST contain, at minimum:

```text
record_0 (genesis)
record_1
record_2
payload_0 / payload_1 / payload_2 as required by event_payload_hash
```

For every record it MUST provide:

```text
canonical_input_without_derived_hashes
canonical_bytes_hex
integrity_hash
previous_record_hash
event_payload_hash
audit_record_hash
```

The fixture MUST also contain expected negative outcomes for at least:

```text
field mutation
payload mutation
previous_record_hash mutation
record reorder
record deletion
record duplication
wrong domain prefix
cross-domain hash substitution
```

Golden Fixtures MUST NOT be frozen before Contract v0 is reviewed and DQ-003 Candidate C is accepted.

## Decision rule

If either implementation requires an adapter to invent Audit Record semantics rather than map an already-defined protocol object, DQ-003 remains **BLOCKED** and the specification must be completed before implementation work proceeds.

The intended sequence is:

```text
Audit Record Contract v0
        ↓
review / resolve open semantics
        ↓
Golden Fixture
        ↓
RI-PY implementation
RI-RS implementation
        ↓
cross-language comparison
        ↓
DQ-003 decision
        ↓
if accepted: normative APS-200 update
```
