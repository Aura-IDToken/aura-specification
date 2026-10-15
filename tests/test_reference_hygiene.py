from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "check_reference_hygiene", ROOT / "scripts" / "check-reference-hygiene.py"
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load reference-hygiene checker")
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class ReferenceHygieneTests(unittest.TestCase):
    def scan(self, files: dict[str, str]) -> dict:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, content in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            return checker.scan_repository(root)

    def test_detects_missing_local_link(self) -> None:
        report = self.scan({"README.md": "[missing](docs/missing.md)"})
        self.assertEqual(len(report["broken_local_links"]), 1)
        self.assertEqual(report["broken_local_links"][0]["target"], "docs/missing.md")

    def test_detects_broken_markdown_anchor(self) -> None:
        report = self.scan({
            "README.md": "[section](target.md#does-not-exist)",
            "target.md": "# Existing section\n",
        })
        self.assertEqual(len(report["broken_anchors"]), 1)

    def test_ignores_explicit_template_placeholders(self) -> None:
        report = self.scan({
            "templates/ADR.md": (
                "[APS placeholder](../aps/APS-xxx_...) and "
                "[invariant placeholder](../invariants/INVARIANT_REGISTRY.md#inv-xxx)"
            ),
            "invariants/INVARIANT_REGISTRY.md": "# Invariant registry\n",
        })
        self.assertEqual(report["broken_local_links"], [])
        self.assertEqual(report["broken_anchors"], [])

    def test_empty_link_fails(self) -> None:
        report = self.scan({"README.md": "[empty]()" })
        self.assertEqual(len(report["empty_links"]), 1)

    def test_unapproved_system_path_fails(self) -> None:
        root_path = "/" + "home/" + "runner/work/repo/repo/file.md"
        report = self.scan({"README.md": "Path: " + root_path})
        self.assertEqual(len(report["non_portable_system_path_violations"]), 1)

    def test_known_primary_evidence_paths_are_preserved_narrowly(self) -> None:
        name = "conformance/boundary/evidence/controlled-p01-handoff/CROSS-RECEIVER-COMPARISON.txt"
        issued = "/" + "home/" + "user/aura-specification/conformance/boundary/p01/FIX-DIGEST-P01.canonical.json"
        report = self.scan({name: "Recorded path: " + issued})
        self.assertEqual(report["non_portable_system_path_violations"], [])
        self.assertEqual(len(report["preserved_primary_evidence_paths"]), 1)

    def test_duplicate_heading_anchors_are_supported(self) -> None:
        report = self.scan({
            "README.md": "[second](target.md#section-1)",
            "target.md": "# Section\n# Section\n",
        })
        self.assertEqual(report["broken_anchors"], [])


if __name__ == "__main__":
    unittest.main()
