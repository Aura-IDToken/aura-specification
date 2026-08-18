#!/usr/bin/env python3
"""CROSS-LANGUAGE-002 independent comparator.

Compares two DQ-002 vector files emitted by different reference
implementations and, where a normative fixture pins a value, checks both
against the fixture rather than against each other.

The comparator imports neither implementation. It only reads JSON.

Usage:
    compare_vectors.py --a RI-PY-VECTORS.json --b RI-RS-VECTORS.json \
        [--fixture FIX-CK003-DQ002-RFC6962-EDGE-MATRIX.json] \
        [--two-leaf FIX-CK003-DQ002-RFC6962-2LEAF.json]

Exit code 0 = equal and fixture-conformant. Non-zero = divergence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from typing import Any, Dict, List, Tuple

SCHEMA = "aura/dq-002/cross-language-vectors/1"


def load(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def canonical(value: Any) -> bytes:
    """Stable byte form for digesting. Not RFC 8785 — comparison aid only."""
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def walk(prefix: str, a: Any, b: Any, diffs: List[str]) -> None:
    if type(a) is not type(b):
        diffs.append(f"{prefix}: type {type(a).__name__} != {type(b).__name__}")
        return
    if isinstance(a, dict):
        for key in sorted(set(a) | set(b)):
            if key not in a:
                diffs.append(f"{prefix}.{key}: missing in A")
            elif key not in b:
                diffs.append(f"{prefix}.{key}: missing in B")
            else:
                walk(f"{prefix}.{key}", a[key], b[key], diffs)
    elif isinstance(a, list):
        if len(a) != len(b):
            diffs.append(f"{prefix}: length {len(a)} != {len(b)}")
            return
        for i, (x, y) in enumerate(zip(a, b)):
            walk(f"{prefix}[{i}]", x, y, diffs)
    elif a != b:
        diffs.append(f"{prefix}: {a!r} != {b!r}")


def check_fixture(vectors: Dict[str, Any], fixture: Dict[str, Any], label: str) -> List[str]:
    problems: List[str] = []
    for i, expected in enumerate(fixture["leaf_hashes_hex"]):
        got = vectors["leaf_hashes_hex"][i]
        if got != expected:
            problems.append(f"{label}: leaf_hashes_hex[{i}] {got} != fixture {expected}")
    by_size = {t["tree_size"]: t for t in vectors["trees"]}
    for tree in fixture["trees"]:
        n = tree["tree_size"]
        if n not in by_size:
            problems.append(f"{label}: tree N={n} absent")
            continue
        if by_size[n]["root_hex"] != tree["root_hex"]:
            problems.append(
                f"{label}: N={n} root {by_size[n]['root_hex']} != fixture {tree['root_hex']}"
            )
        got_paths = {p["leaf_index"]: p["path_hex"] for p in by_size[n]["audit_paths"]}
        for entry in tree["audit_paths"]:
            m = entry["leaf_index"]
            if got_paths.get(m) != entry["path_hex"]:
                problems.append(f"{label}: N={n} m={m} audit path != fixture")
    return problems


def check_two_leaf(vectors: Dict[str, Any], fixture: Dict[str, Any], label: str) -> List[str]:
    exp = fixture["expected"]
    got = vectors["fixture_2leaf"]
    pairs = (
        ("leaf_a", got["leaf_a_hex"], exp["leaf_a_hash_hex"]),
        ("leaf_b", got["leaf_b_hex"], exp["leaf_b_hash_hex"]),
        ("root", got["root_hex"], exp["root_hash_hex"]),
    )
    return [f"{label}: {n} {g} != fixture {e}" for n, g, e in pairs if g != e]


def negative_controls(vectors: Dict[str, Any], label: str) -> List[str]:
    """Assert the verifier is not a constant-true function."""
    problems: List[str] = []
    saw_rejection = False
    for tree in vectors["verification_matrix"]:
        n = tree["tree_size"]
        for case in tree["cases"]:
            m = case["leaf_index"]
            if not case["valid"]:
                problems.append(f"{label}: N={n} m={m} valid proof rejected")
            if case["tampered_leaf_accepted"]:
                problems.append(f"{label}: N={n} m={m} tampered leaf accepted")
            if case["tampered_root_accepted"]:
                problems.append(f"{label}: N={n} m={m} tampered root accepted")
            if any(case["tampered_sibling_accepted"]):
                problems.append(f"{label}: N={n} m={m} tampered sibling accepted")
            if case["accepted_leaf_indices"] != [m]:
                problems.append(
                    f"{label}: N={n} m={m} accepted indices "
                    f"{case['accepted_leaf_indices']} != [{m}]"
                )
            if n not in case["accepted_tree_sizes"]:
                problems.append(f"{label}: N={n} m={m} true tree size rejected")
            if case["tampered_leaf_accepted"] is False:
                saw_rejection = True
    if not saw_rejection:
        problems.append(f"{label}: no rejection observed; verifier may be constant-true")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True, help="vector file A (e.g. RI-PY)")
    ap.add_argument("--b", required=True, help="vector file B (e.g. RI-RS)")
    ap.add_argument("--label-a", default="A")
    ap.add_argument("--label-b", default="B")
    ap.add_argument("--fixture", help="edge-matrix fixture")
    ap.add_argument("--two-leaf", help="two-leaf fixture")
    args = ap.parse_args()

    a, b = load(args.a), load(args.b)
    la, lb = args.label_a, args.label_b

    failures: List[str] = []

    for label, v in ((la, a), (lb, b)):
        if v.get("schema") != SCHEMA:
            failures.append(f"{label}: schema {v.get('schema')!r} != {SCHEMA!r}")

    diffs: List[str] = []
    walk("$", a, b, diffs)

    if args.fixture:
        fx = load(args.fixture)
        failures += check_fixture(a, fx, la) + check_fixture(b, fx, lb)
    if args.two_leaf:
        fx2 = load(args.two_leaf)
        failures += check_two_leaf(a, fx2, la) + check_two_leaf(b, fx2, lb)

    failures += negative_controls(a, la) + negative_controls(b, lb)

    digest_a = hashlib.sha256(canonical(a)).hexdigest()
    digest_b = hashlib.sha256(canonical(b)).hexdigest()

    print("CROSS-LANGUAGE-002 vector comparison")
    print(f"  {la} file            : {args.a}")
    print(f"  {lb} file            : {args.b}")
    print(f"  {la} canonical sha256: {digest_a}")
    print(f"  {lb} canonical sha256: {digest_b}")
    print(f"  structural diffs     : {len(diffs)}")
    print(f"  fixture/NC failures  : {len(failures)}")

    for line in diffs[:50]:
        print(f"  DIFF {line}")
    if len(diffs) > 50:
        print(f"  ... {len(diffs) - 50} more diffs suppressed")
    for line in failures[:50]:
        print(f"  FAIL {line}")
    if len(failures) > 50:
        print(f"  ... {len(failures) - 50} more failures suppressed")

    equal = not diffs and digest_a == digest_b
    ok = equal and not failures
    print(f"  RESULT               : {'EQUAL + CONFORMANT' if ok else 'DIVERGENT'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
