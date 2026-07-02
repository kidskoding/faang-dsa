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

### 6. [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)

- Pattern: exact-match search driven by a comparison oracle instead of array reads.

### 7. [Arranging Coins](https://leetcode.com/problems/arranging-coins/)

- Pattern: search on answer space for the largest full row count under a triangular-sum bound.

## Mediums

These are the binary search mediums you should drill for FAANG-style interviews.

### 8. [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

- Pattern: treat a row-sorted, column-sorted grid as one flattened sorted array.

### 9. [Find Peak Element](https://leetcode.com/problems/find-peak-element/)

- Pattern: binary search using the local slope instead of full sortedness.

### 10. [Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)

- Pattern: boundary search for the first element strictly greater than the target, with wraparound.

### 11. [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

- Pattern: boundary search for the left edge of a fixed-size window.

### 12. [Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/)

- Pattern: binary search on pair-index parity to locate where the pairing breaks.

### 13. [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

- Pattern: identify which half is sorted, then decide if the target lies inside it.

### 14. [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

- Pattern: boundary search for the rotation pivot.

### 15. [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

- Pattern: binary search on the value range using a count-of-elements-at-most predicate.

### 16. [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

- Pattern: search on the value range, counting entries at most the midpoint per row.

### 17. [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

- Pattern: search on answer space for the minimum feasible eating speed.

### 18. [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

- Pattern: search on answer space for the minimum feasible ship capacity.

### 19. [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)

- Pattern: search on answer space for the minimum wait day that yields enough bouquets.

### 20. [Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/)

- Pattern: search on answer space for the maximum minimum gap achievable when placing balls.

### 21. [Minimum Speed to Arrive on Time](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/)

- Pattern: search on answer space for the minimum speed that keeps total travel time in budget.

### 22. [Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)

- Pattern: binary search on the answer for the minimum feasible divisor.

### 23. [Successful Pairs of Spells and Potions](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/)

- Pattern: boundary search per spell over sorted potions for the first passing product.

### 24. [Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/)

- Pattern: boundary search on the count of missing values before each index.

### 25. [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)

- Pattern: boundary search over stored timestamps to find the latest value at or before a query time.

## Hards And Extensions

These are the binary search follow-ups that push beyond the standard medium set.

### 26. [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

- Pattern: rotated array search with duplicates, falling back to shrinking both ends.

### 27. [Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

- Pattern: rotation pivot search with duplicates at the boundary.

### 28. [Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/)

- Pattern: locate the peak, then run separate ascending and descending searches with a limited API.

### 29. [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)

- Pattern: search on answer space for the minimum largest subarray sum under a split-count constraint.

### 30. [Kth Smallest Number in Multiplication Table](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/)

- Pattern: search on the value range, counting multiplication-table entries at most the midpoint.

### 31. [Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/)

- Pattern: search on the distance value range with a two-pointer count of pairs within it.

### 32. [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

- Pattern: binary search a partition index instead of merging.

### 33. [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)

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
7. [Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/)
8. [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
9. [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
10. [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
11. [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
12. [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
13. [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)
14. [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
15. [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)
16. [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)
17. [Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/)
18. [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)
19. [Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/)
20. [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
```
