# DQ-002 Evidence Pack — Hash Domain

**Status:** Evidence / decision proposal — NOT APPROVED
**Workstream:** CK-003 Remediation
**DQ:** DQ-002 — cross-language hash-domain compatibility
**Branch:** `ck003/dq-002-hash-domain`

## Scope

This pack records the current normative specification and the observed RI-PY / RI-RS hashing behavior. It does not modify either reference implementation and does not freeze a new protocol rule.

## Finding

The current implementations do not share one hash domain for Merkle construction.

- **RI-RS / Aura-Guard:** RFC 6962-style domain separation: leaf = `SHA-256(0x00 || data)` and node = `SHA-256(0x01 || left_bytes || right_bytes)`. Odd nodes are promoted unchanged.
- **RI-PY / Aura Core:** `audit/merkle.py` hashes leaf strings as UTF-8 with plain SHA-256, then hashes concatenated hexadecimal digest strings; odd nodes are duplicated.

The difference is semantic and byte-level, so identical logical events can produce different roots.

## Normative status

APS-200 currently requires `integrity_hash` to be a SHA-256 hash of the canonical serialization, but explicitly leaves canonical serialization for RI-PY ↔ RI-RS interoperability as TODO. APS-300 likewise leaves the canonical `evidence_hash` algorithm TODO. APS-500 says canonical fixtures depend on APS-200 / APS-300 finalization.

Therefore this pack establishes an **open specification gap**, not a completed protocol decision.

## Cross-language fixture

`fixtures/FIX-CK003-DQ002-RFC6962-2LEAF.json` defines two raw leaf payloads (`a`, `b`) and the RFC-6962 expected leaf and root digests. The expected values are independent SHA-256 calculations.

## Decision requested

Approve an ADR establishing a single normative Merkle hash domain for all conformant implementations, with explicit byte-level rules and a cross-language conformance fixture. The proposed rule in the ADR is RFC 6962-style domain separation.

**No merge is authorized by this pack.**