# CK-003 Core v3.3 — Conformance Gap Matrix

**Classification:** EVIDENCE / WORKING
**Status:** OPEN WORKLIST

| Contract area | Current Core v3.3 evidence | Target contract | Action |
|---|---|---|---|
| ARI arithmetic | Fixed-point integer path | Preserve deterministic fixed-point semantics | Conformance test |
| Vector dimension | Explicit `ValueError` guard | Fail closed | Preserve + test |
| Canonical event bytes | Existing legacy representations exist | One canonical serialization boundary | APS-001/APS-200 closure |
| Leaf hash | `SHA-256(UTF-8(sorted JSON))` | `SHA-256(0x00 || canonical_bytes)` | Replace protocol path after spec freeze |
| Merkle node hash | No canonical RFC-6962 byte-domain implementation in current `core/merkle.py` | `SHA-256(0x01 || left[32] || right[32])` | Replace protocol path after spec freeze |
| Certificate numbers | `float` presentation fields | Explicit digest-domain numeric representation | DQ-003 / APS-200 closure |
| Certificate fingerprint | Sorted JSON UTF-8 | Canonical bytes defined by APS-200 | DQ-002 + serialization closure |
| Timestamp handling | Certificate accepts string; other Core paths require audit | D-TIME-001 exact format | DQ-004 / serialization closure |
| Cross-language equality | Not established by this source archive | Byte-identical RI-PY / RI-RS fixtures | Fixture corpus + runner |
| Full test collection | Blocked by missing `unittest` import | Collection succeeds | P1 test repair |

## Priority

**P0:** canonical serialization, hash-domain implementation boundary, certificate digest-domain representation, complete fixture corpus.

**P1:** test collection repair, executable conformance runner, cross-language equality.

**P2:** release traceability and architecture/security/regulatory review.

This matrix is not a claim that all listed gaps are independently proven against every repository revision. It is the controlled Core v3.3 worklist derived from the verified source snapshot.
