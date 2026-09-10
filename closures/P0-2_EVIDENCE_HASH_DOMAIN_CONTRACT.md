# P0-2 — Evidence / Hash Domain Contract

- **Status:** ACCEPTED BY CHIEF ARCHITECT — 2026-08-22
- **Classification:** Protocol contract / closure artifact
- **Normative authorities:** `aps/APS-200_CANONICAL_DATA_MODEL.md` §8 and `aps/APS-300_EVIDENCE_MODEL.md` §5
- **Related:** P0-1, INV-004, INV-005, INV-011, CONF-003, CONF-004, CONF-010, DQ-002
- **Scope:** Evidence hashing, direct object integrity hashing, and Merkle domain separation

## 1. Purpose

This contract fixes the distinction between canonical representation and the cryptographic domains that consume it.

Canonical bytes are the common input boundary. Different protocol values MUST NOT be conflated merely because they are all represented as hexadecimal SHA-256 strings.

```text
semantic object
      ↓
RFC 8785 JCS
      ↓
canonical UTF-8 bytes B
      ├──────────────────────────────┐
      │                              │
      ↓                              ↓
SHA-256(B)                      SHA-256(0x00 || B)
      │                              │
      ↓                              ↓
object/evidence digest          Merkle leaf digest
                                     │
                                     ↓
                        SHA-256(0x01 || L || R)
                                     │
                                     ↓
                              Merkle parent/root
```

## 2. Domain definitions

### 2.1 Canonical bytes

For a JSON protocol object `O`:

```text
B = UTF-8(RFC8785_JCS(O))
```

`B` is the canonical representation boundary defined by P0-1 / APS-200 §8.

### 2.2 Direct object integrity digest

For a canonical object whose integrity field is excluded from its own digest:

```text
integrity_hash(O) = SHA-256(B_without_integrity_hash)
```

The digest is represented externally as lowercase hexadecimal text. The hexadecimal representation is not a hash input.

### 2.3 Evidence digest

For an Evidence object `E`:

```text
canonical_bytes(E) = UTF-8(RFC8785_JCS(E without evidence_hash))
evidence_hash(E)   = SHA-256(canonical_bytes(E))
```

This is the explicit APS-300 §5.1 evidence domain.

### 2.4 Input and output digests

For canonical input object `I` and canonical output object `O`:

```text
input_hash  = SHA-256(canonical_bytes(I))
output_hash = SHA-256(canonical_bytes(O))
```

These digests identify the canonical payloads. They are not Merkle leaf hashes unless a separate Merkle rule explicitly applies.

### 2.5 Merkle leaf domain

For canonical bytes `B`:

```text
leaf_hash = SHA-256(0x00 || B)
```

`0x00` is one raw octet and MUST be part of the hashed input.

### 2.6 Merkle interior-node domain

For raw 32-byte child digests `L` and `R`:

```text
node_hash = SHA-256(0x01 || L || R)
```

`0x01` is one raw octet. `L` and `R` MUST be raw 32-byte digests, never hexadecimal text.

### 2.7 Evidence chain domain

APS-300 defines an optional evidence chain using:

```text
previous_evidence_hash = evidence_hash(previous_evidence_object)
```

No alternative chain-link byte domain is permitted for an APS-300 Evidence chain.

## 3. Non-conflation rules

The following values are distinct protocol concepts:

| Value | Domain | May be substituted for another? |
|---|---|---|
| `canonical_bytes` | RFC 8785 JCS UTF-8 bytes | No |
| `integrity_hash` | SHA-256 over the applicable object canonical bytes excluding its own field | No |
| `evidence_hash` | SHA-256 over Evidence canonical bytes excluding `evidence_hash` | No |
| `input_hash` | SHA-256 over canonical input bytes | No |
| `output_hash` | SHA-256 over canonical output bytes | No |
| `leaf_hash` | SHA-256(0x00 || canonical bytes) | No |
| `node_hash` | SHA-256(0x01 || raw left || raw right) | No |
| `previous_evidence_hash` | prior Evidence `evidence_hash` | No |

