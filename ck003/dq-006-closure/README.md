# DQ-006 Closure Package — Canonical Serialization / Cross-Language Equality

> **SUPERSEDED — 2026-08-20.** This record is retained for history only.
> The single authoritative DQ-006 closure record is [`../../closures/DQ-006_CLOSURE_PACKAGE.md`](../../closures/DQ-006_CLOSURE_PACKAGE.md),
> which reconciles this material against APS-200 §8, APS-300 §5, ADR-CK003-DQ006 and CONF-003.
> Where this document differs from that record — including its status line — that record governs.
> **DQ-006 status of record: OPEN.**

**Workstream:** CK-003 Remediation  
**Decision:** DQ-006  
**Gate:** CROSS-LANGUAGE-001 ARTIFACT BRIDGE  
**Status:** PASS — closure package prepared  
**Repository:** `Aura-IDToken/aura-specification`  
**Branch:** `ck003/dq-006-closure`

## Purpose

This package records the evidence required to close DQ-006 after independent RI-PY / RI-RS execution of CANONICAL-001 and byte-level equality verification.

## Closure basis

- RFC 8785 JCS is the frozen canonicalization contract.
- RI-PY uses `rfc8785==0.1.4` in the conformance boundary only.
- RI-RS uses `serde_json_canonicalizer==0.3.2` in the conformance boundary only.
- `SHA-256(canonical_bytes)` is the digest operation.
- RFC 6962 leaf domain is `0x00 || canonical_bytes`.
- Production hash/Merkle runtime was not changed by the conformance work.
- CROSS-LANGUAGE-001 independently compared RI-PY and RI-RS actual artifacts.

## Contents

- `DQ-006-CLOSURE.md` — normative closure record and decision.
- `CROSS-LANGUAGE-001-EVIDENCE.md` — execution/equality evidence ledger.
- `canonical-001-evidence-manifest.json` — machine-readable evidence index.

## Source evidence

RI-PY execution evidence is anchored to `Aura-IDToken/aura-poc-a-core-v3.3` commit `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` and its parent execution commit `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f`.

RI-RS execution evidence is anchored to `Aura-IDToken/aura-guard-v1.3` commit `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0` and its parent execution commit `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2`.

The evidence commits are GitHub-verified and record the actual execution, artifacts, equality result and production-integrity checks.

## Scope boundary

This package closes the **DQ-006 evidence/decision gate**. It does not by itself close DQ-002, APS-001, INV-001…INV-015, or the complete release gate. Those require their own closure evidence.
