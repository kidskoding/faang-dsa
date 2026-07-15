# Heaps Problem Set

## Goal

Build heap intuition across the core heap techniques — plain min/max-heap
basics, size-k top-k heaps, the balanced two-heap median pattern, and k-way
merge — then use each technique to solve the medium and hard heap problems
that show up in LeetCode-style interviews.

## How To Use

Each section maps to one solution file in this folder and to one heap
technique. Work a section top to bottom: problems are ordered roughly easy
to hard, and the implemented ones come first. `solves:` names the function
in that section's file; `solves: (todo)` means the solution is not written
yet.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Heap Basics

`heap_basics_problems.py` — plain min-heap and max-heap moves you should be
able to do without thinking too hard.

### 1. [Kth Largest Element In An Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

- solves: `kth_largest_element`
- Pattern: keep a size-k min heap to expose the kth largest at the top.

### 2. [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)

- solves: `last_stone_weight`
- Pattern: repeatedly pop the two largest values from a max heap.

### 3. [K Closest Points To Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

- solves: `k_closest_points`
- Pattern: keep a size-k max heap keyed by squared distance instead of sorting all points.

### 4. [Kth Largest Element In A Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

- solves: `KthLargest`
- Pattern: maintain a persistent size-k min heap across `add` calls.

### 5. [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

- solves: `meeting_rooms_ii`
- Pattern: min heap of active end times tracks the rooms in use.

### 6. [Maximum Product After K Increments](https://leetcode.com/problems/maximum-product-after-k-increments/)

- solves: `maximum_product`
- Pattern: min heap so each increment lands on the current smallest value.

### 7. [Remove Stones To Minimize The Total](https://leetcode.com/problems/remove-stones-to-minimize-the-total/)

- solves: `min_stone_sum`
- Pattern: max heap halves the largest pile on each of the k operations.

## Top-K

`top_k_problems.py` — count frequencies, then use a size-k or full heap over
the counts to avoid sorting the full input.

### 8. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

- solves: `top_k_frequent`
- Pattern: count frequencies, then keep a size-k heap over the counts.

### 9. [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

- solves: `top_k_frequent_words`
- Pattern: heap with a tie-break comparator on frequency and lexical order.

### 10. [Task Scheduler](https://leetcode.com/problems/task-scheduler/)

- solves: `least_interval`
- Pattern: max heap of task counts schedules the most frequent task first.

### 11. [Reorganize String](https://leetcode.com/problems/reorganize-string/)

- solves: `reorganize_string`
- Pattern: max heap of character counts interleaves the most frequent letters.

### 12. [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)

- solves: `frequency_sort`
- Pattern: max heap of character counts emits letters in descending frequency.

### 13. [Least Number Of Unique Integers After K Removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/)

- solves: `find_least_num_of_unique_ints`
- Pattern: min heap of counts removes the rarest values first to shrink the unique set.

## Two Heaps

`two_heaps_problems.py` — balance a max heap over the low half and a min heap
over the high half around a running boundary.

### 14. [Find Median From Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

- solves: `MedianFinder`
- Pattern: max heap for the lower half, min heap for the upper half.

### 15. [IPO](https://leetcode.com/problems/ipo/)

- solves: `find_maximized_capital`
- Pattern: min heap gates projects by capital, max heap picks the best profit.

### 16. [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)

- solves: `median_sliding_window`
- Pattern: two heaps with lazy deletion as the window slides.

### 17. [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/)

- solves: `get_order`
- Pattern: min heap by availability feeds a min heap by processing time and index.

### 18. [Process Tasks Using Servers](https://leetcode.com/problems/process-tasks-using-servers/)

- solves: `assign_tasks`
- Pattern: one heap of free servers by weight, one heap of busy servers by free time.

## K-Way Merge

`k_way_merge_problems.py` — a heap holding one candidate per stream merges or
scans across k sorted or independent sources.

### 19. [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

- solves: `merge_k_lists`
- Pattern: heap holds one candidate per list, always advancing the smallest.

### 20. [Smallest Range Covering Elements From K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)

- solves: `smallest_range`
- Pattern: heap tracks the current min across k lists while a running max bounds the range.

### 21. [Employee Free Time](https://leetcode.com/problems/employee-free-time/)

- solves: `employee_free_time`
- Pattern: heap merges each employee's sorted intervals to find shared gaps.

### 22. [Design Twitter](https://leetcode.com/problems/design-twitter/)

- solves: `Twitter`
- Pattern: merge each followee's recent tweets with a heap keyed by timestamp.

### 23. [Find K Pairs With Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

- solves: `k_smallest_pairs`
- Pattern: heap expands the frontier of pair sums across two sorted arrays.

### 24. [Kth Smallest Element In A Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

- solves: `kth_smallest`
- Pattern: heap merges sorted rows, popping k times to reach the kth smallest.

### 25. [Super Ugly Number](https://leetcode.com/problems/super-ugly-number/)

- solves: `nth_super_ugly_number`
- Pattern: heap merges the multiples generated from each prime factor.

## Hards And Extensions

`heap_hards_problems.py` — layer heaps onto Dijkstra-style scans, greedy
scheduling, and event sweeps. Expect them in senior loops and harder
onsites.

### 26. [Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/)

- solves: `trap_rain_water`
- Pattern: min heap processes the boundary inward, raising water to the lowest wall.

### 27. [Minimum Cost To Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/)

- solves: `mincost_to_hire_workers`
- Pattern: sort by wage ratio, then a max heap of quality drops the costliest worker.

### 28. [Swim In Rising Water](https://leetcode.com/problems/swim-in-rising-water/)

- solves: `swim_in_water`
- Pattern: Dijkstra-style min heap expands the cheapest-elevation frontier to the corner.

### 29. [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

- solves: `get_skyline`
- Pattern: sweep building edges with a heap of active heights to emit key points.

### 30. [Maximum Performance Of A Team](https://leetcode.com/problems/maximum-performance-of-a-team/)

- solves: `max_performance`
- Pattern: sort by efficiency, then a min heap of speeds caps the team at size k.

### 31. [Minimum Number Of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/)

- solves: `min_refuel_stops`
- Pattern: max heap of passed fuel stops greedily refuels the largest tank when stranded.

### 32. [Find The Kth Smallest Sum Of A Matrix With Sorted Rows](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/)

- solves: `kth_smallest`
- Pattern: heap expands row-index combinations to enumerate the k smallest sums.

### 33. [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/)

- solves: `schedule_course`
- Pattern: sort by deadline, then a max heap of durations swaps out the longest course when over budget.

### 34. [Network Delay Time](https://leetcode.com/problems/network-delay-time/)

- solves: `network_delay_time`
- Pattern: Dijkstra shortest path using a min heap on an adjacency list.
