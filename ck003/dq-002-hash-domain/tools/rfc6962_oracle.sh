#!/usr/bin/env bash
#
# DQ-002 independent RFC 6962 oracle.
#
# PURPOSE
#   Produce Merkle Tree Hash (MTH) and audit-path values for the DQ-002
#   normative hash domain using a toolchain that shares no code with either
#   reference implementation:
#
#     * SHA-256      : GNU coreutils `sha256sum`
#     * hex <-> bytes: perl `pack`/`unpack` (no cryptographic role)
#     * tree logic   : this script
#
#   RI-PY uses CPython `hashlib`; RI-RS uses the pure-Rust `sha2` crate. This
#   oracle is therefore a third, independent producer of expected values. It
#   exists so that cross-language equality is asserted against externally
#   specified values rather than against either implementation's own output.
#
# CONTRACT (DQ-002 / ADR-CK003-DQ002-HASH-DOMAIN)
#   leaf  : SHA-256(0x00 || leaf_data_bytes)
#   node  : SHA-256(0x01 || left_digest_raw_32 || right_digest_raw_32)
#   empty : SHA-256("")
#   shape : RFC 6962 recursive split at the largest power of two strictly < n
#           A single unpaired node is promoted unchanged. No duplication.
#
# STATUS
#   EVIDENCE TOOL. This script does not define protocol rules; it recomputes
#   the rules stated in the approved-pending ADR. It is deterministic and
#   performs no network access.
#
# USAGE
#   ./rfc6962_oracle.sh            # emit the DQ-002 edge-case matrix as JSON
#   ./rfc6962_oracle.sh selftest   # verify against the 2-leaf normative fixture

set -euo pipefail
export LC_ALL=C

# ---------------------------------------------------------------- primitives

# sha256 over the bytes described by a lowercase hex string (may be empty).
sha256hex() {
  perl -e 'print pack("H*", $ARGV[0])' "$1" | sha256sum | cut -d' ' -f1
}

# lowercase hex of a UTF-8 string argument
tohex() {
  perl -e 'print unpack("H*", $ARGV[0])' "$1"
}

leaf_hash_hex() { sha256hex "00$1"; }          # $1 = data hex
node_hash_hex() { sha256hex "01$1$2"; }        # $1,$2 = 32-byte digest hex

# ---------------------------------------------------------------- tree shape

# largest power of two strictly less than n (n >= 2)
lpo2lt() {
  local n=$1 k=1
  while [ $((k * 2)) -lt "$n" ]; do k=$((k * 2)); done
  echo "$k"
}

# LEAVES is a global array of leaf-hash hex strings.
declare -a LEAVES=()

# mth START END  -> Merkle Tree Hash of LEAVES[START..END)
mth() {
  local s=$1 e=$2 n=$(( $2 - $1 ))
  if [ "$n" -eq 0 ]; then sha256hex ""; return; fi
  if [ "$n" -eq 1 ]; then echo "${LEAVES[$s]}"; return; fi
  local k l r
  k=$(lpo2lt "$n")
  l=$(mth "$s" $((s + k)))
  r=$(mth $((s + k)) "$e")
  node_hash_hex "$l" "$r"
}

# apath M START END -> audit path for absolute leaf index M, one hex per line
apath() {
  local m=$1 s=$2 e=$3 n=$(( $3 - $2 ))
  [ "$n" -le 1 ] && return 0
  local k
  k=$(lpo2lt "$n")
  if [ $((m - s)) -lt "$k" ]; then
    apath "$m" "$s" $((s + k))
    mth $((s + k)) "$e"
  else
    apath "$m" $((s + k)) "$e"
    mth "$s" $((s + k))
  fi
}

# ---------------------------------------------------------------- self test

