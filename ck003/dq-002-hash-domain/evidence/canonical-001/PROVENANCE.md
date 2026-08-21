# CANONICAL-001 artifacts — transport provenance

**Classification:** EVIDENCE (transported, not regenerated)
**Transported:** 2026-08-21, DQ-002 final closure revalidation
**Purpose:** bind the DQ-002 leaf-domain claim to the *actual* RI-PY and RI-RS
execution artifacts rather than to a constant copied into a specification
document.

## Why these files are here

`closures/DQ-006_CLOSURE_PACKAGE.md` §5, §6 and §11 name these artifacts by
repository, commit and SHA-256, but the artifacts themselves live only on
branches that are unmerged in both reference repositories (deviation D-2). A
reviewer cloning either reference repository at `main` cannot reach them.

They are copied here **byte-identically** so that the DQ-002 revalidation
harness reads real execution output, and so that the DQ-002 evidence chain is
resolvable from the specification repository alone. Nothing was regenerated,
re-keyed or reformatted. Transport does not repair D-2 in the reference
repositories; DQ-006 residual **R2** still owns that.

## Files

| File | SHA-256 | Source repository | Source path | Source commit |
|---|---|---|---|---|
| `input.json` | `649bb748464ce78fe1a1d7104689d2dee736fb80777db6569592bc0d3d039261` | `Aura-IDToken/aura-poc-a-core-v3.3` | `conformance/corpus/canonical-001/input.json` | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` |
| `manifest.json` | `28890ee7bcc14d37cfd433d496d48f1296fabffa3ad4f2e42c4c0a772ae5aa10` | `Aura-IDToken/aura-poc-a-core-v3.3` | `conformance/corpus/canonical-001/manifest.json` | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` |
| `ri-py.json` | `6b5b5ccd54901181b9af45421d051ea5ea53096fbf632ab1e25a66705f2b856c` | `Aura-IDToken/aura-poc-a-core-v3.3` | `conformance/corpus/canonical-001/ri-py.json` | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` |
| `ri-rs.json` | `a6ebad019118a7806ae927c4802a60056cb9e0c90f3cb1ef2a5e0cf359af329c` | `Aura-IDToken/aura-poc-a-core-v3.3` (transported from `Aura-IDToken/aura-guard-v1.3`) | `conformance/corpus/canonical-001/ri-rs.json` | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` |

`ri-rs.json` was produced in `Aura-IDToken/aura-guard-v1.3` at execution commit
`4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2` and transported byte-identically
into the RI-PY corpus by the CROSS-LANGUAGE-001 gate (DQ-006 deviation D-6).
This directory is a second byte-identical transport of the same file; the
digest is unchanged across both hops.

Every digest above was re-verified by `git show <commit>:<path> | sha256sum`
against the reference repository during this transport, and each matches the
value recorded in `closures/DQ-006_CLOSURE_PACKAGE.md`.

## Extraction command

```sh
# in a clone of Aura-IDToken/aura-poc-a-core-v3.3
git fetch origin claude/cross-language-canonical-001-n4v2c5
for f in input.json manifest.json ri-py.json ri-rs.json; do
  git show 3e8e0e32:conformance/corpus/canonical-001/$f
done
```

## Consumer

`../../tools/dq002_hash_domain_revalidation.py` reads `canonical_bytes_hex`
from `ri-py.json` and `ri-rs.json` and recomputes the SHA-256 digest and the
RFC 6962 leaf itself. The frozen reference constants in that harness are a
secondary cross-check only; they never substitute for artifact input.
