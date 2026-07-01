# Advanced Problem Set

## Goal

Push past general graph traversal into the structures and algorithms that show up when a
plain BFS/DFS is not enough: union-find connectivity, shortest-path extensions beyond
plain Dijkstra, minimum spanning trees, mutable range queries, and linear-time string
matching.

## How To Use

Work the file in order. The bands follow the module topic order: union find, shortest
paths, minimum spanning tree, range structures, then string algorithms. `10_graphs`
already drills general traversal, topological sort, and baseline weighted shortest
paths — this workbook stays narrow on the union-find/MST/range/string angle and only
repeats a title when it is the deliberate anchor problem for a technique.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Union Find

These problems teach disjoint set union with path compression and union by size/rank.

### 1. [Number Of Provinces](https://leetcode.com/problems/number-of-provinces/)

- Pattern: union adjacent cities from an adjacency matrix, then count roots.

### 2. [Number Of Islands II](https://leetcode.com/problems/number-of-islands-ii/)

- Pattern: online connectivity — union find answers component count after each add.

### 3. [Satisfiability Of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/)

- Pattern: union equal variables first, then check inequalities against roots.

### 4. [Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/)

- Pattern: union swappable indices into components, then sort each component independently.

## Shortest Paths Extensions

These problems teach shortest-path variants beyond a single unweighted or nonnegative-weight
run: relaxation-based algorithms, path counting, and all-pairs distances.

### 5. [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

- Pattern: Bellman-Ford style relaxation limited to k rounds.

### 6. [Number Of Ways To Arrive At Destination](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/)

- Pattern: Dijkstra distances plus a parallel count of shortest-path ways.

### 7. [Find The City With The Smallest Number Of Neighbors At A Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

- Pattern: Floyd-Warshall all-pairs shortest paths.

## Minimum Spanning Tree

These problems teach building a minimum-cost tree that connects every node, with Prim's
and Kruskal's algorithms.

### 8. [Min Cost To Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)

- Pattern: Prim's algorithm growing a tree from a min heap of frontier edges.

### 9. [Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)

- Pattern: Kruskal's algorithm with union find over sorted edges.

### 10. [Optimize Water Distribution In A Village](https://leetcode.com/problems/optimize-water-distribution-in-a-village/)

- Pattern: MST with a virtual node representing the free well option.

## Range Structures

These problems teach Fenwick tree (BIT) and segment tree style structures for mutable
range queries.

### 11. [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)

- Pattern: Fenwick tree supporting point update and prefix sum query.

### 12. [Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/)

- Pattern: 2D Fenwick tree combining row and column prefix sums.

### 13. [Count Of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

- Pattern: Fenwick tree over coordinate-compressed values, scanned right to left.

### 14. [Count Of Range Sum](https://leetcode.com/problems/count-of-range-sum/)

- Pattern: Fenwick tree over compressed prefix sums to count valid range sums.

## String Algorithms

These problems teach KMP's failure function and its use for pattern matching, prefix
reuse, and palindrome construction.

### 15. [Find The Index Of The First Occurrence In A String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

- Pattern: KMP pattern matching using a failure table to avoid backtracking the text pointer.

### 16. [Repeated String Match](https://leetcode.com/problems/repeated-string-match/)

- Pattern: build a candidate string by repetition, then KMP search for the pattern.

### 17. [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)

- Pattern: KMP failure function on `s + separator + reverse(s)` finds the longest palindromic prefix.

### 18. [Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/)

- Pattern: the KMP failure function's final value is the longest proper prefix that is also a suffix.

## Divide And Conquer

These problems teach the divide/conquer/combine recurrence pattern: splitting
on structure (operators, spatial coordinates, array halves) and combining sub-results with a
non-trivial merge step.

### 19. [Different Ways To Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/)

- Pattern: split on each operator, recursively solve both sides, combine every result pair.

### 20. [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

- Pattern: divide buildings in half, recursively get each skyline, merge with a line sweep.

### 21. Closest Pair Of Points

- Not on LeetCode as a standalone problem (classic algorithm, sometimes asked directly in
  interviews); implement the divide-and-conquer version yourself.
- Pattern: divide by x-coordinate, recurse on each half, combine by checking a narrow strip.

### 22. [Beautiful Array](https://leetcode.com/problems/beautiful-array/)

- Pattern: recursively build odd/even-biased halves whose combination avoids arithmetic triples.

## Bitmask DP

These problems teach state-compression DP: `dp[mask]` (or `dp[mask][i]`) tracks the best
result for each subset of items, built up by adding one unset item at a time. `Shortest
Path Visiting All Nodes` is skipped here — it already anchors `10_graphs` as problem 53 and
this workbook does not repeat a title outside its deliberate anchor module.

### 23. [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

- Pattern: `dp[mask]` tracks which numbers are already placed into a completed bucket.

### 24. [Smallest Sufficient Team](https://leetcode.com/problems/smallest-sufficient-team/)

- Pattern: `dp[skill_mask]` stores the smallest team (as a set of people) covering that skill mask.

### 25. [Parallel Courses II](https://leetcode.com/problems/parallel-courses-ii/)

- Pattern: `dp[mask]` stores the minimum semesters to complete exactly the courses in mask, transitioning by taking any valid subset of newly-available courses each round.
