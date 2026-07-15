# faang-dsa

## Goal

A teaching-first DSA curriculum for SWE internship, co-op, and new-grad interviews targeting Meta, Amazon, Microsoft, Apple, Google, Airbnb, Bloomberg, Coinbase, Palantir, Salesforce, TikTok/ByteDance, Oracle, NVIDIA, Snowflake, Databricks, Capital One, IBM, OpenAI, ServiceNow, Uber, and analogous FAANG+ companies.

The repo should teach concepts deeply inside numbered module folders, provide from-scratch implementations/templates, and give guided practice that builds toward timed mixed interview performance.

______________________________________________________________________

## Core Principles

- Structure the curriculum by interview pattern, not traditional CS taxonomy.
- Use the numbered chapter folders as the source of truth.
- Teach concepts explicitly with chapter READMEs, focused comments, examples, tests, and guided practice.
- Implement data structures from scratch when the structure itself is being learned.
- Use normal Python interview tools (`dict`, `set`, `list`, `heapq`, `deque`) in problem solutions unless the point of the problem is to implement that structure.
- Prioritize high-frequency interview patterns before low-frequency advanced algorithms.
- Keep each numbered module's problem set single-technique. A problem stays in a module if that module's technique solves it cleanly, even when another pattern (e.g. DP) is an alternative solution. A problem that genuinely requires chaining two or more patterns to solve belongs in `18_mixed_interview_practice/`, not a single-technique module.
- Company-specific drilling belongs in `company_problem_sets/`; do not claim those are exact interview question lists.

______________________________________________________________________

## Structure

```text
faang-dsa/
├── 00_fundamentals/
├── 01_arrays_and_hashing/
├── 02_two_pointers/
├── 03_stack/
├── 04_sliding_window/
├── 05_binary_search/
├── 06_linked_lists/
├── 07_trees/
├── 08_heaps/
├── 09_backtracking/
├── 10_graphs/
├── 11_dp/
├── 12_greedy/
├── 13_intervals/
├── 14_tries/
├── 15_bit_manipulation/
├── 16_math_geometry/
├── 17_advanced/
├── 18_mixed_interview_practice/
└── company_problem_sets/
```

______________________________________________________________________

## Priority

Highest interview review priority:

1. Arrays, strings, hash maps, sets, prefix sums, two pointers, sliding window
1. Stacks/queues, binary search, trees
1. Heaps, backtracking, graphs/grids, intervals
1. Backtracking, DP, greedy
1. Linked lists and tries
1. Union find, shortest paths, sorting internals, and advanced structures after the core is reliable

For Google specifically, overweight trees, graphs, recursion, backtracking, DP, and binary search on answer.

______________________________________________________________________

## Chapter Quality Bar

Each chapter should eventually include:

- concept explanation: what it is, when to use it, pitfalls, and complexity
- implementation: clear Python code for the structure or algorithm
- tests: module-local tests under that module's `tests/` folder
- guided practice: warmups, core interview problems, follow-ups, and review problems

Guided practice belongs inside the numbered module folder that teaches the concept. Do not create a separate top-level `problems/` folder.

Size each technique section (each `.py` file / `##` section in a module problem set) to the number of problems that actually builds mastery of that technique — enough coverage to go from warmup to hard and drill the pattern until it is automatic, not a fixed count. Do not leave a section thin (roughly, fewer than 4-5 problems is a smell); if migrating problems out leaves a section sparse, backfill it with more problems of that same technique. The number of problems is the lever that ensures mastery, so err toward more coverage per technique rather than a minimal set.

Tests belong inside the numbered module folder that owns the concept. Do not create a separate top-level `tests/` folder.

Company-specific drilling belongs in `company_problem_sets/`. These should be curated practice plans, not claims about exact company interview questions. Company files should use one `## Problem Set` section with the main high-signal LeetCode-style problems, followed by `## Review Modules`; do not split company files into `Warmups`, `Core`, `Stretch`, or `Major LeetCode Problems`. Do not force a fixed problem count; include enough problems to cover the company's core live-coding techniques. Avoid excessive cross-company overlap by repeating only deliberate anchor problems and otherwise choosing different high-signal problems from the same technique family.

______________________________________________________________________

## Python Standards

- Python 3.11+
- pytest for testing
- type hints on all method signatures
- Files: `snake_case`
- Classes: `PascalCase`
- Methods: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
