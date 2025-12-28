#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(".")
SUMMARY = ROOT / "SUMMARY.md"

# Ordner -> Gruppenname (du kannst das Mapping jederzeit ändern)
GROUPS = [
    ("vegan", "Vegan"),
    ("vegetarisch", "Vegetarisch"),
    ("fleischgerichte", "Fleischgerichte"),
    ("omas-rezepte", "Omas Rezepte"),
    ("grundlagen", "Grundlagen"),
]

H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)

def title_from_md(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return path.stem.replace("-", " ")
    m = H1_RE.search(text)
    if m:
        return m.group(1).strip()
    return path.stem.replace("-", " ")

def md_files_in(folder: Path):
    # Nur echte Rezeptseiten: *.md, aber kein README.md, keine SUMMARY.md
    files = []
    for p in sorted(folder.glob("*.md")):
        if p.name.lower() in ("readme.md", "summary.md"):
            continue
        files.append(p)
    return files

lines = []
lines.append("# Rezepte\n")

for folder_name, group_title in GROUPS:
    folder = ROOT / folder_name
    if not folder.exists() or not folder.is_dir():
        continue

    files = md_files_in(folder)
    if not files:
        continue

    lines.append(f"## {group_title}\n")
    for f in files:
        title = title_from_md(f)
        rel = f.as_posix()
        lines.append(f"- [{title}]({rel})\n")
    lines.append("\n")

content = "".join(lines).rstrip() + "\n"
SUMMARY.write_text(content, encoding="utf-8")
print(f"Wrote {SUMMARY}")
