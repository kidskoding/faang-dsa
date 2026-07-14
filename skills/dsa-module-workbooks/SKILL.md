______________________________________________________________________

## name: dsa-module-workbooks description: Create and update DSA curriculum modules with a single workbook, problem ladder, stubs, and tests for fundamentals, mediums, and hard extensions.

# DSA Module Workbooks

Use this skill when building or revising a curriculum module that should teach a topic from fundamentals through interview-ready practice.

## Curriculum Order

Use this live-coding-first module order:

1. `00_fundamentals`
1. `01_arrays_and_hashing`
1. `02_two_pointers`
1. `03_sliding_window`
1. `04_stack`
1. `05_binary_search`
1. `06_linked_lists`
1. `07_trees`
1. `08_heaps`
1. `09_backtracking`
1. `10_graphs`
1. `11_dp`
1. `12_greedy`
1. `13_intervals`
1. `14_tries`
1. `15_bit_manipulation`
1. `16_math_geometry`
1. `17_advanced`
1. `18_mixed_interview_practice`

Do not create a separate design-data-structures module. Put design-style implementations inside the pattern module that powers them.

Advanced graph algorithms, sorting internals, divide and conquer, segment trees, Fenwick trees, KMP, rolling hash, and similar lower-frequency topics belong in `17_advanced`.

## Output Shape

Every module should use the same scaffold:

1. A module `README.md` that acts as a problem index and lists the problem set problems only.
1. A single problem set markdown file for the module.
1. Problem stubs in a module-local `problem_set/` or equivalent, with importable filenames that stay friendly to tests.
1. Tests grouped by the same problem categories.

## Learning Model

Each module should eventually have four layers:

1. Concept explanation.
1. From-scratch implementation.
1. Module-local tests.
1. Guided practice through a focused problem set.

Design-style data structure problems belong inside the pattern module that powers them. For example, LRU Cache belongs with linked lists and hash maps; Median Finder belongs with heaps.

## Workbook Structure

Write the problem set in one file and keep it linear:

1. Use `Fundamentals`, `Mediums`, and `Hards And Extensions` as the outer workbook sections.
1. Keep the module `## Topics` order stable inside those sections.
1. Within each band, follow the topic order from the module README.
1. Start with approachable problems for each topic, then add common mediums, then hard extensions.
1. For broad modules like trees, graphs, DP, backtracking, and heaps, avoid a flat topic list when the topic families are large enough to justify bands.

Avoid splitting the workbook into multiple overlapping lists unless the user explicitly wants separate tracks.

## Problem List Rules

1. Start with fundamentals that teach the core pattern.
1. Add the common medium problems next.
1. Finish with harder extensions or follow-ups.
1. Do not repeat the same problem in multiple sections.
1. Keep the problem set as a checklist first, then add brief pattern notes.
1. Use real interview/LeetCode-style problem titles for numbered problem set entries.
1. Do not use abstract course units as problem titles, such as "Graph BFS", "Grid DFS", or "Topological Sort".
1. Put abstract concepts and traversal families in `## Topics`; put the concrete application under each problem's `- Pattern:` note.
1. Prefer broad coverage over artificially short lists for every module. Heavy modules such as trees, graphs, DP, backtracking, and heaps should be especially broad and include as many high-value interview problems as needed for mastery.
1. A `Recommended Order` section is only a priority path for time-constrained study; it must not be treated as the full problem set or as a cap on coverage.
1. Do not put a `Mastery Rule` section inside the problem set workbook. The global mastery rule belongs in the repo-level `README.md`.
1. The canonical problem list should mirror the topic order in the module README, grouped under the workbook bands.
1. If a problem comes from LeetCode, link the problem title to its LeetCode page in the workbook.

Each numbered workbook entry should follow this shape:

```md
### 1. [Problem Title](https://leetcode.com/problems/problem-slug/)
- Pattern: the reusable idea this problem teaches.
```

## Implementation Files

When creating stubs:

1. Group functions by the workbook sections.
1. Split the core files by concept so each file stays small, importable, and testable.
1. Keep one function per problem.
1. Leave `NotImplementedError` in place until the user is ready to implement.
1. Match test names to the function names and workbook sections.

For `10_graphs`, split traversal files by context:

1. `graph_representations.py`
1. `graph_bfs.py`
1. `graph_dfs.py`
1. `grid_dfs.py`
1. `grid_bfs.py`
1. `multi_source_bfs.py`
1. `topological_sort.py`

Treat grids as implicit graphs. Teach grid DFS, grid BFS, and multi-source BFS as separate course units.

## Tests

When creating tests:

1. Add a test file for each major workbook section.
1. Cover empty, single-node, normal, and skewed cases where relevant.
1. Use the same representative sample tree or input across problems when useful.
1. Keep tests focused so the user can run one problem at a time with `pytest -k`.
1. Treat hard extensions as workbook-only unless the user explicitly wants scaffolds for them.

## Editing Rules

1. Prefer one unified workbook over duplicate warmup/core files unless the user explicitly wants separate tracks.
1. If the user asks for a simpler progression, collapse repetition into one file.
1. Update the module README to be a minimal problem index that lists the problem set problems in order and links to the canonical problem set.
1. Keep the README minimal. Do not add goal/lesson prose unless the user explicitly asks for it.
1. Keep Python filenames importable and stable. Use the workbook and README for ordering, not numeric filename prefixes, unless the user explicitly wants that tradeoff.
1. Keep the same scaffold for every module: `README.md`, one problem set `.md`, `problem_set/`, and `tests/`.
1. Keep explanations concise and pattern-driven.
1. When updating a module README, copy only the concrete problem titles from the workbook's problem set, not abstract topic names.
1. Do not repeat the global mastery rule in module READMEs unless the user explicitly asks for a module-specific variant.

## Typical Workflow

1. Read the module README and existing workbook.
1. Merge or reorganize the workbook into fundamentals, mediums, and hard extensions.
1. Create stubs for the workbook problems.
1. Create tests grouped by section.
1. Implement one problem at a time and run the matching tests.
1. Update complexity notes after the logic is stable.
