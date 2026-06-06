______________________________________________________________________

## name: module-readme-template description: Create or update numbered DSA module README files with a consistent module header, topics, problem set index, and additional notes section.

# Module README Template

Use this skill when creating or updating a numbered module `README.md` in the DSA curriculum.

## Required Order

Each module README should follow this order:

1. `Module xx: _______`
1. `## Topics`
1. `## Problem Set`
1. `## Additional Notes`

## Content Rules

1. Keep the README minimal and index-like.
1. Use `## Topics` for the concepts covered by the module.
1. Use `## Problem Set` for the canonical ordered list of concrete interview/LeetCode-style problems.
1. Use `## Additional Notes` only for short clarifications, edge-case reminders, or module-specific guidance.
1. Keep problem titles in the same order as the workbook.
1. If the workbook is banded, keep the README order aligned with the same band progression and topic order.
1. Do not add long teaching prose, summaries, or duplicated workbook explanations.
1. Do not put abstract lesson names in `## Problem Set`; names like BFS, DFS, grid traversal, and topological sort belong in `## Topics`.
1. Do not repeat the global mastery rule in module READMEs unless the user explicitly asks for a module-specific variant.
1. If the problem comes from LeetCode, include the associated LeetCode link beside the workbook link.
1. For broad modules, mirror the workbook's `Fundamentals`, `Mediums`, and `Hards And Extensions` progression even if the README stays a flat index.

## Recommended Shape

```md
# Module xx: Name

## Topics

- Topic 1
- Topic 2

## Problem Set

1. Problem One
2. Problem Two

## Additional Notes

- Optional short note
```

## Workflow

1. Read the module workbook/problem set first.
1. Copy the topic order and problem order into the README.
1. Keep the README concise.
1. Update the README when the workbook order changes.
