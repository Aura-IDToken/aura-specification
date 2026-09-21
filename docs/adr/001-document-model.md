---
ADR: ADR-001
Title: Document Model — ARC → SPEC → APS
Status: DRAFT
Version: 1.0
Date: 2026-08-02
Authors: Chief Specification Architect
Decision Owner: Protocol Custodian
Canonical language: English

---

## Context

The repository is evolving from a collection of APS-numbered documents toward a managed documentation architecture that introduces three artifact classes: ARC (Architecture Baseline), SPEC (normative specification sections), and APS (aggregated Protocol Specification). Recent changes introduced ARC and SPEC templates and mapping placeholders but did not include a formal decision recording the canonical model, ownership, lifecycle, or enforcement mechanisms.

This ADR records the proposed canonical document model for Aura Protocol documentation and prescribes lifecycle, ownership, identifier rules, traceability, repository invariants, and required CI enforcement to make the model operational.

## Decision (summary)

We adopt the following canonical document model for Aura Protocol documentation:

- ARC — Architecture Baseline
  - Purpose: Immutable record of an accepted architecture baseline (design rationale, scope, acceptance evidence).
  - Lifecycle: Draft → REVIEW → ACCEPTED. Once ACCEPTED, an ARC file is treated as FROZEN (immutable) and assigned an ARC-### identifier.
  - Ownership: Architecture Board (owner/approver).
  - Canonical status: Canonical for architecture baselines.

- SPEC — Normative Specification Section
  - Purpose: Normative specification units that express requirements (MUST/SHOULD/MAY) derived from one or more ARCs.
  - Lifecycle: DRAFT → REVIEW → APPROVED → FROZEN. A SPEC becomes FROZEN only after explicit approval by the Protocol Custodian.
  - Ownership: Protocol Custodian (owner/approver for normative acceptance).
  - Canonical status: Canonical for normative requirements; each SPEC must reference at least one ARC.
  - Retention policy: SPEC documents are permanent canonical artifacts unless superseded by a new SPEC or explicitly superseded by an APS release. The canonical origin of each normative statement remains the SPEC that introduced it.

