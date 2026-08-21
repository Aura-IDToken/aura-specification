# Core Evidence Consolidation — Index

**Status:** ACTIVE
**Branch:** `ck003/closure-workspace`
**Review date:** 2026-08-18

## Verified source artifacts

| Source | Integrity / identity | Use |
|---|---|---|
| `aura-poc-a-core-v3.3-main (8).zip` | SHA-256 `15dc7938da2d723248351fb6daa364ea36912ee35d64fe50c47798cb53f516b3` | Core v3.3 evidence |
| `aura-guard-v1.3-main (2).zip` | SHA-256 `4fef5720782c16eca55b896b24a40a3f833b401d14ba409de327ffce4bac80ff` | Guard evidence; not yet consolidated |
| `APS-001_PROTOCOL_SPECIFICATION.md` | Git blob SHA-1 `51fde2452f90e3daacd8ddb7fd49c76dafef7f8f` | Current normative draft |
| `APS-200_CANONICAL_DATA_MODEL.md` | Git blob SHA-1 `c974f59088935883657b1c3b2742bb48a63e52fb` | Canonical data model |
| `INVARIANT_REGISTRY.md` | Git blob SHA-1 `b7dffa0a11b5d1cad6c835e682e4e93905dc580c` | Invariant evidence |

## Consolidated verified findings

1. Core v3.3 has a fixed-point integer ARI measurement path.
2. Core v3.3 has an explicit vector-dimension fail-closed guard.
3. Current `core/merkle.py` is not the selected RI-RS canonical hash-domain implementation.
4. Current certificate fingerprinting uses sorted JSON UTF-8 and float presentation fields.
5. Core test collection is currently blocked by a missing `unittest` import in `core/test_ari_observability.py` in the supplied source snapshot.
6. APS-001 is currently `0.2-DRAFT`; it explicitly records the RI-RS hash-domain model but still lists canonical serialization, DQ-004, full conformance coverage, fixture corpus, conformance runner, CI, and architecture approval as closure dependencies.
7. APS-200 §8 explicitly leaves canonical serialization for RI-PY/RI-RS interoperability as TODO.
8. APS-200 ENT-007 requires `event_type` but does not yet define its semantic vocabulary/registry.

## Next controlled sequence

`APS-001 → DQ-004 → INV-001…015 → fixture corpus → RI-PY → RI-RS → cross-language equality → CI → Release Gate`.

## Evidence discipline

No implementation finding in this index is normative by itself. Normative meaning is assigned only by approved specification/ADR decisions.
