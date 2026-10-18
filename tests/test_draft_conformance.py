from __future__ import annotations

import builtins
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]


def load_module(module_name: str, path: Path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module



def load_gate_with_missing_dependencies(module_name: str, blocked: set[str]):
    original_import = builtins.__import__

    def guarded_import(name, globals=None, locals=None, fromlist=(), level=0):
        if any(name == dependency or name.startswith(dependency + ".") for dependency in blocked):
            raise ImportError(f"simulated missing dependency: {name}")
        return original_import(name, globals, locals, fromlist, level)

    path = ROOT / "scripts" / "check-fix001-evidence.py"
    with mock.patch("builtins.__import__", side_effect=guarded_import):
        return load_module(module_name, path)


fix001 = load_module("check_fix001_evidence", ROOT / "scripts" / "check-fix001-evidence.py")
runner = load_module("run_draft_conformance", ROOT / "scripts" / "run-draft-conformance.py")


class Fix001GateTests(unittest.TestCase):
    def test_run_fix001_gate_happy_path_returns_all_conf_results(self) -> None:
        results = fix001.run_fix001_gate()
        self.assertEqual(set(results), set(fix001.FIX001_CONF_MESSAGES))

    def test_run_fix001_gate_detects_fixture_mismatch(self) -> None:
        fixture = fix001.load_json(fix001.FIXTURE_PATH)
        fixture["expected_output"]["decision"] = "DENY"

        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "bad-fix001.json"
            path.write_text(json.dumps(fixture), encoding="utf-8")
            with mock.patch.object(fix001, "FIXTURE_PATH", path):
                with self.assertRaises(AssertionError):
                    fix001.run_fix001_gate()


class DraftRunnerTests(unittest.TestCase):
    def test_build_report_summary_counts(self) -> None:
        report = runner.build_report()
        self.assertEqual(len(report["results"]), 15)
        self.assertEqual(report["summary"]["PASS"], 8)
        self.assertEqual(report["summary"]["OPEN"], 2)
        self.assertEqual(report["summary"]["BLOCKED"], 3)
        self.assertEqual(report["summary"]["READY"], 2)

    def test_build_report_conf008_failure_result(self) -> None:
        fake_fix001_results = [
            runner.make_result(conf_id, "PASS", "ok") for conf_id in runner.FIX001_CONF_IDS
        ]

        with mock.patch.object(runner, "run_fix001_results", return_value=fake_fix001_results):
            with mock.patch.object(
                runner, "run_conf008_result", side_effect=RuntimeError("boom")
            ):
                report = runner.build_report()

        conf008 = next(result for result in report["results"] if result["id"] == "CONF-008")
        self.assertEqual(conf008["status"], "FAIL")
        self.assertIn("boom", conf008["note"])
        self.assertEqual(report["summary"]["FAIL"], 1)

    def test_run_conf012_result_passes(self) -> None:
        result = runner.run_conf012_result()
        self.assertEqual(result["id"], "CONF-012")
        self.assertEqual(result["status"], "PASS")

    def test_build_report_conf012_failure_result(self) -> None:
        fake_fix001_results = [
            runner.make_result(conf_id, "PASS", "ok") for conf_id in runner.FIX001_CONF_IDS
        ]

        with mock.patch.object(runner, "run_fix001_results", return_value=fake_fix001_results):
            with mock.patch.object(
                runner, "run_conf008_result", return_value=runner.make_result("CONF-008", "PASS", "ok")
            ):
                with mock.patch.object(
                    runner, "run_conf012_result", side_effect=RuntimeError("audit boom")
                ):
                    report = runner.build_report()

        conf012 = next(result for result in report["results"] if result["id"] == "CONF-012")
        self.assertEqual(conf012["status"], "FAIL")
        self.assertIn("audit boom", conf012["note"])

    def test_run_fix001_results_failure_is_reported_as_failures(self) -> None:
        failing_gate = mock.Mock()
        failing_gate.run_fix001_gate.side_effect = RuntimeError("fix001 boom")

        with mock.patch.object(runner, "load_fix001_gate_module", return_value=failing_gate):
            results = runner.run_fix001_results()

        self.assertEqual({result["status"] for result in results}, {"FAIL"})
        self.assertEqual({result["id"] for result in results}, set(runner.FIX001_CONF_IDS))
        self.assertTrue(all("fix001 boom" in result["note"] for result in results))


class Fix001DependencyTests(unittest.TestCase):
    def test_import_with_both_dependencies_available(self) -> None:
        gate = load_gate_with_missing_dependencies("gate_deps_available", set())
        self.assertIsNotNone(gate.jcs)
        self.assertIsNotNone(gate.Draft202012Validator)
        gate.require_runtime_dependencies()

    def test_import_without_jcs_and_gate_fails_without_pass_output(self) -> None:
        gate = load_gate_with_missing_dependencies("gate_without_jcs", {"jcs"})
        self.assertIsNone(gate.jcs)
        self.assertIsNotNone(gate.Draft202012Validator)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            with self.assertRaisesRegex(RuntimeError, "Missing dependency: jcs"):
                gate.run_fix001_gate()
        self.assertNotIn("PASS", output.getvalue())

    def test_import_without_jsonschema_and_gate_fails_without_pass_output(self) -> None:
        gate = load_gate_with_missing_dependencies("gate_without_jsonschema", {"jsonschema"})
        self.assertIsNotNone(gate.jcs)
        self.assertIsNone(gate.Draft202012Validator)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            with self.assertRaisesRegex(RuntimeError, "Missing dependency: jsonschema"):
                gate.run_fix001_gate()
        self.assertNotIn("PASS", output.getvalue())

    def test_import_without_both_dependencies_and_gate_fails_without_pass_output(self) -> None:
        gate = load_gate_with_missing_dependencies(
            "gate_without_both_dependencies", {"jcs", "jsonschema"}
        )
        self.assertIsNone(gate.jcs)
        self.assertIsNone(gate.Draft202012Validator)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            with self.assertRaisesRegex(RuntimeError, "jcs and/or jsonschema"):
                gate.run_fix001_gate()
        self.assertNotIn("PASS", output.getvalue())


class Fix001MutationTests(unittest.TestCase):
    def test_hash_mutation_changes_digest_even_when_first_character_is_f(self) -> None:
        original = "f" + ("a" * 63)
        mutated = fix001.mutate_hash_first_character(original)
        self.assertNotEqual(mutated, original)
        self.assertEqual(len(mutated), 64)
        self.assertRegex(mutated, r"^[0-9a-f]{64}$")
        self.assertEqual(mutated[1:], original[1:])

    def test_hash_mutation_changes_digest_when_first_character_is_zero(self) -> None:
        original = "0" + ("b" * 63)
        mutated = fix001.mutate_hash_first_character(original)
        self.assertNotEqual(mutated, original)
        self.assertEqual(mutated[0], "1")
        self.assertEqual(mutated[1:], original[1:])

    def test_mutation_detection_changes_hash_that_starts_with_f(self) -> None:
        original_hash = "f" + ("a" * 63)
        fixture = {
            "expected_evidence": {
                "evidence_object": {"output_hash": original_hash}
            }
        }
        seen_hashes: list[str] = []

        def verify_mutated_fixture(mutated: dict) -> None:
            new_hash = mutated["expected_evidence"]["evidence_object"]["output_hash"]
            seen_hashes.append(new_hash)
            self.assertNotEqual(new_hash, original_hash)
            raise AssertionError("simulated integrity mismatch")

        with mock.patch.object(fix001, "verify_pack_hashes", side_effect=verify_mutated_fixture):
            fix001.verify_mutation_detection(fixture)

        self.assertEqual(len(seen_hashes), 1)
        self.assertEqual(fixture["expected_evidence"]["evidence_object"]["output_hash"], original_hash)

    def test_hash_mutation_rejects_empty_digest(self) -> None:
        with self.assertRaisesRegex(ValueError, "must not be empty"):
            fix001.mutate_hash_first_character("")


if __name__ == "__main__":
    unittest.main()
