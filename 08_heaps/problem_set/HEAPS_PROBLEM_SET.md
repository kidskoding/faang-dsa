# Heaps Problem Set

## Goal

Build heap intuition from the ground up, then use that foundation to solve the
top-k, two-heap, and k-way merge problems that show up in LeetCode-style
interviews.

## How To Use

Work the file in order. Heap Basics comes first, then Top-K, then Two Heaps,
then K-Way Merge.

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

## Top-K

These use a size-k heap to avoid sorting the full input.

### 6. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

- Pattern: count frequencies, then keep a size-k heap over the counts.

### 7. [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

- Pattern: heap with a tie-break comparator on frequency and lexical order.

### 8. [Task Scheduler](https://leetcode.com/problems/task-scheduler/)

- Pattern: max heap of task counts schedules the most frequent task first.

### 9. [Reorganize String](https://leetcode.com/problems/reorganize-string/)

- Pattern: max heap of character counts interleaves the most frequent letters.

## Two Heaps

These balance a low half and a high half around a heap boundary.

### 10. [Find Median From Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

- Pattern: max heap for the lower half, min heap for the upper half.

### 11. [IPO](https://leetcode.com/problems/ipo/)

- Pattern: min heap gates projects by capital, max heap picks the best profit.

### 12. [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)

- Pattern: two heaps with lazy deletion as the window slides.

## K-Way Merge

These use a heap to merge or scan across k sorted or independent streams.

### 13. [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

- Pattern: heap holds one candidate per list, always advancing the smallest.

### 14. [Smallest Range Covering Elements From K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)

- Pattern: heap tracks the current min across k lists while a running max bounds the range.

### 15. [Design Twitter](https://leetcode.com/problems/design-twitter/)

- Pattern: merge each followee's recent tweets with a heap keyed by timestamp.

### 16. [Employee Free Time](https://leetcode.com/problems/employee-free-time/)

- Pattern: heap merges each employee's sorted intervals to find shared gaps.

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
13. [Smallest Range Covering Elements From K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)
14. [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)
15. [Design Twitter](https://leetcode.com/problems/design-twitter/)
16. [Employee Free Time](https://leetcode.com/problems/employee-free-time/)
```
