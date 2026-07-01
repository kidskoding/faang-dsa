# Binary Search Problem Set

## Goal

Build binary search intuition from the ground up, then use that foundation to solve the boundary-search, rotated-array, and search-on-answer problems that show up in LeetCode-style interviews.

## How To Use

Work the file in order. The early sections are the fundamentals. The later sections are the medium and hard extensions.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Fundamentals

These are the binary search basics you should be able to do without thinking too hard.

### 1. [Binary Search](https://leetcode.com/problems/binary-search/)

- Pattern: exact-match search over a sorted array.

### 2. [Search Insert Position](https://leetcode.com/problems/search-insert-position/)

- Pattern: find the first index where the value could be inserted.

### 3. [First Bad Version](https://leetcode.com/problems/first-bad-version/)

- Pattern: monotonic predicate boundary search.

### 4. [Sqrt(x)](https://leetcode.com/problems/sqrtx/)

- Pattern: binary search over the answer space for the largest value whose square fits.

### 5. [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

- Pattern: two boundary searches, one for the first true and one for the last true.

## Mediums

These are the binary search mediums you should drill for FAANG-style interviews.

### 6. [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

- Pattern: treat a row-sorted, column-sorted grid as one flattened sorted array.

### 7. [Find Peak Element](https://leetcode.com/problems/find-peak-element/)

- Pattern: binary search using the local slope instead of full sortedness.

### 8. [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

- Pattern: boundary search for the left edge of a fixed-size window.

### 9. [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

- Pattern: identify which half is sorted, then decide if the target lies inside it.

### 10. [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

- Pattern: boundary search for the rotation pivot.

### 11. [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

- Pattern: search on answer space for the minimum feasible eating speed.

### 12. [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

- Pattern: search on answer space for the minimum feasible ship capacity.

### 13. [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)

- Pattern: boundary search over stored timestamps to find the latest value at or before a query time.

## Hards And Extensions

These are the binary search follow-ups that push beyond the standard medium set.

### 14. [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

- Pattern: rotated array search with duplicates, falling back to shrinking both ends.

### 15. [Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

- Pattern: rotation pivot search with duplicates at the boundary.

### 16. [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)

- Pattern: search on answer space for the minimum largest subarray sum under a split-count constraint.

### 17. [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

- Pattern: binary search a partition index instead of merging.

### 18. [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)

- Pattern: eliminate a full row or column at each step from a sorted-corner start.

## Recommended Order

If you want the shortest path to binary search fluency, do them in this order:

```text
1. [Binary Search](https://leetcode.com/problems/binary-search/)
2. [Search Insert Position](https://leetcode.com/problems/search-insert-position/)
3. [First Bad Version](https://leetcode.com/problems/first-bad-version/)
4. [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
5. [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
6. [Find Peak Element](https://leetcode.com/problems/find-peak-element/)
7. [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
8. [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
9. [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
10. [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
11. [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)
12. [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)
13. [Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)
14. [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)
15. [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
```
