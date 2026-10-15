# CANONICAL-003 — multi-axis JCS discriminator candidate

Status: candidate / experimental / non-normative. RI-PY and RI-RS have not executed this vector. It is not closure evidence by itself. The repository already contains CANONICAL-002 as a sorting-only candidate; this vector uses a new ID instead of silently changing it or reusing an identifier.

## Artifacts

- CANONICAL-003_jcs_full_discriminator.json — fixture wrapper and protocol_object.
- CANONICAL-003_jcs_full_discriminator.expected.jcs — exact RFC 8785 bytes for /protocol_object, with no trailing LF.
- CANONICAL-003_jcs_full_discriminator.naive-python.json — compact Python json.dumps(..., sort_keys=True) baseline using ensure_ascii=True by default; intentionally non-canonical.
- CANONICAL-003_jcs_full_discriminator.manifest.json — lengths, hashes, oracle method, test dimensions and execution requirements.

## Expected values

- Canonicalized JSON Pointer: /protocol_object
- UTF-8 byte length: 577
- Canonical SHA-256: 9fb648c388c4485575d25c1d6171ba691fec51c1b433b11f4d61197bbe2a5509
- RFC 6962 leaf SHA-256: 38672ea2bd0ea87b2446efce8d4ba4adeb822e0baaecee4a54b73179198d2b3e
- Full fixture SHA-256: 1cde8282d6df99defc16b8652cb0f43a8f327c35b8f356a8612b835ed996ec73
- Naive Python baseline SHA-256: dcecce9fd0514104b6afb85d5e07abbcca7d68fbf3b062d12766cc70f3d07d68

Canonical hashes cover only exact JCS bytes of /protocol_object. No BOM, token whitespace or trailing LF is included.

## Discriminating dimensions

### Number serialization

10.0 → 10; 1e5 → 100000; 1e-6 → 0.000001; 1e-7 → 1e-7; 1e20 → 100000000000000000000; 1e21 → 1e+21; -0.0 → 0; 333333333.33333329 → 333333333.3333333.

### UTF-16 key order

Expected order: Z, a, U+10000, U+1F600, U+1FAE0, U+E000. Supplementary characters sort before U+E000 because of their UTF-16 high-surrogate code units. Python code-point sorting puts U+E000 before supplementary code points. Uppercase Z before lowercase a is coverage only and does not by itself distinguish Python sort_keys=True from JCS.

### String escaping

The vector combines control characters, quote, reverse solidus, an unescaped slash, non-ASCII text, emoji, U+2028 and U+2029. JCS uses mandated short escapes for five control characters, lowercase hexadecimal escapes for other U+0000–U+001F controls, and emits other Unicode as-is.

## Oracle and receiver contract

Generated using Node.js v20.20.2: JSON.parse, recursive key sorting using ECMAScript Array.prototype.sort, JSON.stringify and SHA-256 of exact UTF-8 output bytes. RFC 8785 specifies ECMAScript-compatible primitive serialization and UTF-16 code-unit property ordering. This oracle is separate from the Python and Rust receivers.

For RI-PY and RI-RS, record exact source commit, runtime/toolchain, input fixture SHA-256, canonical byte length/hex, canonical SHA-256, RFC 6962 leaf hash, byte equality and exit code. Do not change the oracle to match a receiver; disagreement is a failure to investigate.
