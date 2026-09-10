# P0-1 — Canonical Representation Contract

- **Status:** ACCEPTED BY CHIEF ARCHITECT — 2026-08-22
- **Classification:** Protocol contract / closure artifact
- **Normative authority:** `aps/APS-200_CANONICAL_DATA_MODEL.md` §8
- **Related:** INV-002, INV-003, INV-006, INV-011, CONF-003, ADR-CK003-DQ006
- **Scope:** Canonical representation of protocol objects for the normative JSON interoperability profile

## 1. Contract

For protocol objects whose normative representation is JSON, Aura Protocol uses **RFC 8785 JSON Canonicalization Scheme (JCS)** as the canonical serialization profile.

The canonical representation boundary is the exact UTF-8 byte sequence emitted by RFC 8785 JCS:

```text
validated protocol object
        ↓
semantic object model
        ↓
RFC 8785 JCS
        ↓
UTF-8 canonical bytes
        ↓
applicable hash domain
```

Canonical-byte equality is the interoperability criterion. The following MUST NOT be treated as canonical representation:

- source JSON text;
- parser/insertion order;
- pretty-printed JSON;
- implementation-specific serializer output;
- hexadecimal digest strings;
- semantic equality without byte-level equality.

## 2. Normative rules

1. Protocol objects MUST be schema-validated before canonicalization.
2. Member ordering MUST be determined by RFC 8785 JCS.
3. Insignificant whitespace MUST NOT occur in canonical bytes.
4. Strings MUST follow RFC 8785 JSON serialization and UTF-8 encoding.
5. Numbers MUST follow RFC 8785 serialization rules; non-finite values are rejected.
6. Hash functions MUST consume canonical bytes directly.
7. Digest hexadecimal text MUST never be substituted for digest bytes as a hash input.
8. Canonical serialization defines representation only; it does not define event semantics, version semantics, identity semantics, or Merkle construction semantics.
9. Any change capable of changing canonical bytes is a versioned protocol change and requires compatibility and fixture-impact analysis.

## 3. Hash boundary

Where a protocol rule requires a direct object digest:

```text
SHA-256(canonical_bytes)
```

Where a Merkle leaf is required under the Aura RFC-6962-style profile:

```text
SHA-256(0x00 || canonical_bytes)
```

The `0x00` value is one raw octet. It MUST NOT be represented as textual `0x00`, hexadecimal text, or another wrapper.

Interior-node hashing uses:

```text
SHA-256(0x01 || left_digest || right_digest)
```

where `left_digest` and `right_digest` are the raw 32-byte digests.

## 4. Implementation boundary

The protocol contract is independent of implementation libraries.

Current conformance engines are:

- RI-PY: `rfc8785==0.1.4` — conformance-only;
- RI-RS: `serde_json_canonicalizer==0.3.2` — conformance-only.

Neither library is mandated as a production runtime dependency. Production implementations MUST satisfy RFC 8785 semantics.

## 5. Existing closure evidence

CANONICAL-001 establishes, for the frozen fixture, byte-level equality and equality of:

- canonical UTF-8 bytes;
- `SHA-256(canonical_bytes)`;
- `SHA-256(0x00 || canonical_bytes)`.

The current DQ-006 record explicitly identifies a limitation: CANONICAL-001 is JCS-degenerate and therefore does not by itself discriminate RFC 8785 from a sorted-JSON serializer. That limitation remains an evidence/conformance gap and is not a reason to alter the canonical representation decision.

## 6. Closure boundary

P0-1 closes the **protocol decision**: RFC 8785 JCS is the canonical JSON representation profile.

P0-1 does **not** silently declare DQ-006 evidence complete. The following remain separate execution gates:

- an RFC-8785-discriminating cross-language fixture;
- reachable closure evidence in the default branches of RI-PY and RI-RS;
- final DQ-006 closure verdict/rate-limiting governance action.

These are evidence/conformance gates, not unresolved canonical-format choices.

## 7. Traceability

```text
AURA Constitution
      ↓
APS-200 §8
      ↓
ADR-CK003-DQ006
      ↓
P0-1 Canonical Representation Contract
      ↓
CONF-003
      ↓
CANONICAL-001 / future discriminating fixtures
      ↓
RI-PY ↔ RI-RS
```

## 8. Decision record

The Chief Architect explicitly authorized proceeding with P0-1 on 2026-08-22, followed by P0-2 Evidence/Hash Domain Contract. This artifact records that sequencing and preserves the distinction between a frozen protocol decision and the remaining execution evidence gates.
