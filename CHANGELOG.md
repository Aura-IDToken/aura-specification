# Changelog

All notable changes to the Aura Protocol Specification are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows the model defined in [VERSIONING.md](VERSIONING.md).

---

## [Unreleased]

### Added
- `governance/AURA-AFI-AEP-001_FOUNDING_INSTRUMENT_AND_AUTHORITY_EVIDENCE_PROCEDURE_v0.1-DRAFT.md` as a proposed, non-constitutive procedure for documenting Genesis authority evidence
- Initial canonical repository structure
- Root governance documents (GOVERNANCE.md, CONTRIBUTING.md, VERSIONING.md, STYLE_GUIDE.md)
- Directory scaffold for all specification areas
- APS-000 through APS-950 canonical Markdown documents
- Protocol Invariant Registry (INV-001 – INV-015)
- Conformance Test stubs (CONF-001 – CONF-010)
- Traceability Model
- ADR and RFC process templates
- SPEC-002 draft for the Constitution Artifact contract, including unresolved architectural decisions, traceability matrix, proposed acceptance criteria, and formal NOT READY status
- RFC-001 (`rfcs/RFC-001_APS001_MILESTONE1_EXECUTION_SCOPE.md`) to formalize Milestone 1 first-increment scope, synchronization targets, and acceptance criteria for APS-001 alignment
- `GOVERNANCE_STATUS_INDEX.md` as a short navigation index for current, historical, and non-constitutive governance/status artifacts
- Draft machine-readable APS-200 entity schemas and APS-300 evidence schemas under `fixtures/schemas/`
- Current DQ-003 version-compatibility matrix artifacts under `ck003/decisions/DQ-003/`, bound compatibility fixture `fixtures/compatibility/FIX-COMPAT-001_VERSION_MATRIX.json`, repo-native draft runner `scripts/run-draft-conformance.py`, and GitHub Actions workflow `.github/workflows/draft-conformance.yml`
- Current DQ-004 event-type registry artifacts under `ck003/decisions/DQ-004/` for the local CONF-012 gate

