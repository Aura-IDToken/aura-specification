# DQ-002 — Final Closure

**Status:** CLOSED — PASS  
**Closure date:** 2026-08-19  
**Dependent gate:** DQ-006  
**Decision branch:** `ck003/dq-006-closure-package`

## 1. Decision

DQ-002 is formally closed as **PASS**.

The closure follows successful DQ-006 cross-language conformance. The canonical digest boundary is now backed by independently executed RI-PY and RI-RS evidence and is no longer supported solely by a shared expected digest.

## 2. Frozen Hash-Domain Contract

For CANONICAL-001 and the corresponding protocol boundary:

1. Canonical input is serialized using the frozen RFC 8785 JCS profile.
2. The record digest domain is the exact canonical byte sequence:

```text
SHA-256(canonical_bytes)
```

3. The RFC 6962 leaf domain is the raw octet prefix followed by the exact canonical bytes:

```text
SHA-256(0x00 || canonical_bytes)
```

4. `0x00` is a raw binary octet, not the ASCII string `"0x00"`.
5. No JSON reserialization, hexadecimal representation, whitespace transformation, or textual wrapper is introduced between canonicalization and hashing.
6. RFC 6962 interior-node domain separation remains `0x01` and is not substituted for the leaf domain.

## 3. CANONICAL-001 Evidence

Canonical bytes:

```text
7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d
```

SHA-256(canonical_bytes):

```text
b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
```

SHA-256(0x00 || canonical_bytes):

```text
ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

Both RI-PY and RI-RS independently generated these values and the equality runner verified byte, SHA-256 and leaf equality.

## 4. Conformance Evidence

RI-PY:

- `rfc8785==0.1.4`
- CANONICAL-001: PASS
- JCS-B01…B06: PASS
- cross-language artifact: PASS

RI-RS:

- `serde_json_canonicalizer==0.3.2`
- CANONICAL-001: PASS
- cross-language artifact: PASS

Cross-language:

- canonical bytes equality: PASS
- SHA equality: PASS
- leaf equality: PASS
- independent recomputation: PASS
- negative controls: PASS

## 5. Production Boundary

The conformance work did not modify production hash/Merkle core behavior. JCS engines are conformance-only dependencies.

Therefore DQ-002 closes the **protocol contract**, not a mandate to introduce JCS into production runtime.

## 6. Relationship to DQ-006

DQ-006 established that RI-PY and RI-RS independently execute the same canonicalization/hash/leaf contract.

DQ-002 now records the resulting hash-domain semantics as frozen protocol semantics.

Dependency chain:

```text
DQ-006 PASS
    ↓
independent cross-language evidence
    ↓
canonical bytes equality
    ↓
SHA-256 equality
    ↓
RFC-6962 leaf equality
    ↓
DQ-002 FINAL CLOSURE
```

## 7. Remaining Scope

DQ-002 closure does not by itself close:

- APS-001 overall specification closure;
- DQ-003 versioning closure;
- DQ-004 event-type semantic closure;
- INV-001…INV-015 as a complete set;
- full canonical fixture corpus;
- specification/core/guard CI gates;
- release gate.

Those remain governed by their respective closure criteria.

## 8. Final Verdict

**DQ-002 = CLOSED / PASS.**

The hash-domain contract is frozen and backed by executable cross-language evidence.
