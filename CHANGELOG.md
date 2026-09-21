# Changelog

All notable changes to the Aura Protocol Specification are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows the model defined in [VERSIONING.md](VERSIONING.md).

---

## [Unreleased]

### Added
- Initial canonical repository structure
- Root governance documents (GOVERNANCE.md, CONTRIBUTING.md, VERSIONING.md, STYLE_GUIDE.md)
- Directory scaffold for all specification areas
- APS-000 through APS-950 canonical Markdown documents
- Protocol Invariant Registry (INV-001 – INV-015)
- Conformance Test stubs (CONF-001 – CONF-010)
- Traceability Model
- ADR and RFC process templates
- SPEC-002 draft for the Constitution Artifact contract, including unresolved architectural decisions, traceability matrix, proposed acceptance criteria, and formal NOT READY status

### Changed
- README.md restructured as canonical repository index
- Existing APS .txt source files preserved in root; canonical Markdown versions added in /aps/
- **APS-200 §8** now binds the canonical serialization profile: RFC 8785 JCS, UTF-8 `canonical_bytes`, prohibited digest inputs, the SHA-256 / RFC 6962 byte domain, the cross-implementation byte-identity requirement, the scope boundary against event and version semantics, and migration. Declared the single normative authority for canonical serialization (DQ-006)
- **APS-300 §5** now binds `evidence_hash`, `input_hash` and `output_hash` to APS-200 §8 canonical bytes, separates the evidence-hash and Merkle domains, and states migration; §8 chain links defer to §5.1 (DQ-006)
- **APS-001** Appendix A reconciled: the canonical serialization profile and the APS-300 cryptographic binding are no longer open closure dependencies
- **CONF-003** rewritten as a normative conformance requirement demanding independently produced RI-PY/RI-RS artifacts, gate-side digest and leaf recomputation, negative controls, and a JCS-discriminating fixture
- **ADR-CK003-DQ006** reconciled to ACCEPTED, distinguishing the normative protocol contract from conformance implementation detail
- **DQ-006 status of record** reconciled from CLOSED to **OPEN** in `closures/DQ-006_CLOSURE_PACKAGE.md`, now the single authoritative closure record; four duplicate records marked SUPERSEDED. Cross-language byte/SHA-256/leaf equality on CANONICAL-001 remains PASS; closure is withheld pending a JCS-discriminating cross-language vector, evidence reachability, and ratification

---

## [0.1.0] — 2026-07-23

### Added
- Initial import of APS source documents (APS-000, APS-100, APS-200, APS-300, APS-400, APS-500, APS-900, APS-950) as authoritative text files
- AURA Constitution v1.0 (FROZEN)

---

<!-- Links section -->
[Unreleased]: https://github.com/AuraIDToken/aura-specification/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/AuraIDToken/aura-specification/releases/tag/v0.1.0
