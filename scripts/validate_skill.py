#!/usr/bin/env python3
"""Structural validator for a skill directory.

Checks the things that silently rot: frontmatter, relative links, placeholder
text, empty files, oversized modules, and code-fence balance.

usage:
    python scripts/validate_skill.py [path-to-skill-root]

exit code 0 = clean, 1 = errors found. warnings never fail the build.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REQUIRED = [
    "SKILL.md",
    "references/research-foundations.md",
    "references/research/01-storyscope.md",
    "references/research/02-ghostbuster.md",
    "references/research/03-detectgpt.md",
    "references/research/04-dna-gpt.md",
    "references/research/05-fingerprinting.md",
]

PLACEHOLDERS = re.compile(r"\b(TODO|TBD|FIXME|XXX|lorem ipsum|coming soon)\b", re.I)
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKIP_DIRS = {".git", "__pycache__", ".github", "notes", "research", "raw", "judging"}

# canonical header keys, and the variants agents and contributors actually write
HEADER_KEYS = {
    "purpose": "Purpose",
    "read when": "Read when",
    "when to read": "Read when",
    "related": "Related",
    "connections": "Related",
    "links": "Related",
    "назначение": "Purpose",
    "когда читать": "Read when",
    "связи": "Related",
}
HEADER_DIRS = ("references", "methodologies", "workflows", "examples")


def normalise_tags(path: Path) -> bool:
    """Unify evidence tags. Returns True if the file changed."""
    text = path.read_text(encoding="utf-8")
    new = text
    for src in ("данные", "Данные", "data", "Data"):
        new = new.replace(f"[{src}:", "[data:")
        new = new.replace(f"[{src} :", "[data:")
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def normalise_headers(path: Path) -> bool:
    """Rewrite header keys to the canonical three. Returns True if the file changed."""
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    changed = False
    for i, line in enumerate(lines[:12]):
        if not line.startswith(">"):
            continue
        body = line[1:].lstrip()
        key, sep, rest = body.partition(":")
        if not sep:
            continue
        canonical = HEADER_KEYS.get(key.strip().lower())
        if canonical and key.strip() != canonical:
            lines[i] = f"> {canonical}:{rest}"
            changed = True
    if changed:
        path.write_text("".join(lines), encoding="utf-8")
    return changed


def has_header(path: Path, text: str) -> bool:
    head = "\n".join(text.splitlines()[:12])
    return "> Purpose:" in head and "> Read when:" in head



def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line or line.strip().startswith("#"):
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip().strip("\"'")
    return data


def iter_markdown(root: Path):
    for path in sorted(root.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def check_links(path: Path, text: str, root: Path) -> list[str]:
    errors = []
    for target in LINK.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#", 1)[0].strip()
        if not clean:
            continue
        resolved = (path.parent / clean).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(root)}: broken link -> {target}")
    return errors


def check_fences(path: Path, text: str) -> list[str]:
    fences = len(re.findall(r"^\s*```", text, re.M))
    if fences % 2:
        return [f"{path.relative_to(root_global[0])}: unbalanced code fences ({fences})"]
    return []


root_global: list[Path] = []


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    fix = "--fix" in sys.argv
    root = Path(args[0] if args else Path.cwd()).resolve()
    root_global.append(root)
    errors: list[str] = []
    warnings: list[str] = []
    fixed: list[str] = []

    if fix:
        for path in iter_markdown(root):
            changed = normalise_headers(path)
            changed = normalise_tags(path) or changed
            if changed:
                fixed.append(str(path.relative_to(root)))
        if fixed:
            print("normalised headers/tags in:\n  " + "\n  ".join(fixed))

    for rel in REQUIRED:
        if not (root / rel).exists():
            errors.append(f"missing required file: {rel}")

    skill = root / "SKILL.md"
    if skill.exists():
        text = skill.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        if not meta.get("name"):
            errors.append("SKILL.md: frontmatter is missing 'name'")
        elif meta["name"].lower() != root.name.lower():
            errors.append(
                f"SKILL.md: name '{meta['name']}' does not match directory '{root.name}'"
            )
        desc = meta.get("description", "")
        if not desc:
            errors.append("SKILL.md: frontmatter is missing 'description'")
        elif len(desc) > 1024:
            errors.append(f"SKILL.md: description is {len(desc)} chars (max 1024)")
        elif len(desc) < 80:
            warnings.append("SKILL.md: description is very short, triggering may suffer")
        lines = text.count("\n") + 1
        if lines > 500:
            warnings.append(f"SKILL.md: {lines} lines, progressive disclosure says <500")

    docs = list(iter_markdown(root))
    if len(docs) < 20:
        warnings.append(f"only {len(docs)} markdown files, this looks thin")

    for path in docs:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root)
        if not text.strip():
            errors.append(f"{rel}: empty file")
            continue
        if PLACEHOLDERS.search(text):
            hit = PLACEHOLDERS.search(text)
            errors.append(f"{rel}: placeholder text '{hit.group(0)}'")
        errors.extend(check_links(path, text, root))
        errors.extend(check_fences(path, text))
        lines = text.count("\n") + 1
        if lines > 520:
            warnings.append(f"{rel}: {lines} lines, consider splitting")
        if (
            path.name not in ("README.md", "SKILL.md")
            and lines > 40
            and not text.lstrip().startswith("#")
        ):
            warnings.append(f"{rel}: does not start with a heading")
        if (
            path.name != "README.md"
            and any(part in HEADER_DIRS for part in rel.parts)
            and not has_header(path, text)
        ):
            errors.append(f"{rel}: missing the '> Purpose:' / '> Read when:' header block")

    refs = root / "references"
    if refs.exists() and not (refs / "research-foundations.md").exists():
        errors.append("references/research-foundations.md is required")

    for w in warnings:
        print(f"warn  {w}")
    for e in errors:
        print(f"error {e}")

    print(
        json.dumps(
            {
                "root": str(root),
                "markdown_files": len(docs),
                "errors": len(errors),
                "warnings": len(warnings),
                "result": "fail" if errors else "pass",
            }
        )
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
