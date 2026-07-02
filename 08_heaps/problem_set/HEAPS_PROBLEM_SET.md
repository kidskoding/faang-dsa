# Heaps Problem Set

## Goal

Build heap intuition from the ground up, then use that foundation to solve the
top-k, two-heap, and k-way merge problems that show up in LeetCode-style
interviews.

## How To Use

Work the file in order. Heap Basics comes first, then Top-K, then Two Heaps,
then K-Way Merge, then the harder extensions.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Heap Basics

These are the min-heap and max-heap basics you should be able to do without
thinking too hard.

### 1. [Kth Largest Element In An Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

- Pattern: keep a size-k min heap to expose the kth largest at the top.

### 2. [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)

- Pattern: repeatedly pop the two largest values from a max heap.

### 3. [K Closest Points To Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

- Pattern: order candidates by distance with a heap instead of sorting all points.

### 4. [Kth Largest Element In A Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

- Pattern: maintain a persistent size-k min heap across `add` calls.

### 5. [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

- Pattern: min heap of active end times tracks the rooms in use.

### 6. [Maximum Product After K Increments](https://leetcode.com/problems/maximum-product-after-k-increments/)

- Pattern: min heap so each increment lands on the current smallest value.

### 7. [Remove Stones To Minimize The Total](https://leetcode.com/problems/remove-stones-to-minimize-the-total/)

- Pattern: max heap halves the largest pile on each of the k operations.

## Top-K

These use a size-k heap to avoid sorting the full input.

### 8. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

- Pattern: count frequencies, then keep a size-k heap over the counts.

### 9. [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

- Pattern: heap with a tie-break comparator on frequency and lexical order.

### 10. [Task Scheduler](https://leetcode.com/problems/task-scheduler/)

- Pattern: max heap of task counts schedules the most frequent task first.

### 11. [Reorganize String](https://leetcode.com/problems/reorganize-string/)

- Pattern: max heap of character counts interleaves the most frequent letters.

### 12. [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)

- Pattern: max heap of character counts emits letters in descending frequency.

### 13. [Least Number Of Unique Integers After K Removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/)

- Pattern: min heap of counts removes the rarest values first to shrink the unique set.

## Two Heaps

These balance a low half and a high half around a heap boundary.

### 14. [Find Median From Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

- Pattern: max heap for the lower half, min heap for the upper half.

### 15. [IPO](https://leetcode.com/problems/ipo/)

- Pattern: min heap gates projects by capital, max heap picks the best profit.

### 16. [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)

- Pattern: two heaps with lazy deletion as the window slides.

### 17. [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/)

- Pattern: min heap by availability feeds a min heap by processing time and index.

### 18. [Process Tasks Using Servers](https://leetcode.com/problems/process-tasks-using-servers/)

- Pattern: one heap of free servers by weight, one heap of busy servers by free time.

## K-Way Merge

These use a heap to merge or scan across k sorted or independent streams.

### 19. [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

- Pattern: heap holds one candidate per list, always advancing the smallest.

### 20. [Smallest Range Covering Elements From K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)

- Pattern: heap tracks the current min across k lists while a running max bounds the range.

### 21. [Employee Free Time](https://leetcode.com/problems/employee-free-time/)

- Pattern: heap merges each employee's sorted intervals to find shared gaps.

### 22. [Find K Pairs With Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

- Pattern: heap expands the frontier of pair sums across two sorted arrays.

### 23. [Kth Smallest Element In A Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

- Pattern: heap merges sorted rows, popping k times to reach the kth smallest.

### 24. [Super Ugly Number](https://leetcode.com/problems/super-ugly-number/)

- Pattern: heap merges the multiples generated from each prime factor.

## Hards And Extensions

These layer heaps onto Dijkstra-style scans, greedy scheduling, and event
sweeps. Expect them in senior loops and harder onsites.

### 25. [Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/)

- Pattern: min heap processes the boundary inward, raising water to the lowest wall.

### 26. [Minimum Cost To Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/)

- Pattern: sort by wage ratio, then a max heap of quality drops the costliest worker.

### 27. [Swim In Rising Water](https://leetcode.com/problems/swim-in-rising-water/)

- Pattern: Dijkstra-style min heap expands the cheapest-elevation frontier to the corner.

### 28. [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

- Pattern: sweep building edges with a heap of active heights to emit key points.

### 29. [Maximum Performance Of A Team](https://leetcode.com/problems/maximum-performance-of-a-team/)

- Pattern: sort by efficiency, then a min heap of speeds caps the team at size k.

### 30. [Minimum Number Of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/)

- Pattern: max heap of passed fuel stops greedily refuels the largest tank when stranded.

### 31. [Find The Kth Smallest Sum Of A Matrix With Sorted Rows](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/)

- Pattern: heap expands row-index combinations to enumerate the k smallest sums.

### 32. [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/)

- Pattern: sort by deadline, then a max heap of durations swaps out the longest course when over budget.

### 33. [Network Delay Time](https://leetcode.com/problems/network-delay-time/)

- Pattern: Dijkstra shortest path using a min-heap on an adjacency list.

## Recommended Order

If you want the shortest path to heap fluency, do them in this order:

```text
1. [Kth Largest Element In An Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
2. [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)
3. [K Closest Points To Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
4. [Kth Largest Element In A Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
5. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
6. [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)
7. [Task Scheduler](https://leetcode.com/problems/task-scheduler/)
8. [Reorganize String](https://leetcode.com/problems/reorganize-string/)
9. [Find Median From Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
10. [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
11. [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
12. [IPO](https://leetcode.com/problems/ipo/)
13. [Find K Pairs With Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)
14. [Kth Smallest Element In A Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
15. [Smallest Range Covering Elements From K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)
16. [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)
17. [Network Delay Time](https://leetcode.com/problems/network-delay-time/)
18. [Minimum Number Of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/)
19. [Minimum Cost To Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/)
20. [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)
```
