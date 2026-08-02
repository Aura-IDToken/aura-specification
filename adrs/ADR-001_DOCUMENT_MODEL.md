---
ADR: ADR-001
Title: Document Model — ARC → SPEC → APS
Status: PROPOSED
Date: 2026-08-02
Authors: Chief Specification Architect
Decision Owner: Protocol Custodian

---

## Context

The repository is evolving from a collection of APS-numbered documents toward a managed documentation architecture that introduces three new artifact classes: ARC (Architecture Baseline), SPEC (normative specification sections), and an aggregated APS (umbrella Protocol Specification). The change in PR #9 introduced templates and folder structure for ARC and SPEC but did not include a formal decision recording the canonical model, ownership, lifecycle, or enforcement mechanisms.

This ADR records the architectural decision required to define the canonical document model and the rules for traceability, ownership, and release.

## Decision

We adopt the following canonical document model for Aura Protocol documentation:

- ARC — Architecture Baseline
  - Purpose: Immutable record of an accepted architecture baseline (design rationale, scope, acceptance evidence).
  - Lifecycle: Draft → REVIEW → ACCEPTED. Once ACCEPTED, an ARC file is treated as frozen (immutable) and assigned an ARC-### identifier.
  - Ownership: Architecture Board (owner/approver).
  - Canonical status: Canonical for architecture decisions and baselines.

- SPEC — Normative Specification Section
  - Purpose: Normative specification units that express requirements (MUST/SHOULD/MAY) derived from one or more ARCs.
  - Lifecycle: DRAFT → REVIEW → APPROVED → FROZEN. A SPEC becomes frozen only after explicit approval by the Protocol Custodian.
  - Ownership: Protocol Custodian (owner/approver for normative acceptance).
  - Canonical status: Canonical for normative requirements; each SPEC must reference at least one ARC.
  - Retention policy: SPEC documents are permanent canonical artifacts unless superseded by a new SPEC or by an APS release that explicitly supersedes them. The canonical origin of each normative statement remains the SPEC that introduced it.

- APS — Aggregated Protocol Specification / Publication
  - Purpose: Official published protocol release that aggregates approved SPECs into a single umbrella specification (APS-###) intended for implementers and external stakeholders.
  - Lifecycle: Composed from frozen SPECs, released by Release Authority. APS artifacts are immutable release outputs and are assigned APS-### identifiers.
  - Ownership: Release Authority (owner/approver for publication).
  - Canonical status: Canonical published artifact for a given release; the source of truth for a release is the collection of approved SPECs and their ARC mappings, not the APS PDF alone.

Traceability Rules

- Every SPEC SHALL reference at least one ARC (INV-DOC-002).
- Every normative requirement (REQ-###) in a SPEC SHALL include a traceability backlink to the ARC element that motivated it and to its SPEC origin (ARC ID, SPEC ID, REQ ID).
- An APS release SHALL be reproducible from the set of frozen SPECs it aggregates (INV-DOC-003). The release process must record the mapping of included SPEC IDs and their commit SHAs.
- The machine-readable mapping file (`compliance/arc_to_spec_mapping.yaml`) SHALL be the authoritative mapping source for CI validation. The mapping schema and validation rules are defined in a companion RFC (see Actions).

Identifier Rules

- Identifiers SHALL be globally unique and conform to the canonical prefixes: ARC-###, ADR-###, RFC-###, SPEC-###, APS-###, INV-###, REQ-###, EVID-###.
- Naming and identifiers are case-sensitive and SHALL be referenced exactly as assigned.

Owners and Authorities

- Protocol Custodian: approves SPECs, is owner of SPEC lifecycle, and is signatory for normative acceptance.
- Architecture Board: approves and owns ARC baselines and ADRs related to architecture decisions.
- Release Authority: owns APS publication and release mechanics.
- Compliance Authority / Auditor: owns TRACEABILITY artifacts and evidence retention policy.

Repository Invariants (Selected)

- INV-DOC-001: Every normative statement SHALL have exactly one origin SPEC or APS mapping.
- INV-DOC-002: Every SPEC SHALL reference at least one ARC.
- INV-DOC-003: Every APS SHALL be reproducible from approved SPEC documents (buildable list of SPEC IDs & SHAs).
- INV-DOC-004: No orphan document SHALL exist; every document MUST be reachable from the Constitution, ARC, SPEC, ADR, RFC, or APS index.
- INV-DOC-005: Every identifier SHALL be globally unique.
- INV-DOC-006: Canonical terminology SHALL be defined exactly once in CANONICAL_GLOSSARY.md and referenced by SPECs and ARCs.
- INV-DOC-007: Every release SHALL include traceable evidence artifacts linking tests and evidence to SPEC requirements.
- INV-DOC-008: Frozen artifacts SHALL NOT be modified; corrections require a new superseding artifact and an explicit link to the correction.

Lifecycle Summary

1. Idea / Problem Statement (informal)
2. RFC (community proposal) — RFC-###
3. ADR (if required for architecture) — ADR-###
4. ARC (architecture baseline derived from ADR/RFC) — ARC-###: ACCEPTED by Architecture Board
5. SPEC (author normative requirements derived from ARC) — SPEC-###: APPROVED by Protocol Custodian
6. APS (release aggregation) — APS-###: Published by Release Authority
7. Implementation & Conformance Tests — produce Evidence (EVID-###) and Compliance artifacts

CI and Enforcement

- A CI job (`doc/ci/validate-ids`) shall enforce identifier format and uniqueness across the repository.
- A CI job (`doc/ci/traceability-check`) shall validate that every SPEC references at least one ARC and that arc_to_spec_mapping.yaml contains entries for each frozen SPEC.
- A CI job (`doc/ci/frozen-check`) shall prevent direct modification of files marked FROZEN (by checking headers and approved status).

Consequences

- The repository will require updates to templates (SPEC_TEMPLATE.md, ARC_TEMPLATE.md), README orientation text, and governance to reflect these decisions.
- PR #9's additions (ARC and SPEC templates and mapping placeholders) are consistent with this model but are not sufficient alone; the ADR must be accepted before marking AURA_DOCUMENT_ARCHITECTURE.md as CANONICAL.

Actions (required to complete decision)

1. Protocol Custodian review and APPROVAL of this ADR. Approval MUST be recorded in an ADR acceptance section and by merging this ADR file into the canonical branch.
2. RFC to define `arc_to_spec_mapping.yaml` schema and CI enforcement details (if not already present).
3. After ADR approval, create AURA_DOCUMENT_ARCHITECTURE.md (Level 0 canonical document) that references this ADR and describes the model as a reference architecture (no decision-making content).
4. Implement CI checks as specified above and provide a migration plan for existing APS documents.

Open Questions (require Protocol Custodian resolution)

- Retention policy detail: whether SPEC documents after aggregation are archived or remain active canonical artifacts (proposal: remain canonical unless superseded).
- Exact approval thresholds and sign-off procedure for Architecture Board and Protocol Custodian (quorum, signature format).

## Status and Acceptance

This ADR is PROPOSED and requires explicit approval by the Protocol Custodian. Approval is recorded by adding an `Accepted-by: <Protocol Custodian>` line and merging this ADR into the repository's canonical branch.

---

