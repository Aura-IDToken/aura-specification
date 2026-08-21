# GATE A — APS-001 Specification Closure Matrix

**Classification:** DECISION / WORKING
**Status:** OPEN — EXECUTION CONTROL
**Review date:** 2026-08-21 (DQ-002 row reconciled by DQ-002 FINAL CLOSURE REVALIDATION; 2026-08-20 DQ-006 CLOSURE RECONCILIATION otherwise unchanged)

## Authority baseline

Current APS-001 is `0.2-DRAFT`, `DRAFT — ARCHITECTURE REVIEW REQUIRED`, SHA-1 `51fde2452f90e3daacd8ddb7fd49c76dafef7f8f`.

The document already defines the protocol execution lifecycle, fail-closed model, canonical-byte requirement, RI-RS hash-domain model, conformance requirements, version binding, and release gate. Its Appendix A explicitly lists the remaining closure dependencies.

## Closure matrix

| Item | Current evidence | Gate A status | Next evidence |
|---|---|---|---|
| APS-001 scope/execution lifecycle | APS-001 §1–2 | SUBSTANTIALLY DEFINED | Architecture review |
| DQ-002 hash-domain | APS-001 §7.1–§7.2 records the model; cross-language equality re-executed 2026-08-21 (41/41 revalidation checks, RI-PY 158, RI-RS 51) | **BLOCKED** — see `closures/DQ-002_FINAL_CLOSURE.md` | ADR approval (R-1) + approved Merkle tree-construction profile (R-2) + close F1/F2/F3 (R-3…R-5) + successful CI run (R-6) |
| DQ-003 version semantics | APS-001 §12 distinguishes protocol/schema version | OPEN — binding matrix required | Version fixture + conformance |
| DQ-004 event semantics | APS-200 ENT-007 requires `event_type` but leaves semantics open | OPEN | Event registry/ADR + fixture |
| Canonical serialization | APS-200 §8 binds RFC 8785 JCS, UTF-8 canonical bytes and the SHA-256 / RFC 6962 domains | DECIDED / NORMATIVE — evidence partial | Discriminating cross-language vector (DQ-006 R1) + entity schemas |
| APS-300 evidence cryptographic binding | APS-300 §5.1–§5.3 binds `evidence_hash` to APS-200 §8 canonical bytes and separates the leaf/node domains | DECIDED / NORMATIVE | Evidence Pack container + EPR profiles |
| INV-001…INV-015 coverage | Registry exists; not all executable coverage is evidenced | OPEN | Gate B matrix |
| Canonical fixture corpus | APS-500 contract exists; completeness not yet evidenced | OPEN | Gate B corpus |
| RI-PY / RI-RS equality | CROSS-LANGUAGE-001 PASS on CANONICAL-001 (bytes, SHA-256, RFC 6962 leaf), evidence unmerged | PARTIAL | Merge evidence to default branches (DQ-006 R2) + full corpus |
| CI gate | Current master plan says repository-native CI was not evidenced at its recorded baseline | OPEN | Gate C workflow + run evidence |
| Architecture Review | APS-001 explicitly requires approval | OPEN | Gate D review record |

## Blocking rule

APS-001 MUST NOT be promoted to approved v1.0 while any mandatory semantic dependency remains unresolved or lacks an executable verification path.

## Execution order

`APS-001 closure → DQ-004 → INV-001…015 → fixture corpus → RI-PY → RI-RS → cross-language equality → CI → Release Gate`.
