# DQ-006 Closure Package — Canonical Serialization / Cross-Language Equality

**Workstream:** CK-003 Remediation  
**Decision:** DQ-006  
**Gate:** CROSS-LANGUAGE-001 artifact bridge  
**Fixture:** CANONICAL-001  
**Status:** **CLOSED — PASS**  
**Repository:** `Aura-IDToken/aura-specification`  
**Requested branch:** `ck003/dq-006-closure`  
**Actual branch:** `claude/dq-006-closure-98ky0s` (mandated by the execution environment; naming deviation only, no protocol-semantic impact)

This directory is the **single canonical location** for the DQ-006 closure package.

## Purpose

Convert the independently executed and independently verified CANONICAL-001 /
CROSS-LANGUAGE-001 evidence into a formal, auditable DQ-006 closure.

## Contents

| File | Role |
|---|---|
| `DQ-006-CLOSURE.md` | Canonical closure record — decision, contract, criteria, scope of proof, non-closures |
| `DQ-006_EVIDENCE_INDEX.md` | Evidence table `DQ006-E01` … `DQ006-E07` with repositories, paths and commits |
| `DQ-006_CROSS_LANGUAGE_MATRIX.md` | Equality matrix, provenance, independence, gate checks, negative controls |
| `CROSS-LANGUAGE-001-EVIDENCE.md` | Execution/equality evidence ledger |
| `canonical-001-evidence-manifest.json` | Machine-readable evidence index |

## Closure basis

- RFC 8785 JCS is the canonical serialization profile under test.
- RI-PY uses `rfc8785==0.1.4`; RI-RS uses `serde_json_canonicalizer==0.3.2` — **conformance-only**, in both cases.
- The digest domain is `SHA-256(canonical_bytes)`.
- The RFC 6962 leaf domain is `SHA-256(0x00 || canonical_bytes)`, where `0x00` is one raw octet.
- CROSS-LANGUAGE-001 compared two independently produced artifacts and independently recomputed each digest and leaf.
- Production hash/Merkle runtime was not changed by the conformance work.

## Division of responsibility

The **specification repository** holds the closure record, the evidence index, the traceability
and immutable result references. The **reference implementation repositories** remain the source
of the execution artifacts. Artifacts are not duplicated here.

## Source evidence

| Implementation | Repository | Execution commit | Artifact publication commit |
|---|---|---|---|
| RI-PY | `Aura-IDToken/aura-poc-a-core-v3.3` | `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f` | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` |
| RI-RS | `Aura-IDToken/aura-guard-v1.3` | `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2` | `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0` |

## Scope boundary

This package closes the **DQ-006 evidence/decision gate** only. It does not close DQ-001,
DQ-002, DQ-003, DQ-004, APS-001, INV-001…INV-015, the fixture corpus, CI gates or the release
gate, and it does not amend `APS-200 §8`. See `DQ-006-CLOSURE.md` §11, §13 and §14.
