# faang-dsa

DSA prep in Python for internship, co-op, and new-grad interviews at Meta, Amazon, Microsoft, Apple, Google, Airbnb, Bloomberg, Coinbase, Stripe, Slack / Salesforce, TikTok/ByteDance, Oracle, NVIDIA, Snowflake, Databricks, Capital One, IBM, OpenAI, ServiceNow, Uber, and analogous FAANG+ companies.

## Goal

This repo is a teaching-first DSA curriculum for big-tech live coding interviews. It should help you understand each concept from the ground up, implement it cleanly, practice it with guided problems, and then recognize it under mixed interview conditions.

The target is to solve most LeetCode mediums in 25-35 minutes with clean code, clear complexity analysis, and good edge-case coverage.

## Learning Model

Each module should eventually have four layers:

1. Concept explanation: what the idea is, when to use it, common traps, and complexity.
2. From-scratch implementation: the data structure or algorithm written clearly in Python.
3. Tests: normal cases, edge cases, and failure cases.
4. Guided practice: warmups, core interview problems, follow-ups, and review problems.

The numbered folders are modules. Each module owns the full learning experience for that subject: lessons, implementations, tests, and guided practice.

## Repository Layout

```text
faang-dsa/
├── 00_fundamentals/
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
└── problem_sets/
```

## Guided Curriculum

Work through the curriculum module by module. Each module has the same loop:

1. Read the module folder `README.md`.
2. Study the implementation files.
3. Run or expand the module-local tests.
4. Complete warmup practice.
5. Complete core practice.
6. Do one review problem without hints before moving on.

### Module 00: Fundamentals

Goal: build the baseline reasoning needed for every later module.

Study:

- Time complexity
- Space complexity
- Output space versus auxiliary space
- Recursion call stacks
- Common array, tree, graph, heap, and hash-map complexity patterns

Practice:

- For every implementation, write `Input size`, `Time`, and `Space`
- Explain the complexity out loud in one sentence
- Revisit this module whenever a Big-O explanation feels unclear

### Module 01: Arrays

Goal: master the highest-frequency array, string, and hashing patterns.

Study:

- Dynamic arrays
- Strings as arrays
- Prefix / suffix sums
- Two pointers
- Sliding window
- Running state
- Kadane's algorithm
- Matrix basics

Practice:

- Warmups: Two Sum, Best Time to Buy and Sell Stock, Valid Palindrome
- Core: Product Except Self, Subarray Sum Equals K, Longest Substring Without Repeating Characters, Minimum Window Substring, Minimum Size Subarray Sum, Maximum Subarray, Spiral Matrix, Rotate Image
- Follow-ups: handle negatives, duplicates, empty inputs, Unicode/string assumptions, and variable window constraints
- Review: solve a random array problem without knowing the pattern first

### Module 02: Linked Lists

Goal: learn pointer manipulation and linked-list interview patterns.

Study:

- Singly linked lists
- Doubly linked lists
- Fast / slow pointers
- Reversal patterns
- Cycle detection
- Merge and split patterns

Practice:

- Warmups: Reverse Linked List, Merge Two Sorted Lists
- Core: Linked List Cycle, Remove Nth Node From End, Reorder List, Add Two Numbers
- Follow-ups: cycle entry, odd/even splitting, in-place constraints

### Module 03: Stacks And Queues

Goal: learn LIFO/FIFO structures and range patterns built on them.

Study:

- Stack and queue mechanics
- Deques
- Monotonic stack
- Monotonic queue
- Expression parsing basics

Practice:

- Warmups: Valid Parentheses, Implement Queue Using Stacks
- Core: Min Stack, Daily Temperatures, Next Greater Element, Evaluate Reverse Polish Notation, Sliding Window Maximum
- Follow-ups: expression parsing, duplicate values in monotonic structures, max/min window maintenance

### Module 04: Recursion And Backtracking

Goal: build recursive reasoning and systematic search over choices.

Study:

- Recursion base cases
- Recursive call stacks
- Subsets
- Permutations
- Combinations
- Constraint backtracking
- Grid backtracking

Practice:

- Warmups: Subsets, Permutations
- Core: Combination Sum, Generate Parentheses, Palindrome Partitioning, Word Search, N-Queens-style constraint search
- Follow-ups: pruning, duplicate handling, recursion-to-iteration

### Module 05: Divide And Conquer

Goal: learn how to split problems, solve subproblems, and combine results.

Study:

- Recursive decomposition
- Merge-style combine steps
- Partitioning
- Recurrence analysis

Practice:

- Warmups: Merge two sorted arrays, recursive array sum
- Core: Sort List, Kth Largest Element, Count Inversions
- Follow-ups: stability, in-place partitioning, recursion depth

### Module 06: Searching

Goal: master binary search as both an algorithm and a problem-solving technique.

Study:

