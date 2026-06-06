from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "book-src"


def existing_markdown_files() -> list[Path]:
    excluded_parts = {".git", ".venv", ".pytest_cache", "book", "book-src"}
    paths: set[Path] = set()
    for path in ROOT.rglob("*.md"):
        if any(part.startswith(".") or part in excluded_parts for part in path.parts):
            continue
        paths.add(path.relative_to(ROOT))
    return sorted(paths)


def chapter_line(title: str, path: Path) -> str:
    return f"- [{title}]({path.as_posix()})"


def copy_markdown_sources() -> None:
    if SOURCE_DIR.exists():
        shutil.rmtree(SOURCE_DIR)
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)

    for source in existing_markdown_files():
        target = SOURCE_DIR / ("index.md" if source.as_posix() == "README.md" else source)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text((ROOT / source).read_text(encoding="utf-8"), encoding="utf-8")


def write_summary() -> None:
    summary_path = SOURCE_DIR / "SUMMARY.md"
    lines: list[str] = ["# Summary", ""]

    sections: list[tuple[str, list[tuple[str, str]]]] = [
        ("Introduction", [("Home", "index.md")]),
        (
            "Foundations",
            [
                ("Overview", "00_fundamentals/README.md"),
                ("Time and Space Complexity", "00_fundamentals/time_and_space_complexity.md"),
                ("Common Operation Costs", "00_fundamentals/common_operation_costs.md"),
                ("Interview Problem Solving", "00_fundamentals/interview_problem_solving.md"),
                ("Python Basics", "00_fundamentals/python_basics.md"),
            ],
        ),
        (
            "Patterns",
            [
                ("Arrays and Hashing", "01_arrays_and_hashing/README.md"),
                ("Two Pointers", "02_two_pointers/README.md"),
                ("Sliding Window", "03_sliding_window/README.md"),
                ("Stack", "04_stack/README.md"),
                ("Binary Search", "05_binary_search/README.md"),
                ("Linked Lists", "06_linked_lists/README.md"),
                ("Trees", "07_trees/README.md"),
                ("Heaps", "08_heaps/README.md"),
                ("Backtracking", "09_backtracking/README.md"),
                ("Graphs", "10_graphs/README.md"),
                ("Dynamic Programming", "11_dp/README.md"),
                ("Greedy Algorithms", "12_greedy_algorithms/README.md"),
                ("Intervals", "13_intervals/README.md"),
                ("Tries", "14_tries/README.md"),
                ("Bit Manipulation", "15_bit_manipulation/README.md"),
                ("Math and Geometry", "16_math_geometry/README.md"),
                ("Advanced Topics", "17_advanced/README.md"),
                ("Mixed Interview Practice", "18_mixed_interview_practice/README.md"),
            ],
        ),
        (
            "Company Practice",
            [
                ("Overview", "company_problem_sets/README.md"),
                ("Meta", "company_problem_sets/01_meta.md"),
                ("Amazon", "company_problem_sets/02_amazon.md"),
                ("Microsoft", "company_problem_sets/03_microsoft.md"),
                ("Apple", "company_problem_sets/04_apple.md"),
                ("Google", "company_problem_sets/05_google.md"),
                ("Airbnb", "company_problem_sets/06_airbnb.md"),
                ("Bloomberg", "company_problem_sets/07_bloomberg.md"),
                ("Coinbase", "company_problem_sets/08_coinbase.md"),
                ("Palantir", "company_problem_sets/09_palantir.md"),
                ("Salesforce", "company_problem_sets/10_salesforce.md"),
                ("TikTok / ByteDance", "company_problem_sets/11_tiktok_bytedance.md"),
                ("Oracle", "company_problem_sets/12_oracle.md"),
                ("NVIDIA", "company_problem_sets/13_nvidia.md"),
                ("Snowflake", "company_problem_sets/14_snowflake.md"),
                ("Databricks", "company_problem_sets/15_databricks.md"),
                ("Capital One", "company_problem_sets/16_capital_one.md"),
                ("IBM", "company_problem_sets/17_ibm.md"),
                ("OpenAI", "company_problem_sets/18_openai.md"),
                ("ServiceNow", "company_problem_sets/19_servicenow.md"),
                ("Uber", "company_problem_sets/20_uber.md"),
                ("Other Big Tech", "company_problem_sets/other_big_tech/README.md"),
                ("Other Companies", "company_problem_sets/other/README.md"),
            ],
        ),
        (
            "Practice Sets",
            [
                ("Trees Problem Set", "07_trees/problem_set/TREE_PROBLEM_SET.md"),
                ("Graph Problem Set", "10_graphs/problem_set/GRAPH_PROBLEM_SET.md"),
                ("Grid BFS Problem Set", "other/problem_sets/01_grid_bfs/BFS_GRID_PROBLEM_SET.md"),
            ],
        ),
        (
            "Skill Guides",
            [
                ("Curriculum Workflow", "skills/dsa-curriculum-workflow/SKILL.md"),
                ("Module Workbooks", "skills/dsa-module-workbooks/SKILL.md"),
                ("Module Readme Template", "skills/module-readme-template/SKILL.md"),
            ],
        ),
        ("Contributor Notes", [("CLAUDE", "CLAUDE.md")]),
    ]

    for section_title, chapters in sections:
        lines.append(f"## {section_title}")
        lines.append("")
        for chapter_title, chapter_path in chapters:
            if (SOURCE_DIR / chapter_path).exists():
                lines.append(chapter_line(chapter_title, Path(chapter_path)))
        lines.append("")

    summary_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    copy_markdown_sources()
    write_summary()
