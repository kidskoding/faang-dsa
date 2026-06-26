from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK_SRC = ROOT / "book-src"

EXCLUDED_PARTS = {
    ".git",
    ".venv",
    ".pytest_cache",
    ".ruff_cache",
    "book",
    "book-src",
    "__pycache__",
}


def title_from_markdown(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return title_from_path(path)


def title_from_path(path: Path) -> str:
    stem = path.stem
    stem = re.sub(r"^\d+_", "", stem)
    return stem.replace("_", " ").replace("-", " ").title()


def should_copy(path: Path) -> bool:
    if path.suffix != ".md":
        return False
    if any(part in EXCLUDED_PARTS or part.startswith(".") for part in path.parts):
        return False
    return True


def copy_markdown_sources() -> None:
    if BOOK_SRC.exists():
        shutil.rmtree(BOOK_SRC)
    BOOK_SRC.mkdir(parents=True, exist_ok=True)

    for source in sorted(ROOT.rglob("*.md")):
        rel = source.relative_to(ROOT)
        if not should_copy(rel):
            continue

        target_rel = Path("index.md") if rel.as_posix() == "README.md" else rel
        target = BOOK_SRC / target_rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")


def summary_link(title: str, path: Path | None, indent: int = 0) -> str:
    spaces = "  " * indent
    if path is None:
        return f"{spaces}- [{title}]()"
    return f"{spaces}- [{title}]({path.as_posix()})"


def module_dirs() -> list[Path]:
    return sorted(
        path
        for path in ROOT.iterdir()
        if path.is_dir() and re.match(r"^\d{2}_", path.name)
    )


def module_summary_lines(module: Path) -> list[str]:
    lines: list[str] = []
    readme = module / "README.md"
    if not readme.exists():
        return lines

    module_rel = readme.relative_to(ROOT)
    lines.append(summary_link(title_from_markdown(readme), module_rel))

    notes_dir = module / "notes"
    if notes_dir.exists():
        for note in sorted(notes_dir.glob("*.md")):
            lines.append(summary_link(title_from_markdown(note), note.relative_to(ROOT), 1))

    problem_set_dir = module / "problem_set"
    if problem_set_dir.exists():
        for problem_set in sorted(problem_set_dir.glob("*.md")):
            lines.append(
                summary_link(title_from_markdown(problem_set), problem_set.relative_to(ROOT), 1)
            )

    return lines


def company_summary_lines() -> list[str]:
    lines: list[str] = []
    root = ROOT / "company_problem_sets"
    readme = root / "README.md"
    if not readme.exists():
        return lines

    lines.append(summary_link("Company Problem Sets", readme.relative_to(ROOT)))

    for path in sorted(root.glob("[0-9][0-9]_*.md")):
        lines.append(summary_link(title_from_markdown(path), path.relative_to(ROOT), 1))

    other_tech = root / "other_tech_companies"
    other_tech_readme = other_tech / "README.md"
    if other_tech_readme.exists():
        lines.append(summary_link(title_from_markdown(other_tech_readme), other_tech_readme.relative_to(ROOT), 1))
        for path in sorted(other_tech.glob("[0-9][0-9]_*.md")):
            lines.append(summary_link(title_from_markdown(path), path.relative_to(ROOT), 2))

    other = root / "other"
    other_readme = other / "README.md"
    if other_readme.exists():
        lines.append(summary_link(title_from_markdown(other_readme), other_readme.relative_to(ROOT), 1))
        for path in sorted(other.glob("*.md")):
            if path.name == "README.md":
                continue
            lines.append(summary_link(title_from_markdown(path), path.relative_to(ROOT), 2))

    return lines


def other_practice_lines() -> list[str]:
    lines: list[str] = []
    root = ROOT / "other" / "problem_sets"
    if not root.exists():
        return lines
    for path in sorted(root.rglob("*.md")):
        lines.append(summary_link(title_from_markdown(path), path.relative_to(ROOT)))
    return lines


def write_summary() -> None:
    lines: list[str] = ["# Summary", ""]

    lines.append(summary_link("Home", Path("index.md")))
    lines.append("")

    lines.append("# Curriculum")
    lines.append("")
    for module in module_dirs():
        lines.extend(module_summary_lines(module))
    lines.append("")

    company_lines = company_summary_lines()
    if company_lines:
        lines.append("# Company Practice")
        lines.append("")
        lines.extend(company_lines)
        lines.append("")

    practice_lines = other_practice_lines()
    if practice_lines:
        lines.append("# Other Practice")
        lines.append("")
        lines.extend(practice_lines)
        lines.append("")

    (BOOK_SRC / "SUMMARY.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    copy_markdown_sources()
    write_summary()


if __name__ == "__main__":
    main()
