# faang-dsa

## Goal

A Python repo for FAANG interview prep and competitive programming — deep, from-scratch implementations of data structures and algorithms, tested thoroughly, with problems to reinforce each topic.

---

## Core Principles

- Everything is implemented from scratch — no standard library collections for the structure being learned
- Prefer clarity over cleverness; this is a learning repo
- Every structure has an implementation file and a test file
- No notes, no docs, no theory files

---

## Structure

```text
faang-dsa/
├── README.md
├── arrays/
│   ├── dynamic_array.py
│   └── ...
├── linked_lists/
├── stacks-and-queues/
├── hash_tables/
├── trees/
├── heaps/
├── graphs/
├── sorting/
├── searching/
├── dp/
├── greedy/
├── tries/
├── disjoint_set/
├── tests/
│   ├── test_arrays.py
│   ├── test_linked_lists.py
│   ├── test_stacks.py
│   ├── test_queues.py
│   ├── test_hash_tables.py
│   ├── test_trees.py
│   ├── test_heaps.py
│   ├── test_graphs.py
│   ├── test_sorting.py
│   ├── test_searching.py
│   ├── test_dp.py
│   ├── test_greedy.py
│   ├── test_tries.py
│   └── test_disjoint_set.py
└── problems/
    ├── topic_based/
    └── mixed_review/
```

---

## File Pattern

For each concept:

```text
linked_lists/singly_linked_list.py
tests/test_singly_linked_list.py
```

---

## Implementation Order

1.  dynamic array
2.  arrays and hashing techniques
3.  prefix / suffix sums
4.  two pointers
5.  sliding window (fixed and variable)
6.  Kadane's algorithm (maximum subarray)
7.  singly linked list
8.  doubly linked list
9.  fast & slow pointers
10. stacks, queues, deques
11. monotonic stack / queue
12. recursion and backtracking (subsets, permutations)
13. divide and conquer
14. searching algorithms (linear, binary)
15. binary search as a technique (rotated arrays, search on answer, boundaries)
16. sorting algorithms (bubble, selection, insertion, merge, quick, heap)
17. binary tree
18. tree traversals (inorder, preorder, postorder, level-order)
20. binary search tree
21. BST balancing concepts
22. AVL tree
23. heaps / priority queues
24. two heaps (top-K and k-way merge patterns)
25. intervals (merge intervals, insert interval, meeting rooms)
26. disjoint set union (union find)
27. graph representations (adjacency list, adjacency matrix)
28. graph traversals (BFS, DFS) + cycle detection
29. matrix / 2D grid traversal
30. topological sort (Kahn's algorithm, DFS-based)
31. minimum spanning tree (Kruskal's, Prim's)
32. graph algorithms (Dijkstra, Bellman-Ford, Floyd-Warshall)
33. hash table
34. bloom filter
35. dynamic programming
36. bit manipulation
37. greedy algorithms (activity selection, jump game, gas station, task scheduler)
38. trie
39. advanced topics (bit manipulation, knapsack problem, LCS, segment tree, fenwick tree, KMP, Z-algorithm)

---

## Testing Requirements

Every implementation must be tested for:

- normal cases
- empty structure
- one-element
- repeated inserts and deletes
- edge conditions

---

## Naming Conventions

- Files: `snake_case` — e.g. `singly_linked_list.py`
- Classes: `PascalCase` — e.g. `SinglyLinkedList`
- Methods: `snake_case` — e.g. `push_back`
- Constants: `UPPER_SNAKE_CASE` — e.g. `INITIAL_CAPACITY`

---

## Python Standards

- Python 3.11+
- pytest for testing
- type hints on all method signatures

Each class should handle:
- `__init__`, `__len__`, `__repr__` where applicable
- `__iter__` where it makes sense
- no use of `list`, `dict`, `deque`, `heapq` etc. for the structure being implemented

---

## Problems

The `problems/` folder is for coding problems only — no solution writeups, no notes. Just `.py` files with a problem statement in a comment at the top and a solution below.
