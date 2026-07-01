# Greedy Problem Set

## Goal

Build greedy-choice intuition from the ground up, then use that foundation to solve the
jump-game and interval-greedy problems that show up in LeetCode-style interviews.

## How To Use

Work the file in order. The early sections are the fundamentals. The later sections are
the medium and hard extensions.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Fundamentals

These are the greedy-choice basics you should be able to do without thinking too hard.

### 1. [Assign Cookies](https://leetcode.com/problems/assign-cookies/)

- Pattern: sort both arrays, match the smallest sufficient cookie to each child.

### 2. [Lemonade Change](https://leetcode.com/problems/lemonade-change/)

- Pattern: greedily prefer breaking a larger bill to save smaller bills for later change.

### 3. [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

- Pattern: capture every positive day-to-day price delta.

### 4. [Gas Station](https://leetcode.com/problems/gas-station/)

- Pattern: track a running tank total and reset the candidate start on the first deficit.

## Jump Game Family

These problems all share the "track the farthest reachable index" greedy rule.

### 5. [Jump Game](https://leetcode.com/problems/jump-game/)

- Pattern: track farthest reachable index while scanning; fail if the scan passes it.

### 6. [Jump Game II](https://leetcode.com/problems/jump-game-ii/)

- Pattern: track farthest reach plus a level/boundary counter for minimum jumps.

### 7. [Jump Game III](https://leetcode.com/problems/jump-game-iii/)

- Pattern: greedy reachability turns into a visited-index search from a start index.

## Mediums

These are the interval-greedy mediums you should drill for FAANG-style interviews.

### 8. [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

- Pattern: sort by end time, keep the earliest-ending interval, count removals for the rest.
- Note: heavier interval-scheduling variants (merge, insert, employee free time) live in
  `13_intervals`; here the focus stays on the greedy-choice mechanics.

### 9. [Partition Labels](https://leetcode.com/problems/partition-labels/)

- Pattern: extend the current partition boundary to each character's last occurrence.

### 10. [Candy](https://leetcode.com/problems/candy/)

- Pattern: two greedy passes (left-to-right, right-to-left) taking the max at each index.

## Hards And Extensions

These are the greedy follow-ups that push beyond the standard medium set.

### 11. [Reconstruct Queue by Height](https://leetcode.com/problems/queue-reconstruction-by-height/)

- Pattern: sort tall-first, then insert each person at their k-index so shorter people don't disturb taller placements.

### 12. [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

- Pattern: sort by end coordinate, reuse one arrow while balloons overlap the current end.

### 13. [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)

- Pattern: sort by weight, greedily pair the lightest with the heaviest that still fits.
- Cross-reference: this is the two-pointer technique from `02_two_pointers` applied with a greedy pairing rule.

### 14. [Task Scheduler](https://leetcode.com/problems/task-scheduler/)

- Pattern: greedily schedule the most frequent remaining task first to spread out cooldowns.
- Cross-reference: an alternative implementation uses a max-heap from `08_heaps`; the greedy angle here is the frequency-count formula.

## Recommended Order

If you want the shortest path to greedy fluency, do them in this order:

```text
1. [Assign Cookies](https://leetcode.com/problems/assign-cookies/)
2. [Lemonade Change](https://leetcode.com/problems/lemonade-change/)
3. [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
4. [Jump Game](https://leetcode.com/problems/jump-game/)
5. [Jump Game II](https://leetcode.com/problems/jump-game-ii/)
6. [Gas Station](https://leetcode.com/problems/gas-station/)
7. [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
8. [Partition Labels](https://leetcode.com/problems/partition-labels/)
9. [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)
10. [Jump Game III](https://leetcode.com/problems/jump-game-iii/)
11. [Candy](https://leetcode.com/problems/candy/)
12. [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)
13. [Reconstruct Queue by Height](https://leetcode.com/problems/queue-reconstruction-by-height/)
14. [Task Scheduler](https://leetcode.com/problems/task-scheduler/)
```