- Linear search
- Binary search
- Boundary search
- Rotated arrays
- Search on answer

Practice:

- Warmups: Binary Search, Search Insert Position
- Core: Search in Rotated Sorted Array, Find Minimum in Rotated Sorted Array, Time Based Key-Value Store, Koko Eating Bananas, Capacity to Ship Packages, Split Array Largest Sum
- Follow-ups: duplicate values, impossible cases, off-by-one boundaries

### Module 07: Sorting

Goal: understand sorting mechanics, tradeoffs, and how sorting enables interview patterns.

Study:

- Bubble, selection, and insertion sort
- Merge sort
- Quick sort
- Heap sort
- Stability
- Comparator/key-based sorting

Practice:

- Warmups: Sort Colors, Merge Sorted Array
- Core: K Closest Points, Meeting Rooms, Largest Number
- Follow-ups: stability, custom keys, sorting vs heap tradeoffs

### Module 08: Trees

Goal: build strong tree traversal and recursive reasoning.

Study:

- Binary trees
- DFS traversals
- BFS / level order
- Binary search trees
- Depth, diameter, path, and LCA patterns
- Subtree and symmetry patterns
- Serialization
- Balancing concepts

Practice:

- Warmups: Maximum Depth, Invert Binary Tree
- Core: Diameter of Binary Tree, Level Order Traversal, Validate BST, Lowest Common Ancestor, Path Sum II, Same Tree, Subtree of Another Tree, Serialize and Deserialize Binary Tree
- Follow-ups: iterative traversal, parent pointers, duplicate values

### Module 09: Heaps

Goal: learn priority queues for top-K, scheduling, merging, and streaming problems.

Study:

- Min heap
- Max heap
- Two heaps
- Top-K
- K-way merge
- Median stream
- Scheduling with priorities
- Lazy deletion

Practice:

- Warmups: Kth Largest Element, Last Stone Weight
- Core: Top K Frequent Elements, K Closest Points, Merge K Sorted Lists, Find Median From Data Stream, Task Scheduler
- Follow-ups: bounded heap size, lazy deletion, tuple priorities

### Module 10: Intervals

Goal: learn how to sort, merge, compare, and schedule ranges.

Study:

- Merge intervals
- Insert interval
- Meeting rooms
- Overlap detection
- Sweep-line basics
- Calendar / booking patterns

Practice:

- Warmups: Merge Intervals, Insert Interval
- Core: Meeting Rooms II, Non-overlapping Intervals, Minimum Arrows to Burst Balloons, Employee Free Time, My Calendar basics
- Follow-ups: closed vs half-open intervals, tie-breaking, sweep-line events

### Module 11: Disjoint Set

Goal: learn union find for grouping, connectivity, and cycle detection.

Study:

- Parent arrays
- Path compression
- Union by rank / size
- Connected components
- Cycle detection

Practice:

- Warmups: Find if Path Exists
- Core: Number of Connected Components, Redundant Connection, Accounts Merge
- Follow-ups: union by size vs rank, dynamic components

### Module 12: Graphs

Goal: handle graph traversal, connectivity, ordering, and shortest-path problems.

Study:

- Graph representations
- BFS and DFS
- Cycle detection
- Matrix / grid traversal
- Multi-source BFS
- Topological sort
- Bipartite graphs
- Connected components

Practice:

- Warmups: Number of Islands, Flood Fill, Find if Path Exists
- Core: Clone Graph, Rotting Oranges, Shortest Path in Binary Matrix, Course Schedule, Pacific Atlantic Water Flow, Is Graph Bipartite, Redundant Connection, Network Delay Time
- Follow-ups: visited-state encoding, multi-source initialization, directed vs undirected cycles

### Module 13: Hash Tables

Goal: understand hash table internals and use hashing patterns fluently.

Study:

- Hash table implementation
- Collision handling
- Load factor
- Rehashing
- Frequency maps
- String hashing patterns
- Ordered/hash-set tradeoffs
- Bloom filters

Practice:

- Warmups: Contains Duplicate, Valid Anagram
- Core: Group Anagrams, Longest Consecutive Sequence, Subarray Sum Equals K, Design HashMap, LRU Cache basics
- Follow-ups: custom keys, collision behavior, memory tradeoffs

### Module 14: Dynamic Programming

Goal: learn to model states and transitions instead of memorizing solutions.

Study:

- 1D DP
- 2D DP
- Grid DP
- Knapsack-style DP
- Decision DP
- Longest increasing subsequence
- Longest common subsequence
- Palindrome DP
- Interval DP basics

Practice:

- Warmups: Climbing Stairs, House Robber, Min Cost Climbing Stairs
- Core: Coin Change, Decode Ways, Longest Increasing Subsequence, Unique Paths, Longest Common Subsequence, Partition Equal Subset Sum, Word Break, Palindromic Substrings
- Follow-ups: reconstruct answer, reduce memory, compare top-down vs bottom-up

