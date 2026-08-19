# GATE A — APS-001 Specification Closure Matrix

**Classification:** DECISION / WORKING
**Status:** OPEN — EXECUTION CONTROL
**Review date:** 2026-08-18

## Authority baseline

Current APS-001 is `0.2-DRAFT`, `DRAFT — ARCHITECTURE REVIEW REQUIRED`, SHA-1 `51fde2452f90e3daacd8ddb7fd49c76dafef7f8f`.

The document already defines the protocol execution lifecycle, fail-closed model, canonical-byte requirement, RI-RS hash-domain model, conformance requirements, version binding, and release gate. Its Appendix A explicitly lists the remaining closure dependencies.

## Closure matrix

| Item | Current evidence | Gate A status | Next evidence |
|---|---|---|---|
| APS-001 scope/execution lifecycle | APS-001 §1–2 | SUBSTANTIALLY DEFINED | Architecture review |
| DQ-002 hash-domain | RI-RS model explicitly recorded | DECIDED / IMPLEMENTATION PENDING | Final ADR + fixture + conformance |
| DQ-003 version semantics | APS-001 §12 distinguishes protocol/schema version | OPEN — binding matrix required | Version fixture + conformance |
| DQ-004 event semantics | APS-200 ENT-007 requires `event_type` but leaves semantics open | OPEN | Event registry/ADR + fixture |
| Canonical serialization | APS-200 §8 explicitly TODO | OPEN / BLOCKER | Serialization profile + schemas |
| APS-300 evidence cryptographic binding | APS-001 requires it; APS-300 remains source of detail | OPEN | Evidence model closure |
| INV-001…INV-015 coverage | Registry exists; not all executable coverage is evidenced | OPEN | Gate B matrix |
| Canonical fixture corpus | APS-500 contract exists; completeness not yet evidenced | OPEN | Gate B corpus |
| RI-PY / RI-RS equality | Not proven by current Core archive | OPEN | Shared runner |
| CI gate | Current master plan says repository-native CI was not evidenced at its recorded baseline | OPEN | Gate C workflow + run evidence |
| Architecture Review | APS-001 explicitly requires approval | OPEN | Gate D review record |

## Blocking rule

APS-001 MUST NOT be promoted to approved v1.0 while any mandatory semantic dependency remains unresolved or lacks an executable verification path.

## Execution order

`APS-001 closure → DQ-004 → INV-001…015 → fixture corpus → RI-PY → RI-RS → cross-language equality → CI → Release Gate`.
