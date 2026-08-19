# Independent Verification

**Classification:** EVIDENCE — NON-NORMATIVE
**Method:** recomputation from the frozen hex, not restatement of recorded constants.

---

## 1. What was verified

The CANONICAL-001 vector underlying the DQ-006 closure. The frozen canonical-bytes hex was
decoded and both digests recomputed independently of RI-PY, RI-RS, and every recorded constant
in this repository.

## 2. Execution output (verbatim)

```
interpreter        : 3.11.15 x86_64 Linux
canonical_bytes_len: 100
decoded            : {"event_type":"AUDIT_RECORD","payload":{"value":42},"protocol_version":"1.0","schema_version":"1.0"}
sha256(bytes)      : b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
sha256(0x00||bytes): ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
sha256(0x01||bytes): 491a8dccdaf280c90d6ce9984ecd8b067c26c994aff7144b0a7606e3119a10b1 (negative control: wrong domain)

naive sorted-JSON bytes == frozen canonical bytes : True
naive sorted-JSON sha256                          : b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
```

## 3. Results

### 3.1 The recorded digests reproduce

| Quantity | Recorded | Recomputed | Match |
|---|---|---|---|
| `canonical_bytes_len` | 100 | 100 | yes |
| `SHA-256(canonical_bytes)` | `b6c3660c…a139a4e6` | `b6c3660c…a139a4e6` | yes |
| RFC-6962 leaf `SHA-256(0x00 \|\| bytes)` | `ce6b3673…6648c039` | `ce6b3673…6648c039` | yes |

The arithmetic in the closure package is correct, and the leaf domain is genuinely `0x00` — a
wrong-domain control (`0x01`) yields an unrelated digest.

### 3.2 The vector does not discriminate RFC 8785  ·  **EVIDENCE GAP**

`json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)` produces bytes
**identical** to the frozen canonical bytes, and therefore the identical SHA-256 and the
identical leaf.

The consequence is structural, not cosmetic:

> For CANONICAL-001, a fully conforming RFC 8785 engine and a non-conforming sorted-JSON
> serializer are indistinguishable. Both produce the frozen bytes, the frozen SHA-256 and the
> frozen leaf.

CANONICAL-001 is JCS-degenerate. It has no property that RFC 8785 supplies and ordinary sorted
JSON does not: all keys are ASCII, no key ordering depends on UTF-16 code units, the only number
is a small integer, and no string requires non-trivial escaping.

The CROSS-LANGUAGE-001 result is therefore real but narrower than its citation implies. It
establishes **that RI-PY and RI-RS agree on this object**. It does not establish **that either
implements RFC 8785**, which is the decision DQ-006 cites it for. Two implementations can agree
by both being wrong in the same way — the exact failure mode the program's own negative-control
methodology was designed to catch, applied at the digest level but not at the profile level.

## 4. Candidate discriminating vectors  ·  **CANDIDATE — NOT ESTABLISHED**

Offered as candidates only. Each must be executed against `rfc8785==0.1.4` and
`serde_json_canonicalizer==0.3.2` and its output recorded. **No value below may be treated as an
expected constant until it has been produced by execution.** Neither engine was available in the
environment where this assessment was prepared, so the "expected divergence" column states what
RFC 8785 requires, not what was observed.

| Candidate | Input fragment | Naive `json.dumps` (observed) | RFC 8785 requires |
|---|---|---|---|
| **CAND-NUM-NEGZERO** | `{"a": -0.0}` | `{"a":-0.0}` | `-0` serializes as `0` |
| **CAND-NUM-INTFLOAT** | `{"a": 1.0}` | `{"a":1.0}` | `1.0` serializes as `1` |
| **CAND-NUM-EXP** | `{"a": 1e30}` | `{"a":1e+30}` | ECMAScript `Number::toString` form |
| **CAND-NUM-BIGINT** | `{"a": 10000000000000000000000}` | `{"a":10000000000000000000000}` | value passes through IEEE-754 double semantics |
| **CAND-KEY-UTF16** | keys `"é"`, `"z"`, `"😀"` (U+1F600), `"ﬀ"` (U+FB00) | `{"z":…,"é":…,"ﬀ":…,"😀":…}` (code-point order) | UTF-16 code-unit order — U+1F600 encodes as `D83D DE00` and therefore sorts **before** U+FB00 |
| **CAND-UNI-RAW** | `{"a": "é€"}` | depends on `ensure_ascii` | raw UTF-8, no `\u` escaping |

`CAND-KEY-UTF16` and `CAND-NUM-NEGZERO` are the strongest candidates: both produce a different
byte sequence under JCS than under any sorted-JSON serializer, so either alone would convert the
cross-language bridge from a non-discriminating check into a real conformance test.

**Caution on `CAND-NUM-BIGINT`.** The RI-RS engine's own documentation, quoted in
`ck003/dq-006-canonical-serialization/…/JCS_DEPENDENCY_DECISION.md` on the guard branch, states
that arbitrary-precision numbers are not RFC 8785-conformant and are converted through IEEE-754
double semantics. Adding such a vector may expose an engine limitation rather than an
implementation defect, and the numeric domain is itself an open protocol decision. Do not add it
merely to make a fixture discriminate.

## 5. One survey claim withdrawn

An intermediate reading of `aura-guard-v1.3/src/merkle.rs:169` and
`tests/fixtures/hash_domains/HD-007_merkle_empty_root.json` suggested the empty-root digest was
truncated to 63 characters. **This is incorrect.** Direct extraction confirms both carry
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` — 64 characters, matching
`SHA-256("")`. There is no defect there, and no such finding appears elsewhere in this package.

## 6. Reproduction

```python
import hashlib, json
HEX = ("7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b22"
       "76616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c2273636865"
       "6d615f76657273696f6e223a22312e30227d")
b = bytes.fromhex(HEX)
assert hashlib.sha256(b).hexdigest() == "b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6"
assert hashlib.sha256(b"\x00" + b).hexdigest() == "ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039"
obj = json.loads(b.decode("utf-8"))
naive = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
assert naive == b, "expected JCS-degeneracy for this vector"
```

---

*This document records executed results and candidate proposals. It confers no normative
semantics and establishes no expected value.*
