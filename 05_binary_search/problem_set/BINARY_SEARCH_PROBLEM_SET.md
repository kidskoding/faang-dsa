# Binary Search Problem Set

## Goal

Build binary search intuition across the four search techniques — exact-match
search over a sorted array, monotonic-predicate boundary search, rotated-array
search, and search-on-the-answer — then use each technique to solve the medium
and hard binary search problems that show up in LeetCode-style interviews.

## How To Use

Each section maps to one solution file in this folder and to one search
technique. Work a section top to bottom: problems are ordered roughly easy to
hard, and the implemented ones come first. `solves:` names the function in
that section's file; `solves: (todo)` means the solution is not written yet.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Exact-Match Search

`basic_search_problems.py` — classic binary search that halves a sorted array
looking for an exact target, plus the grid variants that flatten or walk a
sorted matrix.

### 1. [Binary Search](https://leetcode.com/problems/binary-search/)

- solves: `search`
- Pattern: exact-match search over a sorted array.

### 2. [Search Insert Position](https://leetcode.com/problems/search-insert-position/)

- solves: `search_insert`
- Pattern: find the first index where the value could be inserted.

### 3. [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

- solves: `search_matrix`
- Pattern: treat a row-sorted, column-sorted grid as one flattened sorted array.

### 4. [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)

- solves: `search_matrix_ii`
- Pattern: eliminate a full row or column at each step from a sorted-corner start.

### 5. [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)

- solves: `guess_number`
- Pattern: exact-match search driven by a comparison oracle instead of array reads.

## Boundary Search

`boundary_search_problems.py` — binary search for the boundary of a monotonic
false...false, true...true predicate, returning the first (or last) index that
satisfies it.

### 6. [First Bad Version](https://leetcode.com/problems/first-bad-version/)

- solves: `first_bad_version`
- Pattern: monotonic predicate boundary search.

### 7. [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

- solves: `search_range`
- Pattern: two boundary searches, one for the first true and one for the last true.

### 8. [Find Peak Element](https://leetcode.com/problems/find-peak-element/)

- solves: `find_peak_element`
- Pattern: binary search using the local slope instead of full sortedness.

### 9. [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

- solves: `find_closest_elements`
- Pattern: boundary search for the left edge of a fixed-size window.

### 10. [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)

- solves: `TimeMap`
- Pattern: boundary search over stored timestamps to find the latest value at or before a query time.

### 11. [Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)

- solves: `next_greatest_letter`
- Pattern: boundary search for the first element strictly greater than the target, with wraparound.

### 12. [Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/)

- solves: `find_kth_positive`
- Pattern: boundary search on the count of missing values before each index.

### 13. [Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/)

- solves: `single_non_duplicate`
- Pattern: binary search on pair-index parity to locate where the pairing breaks.

### 14. [Successful Pairs of Spells and Potions](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/)

- solves: `successful_pairs`
- Pattern: boundary search per spell over sorted potions for the first passing product.

### 15. [Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/)

- solves: `find_in_mountain_array`
- Pattern: locate the peak, then run separate ascending and descending searches with a limited API.

## Rotated Array Search

`rotated_array_problems.py` — binary search on a rotated sorted array by
deciding which half is sorted, extended to handle duplicate values at the
boundary.

### 16. [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

- solves: `search_rotated`
- Pattern: identify which half is sorted, then decide if the target lies inside it.

### 17. [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

- solves: `find_min_rotated`
- Pattern: boundary search for the rotation pivot.

### 18. [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

- solves: `search_rotated_ii`
- Pattern: rotated array search with duplicates, falling back to shrinking both ends.

### 19. [Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

- solves: `find_min_rotated_ii`
- Pattern: rotation pivot search with duplicates at the boundary.

### 20. [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)

- solves: `peak_index_in_mountain_array`
- Pattern: binary search on the slope of a mountain array, a rotated-array cousin, moving toward the ascending side until the peak is pinned.

## Search On Answer

`search_on_answer_problems.py` — binary search over a value or answer range
using a monotonic feasibility check to find the smallest (or largest) value
that works.

### 21. [Sqrt(x)](https://leetcode.com/problems/sqrtx/)

- solves: `my_sqrt`
- Pattern: binary search over the answer space for the largest value whose square fits.

### 22. [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

- solves: `min_eating_speed`
- Pattern: search on answer space for the minimum feasible eating speed.

### 23. [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

- solves: `ship_within_days`
- Pattern: search on answer space for the minimum feasible ship capacity.

### 24. [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)

- solves: `split_array`
- Pattern: search on answer space for the minimum largest subarray sum under a split-count constraint.

### 25. [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

- solves: `find_median_sorted_arrays`
- Pattern: binary search a partition index instead of merging.

### 26. [Arranging Coins](https://leetcode.com/problems/arranging-coins/)

- solves: `arrange_coins`
- Pattern: search on answer space for the largest full row count under a triangular-sum bound.

### 27. [Minimum Speed to Arrive on Time](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/)

- solves: `min_speed_on_time`
- Pattern: search on answer space for the minimum speed that keeps total travel time in budget.

### 28. [Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)

- solves: `smallest_divisor`
- Pattern: binary search on the answer for the minimum feasible divisor.

### 29. [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

- solves: `find_duplicate`
- Pattern: binary search on the value range using a count-of-elements-at-most predicate.

### 30. [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)

- solves: `min_days`
- Pattern: search on answer space for the minimum wait day that yields enough bouquets.

### 31. [Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/)

- solves: `max_distance`
- Pattern: search on answer space for the maximum minimum gap achievable when placing balls.

### 32. [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

- solves: `kth_smallest`
- Pattern: search on the value range, counting entries at most the midpoint per row.

### 33. [Kth Smallest Number in Multiplication Table](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/)

- solves: `find_kth_number`
- Pattern: search on the value range, counting multiplication-table entries at most the midpoint.

### 34. [Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/)

- solves: `smallest_distance_pair`
- Pattern: search on the distance value range with a two-pointer count of pairs within it.
  </content>
  </invoke>
