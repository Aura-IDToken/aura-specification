# Releases

This directory contains release artifacts for the `aura-specification` repository.

## Structure

Each release has a dedicated subdirectory:

```
releases/
└── vX.Y.Z/
    ├── RELEASE_NOTES.md
    ├── DOCUMENT_STATUS.md
    ├── CONFORMANCE_REPORT.md   (optional at this stage)
    └── CHECKSUMS.sha256
```

## Current Releases

| Version | Date | Status |
|---------|------|--------|
| [v0.1.0](v0.1.0/) | 2026-07-23 | Published — historical snapshot |

> `v0.1.0` is a preserved release artifact. It does not override the repository's current draft statuses or current completion state.

## Release Requirements (APS-950 §9)

Each release MUST include:
- Semantic version number
- Compatibility Statement (which APS version is supported)
- Conformance Report (from Milestone 3 onwards)
- Evidence Pack from Conformance Run (from Milestone 3 onwards)
- Release Notes

See [../VERSIONING.md](../VERSIONING.md) for the versioning model.
