# CK-003 Core v3.3 → Specification Traceability

**Classification:** EVIDENCE / TRACEABILITY
**Status:** INITIAL — TO BE COMPLETED AT GATE B

| Core evidence | Specification authority | Conformance target |
|---|---|---|
| `core/evaluator.py` fixed-point ARI | APS-001 §2; APS-100 invariants | INV-001, INV-006, INV-007 |
| Dimension mismatch raises | APS-001 §2/§8 fail-closed model | INV-008 |
| Existing Merkle implementation | APS-001 §7; APS-200 canonical serialization | INV-003, INV-011 |
| Certificate representation | APS-200; APS-300 | INV-003, INV-009, INV-011 |
| Test collection defect | APS-400 conformance execution requirement | INV-010 |

## Authority rule

The current APS-001 draft explicitly requires every normative requirement to have a path:

`APS-001 → INV-xxx → CONF-xxx → FIX-xxx → Evidence → RI-PY / RI-RS → Release`.

Therefore this file is an evidence bridge, not a substitute for the future APS-400/APS-500/APS-900 closure artifacts.

## Gate status

- GATE A: specification decisions must be closed first.
- GATE B: each row must acquire executable conformance coverage.
- GATE C: the conformance runner must execute the same fixtures for RI-PY and RI-RS.
- GATE D: release traceability must be complete before v1.0 freeze.