selftest() {
  local a b root fail=0
  a=$(leaf_hash_hex "$(tohex a)")
  b=$(leaf_hash_hex "$(tohex b)")
  root=$(node_hash_hex "$a" "$b")
  check() {
    if [ "$2" = "$3" ]; then
      echo "ok   $1 = $2"
    else
      echo "FAIL $1"; echo "  got      $2"; echo "  expected $3"; fail=1
    fi
  }
  check leaf_a "$a" 022a6979e6dab7aa5ae4c3e5e45f7e977112a7e63593820dbec1ec738a24f93c
  check leaf_b "$b" 57eb35615d47f34ec714cacdf5fd74608a5e8e102724e80b24b287c0c27b6a31
  check root   "$root" b137985ff484fb600db93107c77b0365c80d78f5b429ded0fd97361d077999eb
  check empty  "$(sha256hex '')" e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  return $fail
}

# ---------------------------------------------------------------- emit matrix

# Leaf payloads are the ASCII strings leaf-0 .. leaf-7.
emit() {
  local sizes=(0 1 2 3 4 5 6 7 8)
  local maxn=8
  local -a payload_hex=()
  local i
  for ((i = 0; i < maxn; i++)); do payload_hex+=("$(tohex "leaf-$i")"); done

  printf '{\n'
  printf '  "fixture_id": "FIX-CK003-DQ002-RFC6962-EDGE-MATRIX",\n'
  printf '  "fixture_version": "0.1.0",\n'
  printf '  "status": "PROPOSED",\n'
  printf '  "hash_domain": "RFC6962",\n'
  printf '  "generator": "ck003/dq-002-hash-domain/tools/rfc6962_oracle.sh (coreutils sha256sum)",\n'
  printf '  "rules": {\n'
  printf '    "leaf_hash": "SHA-256(0x00 || raw_leaf_bytes)",\n'
  printf '    "node_hash": "SHA-256(0x01 || left_hash_bytes || right_hash_bytes)",\n'
  printf '    "empty_root": "SHA-256(\\"\\")",\n'
  printf '    "odd_leaf_handling": "RFC6962 recursive promotion; no duplication"\n'
  printf '  },\n'
  printf '  "leaf_payloads_utf8": ['
  for ((i = 0; i < maxn; i++)); do
    [ "$i" -gt 0 ] && printf ', '
    printf '"leaf-%d"' "$i"
  done
  printf '],\n'
  printf '  "leaf_hashes_hex": [\n'
  for ((i = 0; i < maxn; i++)); do
    LEAVES[$i]=$(leaf_hash_hex "${payload_hex[$i]}")
    printf '    "%s"%s\n' "${LEAVES[$i]}" "$([ $i -lt $((maxn - 1)) ] && echo , || echo '')"
  done
  printf '  ],\n'
  printf '  "trees": [\n'

  local first_tree=1 n
  for n in "${sizes[@]}"; do
    [ "$first_tree" -eq 0 ] && printf ',\n'
    first_tree=0
    printf '    {\n'
    printf '      "tree_size": %d,\n' "$n"
    printf '      "root_hex": "%s",\n' "$(mth 0 "$n")"
    printf '      "audit_paths": ['
    if [ "$n" -eq 0 ]; then
      printf ']\n'
    else
      printf '\n'
      local m first_p=1
      for ((m = 0; m < n; m++)); do
        [ "$first_p" -eq 0 ] && printf ',\n'
        first_p=0
        printf '        { "leaf_index": %d, "path_hex": [' "$m"
        local step first_s=1
        while read -r step; do
          [ -z "$step" ] && continue
          [ "$first_s" -eq 0 ] && printf ', '
          first_s=0
          printf '"%s"' "$step"
        done < <(apath "$m" 0 "$n")
        printf '] }'
      done
      printf '\n      ]\n'
    fi
    printf '    }'
  done
  printf '\n  ]\n}\n'
}

case "${1:-emit}" in
  selftest) selftest ;;
  emit)     emit ;;
  *) echo "usage: $0 [emit|selftest]" >&2; exit 2 ;;
esac
