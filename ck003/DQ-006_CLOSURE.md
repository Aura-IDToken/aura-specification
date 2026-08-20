# DQ-006 — Canonical Serialization / Cross-Language Closure Package

> **SUPERSEDED — 2026-08-20.** This record is retained for history only.
> The single authoritative DQ-006 closure record is [`../closures/DQ-006_CLOSURE_PACKAGE.md`](../closures/DQ-006_CLOSURE_PACKAGE.md),
> which reconciles this material against APS-200 §8, APS-300 §5, ADR-CK003-DQ006 and CONF-003.
> Where this document differs from that record — including its status line — that record governs.
> **DQ-006 status of record: CLOSED** (2026-08-20, DQ-006 CLOSURE INTEGRATION).
> The closure now rests on two fixtures: CANONICAL-001 and the JCS-discriminating
> CANONICAL-002. Consolidated evidence:
> [`ck003/dq-006-closure/DQ-006_EVIDENCE.md`](../ck003/dq-006-closure/DQ-006_EVIDENCE.md).

**Status:** CLOSED — PASS
**Gate:** DQ-006
**Fixture:** CANONICAL-001
**Closure branch:** `ck003/dq-006-closure-package`
**Scope:** conformance evidence only
**Production runtime changes authorized by this package:** NONE

## 1. Decision

DQ-006 establishes that the RI-PY and RI-RS conformance adapters execute the same frozen CANONICAL-001 serialization and digest contract.

The closure is based on independently produced execution artifacts, followed by byte-level and digest-level equality verification.

This package does **not** close DQ-002, DQ-001, APS-001, or any remaining specification gate. Those decisions remain governed by their own evidence and closure procedures.

## 2. Frozen contract

| Element | Normative conformance value |
|---|---|
| Canonical serialization | RFC 8785 JCS |
| RI-PY engine | `rfc8785==0.1.4` |
| RI-RS engine | `serde_json_canonicalizer==0.3.2` |
| Digest | `SHA-256(canonical_bytes)` |
| Leaf | `SHA-256(0x00 || canonical_bytes)` |
| Leaf domain | `0x00` |
| Runtime integration | Not part of this gate |

The JCS engines remain conformance-scoped. This gate does not authorize replacing or modifying the production hash/Merkle core.

## 3. CANONICAL-001 input

```json
{
  "event_type": "AUDIT_RECORD",
  "protocol_version": "1.0",
  "schema_version": "1.0",
  "payload": {
    "value": 42
  }
}
```

## 4. Independent execution evidence

### RI-PY

Repository: `Aura-IDToken/aura-poc-a-core-v3.3`

Execution commit: `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f`

Engine: `rfc8785==0.1.4`

Observed canonical bytes:

```text
7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d
```

SHA-256:

```text
b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
```

RFC-6962 leaf:

```text
ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

### RI-RS

Repository: `Aura-IDToken/aura-guard-v1.3`

Execution commit: `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2`

Engine: `serde_json_canonicalizer==0.3.2`

Observed canonical bytes, SHA-256 and leaf are identical to RI-PY.

## 5. Equality verdict

| Check | Result |
|---|---|
| RI-PY canonical bytes independently produced | PASS |
| RI-RS canonical bytes independently produced | PASS |
| Canonical byte equality | PASS |
| RI-PY SHA independent verification | PASS |
| RI-RS SHA independent verification | PASS |
| SHA equality | PASS |
| RI-PY leaf independent verification | PASS |
| RI-RS leaf independent verification | PASS |
| Leaf equality | PASS |
| Frozen expected-value cross-check | PASS |

## 6. Negative controls

The equality gate was tested against temporary mutations:

- Modified canonical bytes → gate failed.
- Modified SHA-256 → gate failed.
- Wrong leaf domain (`0x00` → `0x01`) → independent recomputation failed.

The mutations were temporary and were not committed to the canonical corpus.

## 7. Production integrity

The execution report establishes:

- RI-PY `core/` unchanged.
- RI-PY `audit/` unchanged.
- RI-RS `src/` unchanged.
- RI-RS production `Cargo.toml` and `Cargo.lock` unchanged.
- JCS engines are isolated in conformance scope.
- No production hash, Merkle, event-type, or protocol semantics were changed by CROSS-LANGUAGE-001.

## 8. Evidence provenance

Primary implementation evidence:

- RI-PY bridge commit: `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e`
- RI-RS bridge commit: `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0`
- RI-PY execution commit recorded by artifact: `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f`
- RI-RS execution commit recorded by artifact: `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2`

The artifact bridge is therefore traceable to actual source commits rather than to a manually constructed expected-value file.

## 9. Architectural interpretation

DQ-006 closes the **canonical serialization conformance question represented by CANONICAL-001**.

It establishes an executable equality contract between RI-PY and RI-RS at the JCS boundary.

It does **not** establish that every existing Aura object or every existing production hash domain is already conformant. In particular, APS-200 currently describes `integrity_hash` and `event_payload_hash` separately, while historical D-3 evidence records a different Rust `chain_hash` domain. Those questions remain separate decision work.

## 10. Closure conditions

All mandatory DQ-006 closure conditions are satisfied:

- independent RI-PY execution — PASS
- independent RI-RS execution — PASS
- canonical bytes equality — PASS
- SHA-256 equality — PASS
- RFC-6962 leaf equality — PASS
- independent recomputation — PASS
- negative controls — PASS
- production isolation — PASS
- artifact provenance — PASS

## FINAL VERDICT

```text
DQ-006 = CLOSED / PASS
```

**No production implementation change is implied by this closure.**

**Next gate:** DQ-002 final closure / remaining specification reconciliation, subject to its own evidence requirements.
