# ADR-CK003-DQ006 — Canonical Serialization Profile

- **Status:** PROPOSED — approval/freeze required
- **Scope:** Protocol-bound canonical object bytes
- **Related:** INV-003, INV-006, INV-011, APS-200 §8, APS-300, APS-500

## Decision proposal

Aura Protocol SHALL use **JSON Canonicalization Scheme (JCS), RFC 8785**, as the canonical serialization profile for protocol objects whose normative representation is JSON.

The canonicalization pipeline is:

```text
validated protocol object
        ↓
semantic object model
        ↓
JCS / RFC 8785
        ↓
UTF-8 canonical bytes
        ↓
hash domain
```

The canonical byte domain is therefore the exact UTF-8 byte sequence produced by RFC 8785 JCS. A pretty-printed JSON representation, parser-preserving source text, key insertion order, or hexadecimal hash representation is never itself the canonical byte domain.

## Normative constraints proposed

1. Object member ordering SHALL be determined by JCS, not implementation insertion order.
2. No insignificant whitespace SHALL occur in canonical bytes.
3. Strings SHALL use the JCS/JSON UTF-8 representation.
4. Numbers SHALL obey RFC 8785 serialization rules; implementations MUST NOT introduce non-JSON numeric values such as NaN or Infinity.
5. Protocol objects SHALL be schema-validated before canonicalization.
6. Fields excluded from a hash domain MUST be explicitly defined by the applicable object/hash specification; omission MUST NOT be inferred from implementation behaviour.
7. Hashing SHALL consume canonical bytes directly. Hexadecimal digest strings SHALL never be substituted for digest bytes in the cryptographic domain.
8. JCS is the canonical representation profile; alternate wire encodings MAY exist only as transport representations and MUST round-trip to the same semantic object and canonical bytes.

## Why this closes the current ambiguity

APS-200 currently permits JSON, CBOR and Protocol Buffers while requiring deterministic serialization, but §8 leaves the interoperability serialization format TODO. This proposal selects one language-independent, deterministic JSON canonicalization profile for the protocol's canonical byte boundary.

## Compatibility

Changing canonical serialization is a protocol compatibility event. Existing evidence MUST retain its original serialization/hash profile identity. Historical evidence MUST NOT be silently reinterpreted under JCS.

## Conformance

CONF-003 SHALL verify that two independent serializations of the same validated object produce byte-identical JCS output. The canonical fixture corpus SHALL store canonical bytes (or an unambiguous byte encoding) and expected digests.

## Closure gate

This ADR may be marked APPROVED only after:

- [ ] Chief Architect approval is recorded.
- [ ] APS-200 §8 is updated to bind the profile.
- [ ] APS-300 hash/evidence scope is reconciled with canonical bytes.
- [ ] At least one normative cross-language fixture is frozen.
- [ ] RI-PY and RI-RS produce identical canonical bytes and expected digests.
- [ ] Version/migration semantics are documented.

**Important:** this file is a proposal. It does not itself amend or freeze the normative APS documents.