### Changed
- APS-200 ENT-002 / ENT-003 now close the current draft working-profile payload contract (`AURA-DRAFT-CORE-001`), including a concrete request payload, result payload, and working decision vocabulary
- APS-001 now points to the closed draft working-profile request/result payload contract and removes APS-200 machine-readable schemas from its open-dependency list
- `fixtures/schemas/evaluation-request.schema.json` and `fixtures/schemas/evaluation-result.schema.json` now enforce the current draft working-profile payload shape instead of only top-level structure
- APS-300 now closes the current draft `EPR-CORE` integrity-metadata and publication-hash contract needed by `FIX-001`, and APS-200 clarifies that attestation `evidence_reference` targets the Evidence Pack `pack_id`
- `fixtures/schemas/attestation.schema.json` and `fixtures/schemas/evidence-pack.schema.json` now validate the current draft `EPR-CORE` linkage and integrity-metadata vocabulary end-to-end
- `fixtures/core/FIX-001_BASIC_EVALUATION.json` now carries concrete draft Evidence Pack content and computed digest/hash values instead of placeholder evidence publication fields
- `fixtures/README.md`, APS-400, APS-500, completion docs, and traceability docs now reflect that FIX-001 is a concrete working draft fixture rather than a placeholder-only artifact
- Added `scripts/check-fix001-evidence.py` as a repository-local draft execution path for CONF-004, CONF-005, and CONF-010 against `FIX-001`
- CONF-004, CONF-005, and CONF-010 now carry explicit executable preconditions and procedures bound to `FIX-001` and the draft verifier script
- `scripts/check-fix001-evidence.py` now also executes the local deterministic CONF-001 request/result/evidence path for `FIX-001`
- CONF-001 readiness and fixture metadata now point to the same repository-local draft gate as CONF-004/005/010
- `scripts/check-fix001-evidence.py` now also executes a local artifact-level CONF-006 platform-independence replay across multiple draft execution contexts declared by `FIX-001`
- CONF-006 readiness and fixture metadata now point to the same repository-local draft gate as CONF-001/004/005/010
- `scripts/check-fix001-evidence.py` now also executes a local CONF-002 replay path that derives chained replay evidence from the same `FIX-001` request/result/evidence set
- CONF-002 readiness, traceability, and fixture metadata now point to the same repository-local draft gate family
- GOVERNANCE.md, CONTRIBUTING.md, and VERSIONING.md now explicitly allow draft-stage closure work on canonical DRAFT documents without touching FROZEN artifacts, and they treat unpublished digest/checksum placeholders as draft-only rather than release authority
- README.md restructured as canonical repository index
- README.md now links to `GOVERNANCE_STATUS_INDEX.md` as the short routing index for governance/status artifacts
- Selected unsigned root-level governance/status records now link back to `GOVERNANCE_STATUS_INDEX.md` so readers can recover the current routing context from inside analysis and conflict documents
- README.md now points readers to the current authority-binding artifact (`AUTHORITY_BINDING_RECORD_v1.1.md`) and the current DQ-006 status record (`closures/DQ-006_CLOSURE_PACKAGE.md`)
- Added `closures/README.md` as the closure-record index, explicitly separating authoritative closure records from superseded historical copies
- evidence/README.md now marks `evidence/DQ-006_CLOSURE_PACKAGE.md` as a historical copy and redirects readers to `/closures/`
- APS-200 §10 and APS-300 §14 now distinguish the new published top-level structural schemas from the remaining open profile/governance dependencies
- ROADMAP.md, TRACEABILITY_MODEL.md, docs/completion/01_CURRENT_STATE_MATRIX.md, and fixtures/README.md now reflect that machine-readable top-level schemas exist while fixture/evidence semantics remain open
- Existing APS .txt source files preserved in root; canonical Markdown versions added in /aps/
- **APS-200 §8** now binds the canonical serialization profile: RFC 8785 JCS, UTF-8 `canonical_bytes`, prohibited digest inputs, the SHA-256 / RFC 6962 byte domain, the cross-implementation byte-identity requirement, the scope boundary against event and version semantics, and migration. Declared the single normative authority for canonical serialization (DQ-006)
- **APS-300 §5** now binds `evidence_hash`, `input_hash` and `output_hash` to APS-200 §8 canonical bytes, separates the evidence-hash and Merkle domains, and states migration; §8 chain links defer to §5.1 (DQ-006)
- **APS-001** Appendix A reconciled: the canonical serialization profile and the APS-300 cryptographic binding are no longer open closure dependencies
- **CONF-003** rewritten as a normative conformance requirement demanding independently produced RI-PY/RI-RS artifacts, gate-side digest and leaf recomputation, negative controls, and a JCS-discriminating fixture
- **ADR-CK003-DQ006** reconciled to ACCEPTED, distinguishing the normative protocol contract from conformance implementation detail
- **DQ-006 status of record** reconciled from CLOSED to **OPEN** in `closures/DQ-006_CLOSURE_PACKAGE.md`, now the single authoritative closure record; four duplicate records marked SUPERSEDED. Cross-language byte/SHA-256/leaf equality on CANONICAL-001 remains PASS; closure is withheld pending a JCS-discriminating cross-language vector, evidence reachability, and ratification
- Milestone 1 execution planning was initialized in `ROADMAP.md` with explicit M1-I1 scope for APS-001 section synchronization
- APS-100/200/300/400/500/900/950 authority metadata now uses explicit APS-001 section references; Last Review metadata updated for touched normative APS documents
- `compliance/TRACEABILITY_MATRIX.md` now references concrete APS-001 sections for INV-001/002/006/007/008/013 mappings instead of APS-001 TODO placeholders
- APS index/readme links and status entries now consistently point APS-001 to `specification/APS-001_PROTOCOL_SPECIFICATION.md` as DRAFT
- CONF-008, VERSIONING, APS-400, APS-500, traceability docs, and completion/status docs now reflect the explicit DQ-003 compatibility matrix, the bound FIX-COMPAT-001 fixture, the repo-native draft runner, and the new repository-local CI gate
- CONF-012, the event-type registry/docs, FIX-INV-012, APS-400/APS-500, and completion/status docs now reflect the current repository-local DQ-004 auditability gate

---

## [0.1.0] — 2026-07-23

### Added
- Initial import of APS source documents (APS-000, APS-100, APS-200, APS-300, APS-400, APS-500, APS-900, APS-950) as authoritative text files
- AURA Constitution v1.0 (FROZEN)

---

<!-- Links section -->
[Unreleased]: https://github.com/AuraIDToken/aura-specification/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/AuraIDToken/aura-specification/releases/tag/v0.1.0
