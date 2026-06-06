---
name: dsa-module-workbooks
description: Create and update DSA curriculum modules with a single workbook, problem ladder, stubs, and tests for fundamentals, mediums, and hard extensions.
---

# DSA Module Workbooks

Use this skill when building or revising a curriculum module that should teach a topic from fundamentals through interview-ready practice.

## Curriculum Order

Use this live-coding-first module order:

1. `00_fundamentals`
2. `01_arrays_and_hashing`
3. `02_two_pointers`
4. `03_sliding_window`
5. `04_stack`
6. `05_binary_search`
7. `06_linked_lists`
8. `07_trees`
9. `08_heaps`
10. `09_backtracking`
11. `10_graphs`
12. `11_dp`
13. `12_greedy`
14. `13_intervals`
15. `14_tries`
16. `15_bit_manipulation`
17. `16_math_geometry`
18. `17_advanced`
19. `18_mixed_interview_practice`

Do not create a separate design-data-structures module. Put design-style implementations inside the pattern module that powers them.

Advanced graph algorithms, sorting internals, divide and conquer, segment trees, Fenwick trees, KMP, rolling hash, and similar lower-frequency topics belong in `17_advanced`.

## Output Shape

Every module should use the same scaffold:

1. A module `README.md` that acts as a problem index and lists the problem set problems only.
2. A single problem set markdown file for the module.
3. Problem stubs in a module-local `problem_set/` or equivalent, with importable filenames that stay friendly to tests.
4. Tests grouped by the same problem categories.

## Workbook Structure

Write the problem set in one file and keep it linear:

1. Fundamentals.
2. Core mediums.
3. Hard problems and extensions.

Avoid splitting the workbook into multiple overlapping lists unless the user explicitly wants separate tracks.

## Problem List Rules

1. Start with fundamentals that teach the core pattern.
2. Add the common medium problems next.
3. Finish with harder extensions or follow-ups.
4. Do not repeat the same problem in multiple sections.
5. Keep the problem set as a checklist first, then add brief pattern notes.

## Implementation Files

When creating stubs:

1. Group functions by the workbook sections.
2. Split the core files by concept so each file stays small, importable, and testable.
3. Keep one function per problem.
4. Leave `NotImplementedError` in place until the user is ready to implement.
5. Match test names to the function names and workbook sections.

For `10_graphs`, split traversal files by context:

1. `graph_representations.py`
2. `graph_bfs.py`
3. `graph_dfs.py`
4. `grid_dfs.py`
5. `grid_bfs.py`
6. `multi_source_bfs.py`
7. `topological_sort.py`

Treat grids as implicit graphs. Teach grid DFS, grid BFS, and multi-source BFS as separate course units.

## Tests

When creating tests:

1. Add a test file for each major workbook section.
2. Cover empty, single-node, normal, and skewed cases where relevant.
3. Use the same representative sample tree or input across problems when useful.
4. Keep tests focused so the user can run one problem at a time with `pytest -k`.
5. Treat hard extensions as workbook-only unless the user explicitly wants scaffolds for them.

## Editing Rules

1. Prefer one unified workbook over duplicate warmup/core files unless the user explicitly wants separate tracks.
2. If the user asks for a simpler progression, collapse repetition into one file.
3. Update the module README to be a minimal problem index that lists the problem set problems in order and links to the canonical problem set.
4. Keep the README minimal. Do not add goal/lesson prose unless the user explicitly asks for it.
5. Keep Python filenames importable and stable. Use the workbook and README for ordering, not numeric filename prefixes, unless the user explicitly wants that tradeoff.
6. Keep the same scaffold for every module: `README.md`, one problem set `.md`, `problem_set/`, and `tests/`.
7. Keep explanations concise and pattern-driven.

## Typical Workflow

1. Read the module README and existing workbook.
2. Merge or reorganize the workbook into fundamentals, mediums, and hard extensions.
3. Create stubs for the workbook problems.
4. Create tests grouped by section.
5. Implement one problem at a time and run the matching tests.
6. Update complexity notes after the logic is stable.
