# D-1 Physical APS-200 Edit Evidence

**Artifact ID:** D-1-PVE-001  
**Date:** 2026-08-23  
**Authorization:** D-1-PEA-001 — PHYSICAL APS-200 EDIT AUTHORIZATION  
**Repository:** `Aura-IDToken/aura-specification`  
**Branch:** `claude/aps-200-spec-recovery-b7wc2h`  
**Physical edit commit:** `c749a7c00d77ae0c5dfa114aba444aff74ee29db`  
**Parent:** `edf2c5a1bafaa15d95b331ab8728ad5c7885fa55`  
**Edited file:** `aps/APS-200_CANONICAL_DATA_MODEL.md`  
**Post-edit blob SHA:** `a85b3ad3e89c1ee2780b07743f8240f277492468`  
**Pre-edit blob SHA:** `0488eec04e102e87b5724ca385a534d0c5f4e1cd`

## 1. Execution result

**GO — CONTROLLED PHYSICAL APS-200 EDIT executed.**

The physical edit was limited to the current APS-200 §8 serialization/representation material. No historical §8.1–§8.9 numbering was restored.

The physical edit commit contains exactly one changed file:

- `aps/APS-200_CANONICAL_DATA_MODEL.md`

Commit statistics: **9 additions, 1 deletion**.

No CONF-003, fixture, implementation, RI-PY, RI-RS, ENT-007, DQ-003, DQ-004, or C4 material was changed by the physical edit commit.

## 2. Anchor-to-line mapping

Based on the post-edit APS-200 §8 layout:

| Anchor | Post-edit location |
|---|---:|
| A-01 Representation boundary | §8, line 214 |
| A-02 Canonical serialization profile | §8, line 216 — existing wording preserved |
| A-03 Canonical byte boundary | §8, line 218 |
| A-04 Cross-implementation determinism | §8, line 220 |
| A-05 Digest-input boundary | §8, line 222 |
| A-06 Serialization scope boundary | §8, line 234 |

The existing RFC 8785/JCS profile, raw `0x00`/`0x01` hash-domain material, reference vector, and implementation evidence remain in their original relative order.

## 3. Exact semantic delta

The physical patch is the following localized change:

```diff
 ## 8. Serialization Requirements
 
+Representation boundary: A transport representation is not, by itself, the canonical representation of a protocol object. Where this specification requires canonical serialization, the canonical representation MUST be established by the canonical serialization profile defined in this section. A transport encoding or wire representation MUST NOT be treated as canonical solely because it is used for transport.
+
 For the current normative JSON interoperability profile, implementations MUST use **RFC 8785 JSON Canonicalization Scheme (JCS)** when canonical JSON serialization is required by this specification.
 
-The canonical serialization boundary is the UTF-8 byte sequence emitted by the JCS profile. Semantic JSON equivalence, map insertion order, implementation-specific serializers, whitespace conventions, or textual/hexadecimal representations MUST NOT be used as substitutes for canonical-byte equality.
+The canonical serialization boundary is the UTF-8 byte sequence emitted by the JCS profile, which constitutes `canonical_bytes`. Semantic JSON equivalence, map insertion order, implementation-specific serializers, whitespace conventions, or textual/hexadecimal representations MUST NOT be used as substitutes for canonical-byte equality.
+
+Cross-implementation determinism: For the same semantic protocol object, when canonical serialization is required under the same applicable canonical serialization profile, every conformant implementation MUST produce byte-identical `canonical_bytes`.
+
+Digest-input boundary: Where a cryptographic operation explicitly requires canonical serialization, the digest input MUST be the applicable `canonical_bytes` and MUST NOT be substituted with a non-canonical serialization, an implementation-specific serialization, a textual representation of the canonical bytes, or a textual representation of the resulting digest.
 
 For a canonical object `O`:
@@
 The leaf prefix `0x00` is one raw octet. It MUST NOT be represented as the ASCII characters `0x00`, a hexadecimal string, or another textual wrapper. RFC 6962-style interior-node hashing uses `0x01` followed by the two raw 32-byte child digests.
 
+Serialization scope: Canonical serialization defines the canonical representation and byte representation of the protocol object. It does not, by itself, define event semantics, event-type vocabulary, protocol-version compatibility semantics, identity semantics, entity-schema ownership, migration authority, or DQ-003/DQ-004 closure criteria.
+
 The canonicalization/hash boundary is implementation-independent.
```

The single deletion is solely the explicit naming of `canonical_bytes` in the existing canonical-byte boundary sentence. It does not alter the underlying byte boundary.

## 4. Semantic-delta verdict

| Anchor | Delta | Verdict |
|---|---|---|
| A-01 | New explicit transport/canonical distinction, no allow-list | SAFE / authorized |
| A-02 | Existing RFC 8785/JCS requirement preserved | SAFE / preserved |
| A-03 | Existing UTF-8 boundary explicitly names `canonical_bytes` | SAFE / authorized clarification |
| A-04 | Ratified D-2.4 MUST made explicit | SAFE / NO UNAUTHORIZED DELTA |
| A-05 | Ratified D-2.3 digest-input boundary made explicit | SAFE / NO UNAUTHORIZED DELTA |
| A-06 | Ratified serialization negative scope made explicit | SAFE / authorized |

## 5. Preservation checks

Preserved without reinterpretation:

- RFC 8785/JCS authority;
- UTF-8 canonical byte boundary;
- existing hash-domain material;
- raw `0x00` leaf prefix and `0x01` interior-node semantics;
- CANONICAL-001 reference vector;
- DQ-001/DQ-002 authority boundaries;
- implementation-independent canonicalization evidence;
- version-binding statement;
- existing normative material outside the authorized additions.

No new hash domain was introduced.

No `audit_record_hash` was introduced.

No protocol-level `session` concept was introduced.

No historical §8.1–§8.9 structure was restored.

## 6. Reference inventory after edit

The edit intentionally did **not** repair downstream historical references.

Known controlled state:

- `CONF-003 §4.5 → APS-200 §8.4` remains a broken historical reference and is deferred to a separate reference-repair authorization.
- No new historical §8.x authority reference was introduced by the edit.
- Internal APS-200 references to §8 remain valid against the current consolidated §8.
- DQ-003/DQ-004 remain outside §8 authority and remain open.

No reference repair was performed in this commit.

## 7. Conformance and governance firewall verification

The following were not edited by the physical edit commit:

- CONF-003;
- conformance fixtures;
- RI-PY;
- RI-RS;
- ENT-007;
- DQ-003 closure material;
- DQ-004 closure material;
- C4;
- `audit_record_hash` terminology as protocol authority;
- `session` as a protocol object;
- G-6 authority placement.

The physical edit therefore remains within D-1-PEA-001 scope.

## 8. Post-edit acceptance state

**Physical edit execution:** PASS  
**Scope compliance:** PASS  
**Historical numbering restoration:** NO  
**Unauthorized hash-domain change:** NO  
**Unauthorized protocol concept:** NO  
**CONF-003 modification:** NO  
**Implementation modification:** NO  
**DQ-003 closure:** NO  
**DQ-004 closure:** NO  
**C4:** NOT AUTHORIZED

**Custodian post-edit status:** PENDING FINAL ACCEPTANCE.

This artifact records execution evidence only. It does not grant downstream authorization or constitute final Custodian acceptance.
