from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYNC_SCRIPT = ROOT / "scripts" / "sync_mdbook.py"

EXCLUDED_PARTS = {
    ".git",
    ".venv",
    ".pytest_cache",
    ".ruff_cache",
    "book",
    "book-src",
    "__pycache__",
}


def markdown_mtime_snapshot() -> dict[Path, int]:
    snapshot: dict[Path, int] = {}
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if any(part in EXCLUDED_PARTS or part.startswith(".") for part in rel.parts):
            continue
        snapshot[rel] = path.stat().st_mtime_ns
    return snapshot


def sync() -> None:
    subprocess.run([sys.executable, str(SYNC_SCRIPT)], cwd=ROOT, check=True)


def main() -> None:
    sync()
    server = subprocess.Popen(["mdbook", "serve"], cwd=ROOT)
    previous = markdown_mtime_snapshot()

    try:
        while server.poll() is None:
            time.sleep(0.75)
            current = markdown_mtime_snapshot()
            if current != previous:
                sync()
                previous = current
    finally:
        if server.poll() is None:
            server.terminate()
            try:
                server.wait(timeout=5)
            except subprocess.TimeoutExpired:
                server.kill()


if __name__ == "__main__":
    main()
