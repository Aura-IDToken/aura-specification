#!/usr/bin/env python3
"""Check that exactly one document defines the canonical serialization profile.

Classification: TEST. This script is not normative and defines nothing.

CK-003 requires a single authoritative normative canonicalization contract. The
failure mode it guards against is a second document in the *normative* corpus
that defines the profile independently, so that two sources of truth drift apart.

Rule enforced
-------------
Within the normative corpus (``aps/``, ``specification/``, ``invariants/``,
``conformance/``):

* Exactly one document may carry the authority marker
  ``single authoritative source of`` together with a mention of RFC 8785. That
  document is the definition site.
* Every other document that mentions RFC 8785 or JCS MUST cite ``APS-200 §8``
  somewhere in the document, attributing the profile to its authority rather than
  standing as an independent definition of it.

Documents outside the normative corpus (``ck003/``, ``closures/``, ``evidence/``,
``docs/``, ``fixtures/``) are evidence, decision or working artifacts and are not
checked here; their subordination is recorded in their own classification
headers.

Exit code 0 on success, 1 on any failure.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NORMATIVE_DIRS = ("aps", "specification", "invariants", "conformance")
PROFILE_RE = re.compile(r"RFC\s*8785|\bJCS\b")
AUTHORITY_RE = re.compile(r"APS-200\s*§\s*8")
MARKER = "single authoritative source of"


def main() -> int:
    definition_sites: list[Path] = []
    violations: list[str] = []

    paths = sorted(
        p
        for d in NORMATIVE_DIRS
        for p in (ROOT / d).rglob("*.md")
    )

    for path in paths:
        text = path.read_text(encoding="utf-8")
        if not PROFILE_RE.search(text):
            continue

        rel = path.relative_to(ROOT)
        if MARKER in text:
            definition_sites.append(rel)
            continue

        if not AUTHORITY_RE.search(text):
            first = next(
                (
                    (number, line)
                    for number, line in enumerate(text.splitlines(), start=1)
                    if PROFILE_RE.search(line)
                ),
                (0, ""),
            )
            violations.append(
                f"{rel}:{first[0]}: mentions the canonical serialization profile "
                f"but never cites APS-200 §8 — {first[1].strip()[:80]}"
            )

    print(f"normative documents scanned: {len(paths)}")
    print("definition site(s):")
    for site in definition_sites:
        print(f"  {site}")

    ok = True
    if len(definition_sites) != 1:
        print(
            f"\nFAIL  expected exactly 1 definition site, found "
            f"{len(definition_sites)}"
        )
        ok = False
    if violations:
        print(f"\nFAIL  {len(violations)} unattributed profile reference(s):")
        for violation in violations:
            print(f"  - {violation}")
        ok = False

    print()
    print(
        "canonicalization authority check: "
        + ("PASS — one authoritative source" if ok else "FAIL")
    )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
