______________________________________________________________________

## name: module-readme-template description: Create or update numbered DSA module README files with a consistent module header, topics, notes index, problem set index, and additional notes section.

# Module README Template

Use this skill when creating or updating a numbered module `README.md` in the DSA curriculum.

## Required Order

Each module README should follow this order:

1. `Module xx: _______`
2. `## Topics`
3. `## Notes`
4. `## Problem Set`
5. `## Additional Notes`

## Content Rules

1. Keep the README minimal and index-like.
2. Use `## Topics` for the concepts covered by the module.
3. Use `## Notes` for links to concept notes in the module-local `notes/` folder.
4. Name note files with sortable numeric prefixes such as `01_fundamentals.md`, `02_dfs.md`, and `03_bfs.md`.
5. Write notes in a pattern-study style similar to NeetCode or AlgoMonster: `Pattern`, `Intuition`, `How It Works`, `Template`, `Dry Run` or `Example`, `Complexity`, `Pitfalls`, and `Interview Checklist`.
6. Notes should be simple but thorough enough that the user can understand the technique before starting the problem set.
7. Do not add `Problems That Use This` sections to notes; the module README and workbook already list problems.
8. Use `## Problem Set` for the canonical ordered list of concrete interview/LeetCode-style problems.
9. Use `## Additional Notes` only for short clarifications, edge-case reminders, or module-specific guidance.
10. Keep problem titles in the same order as the workbook.
11. If the workbook is banded, keep the README order aligned with the same band progression and topic order.
12. Do not add long teaching prose, summaries, or duplicated workbook explanations.
13. Do not put abstract lesson names in `## Problem Set`; names like BFS, DFS, grid traversal, and topological sort belong in `## Topics`.
14. Do not put long concept explanations in the README; put them in `notes/`.
15. Do not repeat the global mastery rule in module READMEs unless the user explicitly asks for a module-specific variant.
16. If the problem comes from LeetCode, include the associated LeetCode link beside the workbook link.
17. For broad modules, mirror the workbook's `Fundamentals`, `Mediums`, and `Hards And Extensions` progression even if the README stays a flat index.

## Recommended Shape

```md
# Module xx: Name

## Topics

- Topic 1
- Topic 2

## Notes

1. [Topic 1](notes/01_topic_1.md)
2. [Topic 2](notes/02_topic_2.md)

## Problem Set

1. Problem One
2. Problem Two

## Additional Notes

- Optional short note
```

## Workflow

1. Read the module workbook/problem set first.
2. Copy the topic order and problem order into the README.
3. Add or update the notes index when module-local notes exist.
4. Keep the README concise.
5. Update the README when the workbook order changes.
