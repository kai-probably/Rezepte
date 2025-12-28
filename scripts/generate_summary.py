#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(".")
SUMMARY = ROOT / "SUMMARY.md"

EXCLUDE_DIRS = {
    ".git",
    ".github",
    ".gitbook",
    "__MACOSX",
}

H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)

def is_valid_dir(p: Path) -> bool:
    return (
        p.is_dir()
        and not p.name.startswith(".")
        and p.name not in EXCLUDE_DIRS
    )

def is_valid_md(p: Path) -> bool:
    return (
        p.is_file()
        and p.suffix == ".md"
        and p.name.lower() not in ("readme.md", "summary.md")
        and not p.name.startswith("._")
    )

def title_from_md(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return path.stem.replace("-", " ").title()

    m = H1_RE.search(text)
    if m:
        return m.group(1).strip()

    return path.stem.replace("-", " ").title()

lines = ["# Rezepte\n\n"]

for folder in sorted([d for d in ROOT.iterdir() if is_valid_dir(d)]):
    files = sorted([f for f in folder.iterdir() if is_valid_md(f)])
    if not files:
        continue

    group_title = folder.name.replace("-", " ").title()
    lines.append(f"## {group_title}\n")

    for f in files:
        title = title_from_md(f)
        lines.append(f"- [{title}]({f.as_posix()})\n")

    lines.append("\n")

SUMMARY.write_text("".join(lines).rstrip() + "\n", encoding="utf-8")
print("SUMMARY.md generated")
