#!/usr/bin/env python3
"""Audit repository-local Markdown references and non-portable system paths.

This structural checker does not evaluate external HTTP URLs or normative status.
It preserves narrowly allowlisted historical execution-log paths rather than
rewriting primary evidence records.
"""

from __future__ import annotations

import argparse
import collections
import html
import json
import posixpath
import re
import sys
import urllib.parse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {
    ".md", ".markdown", ".rst", ".txt", ".yml", ".yaml", ".toml",
    ".json", ".py", ".sh", ".xml", ".ini", ".cfg", ".csv",
}
TEXT_FILENAMES = {".gitignore", ".gitattributes", ".editorconfig", "CODEOWNERS", "Dockerfile"}
EXCLUDED_DIRS = {".git", ".venv", ".tox", "node_modules", "__pycache__"}

# These values occur only in the named primary execution logs. Keep the
# allowlist exact so a new path, or the same path elsewhere, fails the check.
_ISSUED_FIXTURE = "/" + "home/" + "user/aura-specification/conformance/boundary/p01/FIX-DIGEST-P01.canonical.json"
_PY_RECEIPT = "/" + "home/" + "user/aura-specification/conformance/boundary/evidence/controlled-p01-handoff/RI-PY-P01-RECEIPT.json"
_RS_RECEIPT = "/" + "home/" + "user/aura-specification/conformance/boundary/evidence/controlled-p01-handoff/RI-RS-P01-RECEIPT.json"
PRESERVED_EVIDENCE_PATHS = {
    "conformance/boundary/evidence/controlled-p01-handoff/CROSS-RECEIVER-COMPARISON.txt": {_ISSUED_FIXTURE},
    "conformance/boundary/evidence/controlled-p01-handoff/RI-PY-P01-EXECUTION-LOG.txt": {_ISSUED_FIXTURE, _PY_RECEIPT},
    "conformance/boundary/evidence/controlled-p01-handoff/RI-RS-P01-EXECUTION-LOG.txt": {_ISSUED_FIXTURE, _RS_RECEIPT},
}

# Assemble absolute-path prefixes from fragments so the checker does not
# discover its own pattern literals as violations.
_SYSTEM_PREFIX = (
    re.escape("/" + "home/")
    + r"(?:runner/work|user|oai|ubuntu|vscode)/|/"
    + r"(?:app|workspace|workspaces|tmp|mnt/data|root|opt)/"
)
SYSTEM_PATH_RE = re.compile(
    r"(?<![A-Za-z0-9])(?P<path>(?:" + _SYSTEM_PREFIX + r")[A-Za-z0-9_./\\-]+)"
)
WINDOWS_PATH_RE = re.compile(
    r"(?<![A-Za-z0-9])[A-Za-z]:\\(?:Users|workspaces|workspace|aura)\\[A-Za-z0-9_ .\\-]+",
    re.IGNORECASE,
)
EXTERNAL_SCHEME_RE = re.compile(r"(?i)^(?:https?|mailto|tel|data|javascript|ftp|urn|vscode):")
INLINE_LINK_RE = re.compile(r"!?\[[^\]]*\]\(\s*(?:<([^>\n]*)>|([^\s)]+))?[^)]*\)")
REFERENCE_DEF_RE = re.compile(r"(?m)^\s{0,3}\[([^\]]+)\]:\s*(?:<([^>\n]*)>|(\S+))?\s*$")
HTML_ATTR_RE = re.compile(r"(?i)\b(?:href|src)\s*=\s*([\"'])(.*?)\1")
REFERENCE_USE_RE = re.compile(r"!?\[([^\]]+)\]\[([^\]]*)\]")
HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
TICK = chr(96)


def _strip_fenced_blocks(source: str) -> str:
    """Blank fenced code blocks while preserving line numbers."""
    output = []
    fence_char = None
    fence_size = 0
    opener_re = re.compile(r"^\s{0,3}([" + re.escape(TICK) + r"~]{3,})")
    for line in source.splitlines(keepends=True):
        candidate = opener_re.match(line)
        if fence_char is None and candidate:
            token = candidate.group(1)
            fence_char, fence_size = token[0], len(token)
            output.append("\n" if line.endswith("\n") else "")
            continue
        if fence_char is not None:
            close = re.match(r"^\s{0,3}([" + re.escape(fence_char) + r"]+)\s*$", line.rstrip("\\r\n"))
            if close and len(close.group(1)) >= fence_size:
                fence_char, fence_size = None, 0
            output.append("\n" if line.endswith("\n") else "")
            continue
        output.append(line)
    return "".join(output)


