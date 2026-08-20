# Scripts

This directory contains tooling scripts for traceability validation and repository maintenance.

## Available Scripts

| Script | Purpose | Status |
|--------|---------|--------|
| `validate_canonical_001.py` | Verify the frozen CANONICAL-001 fixture is internally consistent: hex decodes to the recorded length, decodes as UTF-8, parses to the recorded object, and yields the recorded SHA-256 and RFC-6962 leaf — plus two negative controls. Does **not** canonicalize. | Available |
| `check_canonicalization_authority.py` | Verify exactly one document in the normative corpus defines the RFC 8785 profile (APS-200 §8) and every other document that mentions it cites that authority. | Available |

Run both from the repository root:

```sh
python3 scripts/validate_canonical_001.py
python3 scripts/check_canonicalization_authority.py
```

## Planned Scripts

| Script | Purpose | Status |
|--------|---------|--------|
| `check-traceability.sh` | Verify every INV-xxx has a CONF-xxx; every CONF-xxx has a FIX-xxx | TODO |
| `validate-fixtures.sh` | Validate all FIX-xxx JSON files against APS-200 schemas | TODO |
| `generate-traceability-matrix.py` | Auto-generate TRACEABILITY_MATRIX.md from document metadata | TODO |
| `check-doc-headers.sh` | Verify all normative documents have required metadata headers | TODO |
| `check-ids.sh` | Verify no identifier is reused across INV, CONF, FIX, ADR, RFC | TODO |

## Status

> **TODO**: The planned scripts above remain pending finalization of APS-200 §9 schemas and the canonical document format. The canonical-serialization scripts are available now.

## Conventions

- All scripts MUST be idempotent
- All scripts MUST exit 0 on success, non-zero on failure
- All scripts MUST print a summary of findings
- Scripts MUST NOT modify specification content
