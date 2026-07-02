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

| Module | Technique |
|--------|-----------|
| 01 Arrays And Hashing | Hash maps and sets, prefix/suffix sums, frequency counting, Kadane's |
| 02 Two Pointers | Converging and fast/slow pointers on sorted or linear data |
| 03 Sliding Window | Contiguous subarray/substring under a constraint |
| 04 Stack | LIFO, monotonic stack, expression parsing, monotonic deque |
| 05 Binary Search | Search a sorted space or binary-search-on-answer |
| 06 Linked Lists | Pointer manipulation, fast/slow, reversal, merge/split |
| 07 Trees | DFS/BFS recursion, BST ordering, construction, serialization |
| 08 Heaps | Priority queue: top-K, two heaps, k-way merge |
| 09 Backtracking | Exhaustive search with pruning over choices |
| 10 Graphs | BFS/DFS, topological sort, union-find, shortest paths |
| 11 Dynamic Programming | Overlapping subproblems and optimal substructure |
| 12 Greedy Algorithms | Locally optimal choice justified by an exchange argument |
| 13 Intervals | Sort by endpoint, merge, sweep line, difference arrays |
| 14 Tries | Prefix tree for word and prefix queries |
| 15 Bit Manipulation | Bitwise ops, masks, XOR tricks, bitmask enumeration |
| 16 Math And Geometry | Number theory, matrix ops, coordinate geometry |
| 17 Advanced Topics | Union-find, segment/Fenwick trees, string algorithms, bitmask DP |
| 18 Mixed Interview Practice | Timed mixed-pattern drilling and mock interviews |