def _blank_inline_code(source: str) -> str:
    tick = re.escape(TICK)
    pattern = re.compile(r"(?<!" + tick + r")" + tick + r"+[^" + tick + r"\n]*" + tick + r"+(?!"+tick+r")")
    return pattern.sub(lambda match: re.sub(r"[^\n]", " ", match.group(0)), source)


def _slug_heading(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"!??\[([^\]]+)\]\([^)]*\)", r"\\1", text)
    text = re.sub(r"\[([^\]]+)\]\[[^\]]*\]", r"\\1", text)
    tick = re.escape(TICK)
    text = re.sub(tick + r"+([^" + tick + r"]*)" + tick + r"+", r"\\1", text)
    text = html.unescape(text).strip().lower().replace(" ", "-")
    return re.sub(r"[^\w-]", "", text, flags=re.UNICODE)


def _anchors_for(source: str) -> set[str]:
    cleaned = _strip_fenced_blocks(source)
    anchors = set()
    counts = collections.Counter()
    for line in cleaned.splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = _slug_heading(match.group(2))
        counts[base] += 1
        anchors.add(base if counts[base] == 1 else f"{base}-{counts[base] - 1}")
    for match in re.finditer(r"(?i)\b(?:id|name)\s*=\s*[\\\"']([^\\\"']+)[\\\"']", cleaned):
        anchors.add(html.unescape(match.group(1)))
    return anchors


def _is_placeholder(target: str, fragment: str = "") -> bool:
    combined = (target + "#" + fragment).lower()
    return "xxx" in combined or "..." in combined or "<placeholder>" in combined


def _is_external(target: str) -> bool:
    return target.startswith("//") or bool(EXTERNAL_SCHEME_RE.match(target))


def _link_targets(source_path: str, source: str):
    cleaned = _strip_fenced_blocks(source)
    cleaned = re.sub(r"(?s)<!--.*?-->", lambda match: "\n" * match.group(0).count("\n"), cleaned)
    cleaned = _blank_inline_code(cleaned)
    for match in INLINE_LINK_RE.finditer(cleaned):
        target = match.group(1) if match.group(1) is not None else match.group(2)
        yield target, cleaned.count("\n", 0, match.start()) + 1, "markdown-inline", match.group(0)[:180]
    for match in REFERENCE_DEF_RE.finditer(cleaned):
        target = match.group(2) if match.group(2) is not None else match.group(3)
        yield target, cleaned.count("\n", 0, match.start()) + 1, "markdown-reference-definition", match.group(0)[:180]
    for match in HTML_ATTR_RE.finditer(cleaned):
        yield match.group(2), cleaned.count("\n", 0, match.start()) + 1, "html-attribute", match.group(0)[:180]


def _normal_path(path_text: str, source_path: str) -> str:
    path_text = urllib.parse.unquote(path_text)
    if path_text.startswith("/"):
        return path_text.lstrip("/")
    return posixpath.normpath(posixpath.join(posixpath.dirname(source_path), path_text))


def _collect_paths(root: Path):
    files = []
    entries = set()
    for item in root.rglob("*"):
        relative = item.relative_to(root).as_posix()
        parts = Path(relative).parts
        if any(part in EXCLUDED_DIRS for part in parts):
            continue
        entries.add(relative)
        if item.is_file() and (item.suffix.lower() in TEXT_SUFFIXES or item.name in TEXT_FILENAMES):
            files.append(relative)
    return sorted(files), entries


def _path_exists(candidate: str, entries: set[str]) -> str | None:
    if candidate in entries:
        return candidate
    if candidate.endswith("/"):
        for index_name in ("README.md", "index.md", "README.markdown", "index.html"):
            name = candidate + index_name
            if name in entries:
                return name
    return None


