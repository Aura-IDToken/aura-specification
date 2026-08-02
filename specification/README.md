# Specification directory

This directory contains SPEC documents derived from the accepted Architecture Baseline (ARC-001…ARC-025).

Purpose
- SPEC documents are the canonical normative sections that will be aggregated into APS-001 (the umbrella Protocol Specification) for Specification v1.0.
- Each SPEC is strictly derived from one or more ARC documents and MUST include an explicit ARC → SPEC traceability mapping.

Workflow (Sprint 2 - Specification Freeze)
- Never more than one SPEC document in active authoring at a time.
- Cycle: Issue → Branch → Document → Review → PR → Merge → Index update.
- SPEC documents begin as DRAFT and progress to REVIEW → APPROVED → FROZEN in accordance with GOVERNANCE.md.

Location of work
- Create SPEC files in this directory using templates/SPEC_TEMPLATE.md.
- Do not add implementation artifacts, conformance tests, or CI configurations during this sprint.

See also: ../arc/README.md, ../compliance/ARC_TO_SPEC_MAPPING.md
