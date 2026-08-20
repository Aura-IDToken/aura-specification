# CROSS-LANGUAGE-001 Evidence Ledger

> **Subordinate record — reconciled 2026-08-20.** The execution evidence below is correct and
> was re-verified by recomputation. Its closing verdict line `DQ-006 = CLOSED` is superseded:
> `CROSS-LANGUAGE-001 = PASS` still stands for byte, SHA-256 and RFC 6962 leaf equality on
> CANONICAL-001, but the DQ-006 status of record is **OPEN** per
> [`closures/DQ-006_CLOSURE_PACKAGE.md`](../../closures/DQ-006_CLOSURE_PACKAGE.md).
> CANONICAL-001 is JCS-degenerate; see that record §10 (D-1).

## Fixture

`CANONICAL-001`

Canonicalization: RFC 8785 JCS  
Digest: SHA-256(canonical bytes)  
Leaf: SHA-256(`0x00 || canonical bytes`)

## RI-PY execution

Repository: `Aura-IDToken/aura-poc-a-core-v3.3`  
Execution commit: `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f`  
Evidence commit: `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e`  
Engine: `rfc8785==0.1.4`  
Environment: CPython 3.11.15 / Linux x86_64  

Actual canonical bytes length: `100`

Actual canonical bytes hex:

```text
7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d
```

SHA-256:

```text
b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
```

Leaf SHA-256:

```text
ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

Artifact path:
`conformance/corpus/canonical-001/ri-py.json`

## RI-RS execution

Repository: `Aura-IDToken/aura-guard-v1.3`  
Execution commit: `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2`  
Evidence commit: `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0`  
Engine: `serde_json_canonicalizer==0.3.2`  
Environment: rustc 1.94.1 / Linux x86_64  

Actual canonical bytes length: `100`

Actual canonical bytes hex is identical to RI-PY.

SHA-256:

```text
b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6
```

Leaf SHA-256:

```text
ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

Artifact path:
`conformance/corpus/canonical-001/ri-rs.json`

## Equality results

| Property | RI-PY | RI-RS | Equality |
|---|---|---|---|
| canonical bytes | identical 100-byte sequence | identical 100-byte sequence | PASS |
| SHA-256 | `b6c3660c…139a4e6` | `b6c3660c…139a4e6` | PASS |
| RFC 6962 leaf | `ce6b3673…648c039` | `ce6b3673…648c039` | PASS |

The equality runner performs independent recomputation from each artifact before accepting metadata equality.

## Negative controls

### A — modified canonical bytes

Temporary mutation caused the equality gate to fail.  
Expected behavior: **FAIL**  
Observed: **PASS negative-control assertion**.

### B — modified SHA-256

Temporary digest mutation caused independent SHA verification and cross-language digest equality to fail.  
Expected behavior: **FAIL**  
Observed: **PASS negative-control assertion**.

### C — wrong leaf domain

Temporary mutation from `0x00` to `0x01` caused independent leaf recomputation to fail.  
Expected behavior: **FAIL**  
Observed: **PASS negative-control assertion**.

All mutations were performed on temporary copies and were absent from the committed corpus after testing.

## Production-integrity checks

RI-PY:

```text
core/  -> unchanged
 audit/ -> unchanged
```

RI-RS:

```text
src/          -> unchanged
Cargo.toml    -> unchanged
Cargo.lock    -> unchanged
```

JCS dependencies remain in conformance-only package boundaries.

## Git provenance

The two evidence commits are GitHub-verified.

RI-PY evidence commit:
`3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e`

RI-RS evidence commit:
`420653e232cb0ff1e365edd2e4a5eb294d2bb2a0`

The evidence commits explicitly record their execution parents, engines, observed digests, independence constraints and production-integrity checks.

## Evidence classification

- **Execution evidence:** actual RI-PY / RI-RS outputs.
- **Equality evidence:** independent artifact comparison and recomputation.
- **Negative evidence:** controlled mutations rejected by the gate.
- **Integrity evidence:** production runtime unchanged.
- **Provenance evidence:** source/execution commits and artifact publication commits.

## Verdict

`CROSS-LANGUAGE-001 = PASS`

`DQ-006 = CLOSED`