def scan_repository(root: Path = ROOT) -> dict:
    root = Path(root).resolve()
    paths, entries = _collect_paths(root)
    contents = {}
    read_errors = []
    for relative in paths:
        try:
            contents[relative] = (root / relative).read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        except OSError as exc:
            read_errors.append({"file": relative, "error": str(exc)})

    markdown_paths = [p for p in contents if p.lower().endswith((".md", ".markdown"))]
    anchors_cache = {}
    broken_links = []
    broken_anchors = []
    empty_links = []
    undefined_references = []
    placeholders_ignored = 0
    links_checked = 0
    external_links_skipped = 0

    for source_path in markdown_paths:
        source = contents[source_path]
        cleaned = _blank_inline_code(_strip_fenced_blocks(source))
        definitions = {}
        for match in REFERENCE_DEF_RE.finditer(cleaned):
            key = match.group(1).strip().lower()
            value = match.group(2) if match.group(2) is not None else match.group(3)
            definitions[key] = value
        for label, explicit in REFERENCE_USE_RE.findall(cleaned):
            key = (explicit or label).strip().lower()
            if key not in definitions:
                undefined_references.append({
                    "file": source_path,
                    "line": cleaned.count("\n", 0, cleaned.find("[" + label + "]")) + 1,
                    "target": key,
                })

        for target, line, kind, evidence in _link_targets(source_path, source):
            links_checked += 1
            if target is None or not target.strip():
                empty_links.append({"file": source_path, "line": line, "kind": kind, "evidence": evidence})
                continue
            target = target.strip().strip("<>")
            if not target:
                empty_links.append({"file": source_path, "line": line, "kind": kind, "evidence": evidence})
                continue
            if _is_external(target):
                external_links_skipped += 1
                continue
            parsed = urllib.parse.urlsplit(target)
            path_text, fragment = parsed.path, urllib.parse.unquote(parsed.fragment)
            if _is_placeholder(target, fragment):
                placeholders_ignored += 1
                continue
            resolved = source_path if not path_text else _normal_path(path_text, source_path)
            found = _path_exists(resolved, entries)
            if found is None and path_text:
                found = _path_exists(urllib.parse.unquote(path_text).lstrip("/"), entries)
            if found is None:
                broken_links.append({
                    "file": source_path, "line": line, "target": target,
                    "resolved_candidate": resolved, "kind": kind, "evidence": evidence,
                })
                continue
            if fragment and found.lower().endswith((".md", ".markdown")) and found in contents:
                if found not in anchors_cache:
                    anchors_cache[found] = _anchors_for(contents[found])
                if fragment not in anchors_cache[found] and fragment.lower() not in {
                    item.lower() for item in anchors_cache[found]
                }:
                    broken_anchors.append({
                        "file": source_path, "line": line, "target": target,
                        "target_file": found, "fragment": fragment,
                    })

    system_path_findings = []
    system_path_violations = []
    for relative, source in contents.items():
        for regex in (SYSTEM_PATH_RE, WINDOWS_PATH_RE):
            for match in regex.finditer(source):
                literal = match.groupdict().get("path", match.group(0)).rstrip(".,;:")
                finding = {
                    "file": relative,
                    "line": source.count("\n", 0, match.start()) + 1,
                    "path": literal,
                }
                if literal in PRESERVED_EVIDENCE_PATHS.get(relative, set()):
                    system_path_findings.append({**finding, "classification": "preserved-primary-execution-evidence"})
                else:
                    system_path_violations.append({**finding, "classification": "non-portable-system-path"})

    return {
        "root": str(root),
        "files_scanned": len(contents),
        "markdown_files_scanned": len(markdown_paths),
        "markdown_link_destinations_checked": links_checked,
        "external_links_not_http_checked": external_links_skipped,
        "intentional_template_placeholders_ignored": placeholders_ignored,
        "empty_links": empty_links,
        "broken_local_links": broken_links,
        "broken_anchors": broken_anchors,
        "undefined_reference_links": undefined_references,
        "non_portable_system_path_violations": system_path_violations,
        "preserved_primary_evidence_paths": system_path_findings,
        "read_errors": read_errors,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root to scan (defaults to this checkout).")
    parser.add_argument("--json-out", type=Path, help="Optional path for a machine-readable JSON report.")
    args = parser.parse_args(argv)

    report = scan_repository(args.root)
    if args.json_out:
        output = args.json_out if args.json_out.is_absolute() else args.root / args.json_out
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    failures = (
        report["empty_links"]
        + report["broken_local_links"]
        + report["broken_anchors"]
        + report["undefined_reference_links"]
        + report["non_portable_system_path_violations"]
        + report["read_errors"]
    )
    print(
        "Reference hygiene: "
        f"files={report['files_scanned']} markdown={report['markdown_files_scanned']} "
        f"links={report['markdown_link_destinations_checked']} "
        f"empty={len(report['empty_links'])} "
        f"broken-local={len(report['broken_local_links'])} "
        f"broken-anchors={len(report['broken_anchors'])} "
        f"undefined-references={len(report['undefined_reference_links'])} "
        f"system-path-violations={len(report['non_portable_system_path_violations'])} "
        f"preserved-primary-paths={len(report['preserved_primary_evidence_paths'])}"
    )
    if failures:
        for category in (
            "empty_links", "broken_local_links", "broken_anchors",
            "undefined_reference_links", "non_portable_system_path_violations", "read_errors",
        ):
            for item in report[category]:
                print(f"FAIL {category}: {json.dumps(item, ensure_ascii=False)}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
