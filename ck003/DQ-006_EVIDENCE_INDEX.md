# DQ-006 Evidence Index

This index binds the specification closure record to the independently executed RI-PY / RI-RS evidence.

## Repositories

| Implementation | Repository | Execution commit | Bridge commit |
|---|---|---|---|
| RI-PY | `Aura-IDToken/aura-poc-a-core-v3.3` | `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f` | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` |
| RI-RS | `Aura-IDToken/aura-guard-v1.3` | `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2` | `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0` |

## Canonical fixture

`CANONICAL-001`

Canonicalization: RFC 8785 JCS

## Observed equality

```text
canonical_bytes:
7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d

sha256:
b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6

leaf:
ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

## Artifact hashes

RI-PY artifact SHA-256:

```text
6b5b5ccd54901181b9af45421d051ea5ea53096fbf632ab1e25a66705f2b856c
```

RI-RS artifact SHA-256:

```text
a6ebad019118a7806ae927c4802a60056cb9e0c90f3cb1ef2a5e0cf359af329c
```

## Equality runner

The authoritative bridge runner is:

```text
conformance/canonical/test_cross_language_canonical_001.py
```

Negative controls:

```text
conformance/canonical/negative_controls_canonical_001.py
```

Execution evidence:

```text
conformance/corpus/canonical-001/EXECUTION-EVIDENCE.md
```

## Governance boundary

This package records a conformance result. It does not authorize production runtime changes and does not collapse unrelated hash-domain decisions into DQ-006.

## Status

```text
CROSS-LANGUAGE-001 = PASS
DQ-006            = CLOSED / PASS
DQ-002            = NOT CLOSED BY THIS PACKAGE
DQ-001            = NOT CLOSED BY THIS PACKAGE
```
