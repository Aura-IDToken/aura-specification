# DQ-006 — Consolidated Evidence

**Classification:** EVIDENCE
**Status of record:** DQ-006 = **CLOSED** — authority: [`closures/DQ-006_CLOSURE_PACKAGE.md`](../../closures/DQ-006_CLOSURE_PACKAGE.md)
**Integrated:** 2026-08-20
**Scope:** conformance evidence only. No production runtime change is recorded or implied.

This record consolidates the executed evidence supporting DQ-006. It states no
normative rule: the canonical serialization contract lives in **APS-200 §8**,
the evidence-hash byte domain in **APS-300 §5**, the decision in
**ADR-CK003-DQ006**, and the conformance requirement in **CONF-003**.

Every assertion below is traceable to RI-PY execution evidence, RI-RS execution
evidence, a cross-language artifact bridge, or existing normative text. Nothing
here is inference.

---

## 1. Fixtures

DQ-006 rests on two fixtures, not one. The second exists because the first
cannot, by itself, distinguish RFC 8785 from an ordinary sorted-JSON serializer.

| Fixture | Bytes | Role | JCS-discriminating |
|---|---|---|---|
| **CANONICAL-001** | 100 | Original cross-language equality vector | **No** — degenerate |
| **CANONICAL-002** | 655 | Discriminating vector (DQ-006-R1) | **Yes** |

### 1.1 CANONICAL-001

Input:

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

Input digest: `649bb748464ce78fe1a1d7104689d2dee736fb80777db6569592bc0d3d039261`

**VERIFIED EXECUTION EVIDENCE** — produced by execution, not asserted as an expected value:

```text
canonical_bytes_hex:
7b226576656e745f74797065223a2241554449545f5245434f5244222c227061796c6f6164223a7b2276616c7565223a34327d2c2270726f746f636f6c5f76657273696f6e223a22312e30222c22736368656d615f76657273696f6e223a22312e30227d

SHA-256(canonical_bytes):
b6c3660ce6dee498b37443a92bf87c5efead6fe863fcf19197c0baeda139a4e6

RFC-6962 leaf, SHA-256(0x00 || canonical_bytes):
ce6b36733d97699230f37d80a14e14104c19d2e787526a6fc3aaae6b6648c039
```

**Known limitation.** For this object,
`json.dumps(obj, sort_keys=True, separators=(",", ":"))` produces byte-identical
output, and therefore the identical digest and leaf. A conforming RFC 8785
engine and a non-conforming sorted-JSON serializer are indistinguishable here.
CANONICAL-001 therefore evidences cross-implementation **agreement**; on its own
it does not evidence **conformance to RFC 8785**. This is why CANONICAL-002
exists.

### 1.2 CANONICAL-002

Input digest: `aee31642d0186c17daabdc910da64183567a3aa655348cc41195e4f2f7956588` (992 bytes)

Input member order is deliberately non-canonical, so an engine that echoes its
input cannot pass. The file is pure ASCII; non-ASCII characters are written as
`\u` escapes and resolved by the parser before canonicalization.

**VERIFIED EXECUTION EVIDENCE:**

```text
canonical_bytes_len: 655

SHA-256(canonical_bytes):
cdceb08100d88c81adc5a7e4f0462328071711808bc990458c0fa6b2c87d0952

RFC-6962 leaf, SHA-256(0x00 || canonical_bytes):
20fd6065aa4a21233119ad361835e43e64932e7805568947b4715a07c95b9368
```

Discriminating properties exercised, each verified in the produced bytes:

| Property | RFC 8785 result | Ordinary sorted JSON |
|---|---|---|
| Member ordering | UTF-16 code unit — `U+10000`, `U+1F600` precede `U+FB00`, `U+FFFF` | code point — the reverse |
| Non-ASCII | raw UTF-8 | `\uXXXX` |
| `1.0` | `1` | `1.0` |
| `-0.0` | `0` | `-0.0` |
| `1e-7` / `1e-6` | `1e-7` / `0.000001` | `1e-07` / `1e-06` |
| Nested members | canonicalized recursively | — |
| Array order | preserved | preserved |
| Escaping | minimal; solidus unescaped | — |

