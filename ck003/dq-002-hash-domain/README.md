# DQ-002 Evidence Pack — Hash Domain

> **Status of record.** The single authoritative DQ-002 status record is
> [`closures/DQ-002_FINAL_CLOSURE.md`](../../closures/DQ-002_FINAL_CLOSURE.md).
> **DQ-002 = BLOCKED** (revalidated 2026-08-21). Everything in this directory is
> subordinate evidence; nothing here transitions a status. Where a document here
> differs from that record, that record governs.

**Status:** Evidence / decision proposal — NOT APPROVED
**Workstream:** CK-003 Remediation
**DQ:** DQ-002 — cross-language hash-domain compatibility
**Branch:** `ck003/dq-002-hash-domain`

## Scope

This pack records the current normative specification and the observed RI-PY / RI-RS hashing behavior. It does not modify either reference implementation and does not freeze a new protocol rule.

## Finding

The current implementations do not share one hash domain for Merkle construction.

- **RI-RS / Aura-Guard:** RFC 6962-style domain separation: leaf = `SHA-256(0x00 || data)` and node = `SHA-256(0x01 || left_bytes || right_bytes)`. Odd nodes are promoted unchanged.
- **RI-PY / Aura Core:** `audit/merkle.py` hashes leaf strings as UTF-8 with plain SHA-256, then hashes concatenated hexadecimal digest strings; odd nodes are duplicated.

The difference is semantic and byte-level, so identical logical events can produce different roots.

## Normative status

APS-200 currently requires `integrity_hash` to be a SHA-256 hash of the canonical serialization, but explicitly leaves canonical serialization for RI-PY ↔ RI-RS interoperability as TODO. APS-300 likewise leaves the canonical `evidence_hash` algorithm TODO. APS-500 says canonical fixtures depend on APS-200 / APS-300 finalization.

Therefore this pack establishes an **open specification gap**, not a completed protocol decision.

## Contents

| Artifact | Role |
|---|---|
| `README.md` | this index |
| `02_hash_domain_adr.md` · `ADR-CK003-DQ002-HASH-DOMAIN.md` | the decision — both still `PROPOSED`; two ADRs for one decision (residual R-1) |
| `HASH_DOMAIN_EVIDENCE.md` | AS-IS evidence matrix, revalidated 2026-08-21 |
| `CROSS-LANGUAGE-002-EVIDENCE.md` | RI-PY ≡ RI-RS Merkle execution ledger |
| `03_cross_language_fixture.json` | early fixture; carries `DEFECT-DQ002-F1` (wrong node digest, **not corrected**) and does not exercise the DQ-006 boundary |
| `DEFECT-DQ002-F1/F2/F3.md` | open defects |
| `fixtures/` | RFC 6962 2-leaf and edge-matrix fixtures, oracle-generated |
| `evidence/RI-PY-VECTORS.json` · `evidence/RI-RS-VECTORS.json` | emitted cross-language vector sets |
| `evidence/canonical-001/` | CANONICAL-001 execution artifacts transported from the reference repositories — see its `PROVENANCE.md` |
| `evidence/DQ002-REVALIDATION-RESULT.json` | 2026-08-21 revalidation output, 41 checks, 0 failed |
| `tools/rfc6962_oracle.sh` | independent third-producer oracle (coreutils) |
| `tools/compare_vectors.py` | RI-PY vs RI-RS vector comparator |
| `tools/dq002_hash_domain_revalidation.py` | DQ-006 → DQ-002 boundary revalidation + negative controls |

## Reproducing the revalidation

```sh
bash   tools/rfc6962_oracle.sh selftest
python3 tools/compare_vectors.py \
  --a evidence/RI-PY-VECTORS.json --label-a RI-PY \
  --b evidence/RI-RS-VECTORS.json --label-b RI-RS \
  --fixture fixtures/FIX-CK003-DQ002-RFC6962-EDGE-MATRIX.json \
  --two-leaf fixtures/FIX-CK003-DQ002-RFC6962-2LEAF.json
python3 tools/dq002_hash_domain_revalidation.py
```

All three are deterministic, perform no network access, and require only the
Python standard library plus GNU coreutils. None of them mutates a committed
file.

## Cross-language fixture

`fixtures/FIX-CK003-DQ002-RFC6962-2LEAF.json` defines two raw leaf payloads (`a`, `b`) and the RFC-6962 expected leaf and root digests. The expected values are independent SHA-256 calculations.

## Decision requested

Approve an ADR establishing a single normative Merkle hash domain for all conformant implementations, with explicit byte-level rules and a cross-language conformance fixture. The proposed rule in the ADR is RFC 6962-style domain separation.

**No merge is authorized by this pack.**