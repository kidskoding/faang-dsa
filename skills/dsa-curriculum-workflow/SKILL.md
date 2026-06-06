______________________________________________________________________

## name: dsa-curriculum-workflow description: Streamline DSA module updates across the repo by keeping module READMEs, workbooks, tests, and implementation files aligned to one consistent curriculum workflow.

# DSA Curriculum Workflow

Use this skill when creating, revising, or renaming any numbered DSA module in this repo.

## Workflow

1. Read the module README and workbook first.
1. Decide the module's place in the curriculum order.
1. Keep the module README minimal and index-like.
1. Keep the workbook as the canonical problem ladder.
1. Keep implementation files split by concept, not by arbitrary size.
1. Keep tests grouped by the same problem sections.
1. Verify with targeted tests before moving on.

## Required Structure

For every module:

1. `Module xx: Name`
1. `## Topics`
1. `## Problem Set`
1. `## Additional Notes`

## Learning Model

Each module should eventually have four layers:

1. Concept explanation.
1. From-scratch implementation.
1. Module-local tests.
1. Guided practice through a focused problem set.

Design-style data structure problems belong inside the pattern module that powers them. For example, LRU Cache belongs with linked lists and hash maps; Median Finder belongs with heaps.

## Workbook Structure

Use one canonical workbook file per module when possible.

1. Use `Fundamentals`, `Mediums`, and `Hards And Extensions` as the outer workbook sections.
1. Keep the module `## Topics` order stable inside those sections.
1. Within each band, follow the topic order from the module README.
1. Start with approachable problems for each topic, then add common mediums, then hard extensions.
1. For broad modules like trees, graphs, DP, backtracking, and heaps, avoid a flat topic list when the topic families are large enough to justify bands.

Do not repeat the same problem in multiple sections.

Numbered workbook entries must be concrete interview/LeetCode-style problem titles, not abstract lesson names. Use `## Topics` for concepts such as BFS, DFS, grid traversal, heaps, backtracking templates, or topological sort. Under each concrete problem, add a short `- Pattern:` note explaining the reusable idea.

If a problem comes from LeetCode, link the problem title to its LeetCode page in the workbook.

Favor broad mastery coverage over short fixed-size lists for every module. Heavy modules such as trees, graphs, DP, backtracking, and heaps should be especially broad and include as many high-value problems as the topic needs. If the workbook has a `Recommended Order`, treat it as the priority path only, not the full problem set.

Do not put a `Mastery Rule` section inside individual problem set workbooks. The global mastery rule belongs in the repo-level `README.md`.

## README Rules

1. Keep the README short.
1. Copy the topic order from the workbook.
1. Copy the concrete problem order from the workbook.
1. Use `## Additional Notes` only for short clarifications.
1. Do not duplicate workbook explanations in the README.
1. Do not list abstract course units as problems in `## Problem Set`.
1. Do not repeat the global mastery rule in module READMEs unless the user explicitly asks for a module-specific variant.
1. If the module README lists LeetCode problems, include the associated LeetCode link beside the workbook link.

## File Organization Rules

1. Keep filenames importable and stable.
1. Split code by pattern or concept when a module needs multiple files.
1. Keep design-style implementations inside the module that powers them.
1. Treat grids as implicit graphs inside the graphs module.
1. Keep advanced or lower-frequency topics in `17_advanced`.

## Verification Rules

1. Update tests when the workbook changes.
1. Run focused tests for the affected module.
1. Keep the README, workbook, and tests in sync.
