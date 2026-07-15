# Two Pointers Problem Set

## Goal

Build two-pointer intuition across the three array techniques —
opposite-end (converging) pointers, same-direction (fast/slow) pointers,
and in-place mutation — then use each technique to solve the medium and
hard two-pointer problems that show up in LeetCode-style interviews.

## How To Use

Each section maps to one solution file in this folder and to one
two-pointer technique. Work a section top to bottom: problems are ordered
roughly easy to hard, and the implemented ones come first. `solves:` names
the function in that section's file; `solves: (todo)` means the solution is
not written yet.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Opposite-End Pointers

`opposite_end_problems.py` — one pointer at each end converging toward the
middle; move whichever end the comparison rules out.

### 1. [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

- solves: `is_palindrome`
- Pattern: shrink from both ends while skipping non-alphanumeric characters.

### 2. [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

- solves: `two_sum`
- Pattern: move `left` up or `right` down based on whether the sum is too small or too large.

### 3. [Reverse String](https://leetcode.com/problems/reverse-string/)

- solves: `reverse_string`
- Pattern: swap opposite ends in place until the pointers cross.

### 4. [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

- solves: `max_area`
- Pattern: shrink from both ends, always moving the shorter wall.

### 5. [Boats To Save People](https://leetcode.com/problems/boats-to-save-people/)

- solves: `num_rescue_boats`
- Pattern: pair the lightest and heaviest person when they fit under the limit together.

### 6. [3Sum](https://leetcode.com/problems/3sum/)

- solves: `three_sum`
- Pattern: fix one value, then run opposite-end pointers on the rest while skipping duplicates.

### 7. [3Sum Closest](https://leetcode.com/problems/3sum-closest/)

- solves: `three_sum_closest`
- Pattern: fix one value, then track the closest sum seen while narrowing with opposite-end pointers.

### 8. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

- solves: `trap`
- Pattern: track the running max height from each end and trap water against the shorter side.

### 9. [4Sum](https://leetcode.com/problems/4sum/)

- solves: `four_sum`
- Pattern: fix two values, then run opposite-end pointers on the remaining pair while skipping duplicates.

### 10. [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)

- solves: `valid_palindrome`
- Pattern: shrink from both ends, and on the first mismatch try skipping either the left or the right character.

### 11. [Bag Of Tokens](https://leetcode.com/problems/bag-of-tokens/)

- solves: `bag_of_tokens_score`
- Pattern: sort, then spend the cheapest token for score and cash in the most expensive for power at the ends.

### 12. [Minimize Maximum Pair Sum In Array](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/)

- solves: `min_pair_sum`
- Pattern: sort, then pair smallest with largest from opposite ends to flatten the max pair sum.

### 13. [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

- solves: `find_closest_elements`
- Pattern: shrink a window from both ends, dropping whichever end is farther from the target.

### 14. [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)

- solves: `backspace_compare`
- Pattern: scan both strings from the back, skipping characters consumed by backspaces before comparing.

### 15. [Reverse Words In A String](https://leetcode.com/problems/reverse-words-in-a-string/)

- solves: `reverse_words`
- Pattern: reverse the whole string, then reverse each word span with opposite-end pointers.

### 16. [3Sum Smaller](https://leetcode.com/problems/3sum-smaller/)

- solves: `three_sum_smaller`
- Pattern: fix one value, then count all pairs at once when the opposite-end sum drops below the target.

### 17. [3Sum With Multiplicity](https://leetcode.com/problems/3sum-with-multiplicity/)

- solves: `three_sum_multi`
- Pattern: fix one value and count opposite-end pairs, handling equal-value multiplicities with combinatorics.

### 18. [Number Of Subsequences That Satisfy The Given Sum Condition](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

- solves: `num_subseq`
- Pattern: sort, then use opposite-end pointers to count valid min/max windows via powers of two.

## Same-Direction Pointers

`same_direction_problems.py` — both pointers move the same way; a fast
read pointer scans while a slow write pointer trails behind.

### 19. [Remove Element](https://leetcode.com/problems/remove-element/)

- solves: `remove_element`
- Pattern: `write` pointer only advances when `read` finds a value to keep.

### 20. [Remove Duplicates From Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

- solves: `remove_duplicates`
- Pattern: `write` advances only when `nums[read]` differs from `nums[write - 1]`.

### 21. [Move Zeroes](https://leetcode.com/problems/move-zeroes/)

- solves: `move_zeroes`
- Pattern: same-direction compaction, then backfill the tail with zeroes.

### 22. [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

- solves: `find_duplicate`
- Pattern: Floyd's cycle detection treating values as next-index pointers.

### 23. [Partition Labels](https://leetcode.com/problems/partition-labels/)

- solves: `partition_labels`
- Pattern: expand the current partition until the scan pointer reaches the last occurrence of every letter inside it.

### 24. [Longest Mountain In Array](https://leetcode.com/problems/longest-mountain-in-array/)

- solves: `longest_mountain`
- Pattern: walk up then down from each peak, extending a base pointer to measure the widest mountain.

### 25. [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)

- solves: `num_subarray_product_less_than_k`
- Pattern: same-direction window that shrinks from the left whenever the running product hits the limit.

### 26. [Number Of Subarrays With Bounded Maximum](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/)

- solves: `num_subarray_bounded_max`
- Pattern: count subarrays whose max lands in range by tracking the last out-of-range index with two pointers.

### 27. [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)

- solves: `interval_intersection`
- Pattern: advance two pointers across both sorted lists, emitting the overlap and moving the one that ends first.

### 28. [Subarrays With K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)

- solves: `subarrays_with_k_distinct`
- Pattern: exactly-K equals at-most-K minus at-most-(K-1), each computed with a same-direction window.

## In-Place Mutation

`in_place_mutation_problems.py` — rearrange an array in place with two (or
three) pointers, often writing from the back to avoid clobbering unread
values.

### 29. [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

- solves: `merge`
- Pattern: write from the back so unread values are never overwritten.

### 30. [Squares Of A Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

- solves: `sorted_squares`
- Pattern: the largest square is always at one of the two ends; fill the result from the back.

### 31. [Sort Colors](https://leetcode.com/problems/sort-colors/)

- solves: `sort_colors`
- Pattern: Dutch national flag partitioning with low, mid, and high pointers.

### 32. [Rotate Array](https://leetcode.com/problems/rotate-array/)

- solves: `rotate`
- Pattern: reverse-based rotation using opposite-end swaps on three ranges.

### 33. [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/)

- solves: `wiggle_sort`
- Pattern: partition around the median, then interleave halves with three-way pointer indexing.
  </content>
  </invoke>
