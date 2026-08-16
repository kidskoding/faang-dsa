# Greedy Problem Set

## Goal

Build greedy-choice intuition from the ground up — commit to the locally
best move, prove it stays optimal, and recognize the three shapes greedy
takes in interviews: scan-once fundamentals, farthest-reach jump games, and
sort-by-endpoint interval greedy — then use each to solve the medium and
hard greedy problems that show up in LeetCode-style interviews.

## How To Use

Each section maps to one solution file in this folder and to one greedy
shape. Work a section top to bottom: problems are ordered roughly easy to
hard, and the implemented ones come first. `solves:` names the function in
that section's file; `solves: (todo)` means the solution is not written yet.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Fundamentals

`greedy_fundamentals_problems.py` — greedy-choice basics: sort or scan once
and commit to the locally best move at each step.

### 1. [Assign Cookies](https://leetcode.com/problems/assign-cookies/)

- solves: `assign_cookies`
- Pattern: sort both arrays, match the smallest sufficient cookie to each child.

### 2. [Lemonade Change](https://leetcode.com/problems/lemonade-change/)

- solves: `lemonade_change`
- Pattern: greedily prefer breaking a larger bill to save smaller bills for later change.

### 3. [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

- solves: `max_profit`
- Pattern: capture every positive day-to-day price delta.

### 4. [Gas Station](https://leetcode.com/problems/gas-station/)

- solves: `can_complete_circuit`
- Pattern: track a running tank total and reset the candidate start on the first deficit.

### 5. [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)

- solves: `can_place_flowers`
- Pattern: scan left to right and plant greedily whenever a slot and both neighbors are empty.

### 6. [Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/)

- solves: `maximum_units`
- Pattern: sort box types by units descending, then fill the truck highest-value first.

### 7. [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

- solves: `min_add_to_make_valid`
- Pattern: track open balance, counting a fix each time it would go negative or ends positive.

### 8. [Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/)

- solves: `wiggle_max_length`
- Pattern: count direction changes; each sign flip greedily extends the alternating subsequence.

### 9. [Bag of Tokens](https://leetcode.com/problems/bag-of-tokens/)

- solves: `bag_of_tokens_score`
- Pattern: two-pointer greedy, spending power on the cheapest token and buying back with the priciest.

### 10. [Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/)

- solves: `two_city_sched_cost`
- Pattern: sort by the cost difference between cities and send the biggest savers to the cheaper city.

### 11. [Remove K Digits](https://leetcode.com/problems/remove-k-digits/)

- solves: `remove_k_digits`
- Pattern: monotonic stack, popping larger leading digits greedily to minimize the result.

### 12. [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)

- solves: `remove_duplicate_letters`
- Pattern: monotonic-stack greedy keeping smallest lexicographic result with a can-see-later guard.

### 13. [Reorganize String](https://leetcode.com/problems/reorganize-string/)

- solves: `reorganize_string`
- Pattern: always place the most frequent remaining character next, blocking immediate repeats.

### 14. [Minimum Deletions to Make Character Frequencies Unique](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/)

- solves: `min_deletions`
- Pattern: sort frequencies descending and shrink each clashing count to the next free value.

### 15. [Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/)

- solves: `connect_sticks`
- Pattern: min-heap greedy repeatedly merging the two smallest.

### 16. [Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/)

- solves: `furthest_building`
- Pattern: use ladders on the largest climbs (min-heap) and pay bricks for the rest.

### 17. [IPO](https://leetcode.com/problems/ipo/)

- solves: `find_maximized_capital`
- Pattern: unlock affordable projects by capital, then greedily take the max-profit one via a heap.

### 18. [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/)

- solves: `min_refuel_stops`
- Pattern: bank passed stations in a max-heap and refuel from the largest tank only when stranded.

### 19. [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/)

- solves: `schedule_course`
- Pattern: sort by deadline and swap out the longest taken course when a new one overflows the timeline.

## Jump Game Family

`jump_game_problems.py` — track the farthest reachable index; reachability
and minimum-jumps variants share the same greedy reach rule.

### 20. [Jump Game](https://leetcode.com/problems/jump-game/)

- solves: `can_jump`
- Pattern: track farthest reachable index while scanning; fail if the scan passes it.

### 21. [Jump Game II](https://leetcode.com/problems/jump-game-ii/)

- solves: `jump`
- Pattern: track farthest reach plus a level/boundary counter for minimum jumps.

### 22. [Jump Game III](https://leetcode.com/problems/jump-game-iii/)

- solves: `can_reach`
- Pattern: greedy reachability turns into a visited-index search from a start index.

### 23. [Jump Game IV](https://leetcode.com/problems/jump-game-iv/)

- solves: `min_jumps`
- Pattern: BFS over value-buckets, greedily clearing each visited value group to avoid re-expansion.

### 24. [Jump Game VII](https://leetcode.com/problems/jump-game-vii/)

- solves: `can_reach_end`
- Pattern: sliding-window reachability over the string, marking an index reachable when any reachable index lies within the jump range.

### 25. [Minimum Jumps to Reach Home](https://leetcode.com/problems/minimum-jumps-to-reach-home/)

- solves: `minimum_jumps`
- Pattern: BFS over positions with a bounded reachable range and a no-two-consecutive-backward-jumps constraint.

## Sorting-Based Greedy

`interval_greedy_problems.py` — sort by an endpoint (or by frequency) then
greedily commit interval by interval, keeping the earliest-ending or
most-constrained choice.

### 26. [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

- solves: `erase_overlap_intervals`
- Pattern: sort by end time, keep the earliest-ending interval, count removals for the rest.

### 27. [Partition Labels](https://leetcode.com/problems/partition-labels/)

- solves: `partition_labels`
- Pattern: extend the current partition boundary to each character's last occurrence.

### 28. [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

- solves: `find_min_arrow_shots`
- Pattern: sort by end coordinate, reuse one arrow while balloons overlap the current end.

### 29. [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)

- solves: `num_rescue_boats`
- Pattern: sort by weight, greedily pair the lightest with the heaviest that still fits.

### 30. [Reconstruct Queue by Height](https://leetcode.com/problems/queue-reconstruction-by-height/)

- solves: `reconstruct_queue`
- Pattern: sort tall-first, then insert each person at their k-index so shorter people don't disturb taller placements.

### 31. [Task Scheduler](https://leetcode.com/problems/task-scheduler/)

- solves: `least_interval`
- Pattern: greedily schedule the most frequent remaining task first to spread out cooldowns.

### 32. [Candy](https://leetcode.com/problems/candy/)

- solves: `candy`
- Pattern: two greedy passes (left-to-right, right-to-left) taking the max at each index.

### 33. [Hand of Straights](https://leetcode.com/problems/hand-of-straights/)

- solves: `is_n_straight_hand`
- Pattern: repeatedly start a run from the smallest remaining card and consume consecutive values.

### 34. [Advantage Shuffle](https://leetcode.com/problems/advantage-shuffle/)

- solves: `advantage_count`
- Pattern: sort both arrays, beat each opponent with the smallest sufficient card or dump the weakest.

### 35. [Eliminate Maximum Number of Monsters](https://leetcode.com/problems/eliminate-maximum-number-of-monsters/)

- solves: `eliminate_maximum`
- Pattern: sort by arrival time and shoot the soonest-arriving monster each minute.

### 36. [Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals/)

- solves: `partition_disjoint`
- Pattern: prefix-max boundary greedy.

### 37. [Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/)

- solves: `is_possible`
- Pattern: greedily append each number to an existing run before starting a new length-3 subsequence.
