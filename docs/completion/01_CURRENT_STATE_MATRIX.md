# Aura Specification — Current-State Conformance Matrix

**Baseline:** `main` @ `62d2d6bcc1a46dd505ebfe400ad01fa3c6a25bf0`  
**Assessment branch:** `completion/aura-specification-conformance`  
**Assessment rule:** existence of a document is not evidence of conformance.

| Domain | Current state | Evidence | Closure requirement |
|---|---|---|---|
| Constitution | **FROZEN / PASS** | `constitution/AURA_CONSTITUTION.md` | No content change; amendments only through constitutional process |
| APS-000 | **DRAFT** | `aps/APS-000_FOUNDATION_AND_TERMINOLOGY.md` | Complete review + approval |
| APS-001 | **OPEN / CRITICAL** | `specification/APS-001_PROTOCOL_SPECIFICATION.md` is TODO | Author complete root normative specification + Architecture Review |
| APS-100 | **DRAFT / OPEN** | 15 invariants defined | Resolve missing conformance links and align authority with APS-001 |
| APS-200 | **DRAFT / OPEN** | Canonical entities + common object contract | Exact schemas, field constraints, canonical serialization |
| APS-300 | **DRAFT / OPEN** | Evidence model exists | Exact Evidence Pack schema + cryptographic binding |
| APS-400 | **DRAFT / INCOMPLETE** | CONF-001…010 documents exist | Add coverage for INV-007, 012, 013, 014, 015 and executable runner |
| APS-500 | **DRAFT / INCOMPLETE** | Fixture contract exists | Publish canonical machine-readable fixture set and expected outputs |
| APS-900 | **DRAFT / INCOMPLETE** | Traceability model exists | Every normative requirement must resolve to test, fixture, evidence, implementation and release |
| APS-950 | **DRAFT / OPEN** | RI requirements exist | Reference implementation certification after conformance gate |
| Invariant Registry | **DRAFT / INCOMPLETE** | `INVARIANT_REGISTRY.md` | Remove all TODO test assignments and verify all links |
| Traceability Matrix | **DRAFT / INCOMPLETE** | `compliance/TRACEABILITY_MATRIX.md` | Populate objective statuses; no unsupported PASS claims |
| CK-003 DQ-002 | **EVIDENCE BRANCH EXISTS** | `ck003/dq-002-hash-domain` | Independent review + integration after decision is recorded |
| CK-003 DQ-003 | **EVIDENCE BRANCH EXISTS** | `ck003/dq-003-versioning-snapshot` | Independent review + integration after decision is recorded |
| CK-003 DQ-004 | **OPEN** | No DQ-004 closure package on `main` found | Complete event-type semantics, fixture, conformance and gate |
| CI | **OPEN / CRITICAL** | `.github` contains CODEOWNERS/templates but no workflow directory on `main` | Add executable repository-native conformance CI |
| Release v1.0 | **NOT READY** | Roadmap Milestone 4 remains unchecked | Only release after all mandatory gates are evidenced |

## Immediate blockers

1. **APS-001** is the root normative blocker.
2. **INV-010** is currently structurally violated by five invariants without conformance tests: INV-007, INV-012, INV-013, INV-014, INV-015.
3. APS-200/300 do not yet expose exact machine-verifiable schemas sufficient to support cross-language conformance.
4. APS-500 does not yet provide the complete canonical fixture corpus required by APS-400/950.
5. The repository lacks an executable GitHub Actions conformance gate.
6. DQ-002/DQ-003 work exists outside `main`; branch existence is not closure.

## Execution order

`APS-001 → normative reconciliation → DQ closure → APS-200/300 schemas → complete INV/CONF matrix → fixtures → executable runner → CI → RI-PY/RI-RS certification → release evidence`.
