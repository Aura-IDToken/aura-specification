# DEFECT-DQ002-F1 — recorded node digest in `03_cross_language_fixture.json` is wrong

- **Status:** OPEN — awaiting Protocol Custodian resolution
- **Raised by:** CROSS-LANGUAGE-002 execution, 2026-08-18
- **Severity:** Evidence defect. Non-semantic: it does not change the DQ-002 rule.
- **Artifact:** `ck003/dq-002-hash-domain/03_cross_language_fixture.json`
- **Field:** `node.digest_hex`
- **Artifact status claimed in file:** `NORMATIVE_TEST_VECTOR`

## Statement

The file declares an explicit node preimage and a digest over it. The digest
does not match the declared preimage.

| Field | Value |
| --- | --- |
| `node.input_hex` | `01` ‖ `00`×32 ‖ `ff`×32 (65 bytes, as declared) |
| `node.input_length_bytes` | 65 — **correct** |
| `node.digest_hex` (recorded) | `e2bd2dcef148b54e935fe552c7c83978103f85b2d970d55f482717bb3904b7ac` |
| SHA-256 of the declared preimage | `bc6b943b820c449acf880d293c216a24a8066b153f87f2361fae2beda3a72641` |

The recorded value is not the SHA-256 of the bytes the same file specifies.

## Independent confirmation

Three independent SHA-256 implementations agree on `bc6b943b…`:

| Producer | Value |
| --- | --- |
| GNU coreutils `sha256sum` | `bc6b943b820c449acf880d293c216a24a8066b153f87f2361fae2beda3a72641` |
| RI-PY (CPython `hashlib`) | `bc6b943b820c449acf880d293c216a24a8066b153f87f2361fae2beda3a72641` |
| RI-RS (Rust `sha2` crate) | `bc6b943b820c449acf880d293c216a24a8066b153f87f2361fae2beda3a72641` |

Reproduce with coreutils only:

```sh
perl -e 'print pack("H*", $ARGV[0])' \
  01"$(printf '0%.0s' $(seq 64))""$(printf 'f%.0s' $(seq 64))" | sha256sum
```

The other values in the same file are **correct** and were reconfirmed:

- `canonical_serialization.length_bytes` = 58 ✔
- `leaf.input_length_bytes` = 59 ✔
- `leaf.digest_hex` = `ba2749fedbcff14c1409a22c721c8de2e0f9ebd9c4177cc8b3950142b3bfd123` ✔

`fixtures/FIX-CK003-DQ002-RFC6962-2LEAF.json` was independently reconfirmed in
full and contains no defect.

## Blast radius

No executable test in RI-PY, RI-RS, or aura-specification reads
`03_cross_language_fixture.json`. The wrong digest has therefore never been
asserted against, and no implementation was built to it. Both implementations
independently produce the arithmetically correct value.

## Action NOT taken, and why

The value was **not corrected in this change.** `CLAUDE.md` requires that a
detected conflict with a normative artifact is reported rather than silently
reconciled, and the file self-designates as `NORMATIVE_TEST_VECTOR`. Editing a
normative test vector is a Protocol Custodian action, not an agent action —
even when the correction is arithmetically unambiguous.

## Requested resolution

1. Protocol Custodian confirms the arithmetic above.
2. Correct `node.digest_hex` to `bc6b943b820c449acf880d293c216a24a8066b153f87f2361fae2beda3a72641`.
3. Record how a `NORMATIVE_TEST_VECTOR` was published without an executable
   assertion binding it, and bind every published fixture value to a test.
   `FIX-CK003-DQ002-RFC6962-2LEAF.json` and
   `FIX-CK003-DQ002-RFC6962-EDGE-MATRIX.json` are now so bound; this file is
   not.
