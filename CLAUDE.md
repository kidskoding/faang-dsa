# faang-dsa

## Goal

A teaching-first DSA curriculum for SWE internship, co-op, and new-grad interviews targeting Meta, Amazon, Microsoft, Apple, Google, Airbnb, Bloomberg, Coinbase, Stripe, Salesforce, TikTok/ByteDance, Oracle, NVIDIA, Snowflake, Databricks, Capital One, IBM, OpenAI, ServiceNow, Uber, and analogous FAANG+ companies.

The repo should teach concepts deeply inside numbered module folders, provide from-scratch implementations/templates, and give guided practice that builds toward timed mixed interview performance.

---

## Core Principles

- Structure the curriculum by interview pattern, not traditional CS taxonomy.
- Use the numbered chapter folders as the source of truth.
- Teach concepts explicitly with chapter READMEs, focused comments, examples, tests, and guided practice.
- Implement data structures from scratch when the structure itself is being learned.
- Use normal Python interview tools (`dict`, `set`, `list`, `heapq`, `deque`) in problem solutions unless the point of the problem is to implement that structure.
- Prioritize high-frequency interview patterns before low-frequency advanced algorithms.
- Company-specific drilling belongs in `problem_sets/`; do not claim those are exact interview question lists.

---

## Structure

```text
faang-dsa/
├── 01_arrays/
├── 02_linked_lists/
├── 03_stacks_and_queues/
├── 04_recursion_backtracking/
├── 05_divide_conquer/
├── 06_searching/
├── 07_sorting/
├── 08_trees/
├── 09_heaps/
├── 10_intervals/
├── 11_disjoint_set/
├── 12_graphs/
├── 13_hash_tables/
├── 14_dp/
├── 15_bit_manipulation/
├── 16_greedy/
├── 17_tries/
├── 18_advanced/
├── 19_mixed_interview_practice/
├── problem_sets/
└── tests/
```

---

## Priority

Highest interview review priority:

1. Arrays, strings, hash maps, sets, prefix sums, two pointers, sliding window
2. Stacks/queues, binary search, trees
3. Graphs/grids, heaps, intervals
4. Backtracking, DP, greedy
5. Linked lists, tries, union find
6. Bit manipulation and advanced structures after the core is reliable

For Google specifically, overweight trees, graphs, recursion, backtracking, DP, and binary search on answer.

---

## Chapter Quality Bar

Each chapter should eventually include:

- concept explanation: what it is, when to use it, pitfalls, and complexity
- implementation: clear Python code for the structure or algorithm
- tests: normal cases, empty cases, one-element cases, repeated operations, and edge cases
- guided practice: warmups, core interview problems, follow-ups, and review problems

Guided practice belongs inside the numbered module folder that teaches the concept. Do not create a separate top-level `problems/` folder.

Company-specific drilling belongs in `problem_sets/`. These should be curated practice plans, not claims about exact company interview questions.

---

## Python Standards

- Python 3.11+
- pytest for testing
- type hints on all method signatures
- Files: `snake_case`
- Classes: `PascalCase`
- Methods: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
