#!/usr/bin/env python3
"""Check an engineering prompt package for required evaluation-first files."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = ("task_signature.md", "metric.md", "golden_cases.md")
OPTIONAL_V2_FILES = ("meta_prompt.md", "module_map.md", "breakpoint_plan.md")
RAG_AGENT_MARKERS = ("rag", "agent", "retrieval", "query_rewrite", "tool")
MODULE_NAMES = ("query_rewrite", "retrieval", "reasoning", "summarization")


def count_cases(text: str) -> int:
    patterns = [
        r"(?im)^##\s+Case\s+\d+",
        r"(?im)^###\s+Case\s+\d+",
        r"(?im)^-\s*Case\s+\d+",
    ]
    return max(len(re.findall(pattern, text)) for pattern in patterns)


def has_heading(text: str, heading: str) -> bool:
    return bool(re.search(rf"(?im)^#+\s+{re.escape(heading)}\b", text))


def package_mentions_rag_or_agent(package_dir: Path) -> bool:
    haystack_parts: list[str] = []
    for path in package_dir.glob("*.md"):
        try:
            haystack_parts.append(path.read_text(encoding="utf-8-sig"))
        except UnicodeDecodeError:
            haystack_parts.append(path.read_text(errors="ignore"))
    haystack = "\n".join(haystack_parts).lower()
    return any(marker in haystack for marker in RAG_AGENT_MARKERS)


def module_has_metric(module_text: str) -> bool:
    return bool(re.search(r"(?im)^\s*-\s*Metric\s*:", module_text)) or has_heading(module_text, "Metric")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_prompt_package.py <package-dir>", file=sys.stderr)
        return 2

    package_dir = Path(sys.argv[1]).expanduser().resolve()
    if not package_dir.is_dir():
        print(f"FAIL: package directory does not exist: {package_dir}")
        return 1

    failures: list[str] = []
    for name in REQUIRED_FILES:
        path = package_dir / name
        if not path.is_file():
            failures.append(f"missing {name}")
        elif not path.read_text(encoding="utf-8").strip():
            failures.append(f"empty {name}")

    golden_path = package_dir / "golden_cases.md"
    if golden_path.is_file():
        cases = count_cases(golden_path.read_text(encoding="utf-8-sig"))
        if cases < 10:
            failures.append(f"golden_cases.md has {cases} cases; draft at least 10")
        if cases < 50:
            print(f"WARN: golden_cases.md has {cases} cases; production target is 50")

    for name in OPTIONAL_V2_FILES:
        path = package_dir / name
        if path.is_file() and not path.read_text(encoding="utf-8-sig").strip():
            failures.append(f"empty {name}")

    has_any_v2 = any((package_dir / name).is_file() for name in OPTIONAL_V2_FILES)
    if not has_any_v2:
        print("WARN: no v2 files found: meta_prompt.md, module_map.md, or breakpoint_plan.md")

    if package_mentions_rag_or_agent(package_dir):
        module_path = package_dir / "module_map.md"
        if not module_path.is_file():
            failures.append("RAG/Agent package mentions retrieval or agents but is missing module_map.md")
        else:
            module_text = module_path.read_text(encoding="utf-8-sig")
            lower_module_text = module_text.lower()
            for module_name in MODULE_NAMES:
                if module_name not in lower_module_text:
                    failures.append(f"module_map.md missing {module_name} module")
                    continue
                match = re.search(
                    rf"(?is){re.escape(module_name)}(.*?)(?=\n#+\s+\w|\n##\s+\w|$)",
                    module_text,
                )
                if match and not module_has_metric(match.group(1)):
                    failures.append(f"module_map.md {module_name} module missing metric")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("OK: prompt package has required files and at least 10 golden cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
