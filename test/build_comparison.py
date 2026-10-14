"""Freeze the README experiment inputs, then assemble independent skill outputs."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path


TEST = Path(__file__).resolve().parent
ROOT = TEST.parent
INPUT = TEST / "input"
OUTPUT = TEST / "output"
SOURCE = INPUT / "README.md"
MANIFEST = INPUT / "paragraphs.json"
COMPARISON = TEST / "readme-comparison.md"

FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s")
RULE = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")
ITEM = re.compile(r"^\s*(?:[-+*]|\d+[.)])\s+")
TABLE_RULE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$")


def paragraphs(text: str) -> list[dict]:
    """Extract prose, quote paragraphs, and individual list-item paragraphs."""
    lines = text.splitlines(keepends=True)
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))
    result = []
    index = 0
    while index < len(lines):
        line = lines[index]
        fence = FENCE.match(line)
        if fence:
            marker = fence.group(1)
            index += 1
            while index < len(lines):
                closing = lines[index].strip()
                index += 1
                if closing and set(closing) == {marker[0]} and len(closing) >= len(marker):
                    break
            continue
        if not line.strip() or HEADING.match(line) or RULE.match(line):
            index += 1
            continue
        if index + 1 < len(lines) and "|" in line and TABLE_RULE.match(lines[index + 1]):
            index += 2
            while index < len(lines) and lines[index].strip() and "|" in lines[index]:
                index += 1
            continue
        start = index
        index += 1
        while index < len(lines) and lines[index].strip():
            following = lines[index]
            if FENCE.match(following) or HEADING.match(following) or RULE.match(following) or ITEM.match(following):
                break
            if index + 1 < len(lines) and "|" in following and TABLE_RULE.match(lines[index + 1]):
                break
            index += 1
        original = "".join(lines[start:index]).rstrip("\r\n")
        result.append({
            "id": f"p{len(result) + 1:03d}",
            "line": start + 1,
            "start": offsets[start],
            "end": offsets[start] + len(original),
            "original": original,
        })
    return result


def prepare() -> None:
    INPUT.mkdir(parents=True, exist_ok=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    if SOURCE.exists() or MANIFEST.exists():
        raise SystemExit("Inputs already exist; refusing to overwrite experiment inputs.")
    shutil.copyfile(ROOT / "README.md", SOURCE)
    shutil.copytree(ROOT / "skills" / "zh-tech-writing", TEST / "skills" / "zh-tech-writing-zh")
    records = paragraphs(SOURCE.read_text(encoding="utf-8"))
    MANIFEST.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    metadata = {
        "source": "README.md",
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "paragraphs": len(records),
        "chinese_skill": "test/skills/zh-tech-writing-zh/SKILL.md",
        "english_skill": "test/skills/zh-tech-writing-en/SKILL.md",
    }
    (INPUT / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metadata, indent=2))


def load_run(name: str, records: list[dict]) -> dict[str, str]:
    data = json.loads((OUTPUT / f"{name}.json").read_text(encoding="utf-8"))
    # PowerShell can serialize an array container as {"value": [...], "Count": N}.
    # Unwrap that container while leaving the saved raw output and all text intact.
    if isinstance(data, dict) and set(data) == {"value", "Count"} and isinstance(data["value"], list):
        if data["Count"] != len(data["value"]):
            raise ValueError(f"{name}: inconsistent array wrapper count")
        data = data["value"]
    if not isinstance(data, list) or len(data) != len(records):
        raise ValueError(f"{name}: expected {len(records)} paragraph results")
    expected = [record["id"] for record in records]
    actual = [record.get("id") for record in data]
    if actual != expected:
        raise ValueError(f"{name}: paragraph IDs must occur once each, in source order")
    revisions = {}
    for record, entry in zip(records, data, strict=True):
        revision = entry.get("text")
        if not isinstance(revision, str) or not revision.strip():
            raise ValueError(f"{name}: empty result for {record['id']}")
        if "\n\n" in revision.replace("\r\n", "\n"):
            raise ValueError(f"{name}: split paragraph {record['id']}")
        before_links = re.findall(r"\]\(([^)]+)\)", record["original"])
        after_links = re.findall(r"\]\(([^)]+)\)", revision)
        if before_links != after_links:
            raise ValueError(f"{name}: changed link targets in {record['id']}")
        before_code = re.findall(r"`([^`]+)`", record["original"])
        after_code = re.findall(r"`([^`]+)`", revision)
        if before_code != after_code:
            raise ValueError(f"{name}: changed inline code in {record['id']}")
        revisions[record["id"]] = revision
    return revisions


def cell(text: str) -> str:
    # Keep Markdown links and inline code, and prevent nested table delimiters.
    return text.replace("|", "&#124;").replace("\r\n", "\n").replace("\n", "<br>")


def assemble() -> None:
    records = json.loads(MANIFEST.read_text(encoding="utf-8"))
    source = SOURCE.read_text(encoding="utf-8")
    runs = {name: load_run(name, records) for name in ("chinese", "english")}
    for name, revisions in runs.items():
        revised = source
        for record in reversed(records):
            revised = revised[:record["start"]] + revisions[record["id"]] + revised[record["end"]:]
        (OUTPUT / f"README.{name}.md").write_text(revised, encoding="utf-8")
    intro = [
        "# README skill-language comparison",
        "",
        "Both runs used the same frozen README and equivalent skill rules, including identical Chinese examples. "
        "The skill instructions and reference explanations are Chinese in one run and English in the other. "
        "Each run used a fresh agent with the same inherited model and reasoning settings, without conversation history or access to the other run's output. "
        "There is one run per language; this comparison does not establish a statistically reliable winner.",
        "",
        "Each row corresponds to one source paragraph, including quote paragraphs and individual list items. "
        "Paragraph boundaries were held fixed. Headings, fenced code, and example tables were preserved in the complete rewritten READMEs under `output/`. "
        "Quoted counterexamples were retained as teaching examples. Formatting was checked manually; autocorrect was not run in either condition.",
        "",
        "Inputs: `input/README.md`, `input/paragraphs.json`, `skills/zh-tech-writing-zh/`, and `skills/zh-tech-writing-en/`. "
        "Raw independent results: `output/chinese.json` and `output/english.json`. "
        "Runner settings and frozen skill hashes are recorded in [metadata](input/metadata.json). "
        "Local Markdown link targets in table cells are preserved from the source and therefore resolve relative to the original README location.",
        "",
        "The English run saved its JSON array inside a PowerShell `value`/`Count` wrapper. "
        "The assembler unwraps that container without editing paragraph text; the raw output file is retained.",
        "",
        "| Original text | CHN skill | English skill |",
        "| --- | --- | --- |",
    ]
    for record in records:
        values = [record["original"], runs["chinese"][record["id"]], runs["english"][record["id"]]]
        intro.append("| " + " | ".join(cell(value) for value in values) + " |")
    COMPARISON.write_text("\n".join(intro) + "\n", encoding="utf-8")
    for name, revisions in runs.items():
        changed = sum(revisions[record["id"]] != record["original"] for record in records)
        print(f"{name}: {len(records)} paragraphs, {changed} changed")
    print(f"Wrote {COMPARISON.relative_to(ROOT)}")


def verify() -> None:
    metadata = json.loads((INPUT / "metadata.json").read_text(encoding="utf-8"))
    digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if digest != metadata["source_sha256"] or SOURCE.read_bytes() != (ROOT / "README.md").read_bytes():
        raise ValueError("The frozen or working README has changed since input preparation")
    for relative, expected in metadata.get("skill_file_sha256", {}).items():
        if hashlib.sha256((TEST / relative).read_bytes()).hexdigest() != expected:
            raise ValueError(f"Frozen skill changed: {relative}")
    chinese = TEST / "skills" / "zh-tech-writing-zh"
    english = TEST / "skills" / "zh-tech-writing-en"
    for original in sorted(chinese.rglob("*.md")):
        relative = original.relative_to(chinese)
        if original.read_bytes() != (ROOT / "skills" / "zh-tech-writing" / relative).read_bytes():
            raise ValueError(f"Original Chinese skill changed: {relative}")
        translated = english / relative
        before = original.read_text(encoding="utf-8")
        after = translated.read_text(encoding="utf-8")
        for label, pattern in (
            ("link targets", r"\]\(([^)]+)\)"),
            ("inline code", r"(?<!`)`([^`\n]+)`(?!`)"),
            ("fenced examples", r"```[^\n]*\n(.*?)```"),
        ):
            if re.findall(pattern, before, re.DOTALL) != re.findall(pattern, after, re.DOTALL):
                raise ValueError(f"English skill changed {label}: {relative}")
    records = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for record in records:
        if SOURCE.read_text(encoding="utf-8")[record["start"]:record["end"]] != record["original"]:
            raise ValueError(f"Incorrect source alignment: {record['id']}")
    for name in ("chinese", "english"):
        load_run(name, records)
    table_lines = [line for line in COMPARISON.read_text(encoding="utf-8").splitlines() if line.startswith("| ")]
    if len(table_lines) != len(records) + 2 or any(line.count("|") != 4 for line in table_lines):
        raise ValueError("Comparison table must have exactly three columns and one row per source paragraph")
    print(f"Verified {len(records)} aligned rows, three columns, both runs, protected literals, and unchanged source files")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("prepare", "assemble", "verify"))
    args = parser.parse_args()
    {"prepare": prepare, "assemble": assemble, "verify": verify}[args.action]()