A field name, hexadecimal representation, or equal digest value MUST NOT be used to infer domain equivalence.

## 4. Audit Record boundary — explicit remaining reconciliation

APS-200 ENT-007 currently requires:

```text
previous_record_hash
    = hash of the previous Audit Record

event_payload_hash
    = hash of the event payload
```

The current APS corpus does **not yet provide a sufficiently explicit normative equation that maps `previous_record_hash` to one of `integrity_hash`, `evidence_hash`, or another dedicated Audit Record digest domain**.

Therefore this contract deliberately does not invent that mapping.

The following remains a P0 reconciliation item before Audit Record chain semantics can be declared fully closed:

```text
previous_record_hash
        ↓
[AUTHORITATIVE DOMAIN DECISION REQUIRED]
        ↓
exact canonical bytes + exact digest function
```

The existing RI-RS `chain_hash` construction MUST NOT be treated as the normative answer to this unresolved mapping merely because it is implemented.

## 5. Relationship to DQ-002

DQ-002 currently records the RI-RS RFC-6962-style raw-byte/domain-separated Merkle construction as a target decision and explicitly states that implementation conformance remains open.

P0-2 narrows that decision into independently testable domains:

1. direct object/evidence SHA-256 domains;
2. Merkle leaf domain `0x00 || B`;
3. Merkle node domain `0x01 || L || R`;
4. APS-300 evidence-chain linkage via `previous_evidence_hash`;
5. unresolved Audit Record `previous_record_hash` mapping, which requires explicit authority before implementation remediation.

This prevents a Merkle-domain decision from being incorrectly applied to every evidence/hash field in the protocol.

## 6. Verification requirements

A conformant implementation MUST make it possible to independently verify:

- canonical bytes;
- direct object/evidence digest;
- input/output digest where applicable;
- Merkle leaf digest where applicable;
- Merkle interior-node digest where applicable;
- Evidence chain linkage where applicable.

Conformance evidence MUST compare the relevant intermediate values, not only a final Merkle root.

Negative controls MUST include, where applicable:

- wrong canonical bytes;
- altered digest;
- wrong leaf prefix;
- wrong node prefix;
- hexadecimal child digests supplied instead of raw digest bytes;
- altered evidence object;
- altered previous evidence linkage.

## 7. Compatibility and migration

Changing any hash-domain input, excluded field set, domain separator, canonical representation, digest algorithm, or chain-link equation is a protocol compatibility event.

Historical evidence MUST retain enough version/profile information to prevent silent reinterpretation under a newer hash domain.

No production implementation is authorized to silently migrate persisted evidence between domains.

## 8. P0-2 closure boundary

P0-2 closes the **currently supported evidence/Merkle domain equations** recorded by APS-200 §8 and APS-300 §5.

P0-2 does **not** close the still-explicit Audit Record `previous_record_hash` mapping. That item must be resolved before P0-4 can declare the relevant chain invariant closed.

P0-3 therefore MUST build fixtures that distinguish every closed domain and MUST include a fixture/gate for the unresolved Audit Record mapping once its authoritative decision is recorded.

## 9. Traceability

```text
P0-1 Canonical Representation Contract
                ↓
        canonical bytes B
                ↓
     ┌──────────┼───────────┐
     ↓          ↓           ↓
 evidence    input/output   Merkle
   hash         hashes      domains
     ↓          ↓           ↓
     └──────────┼───────────┘
                ↓
        P0-3 Golden Fixtures
                ↓
        P0-4 Invariant Closure
                ↓
      RI-RS ↔ RI-PY / CL-002
```

## 10. Decision record

The Chief Architect explicitly authorized proceeding with P0-1 followed by P0-2 on 2026-08-22. This artifact records the hash-domain contract that is already supported by the current normative corpus and identifies, without inference, the remaining Audit Record chain-domain decision that must be resolved before full conformance closure.
