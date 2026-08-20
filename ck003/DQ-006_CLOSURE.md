# DQ-006 — Canonical Serialization / Cross-Language Closure (SUPERSEDED POINTER)

Status: **SUPERSEDED**  
Superseded by: [`ck003/dq-006-closure/DQ-006-CLOSURE.md`](dq-006-closure/DQ-006-CLOSURE.md)  
Last Review: 2026-08-20

This file previously carried a second copy of the DQ-006 closure text. DQ-006 now has a single
canonical closure package at [`ck003/dq-006-closure/`](dq-006-closure/), which reproduces every
value this file recorded and adds the evidence index, cross-language matrix, closure criteria,
scope of proof and explicit non-closures.

| Artifact | Location |
|---|---|
| Closure record | [`dq-006-closure/DQ-006-CLOSURE.md`](dq-006-closure/DQ-006-CLOSURE.md) |
| Evidence index (`DQ006-E01` … `DQ006-E07`) | [`dq-006-closure/DQ-006_EVIDENCE_INDEX.md`](dq-006-closure/DQ-006_EVIDENCE_INDEX.md) |
| Cross-language matrix | [`dq-006-closure/DQ-006_CROSS_LANGUAGE_MATRIX.md`](dq-006-closure/DQ-006_CROSS_LANGUAGE_MATRIX.md) |
| Evidence ledger | [`dq-006-closure/CROSS-LANGUAGE-001-EVIDENCE.md`](dq-006-closure/CROSS-LANGUAGE-001-EVIDENCE.md) |
| Machine-readable manifest | [`dq-006-closure/canonical-001-evidence-manifest.json`](dq-006-closure/canonical-001-evidence-manifest.json) |

```text
DQ-006 = CLOSED / PASS
```

The architectural observation previously recorded here — that `APS-200` describes
`integrity_hash` and `event_payload_hash` separately while historical D-3 evidence records a
different Rust `chain_hash` domain — is **not** closed by DQ-006 and remains DQ-002 / hash-domain
decision work. See `ck003/dq-002-hash-domain/`.
