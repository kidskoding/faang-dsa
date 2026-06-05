---
name: dsa-curriculum-workflow
description: Streamline DSA module updates across the repo by keeping module READMEs, workbooks, tests, and implementation files aligned to one consistent curriculum workflow.
---

# DSA Curriculum Workflow

Use this skill when creating, revising, or renaming any numbered DSA module in this repo.

## Workflow

1. Read the module README and workbook first.
2. Decide the module's place in the curriculum order.
3. Keep the module README minimal and index-like.
4. Keep the workbook as the canonical problem ladder.
5. Keep implementation files split by concept, not by arbitrary size.
6. Keep tests grouped by the same problem sections.
7. Verify with targeted tests before moving on.

## Required Structure

For every module:

1. `Module xx: Name`
2. `## Topics`
3. `## Problem Set`
4. `## Additional Notes`

## Workbook Structure

Use one canonical workbook file per module when possible.

1. Fundamentals
2. Core mediums
3. Hard problems and extensions

Do not repeat the same problem in multiple sections.

## README Rules

1. Keep the README short.
2. Copy the topic order from the workbook.
3. Copy the problem order from the workbook.
4. Use `## Additional Notes` only for short clarifications.
5. Do not duplicate workbook explanations in the README.

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
