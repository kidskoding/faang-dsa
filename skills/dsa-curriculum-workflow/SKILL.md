---
name: dsa-curriculum-workflow
description: "Create, revise, or rename a numbered DSA module — its README, workbook, problem stubs, and tests. Use when adding or reorganizing a module, changing the problem ladder, or keeping a module's README and workbook in sync."
---

# DSA Curriculum Workflow

The single source of truth for how a numbered module is built. Two other skills
own the pieces this one delegates:

| Concern                                                                      | Skill                        |
| ---------------------------------------------------------------------------- | ---------------------------- |
| Concept notes in `notes/`                                                    | `writing-notes`              |
| Exact file layout, imports, pyproject wiring for `problem_set/` and `tests/` | `problem-set-tests-scaffold` |
| Everything else about a module                                               | this skill                   |

Do not restate note-writing rules here. `writing-notes` owns them, and a second
copy will drift.

## Curriculum Order

Modules are read in order, so a module may assume every module before it:

```text
00_fundamentals          09_backtracking
01_arrays_and_hashing    10_graphs
02_two_pointers          11_dp
03_stacks_and_queues     12_greedy_algorithms
04_sliding_window        13_intervals
05_binary_search         14_tries
06_linked_lists          15_bit_manipulation
07_trees                 16_math_geometry
08_heaps                 17_advanced
                         18_mixed_interview_practice
```

Advanced graph algorithms, sorting internals, divide and conquer, segment and
Fenwick trees, KMP, and other lower-frequency topics live in `17_advanced`.

Do not create a separate design-data-structures module. Design problems go in the
module whose pattern powers them, so LRU Cache sits with linked lists and hash
maps, and Median Finder sits with heaps. Treat grids as implicit graphs inside
`10_graphs`.

## Module Layout

Every module uses the same scaffold:

```text
NN_module/
├── README.md                       minimal index
├── notes/                          concept notes, see writing-notes
│   ├── 01_fundamentals.md
│   └── 02_technique.md
├── <concept>.py                    from-scratch implementations
├── problem_set/
│   ├── MODULE_PROBLEM_SET.md       the canonical workbook
│   └── <category>_problems.py      stubs grouped by pattern
└── tests/
    └── test_<category>_problems.py
```

Four layers, each of which a finished module has:

1. Concept explanation in `notes/`
2. From-scratch implementation
3. Module-local tests
4. Guided practice through the problem set

Never create a top-level `problems/` or `tests/` folder. Both belong inside the
module that owns the concept.

## README Rules

Keep it short and index-like. Required order:

```md
# Module NN: Name

## Topics

- Topic 1
- Topic 2

## Notes

1. [Topic 1](notes/01_topic_1.md)
2. [Topic 2](notes/02_topic_2.md)

## Problem Set

[Name Problem Set](problem_set/NAME_PROBLEM_SET.md) — 38 problems, grouped into
**Section One**, **Section Two**. Each entry names the pattern it teaches and the
stub function it solves, across 4 solution files in `problem_set/`.

The workbook is the canonical list. It is not duplicated here, so the two
cannot drift apart.

## Additional Notes

- Optional short clarification
```

- `## Topics` holds concepts, so BFS, DFS, grid traversal, and topological sort
  go here
- `## Problem Set` is a **pointer to the workbook, never a copy of it**. Give the
  problem count, the technique sections, and one link. Do not list the problems
- The counts and section names must be read off the workbook, not asserted from
  memory, since a wrong count is worse than no count
- Do not duplicate workbook explanations or add teaching prose. Long explanations
  belong in `notes/`
- Do not repeat the global mastery rule, which lives in the repo `README.md`

## Workbook Rules

One canonical workbook per module, kept linear.

- Outer sections are `Fundamentals`, `Mediums`, and `Hards And Extensions`
- Inside each band, follow the module's `## Topics` order
- Numbered entries are concrete interview problem titles, never abstract lesson
  names like "Graph BFS"
- Each entry carries a short `- Pattern:` line naming the reusable idea
- Never repeat a problem across sections
- A `Recommended Order` section, if present, is a priority path for
  time-constrained study and not a cap on coverage
- No `Mastery Rule` section, since that lives in the repo `README.md`

```md
### 1. [Problem Title](https://leetcode.com/problems/problem-slug/)
- Pattern: the reusable idea this problem teaches.
```

**Size sections by mastery, not by a fixed count.** A technique section with
fewer than 4-5 problems is a smell. Heavy modules such as trees, graphs, DP,
backtracking, and heaps should be especially broad. If migrating problems out
leaves a section sparse, backfill it with more problems of the same technique.

**Keep each module single-technique.** A problem stays if the module's technique
solves it cleanly, even when another pattern also works. A problem that genuinely
requires chaining two or more patterns belongs in `18_mixed_interview_practice`.

## Implementation Files And Tests

Split by concept so each file stays small, importable, and testable. One function
per problem, grouped by the workbook's categories, with `raise NotImplementedError`
as the body until the user is ready to solve it.

For the exact stub header format, test helper conventions, namespace-package
imports, and the `pyproject.toml` `pythonpath` wiring, use
`problem-set-tests-scaffold`. Missing the `pythonpath` entry is the most common
scaffolding mistake.

Tests mirror the workbook's categories, one test file per stub file. Cover empty,
single, normal, and edge cases. Treat hard extensions as workbook-only unless
scaffolds are explicitly requested.

## Company Problem Sets

Files in `company_problem_sets/` use one `## Problem Set` section listing
high-signal problems directly, followed by `## Review Modules`.

- No `Warmups`, `Core`, `Stretch`, or `Major LeetCode Problems` headings
- No fixed problem count. Cover the company's core live-coding techniques
- Avoid cross-company overlap. Repeat only deliberate anchor problems, and
  otherwise pick different high-signal problems from the same technique family
- Never claim the list is an exact interview question dump

## Verification

- Update tests whenever the workbook changes
- Run the focused module tests: `python3 -m pytest NN_module/tests -q`
- Keep the README, workbook, and tests in sync in the same commit

## Gotchas

- **Never duplicate the problem list into the README.** Every module once carried
  a partial copy, and every single one had drifted: `04_sliding_window` listed 14
  problems against a workbook of 38, and in 16 of 19 modules every entry linked to
  the same file rather than to LeetCode. Two lists of the same thing always
  diverge, because only one of them gets updated. The README points, the workbook
  lists.
- **The workbook and the tests still drift silently.** Changing the workbook order
  without updating the tests leaves them out of step and nothing fails to warn
  you, so update both in the same commit.
- **Do not restate note rules here.** If you find yourself writing about `Pattern`
  or `Intuition` sections, stop and use `writing-notes` instead. This skill and
  that one previously disagreed, and the duplication is what caused it.
- **Stubs use `raise NotImplementedError`, not `pass`.** The repo has 783 of the
  former and zero of the latter, so match what is there.
- **A sparse technique section is the real defect, not a tidy one.** Resist
  trimming a section to make a module look balanced. Backfill instead.
- **New module means new `pythonpath` entry.** Without it every import in the new
  files fails at collection, and the error points at the test rather than at
  `pyproject.toml`.
