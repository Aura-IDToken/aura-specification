# Specification directory

This directory contains SPEC documents derived from the accepted Architecture Baseline (ARC-001…ARC-025).

## Index

| Document | Title | Version | Status | Notes |
|----------|-------|---------|--------|-------|
| [SPEC-002](SPEC-002_CONSTITUTION_ARTIFACT_CONTRACT.md) | Constitution Artifact Contract | 0.1-DRAFT | DRAFT | Draft-only contract surface; blocked by unresolved architectural decisions and upstream normative gaps |

Purpose
- SPEC documents are the canonical normative sections that will be aggregated into APS-001 (the umbrella Protocol Specification) for Specification v1.0.
- Each SPEC is strictly derived from one or more ARC documents and MUST include an explicit ARC → SPEC traceability mapping.

Workflow (Sprint 2 - Specification Freeze)
- Never more than one SPEC document in active authoring at a time.
- Cycle: Issue → Branch → Document → Review → PR → Merge → Index update.
- SPEC documents begin as DRAFT and progress to REVIEW → APPROVED → FROZEN in accordance with GOVERNANCE.md.
- SPEC-002 is an exception-handled draft contract created to expose normative gaps and required architecture decisions before any implementation or canonical artifact generation work begins.

Location of work
- Create SPEC files in this directory using templates/SPEC_TEMPLATE.md.
- Do not add implementation artifacts, conformance tests, or CI configurations during this sprint.

See also: ../arc/README.md, ../compliance/ARC_TO_SPEC_MAPPING.md
