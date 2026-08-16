# Advanced Problem Set

## Goal

Push past general graph traversal into the structures and algorithms that
show up when a plain BFS/DFS is not enough: union-find connectivity,
shortest-path extensions beyond plain Dijkstra, minimum spanning trees,
mutable range queries, linear-time string matching, divide and conquer, and
bitmask DP. Learn each technique from its solution file, then use it on the
medium and hard problems that carry it in LeetCode-style interviews.

## How To Use

Each section maps to one solution file in this folder and to one advanced
technique. Work a section top to bottom: problems are ordered roughly easy
to hard, and the implemented ones come first. `solves:` names the function
in that section's file; `solves: (todo)` means the solution is not written
yet. `10_graphs` already drills general traversal, topological sort, and
baseline weighted shortest paths — this workbook stays narrow on the
union-find/MST/range/string angle and only repeats a title when it is the
deliberate anchor for a technique.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Union Find

`union_find_problems.py` — disjoint set union with path compression and
union by size; connectivity queries in near-constant amortized time.

### 1. [Number Of Provinces](https://leetcode.com/problems/number-of-provinces/)

- solves: `number_of_provinces`
- Pattern: union adjacent cities from the adjacency matrix, then count distinct roots.

### 2. [Number Of Islands II](https://leetcode.com/problems/number-of-islands-ii/)

- solves: `number_of_islands_ii`
- Pattern: online connectivity — union each new land cell with its land neighbors, track live count.

### 3. [Satisfiability Of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/)

- solves: `equations_possible`
- Pattern: union all "==" pairs first, then reject any "!=" pair sharing a root.

### 4. [Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/)

- solves: `smallest_string_with_swaps`
- Pattern: union swappable indices into components, then sort each component's letters.

### 5. [Redundant Connection](https://leetcode.com/problems/redundant-connection/)

- solves: `find_redundant_connection`
- Pattern: add edges one at a time; the first whose endpoints already share a root closes the cycle.

### 6. [Evaluate Division](https://leetcode.com/problems/evaluate-division/)

- solves: `calc_equation`
- Pattern: weighted union-find carrying edge ratios (or graph DFS).

## Shortest Paths Extensions

`shortest_paths_problems.py` — shortest-path variants beyond a single
nonnegative-weight run: bounded relaxation, path counting, and all-pairs
distances.

### 7. [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

- solves: `find_cheapest_price`
- Pattern: Bellman-Ford style relaxation over at most `k + 1` rounds.

### 8. [Number Of Ways To Arrive At Destination](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/)

- solves: `count_paths`
- Pattern: Dijkstra distances plus a parallel ways-count updated during relaxation.

### 9. [Find The City With The Smallest Number Of Neighbors At A Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

- solves: `find_the_city`
- Pattern: Floyd-Warshall all-pairs shortest paths, then compare reachable-city counts.

### 10. [Network Delay Time](https://leetcode.com/problems/network-delay-time/)

- solves: `network_delay_time`
- Pattern: single-source Dijkstra; the answer is the maximum shortest-path distance over all nodes.

### 11. [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)

- solves: `minimum_effort_path`
- Pattern: Dijkstra variant minimizing the maximum edge weight (min-max path) on a grid.

## Minimum Spanning Tree

`mst_problems.py` — build a minimum-cost tree that connects every node with
Prim's and Kruskal's algorithms.

### 12. [Min Cost To Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)

- solves: `min_cost_connect_points`
- Pattern: Prim's algorithm growing a tree from a min heap of frontier edges.

### 13. [Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)

- solves: `min_cost_connecting_cities`
- Pattern: Kruskal's algorithm — sort edges, union find skips cycle-forming edges.

### 14. [Optimize Water Distribution In A Village](https://leetcode.com/problems/optimize-water-distribution-in-a-village/)

- solves: `min_cost_to_supply_water`
- Pattern: treat each well as an edge from a virtual node 0, then run Kruskal's/Prim's.

### 15. [Find Critical And Pseudo-Critical Edges In Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)

- solves: `find_critical_and_pseudo_critical_edges`
- Pattern: compare the baseline MST weight against forcing each edge out (critical) or in (pseudo-critical).

### 16. [Checking Existence Of Edge Length Limited Paths](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/)

- solves: `distance_limited_paths_exist`
- Pattern: offline Kruskal — sort edges and queries by weight, union up to each limit, then test connectivity.

## Range Structures

`range_structures_problems.py` — Fenwick tree (BIT) structures for mutable
range queries: point update with prefix/range sum in logarithmic time.

### 17. [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)

- solves: `NumArray`
- Pattern: Fenwick tree supporting point update and prefix sum query.

### 18. [Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/)

- solves: `NumMatrix`
- Pattern: 2D Fenwick tree combining row and column prefix sums.

### 19. [Count Of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

- solves: `count_smaller`
- Pattern: Fenwick tree over coordinate-compressed values, scanned right to left.

### 20. [Count Of Range Sum](https://leetcode.com/problems/count-of-range-sum/)