### Module 15: Bit Manipulation

Goal: learn masks, shifts, XOR, and binary-state tricks.

Study:

- Bitwise operators
- Masks
- Shifts
- XOR patterns
- Counting bits
- Subset masks

Practice:

- Warmups: Single Number, Number of 1 Bits
- Core: Counting Bits, Missing Number, Reverse Bits, Subsets with bit masks
- Follow-ups: signed integers, overflow assumptions, mask construction

### Module 16: Greedy

Goal: learn when local choices lead to globally optimal solutions.

Study:

- Activity selection
- Jump game
- Gas station
- Task scheduler
- Sorting-based greedy
- Exchange arguments
- Heap-assisted greedy

Practice:

- Warmups: Assign Cookies, Best Time to Buy and Sell Stock
- Core: Jump Game, Jump Game II, Gas Station, Task Scheduler, Non-overlapping Intervals, Partition Labels
- Follow-ups: prove correctness, find counterexamples, compare greedy vs DP

### Module 17: Tries

Goal: learn prefix trees for string lookup, prefix search, and grid-word problems.

Study:

- Trie nodes
- Insert and search
- Prefix search
- Word dictionary patterns
- Trie plus DFS
- Autocomplete / prefix ranking basics

Practice:

- Warmups: Implement Trie
- Core: Design Add and Search Words Data Structure, Word Search II, Replace Words, Search Suggestions System
- Follow-ups: memory tradeoffs, deleting words, trie plus backtracking

### Module 18: Advanced

Goal: round out lower-frequency but useful topics and sharpen proof-style reasoning.

Study:

- Segment tree
- Fenwick tree
- KMP and Z-algorithm
- MST algorithms
- Floyd-Warshall
- Advanced DP examples
- Rolling hash
- Monotonic binary search / advanced feasibility

Practice:

- Warmups: Range Sum Query Mutable, Implement strStr
- Core: Count of Smaller Numbers After Self, Longest Happy Prefix, Repeated DNA Sequences, Edit Distance, Burst Balloons, Floyd-Warshall-style all-pairs shortest paths
- Follow-ups: coordinate compression, memory reduction, when advanced structures are overkill

### Module 19: Mixed Interview Practice

Goal: stop relying on topic labels and practice like the real interview.

Do this after Modules 01-14 are comfortable.

Weekly loop:

1. Pick 6-10 mixed problems across arrays, linked lists, stacks, binary search, trees, graphs, heaps, backtracking, and DP.
2. Solve each with a 35-minute timer.
3. After each problem, write the missed pattern or bug in the relevant module folder.
4. Re-solve missed problems 3-7 days later.
5. Do one mock interview where you explain before and during coding.

Ready signal:

- Easy problems: 10-15 minutes
- Medium problems: 25-35 minutes
- Hard problems: can make meaningful progress and explain the intended direction
- You consistently explain brute force, optimized approach, complexity, and edge cases

## Target Companies

1. Meta
2. Amazon
3. Microsoft
4. Apple
5. Google
6. Airbnb
7. Bloomberg
8. Coinbase
9. Stripe
10. Slack / Salesforce
11. TikTok/ByteDance
12. Oracle
13. NVIDIA
14. Snowflake
15. Databricks
16. Capital One
17. IBM
18. OpenAI
19. ServiceNow
20. Uber

## Company Emphasis

- Meta, TikTok/ByteDance, Uber: speed on arrays, strings, trees, graphs, heaps, backtracking, and clean implementation.
- Google, OpenAI, Databricks: deeper reasoning on trees, graphs, recursion, DP, backtracking, and optimization tradeoffs.
- Amazon, Microsoft, Apple: balanced LeetCode coverage plus clear communication, edge cases, and behavioral/project stories.
- Stripe, Coinbase, Bloomberg: practical coding, debugging, data modeling, strings/maps, correctness under constraints, and clean code.
- Airbnb, Snowflake, NVIDIA: graphs, DP, system-adjacent problem solving, performance awareness, and careful design choices.
- Slack / Salesforce, Oracle, IBM, ServiceNow, Capital One: strong fundamentals, arrays/hash maps, trees, BFS/DFS, OOP/design-style coding, and reliable communication.

## FAANG+ Generalization

This curriculum also applies to AMD, Snap, DoorDash, Roblox, Palantir, Ramp, Robinhood, Rippling, fintechs, AI startups, infrastructure companies, and other FAANG+ loops.

- Product-heavy companies: arrays, strings, hash maps, trees, graphs, practical debugging, and design-style coding.
- Infrastructure/data companies: graphs, heaps, intervals, DP, binary search on answer, and performance tradeoffs.
- Hardware/AI/platform companies: arrays, graphs, DP, bit manipulation, performance, and clean low-level reasoning.
- Startup-style loops: fast implementation, practical edge cases, data modeling, and readable code.
