from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"


def tracked_markdown_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "*.md"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [Path(line) for line in result.stdout.splitlines() if line.strip()]


def existing_markdown_files() -> list[Path]:
    excluded_parts = {".git", ".venv", "docs", "site"}
    paths: set[Path] = set()
    for path in ROOT.rglob("*.md"):
        if any(part.startswith(".") or part in excluded_parts for part in path.parts):
            continue
        paths.add(path.relative_to(ROOT))
    return sorted(paths)


def read_source_file(path: Path) -> str:
    source_path = ROOT / path
    if source_path.exists():
        return source_path.read_text(encoding="utf-8")

    result = subprocess.run(
        ["git", "show", f"HEAD:{path.as_posix()}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def copy_markdown_sources() -> None:
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    sources = sorted(set(tracked_markdown_files()) | set(existing_markdown_files()))
    for source in sources:
        target = DOCS_DIR / ("index.md" if source.as_posix() == "README.md" else source)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(read_source_file(source), encoding="utf-8")


if __name__ == "__main__":
    copy_markdown_sources()
