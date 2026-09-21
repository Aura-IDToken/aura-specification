# DEFECT-DQ002-F3 — RI-PY test suite cannot be collected without `--ignore`

- **Status:** OPEN — pre-existing, outside DQ-002 scope
- **Raised by:** CROSS-LANGUAGE-002 execution, 2026-08-18
- **Severity:** Evidence blocker. No DQ-002 semantic impact.
- **Repository:** Aura-IDToken/aura-poc-a-core-v3.3
- **Present at commit:** `a7f4d2a219e3153a084b74716054a0e4a4379a28` (untouched by CROSS-LANGUAGE-002)

## Statement

```
$ python3 -m pytest -q
core/test_ari_observability.py:211: in <module>
    class ARIObservabilityTest(unittest.TestCase):
E   NameError: name 'unittest' is not defined
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.24s
```

The module imports `from unittest import mock` (line 62) but references
`unittest.TestCase` (line 211). The bare name `unittest` is never bound.
Collection is interrupted, so **no test in the repository runs at all** — the
failure is not confined to this module.

## Why it matters to CROSS-LANGUAGE-002

Phase 4 requires the complete existing RI-PY suite to execute. It cannot. The
recorded run therefore used `--ignore=core/test_ari_observability.py`
(319 passed, 0 failed, 2 environmental errors). There is no repository-wide
green run to cite, which is one reason CROSS-LANGUAGE-002 is CONDITIONAL PASS
rather than PASS.

## Why it was not fixed here

The one-line fix (`import unittest`) is obvious, but the module is an ARI
observability harness with no DQ-002 relationship. Repairing it inside a
Merkle hash-domain remediation would widen the change beyond the approved
scope and mix unrelated evidence into the same commit.

## Requested resolution

1. Add the missing `import unittest` under a separate change.
2. Re-run the full RI-PY suite with no `--ignore` and record the result.
3. Add a CI gate that fails on collection errors, so a repository-wide
   collection break cannot pass unnoticed again.

## Also observed (not defects, recorded for completeness)

- `test_compliance.py` emits four `PytestReturnNotNoneWarning`s: four test
  functions `return bool` instead of asserting. A returned `False` would not
  fail the test. Pre-existing.
- `audit/test_audit_db_integration.py` and `core/test_cr003_statelessness.py`
  require a Docker daemon (`pgvector/pgvector:pg16`), unavailable on this
  runner. Those suites are NOT EXECUTED, not failed.