Member ordering is the sharpest case. `U+10000` encodes as the surrogate pair
`D800 DC00`, so its first UTF-16 code unit is smaller than `U+FB00` and
`U+FFFF` even though its code point is larger. RFC 8785 must sort it before
them; a code-point sort must place it after.

Sorted-JSON serialization of the same input is **716 bytes** against 655
canonical bytes — the two provably differ.

---

## 2. Cross-language evidence

### 2.1 CANONICAL-001 — gate `CROSS-LANGUAGE-001`

| Property | RI-PY | RI-RS | Equality |
|---|---|---|---|
| Engine | `rfc8785` 0.1.4 | `serde_json_canonicalizer` 0.3.2 | N/A |
| Canonical bytes | 100 B, `7b226576…22312e30227d` | identical | **PASS** |
| SHA-256 | `b6c3660c…a139a4e6` | identical | **PASS** |
| RFC-6962 leaf | `ce6b3673…6648c039` | identical | **PASS** |

### 2.2 CANONICAL-002 — gate `CROSS-LANGUAGE-CANONICAL-002`

| Property | RI-PY | RI-RS | Equality |
|---|---|---|---|
| Engine | `rfc8785` 0.1.4 | `serde_json_canonicalizer` 0.3.2 | N/A |
| Canonical bytes | 655 B | identical | **PASS** |
| SHA-256 | `cdceb081…c87d0952` | identical | **PASS** |
| RFC-6962 leaf | `20fd6065…c95b9368` | identical | **PASS** |

> **Identifier note.** The RI repositories name this gate `CROSS-LANGUAGE-002`.
> That identifier is **already assigned** in this specification to the DQ-002
> Merkle node/root/proof gate
> ([`ck003/cross-language-002/`](../cross-language-002/CROSS-LANGUAGE-002-EVIDENCE.md),
> status OPEN / CONDITIONAL PASS), which is a different gate over a different
> contract. To prevent a false reading that the Merkle gate has passed, this
> specification uses **`CROSS-LANGUAGE-CANONICAL-002`** for the CANONICAL-002
> equality gate. Renaming the RI-side identifier is recorded as an open
> follow-up in the closure package; it is a traceability defect only and
> affects no digest, no byte and no verdict.

### 2.3 Provenance

| Implementation | Repository | Execution commit | Evidence commit |
|---|---|---|---|
| RI-PY / CANONICAL-001 | `Aura-IDToken/aura-poc-a-core-v3.3` | `49d0e4f67e90a7a47e9f067bfc42ab40ee59a56f` | `3e8e0e326a1cfec71e001f4901fc1ee5b7c28c4e` |
| RI-RS / CANONICAL-001 | `Aura-IDToken/aura-guard-v1.3` | `4e9e2284ccdac6d2f40e038e33b4eaeec847aaa2` | `420653e232cb0ff1e365edd2e4a5eb294d2bb2a0` |
| RI-PY / CANONICAL-002 | `Aura-IDToken/aura-poc-a-core-v3.3` | `7bcc600f649a35f76cee5752ce597ac2b71b6d62` | `ea39a53a60336b1715abd41166348eea2ad6f52e` |
| RI-RS / CANONICAL-002 | `Aura-IDToken/aura-guard-v1.3` | `bd4a2fa6b4d11dcfb270b4a4f98b2f359ab32609` | `5685b2a74ca2fabcdbcf36c89733c42ba0141f7e` |

All eight commits were confirmed present on `origin` in their respective
repositories on 2026-08-20 and are reachable by SHA from published remote
branches. **None is merged to a default branch** — see the closure package
§13 (carried item C-1).

Each artifact records the clean-worktree commit that produced it, never its own
publication commit, so no artifact digest is self-referential. All four
artifacts record `worktree_clean: true`.

---

## 3. Independent verification

Distinguishing **engine output** from **independent verification**, as the
evidence architecture requires.

*Engine output* — the canonical bytes above, from `rfc8785` 0.1.4 and
`serde_json_canonicalizer` 0.3.2.

*Independent verification* — performed without either engine, on 2026-08-20,
from the committed corpus:

