______________________________________________________________________

## name: dsa-curriculum-workflow description: Streamline DSA module updates across the repo by keeping module READMEs, workbooks, tests, and implementation files aligned to one consistent curriculum workflow.

# DSA Curriculum Workflow

Use this skill when creating, revising, or renaming any numbered DSA module in this repo.

## Workflow

1. Read the module README and workbook first.
2. Decide the module's place in the curriculum order.
3. Keep the module README minimal and index-like.
4. Keep concept notes in module-local `notes/` folders.
5. Name note files with sortable numeric prefixes such as `01_fundamentals.md`, `02_dfs.md`, and `03_bfs.md`.
6. Write notes in a pattern-study style similar to NeetCode or AlgoMonster: `Pattern`, `Intuition`, `How It Works`, `Template`, `Dry Run` or `Example`, `Complexity`, `Pitfalls`, and `Interview Checklist`.
7. Notes should be simple but thorough enough that the user can understand the technique before starting the problem set.
8. Do not add `Problems That Use This` sections to notes; the module README and workbook already list problems.
9. Keep the workbook as the canonical problem ladder.
10. Keep implementation files split by concept, not by arbitrary size.
11. Keep tests grouped by the same problem sections.
12. Verify with targeted tests before moving on.

## Required Structure

For every module:

1. `Module xx: Name`
2. `## Topics`
3. `## Notes`
4. `## Problem Set`
5. `## Additional Notes`

## Learning Model

Each module should eventually have four layers:

1. Concept explanation.
2. From-scratch implementation.
3. Module-local tests.
4. Guided practice through a focused problem set.

Concept explanation should live in module-local markdown files under `notes/`. The module README should link those notes, not contain long teaching prose.

Design-style data structure problems belong inside the pattern module that powers them. For example, LRU Cache belongs with linked lists and hash maps; Median Finder belongs with heaps.

## Workbook Structure

Use one canonical workbook file per module when possible.

1. Use `Fundamentals`, `Mediums`, and `Hards And Extensions` as the outer workbook sections.
2. Keep the module `## Topics` order stable inside those sections.
3. Within each band, follow the topic order from the module README.
4. Start with approachable problems for each topic, then add common mediums, then hard extensions.
5. For broad modules like trees, graphs, DP, backtracking, and heaps, avoid a flat topic list when the topic families are large enough to justify bands.

Do not repeat the same problem in multiple sections.

Numbered workbook entries must be concrete interview/LeetCode-style problem titles, not abstract lesson names. Use `## Topics` for concepts such as BFS, DFS, grid traversal, heaps, backtracking templates, or topological sort. Under each concrete problem, add a short `- Pattern:` note explaining the reusable idea.

If a problem comes from LeetCode, link the problem title to its LeetCode page in the workbook.

Favor broad mastery coverage over short fixed-size lists for every module. Heavy modules such as trees, graphs, DP, backtracking, and heaps should be especially broad and include as many high-value problems as the topic needs. If the workbook has a `Recommended Order`, treat it as the priority path only, not the full problem set.

Do not put a `Mastery Rule` section inside individual problem set workbooks. The global mastery rule belongs in the repo-level `README.md`.

## README Rules

1. Keep the README short.
2. Copy the topic order from the workbook.
3. Link module-local notes under `## Notes` when notes exist.
4. Copy the concrete problem order from the workbook.
5. Use `## Additional Notes` only for short clarifications.
6. Do not duplicate workbook explanations in the README.
7. Do not list abstract course units as problems in `## Problem Set`.
8. Do not repeat the global mastery rule in module READMEs unless the user explicitly asks for a module-specific variant.
9. If the module README lists LeetCode problems, include the associated LeetCode link beside the workbook link.

## Company Problem Set Rules

Company-specific files in `company_problem_sets/` should use one direct problem list:

1. Use `## Problem Set` as the only problem-list section.
2. Do not use `Warmups`, `Core`, `Stretch`, or `Major LeetCode Problems` headings.
3. List the main high-signal LeetCode-style problems directly.
4. Do not force a fixed problem count. Use as many problems as needed to cover the company's core live-coding techniques.
5. Larger target companies can have broader sets; smaller or secondary sets can be shorter if coverage is still strong.
6. Avoid excessive cross-company overlap. Repeat only deliberate anchor problems, and keep most company lists distinct by emphasizing that company's strongest patterns.
7. If many company files start sharing the same generic problems, replace lower-signal repeats with different high-signal problems from the same technique family.
8. Do not claim the list is an exact interview question dump.
9. Keep `## Review Modules` after the problem list.

## File Organization Rules

1. Keep filenames importable and stable.
2. Split code by pattern or concept when a module needs multiple files.
3. Keep design-style implementations inside the module that powers them.
4. Treat grids as implicit graphs inside the graphs module.
5. Keep advanced or lower-frequency topics in `17_advanced`.

## Verification Rules

1. Update tests when the workbook changes.
2. Run focused tests for the affected module.
3. Keep the README, workbook, and tests in sync.
