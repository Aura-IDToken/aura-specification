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
| DQ-002 hash-domain | RI-RS model recorded; `ADR-CK003-DQ002` is PROPOSED, RI-PY non-conformant, CROSS-LANGUAGE-002 OPEN | BLOCKED — see `ck003/dq-002-hash-domain/DQ-002_CLOSURE_ASSESSMENT.md` | ADR approval + APS-200 §8/APS-300 §5 + RI-PY remediation + CROSS-LANGUAGE-002 |
| DQ-003 version semantics | APS-001 §12 distinguishes protocol/schema version | OPEN — binding matrix required | Version fixture + conformance |
| DQ-004 event semantics | APS-200 ENT-007 requires `event_type` but leaves semantics open | OPEN | Event registry/ADR + fixture |
| Canonical serialization | APS-200 §8 explicitly TODO; RFC 8785 JCS profile proposed in `ADR-CK003-DQ006` and evidenced for `CANONICAL-001` by DQ-006 | OPEN / BLOCKER — normative amendment outstanding | APS-200 §8 amendment + APS-300 reconciliation + schemas |
| APS-300 evidence cryptographic binding | APS-001 requires it; APS-300 remains source of detail | OPEN | Evidence model closure |
| INV-001…INV-015 coverage | Registry exists; not all executable coverage is evidenced | OPEN | Gate B matrix |
| Canonical fixture corpus | APS-500 contract exists; completeness not yet evidenced | OPEN | Gate B corpus |
| RI-PY / RI-RS equality | CROSS-LANGUAGE-001 proves byte/SHA/leaf equality for `CANONICAL-001` (DQ-006 CLOSED); no other fixture is evidenced | OPEN — evidenced for CANONICAL-001 only | Fixture corpus equality beyond CANONICAL-001 |
| CI gate | Current master plan says repository-native CI was not evidenced at its recorded baseline | OPEN | Gate C workflow + run evidence |
| Architecture Review | APS-001 explicitly requires approval | OPEN | Gate D review record |

## Blocking rule

APS-001 MUST NOT be promoted to approved v1.0 while any mandatory semantic dependency remains unresolved or lacks an executable verification path.

## Execution order

`APS-001 closure → DQ-004 → INV-001…015 → fixture corpus → RI-PY → RI-RS → cross-language equality → CI → Release Gate`.