| Check | CANONICAL-001 | CANONICAL-002 |
|---|---|---|
| RI-PY bytes == RI-RS bytes | PASS | PASS |
| `SHA-256(bytes)` recomputed, matches both artifacts | PASS | PASS |
| `SHA-256(0x00 \|\| bytes)` recomputed, matches both artifacts | PASS | PASS |
| Both artifacts declare the same input digest | PASS | PASS |
| Sorted-JSON comparison | equal → **degenerate** | differs → **discriminating** |

The equality gates themselves recompute both digests from the decoded hex on
each side separately, so a mutation applied consistently to both sides cannot
pass unnoticed.

**Stated explicitly:** no fully independent third-party RFC 8785 implementation
was available. The independent basis is the two agreeing engines plus the
structural and arithmetic checks above.

---

## 4. Negative controls

Both gates were demonstrated to be discriminating. Each control copies the
committed corpus to a temporary directory, mutates the copy, and runs the real
gate against it. The committed corpus is hashed before and after and is
unchanged.

| Control | Mutation | CANONICAL-001 | CANONICAL-002 |
|---|---|---|---|
| A | canonical bytes modified | correctly FAIL | correctly FAIL |
| B | SHA-256 modified | correctly FAIL | correctly FAIL |
| C | wrong leaf domain (`0x00` → `0x01`, applied to both sides) | correctly FAIL | correctly FAIL |
| D | one side's bytes replaced by sorted-JSON output of the same input | **not detected** | correctly FAIL |

Control C is caught only by the independent leaf recomputations: because both
leaves are mutated consistently, leaf-to-leaf equality still passes.

Control D is the decisive one. Run against CANONICAL-001 the substitution is
**not detected** — the gate reports 13 passed, because sorted JSON reproduces
those canonical bytes exactly. Run against CANONICAL-002 it fails the gate.
That contrast is the executable demonstration that the corpus now distinguishes
RFC 8785 from a plausible non-conforming serializer.

The incorrect serializer used by control D is confined to the control script and
to temporary copies. It is never installed as an adapter and never written to the
committed corpus.

---

## 5. Production integrity

| Repository | Check | Result |
|---|---|---|
| RI-PY | `core/`, `audit/` | unchanged |
| RI-PY | `rfc8785` referenced outside `conformance/` | none |
| RI-RS | `src/`, `Cargo.lock` | unchanged |
| RI-RS | `serde_json_canonicalizer` placement | `[dev-dependencies]` only |
| RI-RS | `Cargo.toml` | one `[[test]]` target registration for CANONICAL-002 |

The RI-RS `Cargo.toml` delta registers a test target. It adds no dependency,
changes no lockfile, and affects neither the library nor any binary. It is
recorded here rather than omitted.

**No production hash, Merkle, event-type or protocol-semantics code was changed
by any of this work.** Both JCS engines remain conformance-scoped. DQ-006 does
not authorize introducing either engine into a production dependency graph.

---

## 6. Evidence locations

Primary execution evidence is maintained in the reference implementation
repositories, on the branches named in §2.3:

| Artifact | Path (both fixtures, `NNN` = `001` or `002`) |
|---|---|
| Fixture input | `conformance/corpus/canonical-NNN/input.json` |
| RI-PY artifact | `conformance/corpus/canonical-NNN/ri-py.json` |
| RI-RS artifact | `conformance/corpus/canonical-NNN/ri-rs.json` |
| Corpus manifest | `conformance/corpus/canonical-NNN/manifest.json` |
| Execution evidence | `conformance/corpus/canonical-NNN/EXECUTION-EVIDENCE.md` |
| Equality runner | `conformance/canonical/test_cross_language_canonical_NNN.py` |
| Negative controls | `conformance/canonical/negative_controls_canonical_NNN.py` |

Specification-side fixture records:
[`fixtures/corpus/CANONICAL-001_jcs_evidence.json`](../../fixtures/corpus/CANONICAL-001_jcs_evidence.json)
and
[`fixtures/corpus/CANONICAL-002_jcs_evidence.json`](../../fixtures/corpus/CANONICAL-002_jcs_evidence.json).

---

## 7. Governance boundary

This record documents a conformance result. It does not authorize production
runtime changes, does not close DQ-002, DQ-003 or DQ-004, and does not collapse
unrelated hash-domain decisions into DQ-006.
