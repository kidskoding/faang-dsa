"""Reset solved practice problems back to stubs so a module can be redone.

Usage:
    python tools/restub.py 07_trees/problem_set/                    # whole module
    python tools/restub.py 07_trees/problem_set/bst_problems.py    # one file

Each function or method body is replaced with `raise NotImplementedError`,
which the root conftest.py reports as a skipped test. The signature and the
`# Problem N:` / `# Key idea:` comments are kept; filled-in `# Time:` and
`# Space:` answers are blanked so complexity gets re-derived on the redo.
Past solutions live in git history — commit before running this, then compare
attempts later with `git diff <old-commit> -- <file>`.
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

FuncDef = ast.FunctionDef | ast.AsyncFunctionDef


def top_level_functions(tree: ast.Module) -> list[FuncDef]:
    """Module-level functions and methods of module-level classes.

    Nested (helper) functions are excluded: they belong to the body being
    replaced, and rewriting them separately corrupts the outer ranges.
    """
    found: list[FuncDef] = []
    for node in tree.body:
        if isinstance(node, FuncDef):
            found.append(node)
        elif isinstance(node, ast.ClassDef):
            found.extend(child for child in node.body if isinstance(child, FuncDef))
    return found


def restub_file(path: Path) -> int:
    lines = path.read_text().split("\n")
    tree = ast.parse("\n".join(lines))

    changed = 0
    # Rewrite bottom-up so earlier line numbers stay valid.
    for func in sorted(top_level_functions(tree), key=lambda f: f.lineno, reverse=True):
        header_end = func.body[0].lineno - 1  # comments live in def..first-statement
        body_end = func.end_lineno
        body = lines[header_end:body_end]

        code = [line for line in body if line.strip() and not line.strip().startswith("#")]
        if len(code) == 1 and code[0].strip() in ("raise NotImplementedError", "pass"):
            if code[0].strip() == "raise NotImplementedError":
                continue  # already a stub

        indent = " " * (func.col_offset + 4)
        lines[header_end:body_end] = ["", f"{indent}raise NotImplementedError"]

        # Blank filled-in complexity answers in the kept comment block above.
        for i in range(func.lineno, header_end):
            stripped = lines[i].strip()
            if stripped.startswith("# Time:") or stripped.startswith("# Space:"):
                lines[i] = f"{indent}{stripped.split(':', 1)[0]}:"
        changed += 1

    if changed:
        path.write_text("\n".join(lines))
    return changed


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    target = Path(sys.argv[1])
    files = sorted(target.glob("*_problems.py")) if target.is_dir() else [target]
    if not files:
        sys.exit(f"no *_problems.py files under {target}")
    total = 0
    for f in files:
        n = restub_file(f)
        total += n
        print(f"{f}: re-stubbed {n} function(s)")
    print(f"done: {total} function(s) reset — past solutions remain in git history")


if __name__ == "__main__":
    main()
