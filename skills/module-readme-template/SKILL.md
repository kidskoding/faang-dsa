---
name: module-readme-template
description: Create or update numbered DSA module README files with a consistent module header, topics, problem set index, and additional notes section.
---

# Module README Template

Use this skill when creating or updating a numbered module `README.md` in the DSA curriculum.

## Required Order

Each module README should follow this order:

1. `Module xx: _______`
2. `## Topics`
3. `## Problem Set`
4. `## Additional Notes`

## Content Rules

1. Keep the README minimal and index-like.
2. Use `## Topics` for the concepts covered by the module.
3. Use `## Problem Set` for the canonical ordered list of problems.
4. Use `## Additional Notes` only for short clarifications, edge-case reminders, or module-specific guidance.
5. Keep problem titles in the same order as the workbook.
6. Do not add long teaching prose, summaries, or duplicated workbook explanations.

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
2. Copy the topic order and problem order into the README.
3. Keep the README concise.
4. Update the README when the workbook order changes.
