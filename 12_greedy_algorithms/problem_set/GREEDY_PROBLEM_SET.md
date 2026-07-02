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

### 5. [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)

- Pattern: scan left to right and plant greedily whenever a slot and both neighbors are empty.

### 6. [Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/)

- Pattern: sort box types by units descending, then fill the truck highest-value first.

## Jump Game Family

These problems all share the "track the farthest reachable index" greedy rule.

### 7. [Jump Game](https://leetcode.com/problems/jump-game/)

- Pattern: track farthest reachable index while scanning; fail if the scan passes it.

### 8. [Jump Game II](https://leetcode.com/problems/jump-game-ii/)

- Pattern: track farthest reach plus a level/boundary counter for minimum jumps.

### 9. [Jump Game III](https://leetcode.com/problems/jump-game-iii/)

- Pattern: greedy reachability turns into a visited-index search from a start index.

### 10. [Jump Game IV](https://leetcode.com/problems/jump-game-iv/)

- Pattern: BFS over value-buckets, greedily clearing each visited value group to avoid re-expansion.

## Mediums

These are the interval-greedy and frequency-greedy mediums you should drill for FAANG-style interviews.

### 11. [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

- Pattern: sort by end time, keep the earliest-ending interval, count removals for the rest.
- Note: heavier interval-scheduling variants (merge, insert, employee free time) live in
  `13_intervals`; here the focus stays on the greedy-choice mechanics.

### 12. [Partition Labels](https://leetcode.com/problems/partition-labels/)

- Pattern: extend the current partition boundary to each character's last occurrence.

### 13. [Candy](https://leetcode.com/problems/candy/)

- Pattern: two greedy passes (left-to-right, right-to-left) taking the max at each index.

### 14. [Reorganize String](https://leetcode.com/problems/reorganize-string/)

- Pattern: always place the most frequent remaining character next, blocking immediate repeats.

### 15. [Hand of Straights](https://leetcode.com/problems/hand-of-straights/)

- Pattern: repeatedly start a run from the smallest remaining card and consume consecutive values.

### 16. [Remove K Digits](https://leetcode.com/problems/remove-k-digits/)

- Pattern: monotonic stack, popping larger leading digits greedily to minimize the result.

### 17. [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)

- Pattern: monotonic-stack greedy keeping smallest lexicographic result with a can-see-later guard.

### 18. [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

- Pattern: track open balance, counting a fix each time it would go negative or ends positive.

### 19. [Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/)

- Pattern: sort by the cost difference between cities and send the biggest savers to the cheaper city.

### 20. [Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/)

- Pattern: count direction changes; each sign flip greedily extends the alternating subsequence.

### 21. [Bag of Tokens](https://leetcode.com/problems/bag-of-tokens/)

- Pattern: two-pointer greedy, spending power on the cheapest token and buying back with the priciest.

### 22. [Advantage Shuffle](https://leetcode.com/problems/advantage-shuffle/)

- Pattern: sort both arrays, beat each opponent with the smallest sufficient card or dump the weakest.

### 23. [Eliminate Maximum Number of Monsters](https://leetcode.com/problems/eliminate-maximum-number-of-monsters/)

- Pattern: sort by arrival time and shoot the soonest-arriving monster each minute.

### 24. [Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/)

- Pattern: use ladders on the largest climbs (min-heap) and pay bricks for the rest.

### 25. [Minimum Deletions to Make Character Frequencies Unique](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/)

- Pattern: sort frequencies descending and shrink each clashing count to the next free value.

### 26. [Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/)

- Pattern: min-heap greedy repeatedly merging the two smallest.

### 27. [Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals/)

- Pattern: prefix-max boundary greedy.

## Hards And Extensions

These are the greedy follow-ups that push beyond the standard medium set.

### 28. [Reconstruct Queue by Height](https://leetcode.com/problems/queue-reconstruction-by-height/)

- Pattern: sort tall-first, then insert each person at their k-index so shorter people don't disturb taller placements.

### 29. [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

- Pattern: sort by end coordinate, reuse one arrow while balloons overlap the current end.

### 30. [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)

- Pattern: sort by weight, greedily pair the lightest with the heaviest that still fits.
- Cross-reference: this is the two-pointer technique from `02_two_pointers` applied with a greedy pairing rule.

### 31. [Task Scheduler](https://leetcode.com/problems/task-scheduler/)

- Pattern: greedily schedule the most frequent remaining task first to spread out cooldowns.
- Cross-reference: an alternative implementation uses a max-heap from `08_heaps`; the greedy angle here is the frequency-count formula.

### 32. [IPO](https://leetcode.com/problems/ipo/)

- Pattern: unlock affordable projects by capital, then greedily take the max-profit one via a heap.

### 33. [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/)

- Pattern: bank passed stations in a max-heap and refuel from the largest tank only when stranded.

### 34. [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/)

- Pattern: sort by deadline and swap out the longest taken course when a new one overflows the timeline.

### 35. [Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/)

- Pattern: greedily append each number to an existing run before starting a new length-3 subsequence.

## Recommended Order

If you want the shortest path to greedy fluency, do them in this order:

```text
1. [Assign Cookies](https://leetcode.com/problems/assign-cookies/)
2. [Lemonade Change](https://leetcode.com/problems/lemonade-change/)
3. [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
4. [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)
5. [Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/)
6. [Jump Game](https://leetcode.com/problems/jump-game/)
7. [Jump Game II](https://leetcode.com/problems/jump-game-ii/)
8. [Gas Station](https://leetcode.com/problems/gas-station/)
9. [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
10. [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)
11. [Partition Labels](https://leetcode.com/problems/partition-labels/)
12. [Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/)
13. [Remove K Digits](https://leetcode.com/problems/remove-k-digits/)
14. [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)
15. [Reorganize String](https://leetcode.com/problems/reorganize-string/)
16. [Hand of Straights](https://leetcode.com/problems/hand-of-straights/)
17. [Task Scheduler](https://leetcode.com/problems/task-scheduler/)
18. [Candy](https://leetcode.com/problems/candy/)
19. [Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/)
20. [IPO](https://leetcode.com/problems/ipo/)
21. [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/)
```