- solves: `count_range_sum`
- Pattern: Fenwick tree over compressed prefix sums counts sums in `[lower, upper]`.

### 21. [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)

- solves: `reverse_pairs`
- Pattern: Fenwick tree (or merge sort) counting pairs where one value exceeds twice another.

### 22. [My Calendar III](https://leetcode.com/problems/my-calendar-iii/)

- solves: `MyCalendarThree`
- Pattern: segment tree with lazy propagation (range update, range-max query).

## String Algorithms

`string_algorithms_problems.py` — KMP's failure function and Rabin-Karp
hashing for linear-time matching, prefix reuse, and palindrome construction.

### 23. [Find The Index Of The First Occurrence In A String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

- solves: `str_str`
- Pattern: KMP failure table lets the pattern pointer fall back without rewinding the text.

### 24. [Repeated String Match](https://leetcode.com/problems/repeated-string-match/)

- solves: `repeated_string_match`
- Pattern: repeat `a` until it is at least as long as `b`, then KMP search for `b`.

### 25. [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)

- solves: `shortest_palindrome`
- Pattern: failure table of `s + separator + reverse(s)` gives the longest palindromic prefix.

### 26. [Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/)

- solves: `longest_prefix`
- Pattern: the last value of the KMP failure table is the longest prefix that is also a suffix.

### 27. [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)

- solves: `repeated_substring_pattern`
- Pattern: the KMP failure function reveals the smallest repeating block when `n % (n - lps[-1]) == 0`.

## Divide And Conquer

`divide_and_conquer_problems.py` — the divide/conquer/combine recurrence:
split on structure (operators, coordinates, array halves) and combine
sub-results with a non-trivial merge.

### 28. [Different Ways To Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/)

- solves: `diff_ways_to_compute`
- Pattern: split on each operator, recursively solve both sides, combine every result pair.

### 29. [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

- solves: `get_skyline`
- Pattern: divide buildings in half, recursively get each skyline, merge with a line sweep.

### 30. Closest Pair Of Points

- solves: `closest_pair`
- Pattern: divide by x-coordinate, recurse on each half, combine by checking a narrow strip.

### 31. [Beautiful Array](https://leetcode.com/problems/beautiful-array/)

- solves: `beautiful_array`
- Pattern: recursively build odd/even-biased halves whose combination avoids arithmetic triples.

### 32. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

- solves: `max_sub_array`
- Pattern: divide in half; the best subarray is in the left, the right, or crosses the midpoint.

### 33. [Median Of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

- solves: `find_median_sorted_arrays`
- Pattern: binary-search the partition point in the shorter array so both halves balance.

## Bitmask DP

`bitmask_dp_problems.py` — state-compression DP where `dp[mask]` (or
`dp[mask][i]`) tracks the best result for each subset, built up one unset
item at a time.

### 34. [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

- solves: `can_partition_k_subsets`
- Pattern: `dp[mask]` tracks which numbers are already placed into a completed bucket.

### 35. [Smallest Sufficient Team](https://leetcode.com/problems/smallest-sufficient-team/)

- solves: `smallest_sufficient_team`
- Pattern: `dp[skill_mask]` stores the smallest team (as a set of people) covering that skill mask.

### 36. [Parallel Courses II](https://leetcode.com/problems/parallel-courses-ii/)

- solves: `min_number_of_semesters`
- Pattern: `dp[mask]` stores the minimum semesters to complete exactly the courses in mask, taking any valid subset of newly-available courses each round.

### 37. [Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam/)

- solves: `max_students`
- Pattern: `dp[row][mask]` over seat layouts, checking mask validity against broken seats and diagonal neighbors in the prior row.

### 38. [Number Of Ways To Wear Different Hats To Each Other](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/)

- solves: `number_ways`
- Pattern: assign hats (not people) one at a time; `dp[hat][mask]` counts ways to cover the people bitmask.

## Bloom Filters

No stub file, and no numbered problems, because **LeetCode has no Bloom filter
problem**. This is the one topic in the curriculum that is not drilled, and the
absence is deliberate rather than an oversight.

Bloom filters show up as a **design-round question** or as a follow-up when a hash
set stops fitting in memory, which is a conversation rather than a 40-minute
coding problem. Read [the topic](../notes/08_bloom_filters.md) and practise it by
answering these out loud instead:

- Size a filter for 100 million keys at a 1% false positive rate. How many bits,
  how many hash functions, and how do you justify the formula?
- Why can a Bloom filter never return a false negative, and why does that
  one-sided error make it safe in front of a database?
- A colleague proposes deleting a key by clearing its bits. What breaks, and what
  variant fixes it?
- You have two filters built over different shards with the same `m` and `k`. How
  do you merge them, and why does that work?

The closest LeetCode problems are [Design HashSet](https://leetcode.com/problems/design-hashset/)
and [Design HashMap](https://leetcode.com/problems/design-hashmap/), which drill
hashing and collision handling but not probabilistic membership. Both already
appear in `01_arrays_and_hashing`.
