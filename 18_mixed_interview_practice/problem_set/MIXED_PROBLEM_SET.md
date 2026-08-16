# Mixed Interview Practice Problem Set

## Goal

Drill problems that do not sit inside a single technique. Each one chains two
or more patterns, so the work is recognizing which patterns combine and in
what order — the retrieval skill a real interview tests once the pure-pattern
modules are fluent.

## How To Use

Work these interleaved, not grouped by technique. For each problem, first
name the patterns it chains before writing code. `solves:` names the function
in `multi_pattern_problems.py`; `solves: (todo)` means the solution is not
written yet. `chains:` names the patterns the problem combines.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Multi-Pattern Problems

`multi_pattern_problems.py` — problems that require two or more distinct
interview patterns working together; neither pattern alone finishes them.

### 1. [Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)

- solves: `count_range_sum`
- chains: prefix sums + merge-sort (or Fenwick/BIT)
- Pattern: prefix sums set up the problem; counting sums in `[lower, upper]` at scale needs merge-sort divide-and-conquer or a BIT.

### 2. [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)

- solves: `median_sliding_window`
- chains: sliding window + two heaps
- Pattern: a fixed-size window feeds two balanced heaps with lazy deletion to read the median in O(1).

### 3. [LRU Cache](https://leetcode.com/problems/lru-cache/)

- solves: `LRUCache`
- chains: hash map + doubly linked list
- Pattern: hash map for O(1) lookup, doubly linked list for O(1) recency eviction.

### 4. [LFU Cache](https://leetcode.com/problems/lfu-cache/)

- solves: `LFUCache`
- chains: hash maps + per-frequency doubly linked lists
- Pattern: hash maps plus per-frequency linked lists evict the least-frequent, then least-recent, in O(1).

### 5. [Word Search II](https://leetcode.com/problems/word-search-ii/)

- solves: `find_words`
- chains: trie + grid backtracking
- Pattern: build a trie of the words, then run grid backtracking pruned by the trie so all words are matched in one sweep.

### 6. [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)

- solves: `alien_order`
- chains: build graph from strings + topological sort
- Pattern: derive ordering edges from adjacent word pairs, then topological sort the resulting DAG.

### 7. [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)

- solves: `find_ladders`
- chains: BFS + DFS/backtracking
- Pattern: BFS builds shortest-path layers, then a DFS/backtracking pass reconstructs every shortest path.

### 8. [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)

- solves: `max_envelopes`
- chains: sorting + binary-search LIS
- Pattern: sort width ascending and height descending on ties, then run the O(n log n) binary-search LIS on heights.

### 9. [Maximum Number of Events That Can Be Attended II](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/)

- solves: `max_value`
- chains: sorting + DP + binary search
- Pattern: weighted interval scheduling — sort by end, DP over events, binary-search the next non-conflicting event.

### 10. [Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)

- solves: `longest_dup_substring`
- chains: binary search on the answer + Rabin-Karp rolling hash
- Pattern: binary search the answer length, each length checked by a rolling-hash feasibility test.

### 11. [Jump Game VI](https://leetcode.com/problems/jump-game-vi/)

- solves: `max_result`
- chains: DP + monotonic deque
- Pattern: `dp[i] = nums[i] + max(dp[i-k..i-1])`, where a monotonic deque supplies the sliding-window max in O(1).

### 12. [Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/)

- solves: `constrained_subset_sum`
- chains: DP + monotonic deque
- Pattern: `dp[i] = nums[i] + max(0, max(dp[i-k..i-1]))`; a monotonic deque keeps that windowed max in O(1) (the direct twin of Jump Game VI).

### 13. [Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)

- solves: `job_scheduling`
- chains: sorting + DP + binary search
- Pattern: sort jobs by end time, DP over them, binary-search the latest non-overlapping job for each transition.

### 14. [Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/)

- solves: `max_sum_submatrix`
- chains: 2D prefix sums + Kadane + binary search
- Pattern: fix a column band, reduce to 1D running sums, then binary-search a sorted prefix set for the best sum `<= k`.

### 15. [Odd Even Jump](https://leetcode.com/problems/odd-even-jump/)

- solves: `odd_even_jumps`
- chains: DP + monotonic stack (ordered lookup)
- Pattern: a monotonic-stack pass precomputes the next higher/lower index, then backward DP marks which starts reach the end.

### 16. [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/)

- solves: `WeightedRandomPicker`
- chains: prefix sums + binary search
- Pattern: build a prefix-sum table of weights, then binary-search a random target into its bucket.

### 17. [Snapshot Array](https://leetcode.com/problems/snapshot-array/)

- solves: `SnapshotArray`
- chains: hash map + binary search
- Pattern: store per-index (snap_id, value) history, then binary-search the history for the value at a queried snapshot.

### 18. [Stock Price Fluctuation](https://leetcode.com/problems/stock-price-fluctuation/)

- solves: `StockPrice`
- chains: hash map + two heaps (lazy deletion)
- Pattern: a timestamp→price map plus a max heap and a min heap; skip stale heap tops that disagree with the map.

### 19. [Find Servers That Handled Most Number of Requests](https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/)

- solves: `busiest_servers`
- chains: two heaps + ordered/free-set search
- Pattern: a min heap of busy servers by free-time feeds an ordered set of free servers searched for the next available id.

### 20. [Sort Items by Groups Respecting Dependencies](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/)

- solves: `sort_items`
- chains: nested topological sort
- Pattern: topologically sort groups, then topologically sort items within each group, and stitch the two orders together.

### 21. [Create Maximum Number](https://leetcode.com/problems/create-maximum-number/)

- solves: `max_number`
- chains: greedy monotonic stack + k-way merge
- Pattern: for each split, pick the max subsequence from each array with a monotonic stack, then merge the two greedily.

### 22. [House Robber III](https://leetcode.com/problems/house-robber-iii/)

- solves: `rob`
- chains: tree post-order DFS + DP take/skip state
- Pattern: the naive rob-or-skip recursion recomputes subtrees; returning a rob/skip pair up the DFS restores O(n).

### 23. [Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/)

- solves: `min_camera_cover`
- chains: tree post-order DFS + greedy state machine
- Pattern: each subtree reports covered / needs-camera / has-camera, and the parent greedily places cameras on demand.

### 24. [Count Subtrees With Max Distance Between Cities](https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/)

- solves: `count_subgraphs_for_each_diameter`
- chains: bitmask subset enumeration + connectivity check + tree diameter by BFS
- Pattern: n is at most 15, so enumerate every subset of cities, keep the ones that stay connected, and measure each survivor's diameter.