- APS — Aggregated Protocol Specification / Publication
  - Purpose: Official published protocol release that aggregates approved SPECs into a single umbrella specification (APS-###) intended for implementers and external stakeholders.
  - Lifecycle: Composed from frozen SPECs, released by Release Authority. APS artifacts are immutable release outputs and are assigned APS-### identifiers.
  - Ownership: Release Authority (owner/approver for publication).
  - Canonical status: Canonical published artifact for a given release; the source of truth for a release is the collection of approved SPECs and their ARC mappings, not the APS PDF alone.

## Front Matter (minimal required schema)

Every ADR / ARC / SPEC file MUST include a top-of-file YAML front matter containing at minimum the following fields (case-sensitive):

- id: (e.g., SPEC-001, ARC-001, ADR-001)
- status: DRAFT | REVIEW | APPROVED | FROZEN | ACCEPTED
- version: semantic or integer version (e.g., 1.0)
- authority: canonical authority (Protocol Custodian, Architecture Board, Release Authority)
- owner: owning role or entity
- created: YYYY-MM-DD
- last_updated: YYYY-MM-DD
- derived_from: (list of parent identifiers, optional)
- accepted_by: (filled when ACCEPTED)
- commit_sha: (commit SHA at freeze/acceptance)
- supersedes: (identifier, optional)
- superseded_by: (identifier, optional)

Detailed JSON Schema for front matter will be defined in a follow-up RFC.

## Artifact Identity (decision rules)

- Identifiers are immutable and never change once assigned.
- Filenames may change; titles may change; versions may increment.
- Traceability and references MUST use the immutable identifier (ARC-###, SPEC-###, APS-###), not filenames or titles.
- Identifier form is case-sensitive and must be referenced exactly.

## Traceability Rules

- Every SPEC SHALL reference at least one ARC (INV-DOC-002).
- Every normative requirement (REQ-###) in a SPEC SHALL include a traceability backlink to the ARC element that motivated it and to its SPEC origin (ARC ID, SPEC ID, REQ ID).
- An APS release SHALL be reproducible from the set of frozen SPECs it aggregates (INV-DOC-003). The release process must record the mapping of included SPEC IDs and their commit SHAs.
- The machine-readable mapping file (`compliance/arc_to_spec_mapping.yaml`) SHALL be the authoritative mapping source for CI validation. The mapping schema and validation rules are defined in a companion RFC.

## Repository Invariants

- INV-DOC-001: Every normative statement SHALL have exactly one origin SPEC or APS mapping.
- INV-DOC-002: Every SPEC SHALL reference at least one ARC.
- INV-DOC-003: Every APS SHALL be reproducible from approved SPEC documents (buildable list of SPEC IDs & SHAs).
- INV-DOC-004: No orphan document SHALL exist; every document MUST be reachable from the Constitution, ARC, SPEC, ADR, RFC, or APS index.
- INV-DOC-005: Every identifier SHALL be globally unique.
- INV-DOC-006: Canonical terminology SHALL be defined exactly once in CANONICAL_GLOSSARY.md and referenced by SPECs and ARCs.
- INV-DOC-007: Every release SHALL include traceable evidence artifacts linking tests and evidence to SPEC requirements.
- INV-DOC-008: Frozen artifacts SHALL NOT be modified; corrections require a new superseding artifact and an explicit link to the correction.

## CI and Enforcement (proposed)

- doc/ci/validate-ids — enforce identifier format and uniqueness across the repository.
- doc/ci/traceability-check — validate that every FROZEN SPEC references at least one ARC and that arc_to_spec_mapping.yaml contains entries for each frozen SPEC.
- doc/ci/frozen-check — prevent direct modification of files marked FROZEN (by checking headers and approved status).
- doc/ci/glossary-check — validate used terms against CANONICAL_GLOSSARY.md and flag non-canonical synonyms.

## Decision Scope

This ADR governs only the document architecture (artifact classes, lifecycle, identifiers, traceability, and repository invariants). It does NOT:

- Define or change protocol runtime semantics.
- Modify implementation requirements for reference implementations.
- Supersede existing protocol specifications unless explicitly referenced and superseded by a subsequent ADR.

## Open Questions (require Protocol Custodian resolution)

- Retention policy detail: whether SPEC documents after aggregation are archived or remain active canonical artifacts (proposal: remain canonical unless superseded).
- Exact approval thresholds and sign-off procedure for Architecture Board and Protocol Custodian (quorum, signature format).
- Exact schema and enforcement mechanism for `arc_to_spec_mapping.yaml` (refer to RFC action below).

## Actions (required to complete decision)

1. Protocol Custodian review and APPROVAL of this ADR. Approval MUST be recorded in an `accepted_by` field in the front matter and by merging the ADR into the repository's canonical branch.
2. RFC to define `arc_to_spec_mapping.yaml` schema and CI enforcement details.
3. After ADR approval, create AURA_DOCUMENT_ARCHITECTURE.md (Level 0 canonical descriptive document) that references this ADR and describes the model as a reference architecture.
4. Implement CI checks and provide a migration plan for existing APS documents.

## Merge Blockers (Draft PR Checklist — MUST be satisfied before ACCEPTED)
- [ ] Protocol Custodian approval (required)
- [ ] Architecture Board approval (required)
- [ ] Open Questions resolved
- [ ] Lifecycle finalized
- [ ] Authority Matrix approved
- [ ] Front Matter schema approved
- [ ] Repository Invariants reviewed
- [ ] Traceability model approved

## Acceptance procedure

- This ADR is DRAFT until Protocol Custodian adds an `accepted_by` entry and the PR is merged. After merge with `accepted_by`, the ADR status becomes ACCEPTED and subsequent Level 0 documentation (AURA_DOCUMENT_ARCHITECTURE.md) may be published as CANONICAL (descriptive only).

---

