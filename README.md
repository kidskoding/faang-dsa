# faang-dsa

dsa prep in Python for internship, co-op, and new-grad live coding interviews at top companies like Google, Facebook, and Bloomberg

## Goal

This repo is a teaching-first interview prep curriculum. It is organized around reusable live-coding patterns, not broad CS taxonomy. The target is to understand each pattern, implement it cleanly, test it, and recognize it under timed interview conditions

The practical goal is to solve most LeetCode mediums in 25-35 minutes with clear communication, clean complexity analysis, and solid edge-case handling.

## Mastery Rule

A problem is done only when you can:

1. explain the pattern
2. choose the right state, base case, or helper shape
3. write the core logic cleanly
4. pass the relevant tests
5. explain time and space complexity

## How To Prep

Start with [General Technical Interview Preparation](00_fundamentals/notes/01_how_to_prep.md) before choosing a module or company problem set.

The short version:

```text
learn pattern -> solve timed problems -> review misses -> re-solve -> mix topics
```

The notes are for understanding. The problem sets are for reps. The review loop is what makes the patterns automatic.

## Repository Layout

```text
faang-dsa/
├── 00_fundamentals/
├── 01_arrays_and_hashing/
├── 02_two_pointers/
├── 03_sliding_window/
├── 04_stack/
├── 05_binary_search/
├── 06_linked_lists/
├── 07_trees/
├── 08_heaps/
├── 09_backtracking/
├── 10_graphs/
├── 11_dp/
├── 12_greedy_algorithms/
├── 13_intervals/
├── 14_tries/
├── 15_bit_manipulation/
├── 16_math_geometry/
├── 17_advanced/
├── 18_mixed_interview_practice/
└── company_problem_sets/
```

## Order to Follow

| Module | Technique | Description |
|--------|-----------|-------------|
| 01 Arrays And Hashing | Hash maps and sets, prefix/suffix sums, frequency counting, Kadane's | Trade space for O(1) lookups and precompute running aggregates to answer range and subarray questions in one pass. |
| 02 Two Pointers | Converging and fast/slow pointers on sorted or linear data | Walk two indices in coordination to shrink a search space or detect structure without extra memory. |
| 03 Sliding Window | Contiguous subarray/substring under a constraint | Grow and shrink a window over a sequence to track the best or valid run that satisfies a condition. |
| 04 Stack | LIFO, monotonic stack, expression parsing, monotonic deque | Defer work on a stack to match pairs, evaluate expressions, and find next-greater/smaller elements. |
| 05 Binary Search | Search a sorted space or binary-search-on-answer | Halve the search range each step, either over sorted data or over a monotonic answer space. |
| 06 Linked Lists | Pointer manipulation, fast/slow, reversal, merge/split | Rewire node pointers in place to reverse, detect cycles, and restructure lists in O(1) space. |
| 07 Trees | DFS/BFS recursion, BST ordering, construction, serialization | Recurse to return information from subtrees and exploit BST ordering for search and traversal. |
| 08 Heaps | Priority queue: top-K, two heaps, k-way merge | Keep the extreme element cheap to access for streaming, top-K, and merge problems. |
| 09 Backtracking | Exhaustive search with pruning over choices | Build candidates incrementally and abandon branches that cannot lead to a valid solution. |
| 10 Graphs | BFS/DFS, topological sort, shortest paths | Model entities and relationships as nodes and edges to explore connectivity, ordering, and distance. |
| 11 Dynamic Programming | Overlapping subproblems and optimal substructure | Define a state and recurrence, then memoize or tabulate to avoid recomputing shared subproblems. |
| 12 Greedy Algorithms | Locally optimal choice justified by an exchange argument | Commit to the best immediate choice when a proof shows it stays optimal globally. |
| 13 Intervals | Sort by endpoint, merge, sweep line, difference arrays | Order intervals by start or end to merge overlaps, count concurrency, and schedule efficiently. |
| 14 Tries | Prefix tree for word and prefix queries | Store strings by shared prefixes for fast lookup, autocomplete, and wildcard matching. |
| 15 Bit Manipulation | Bitwise ops, masks, XOR tricks, bitmask enumeration | Operate directly on bits to encode sets compactly and exploit XOR cancellation. |
| 16 Math And Geometry | Number theory, matrix ops, coordinate geometry | Apply arithmetic, modular math, and coordinate reasoning to numeric and spatial problems. |
| 17 Advanced Topics | Union-find, segment/Fenwick trees, string algorithms, bitmask DP | Specialized structures and algorithms for range queries, pattern matching, and hard-tier interviews. |
| 18 Mixed Interview Practice | Timed mixed-pattern drilling and mock interviews | Recognize which pattern applies under time pressure across shuffled problems. |
