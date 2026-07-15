# Arrays And Hashing Problem Set

## Goal

Build array and hash-table intuition across the core techniques — hash
maps and sets, in-place array manipulation, prefix and suffix sums, and Kadane's
running-optimum scan — then use each technique to solve the medium and hard
array/hashing problems that show up in LeetCode-style interviews.

## How To Use

Each section maps to one solution file in this folder and to one technique.
Work a section top to bottom: problems are ordered roughly easy to hard,
and the implemented ones come first. `solves:` names the function in that
section's file; `solves: (todo)` means the solution is not written yet.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Hashing

`hashing_problems.py` — hash maps and sets for complement lookups,
membership checks, frequency counts, and signature grouping.

### 1. [Two Sum](https://leetcode.com/problems/two-sum/)

- solves: `two_sum`
- Pattern: complement lookup in a hash map.

### 2. [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

- solves: `contains_duplicate`
- Pattern: seen set membership check.

### 3. [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

- solves: `is_anagram`
- Pattern: compare character frequency maps.

### 4. [Group Anagrams](https://leetcode.com/problems/group-anagrams/)

- solves: `group_anagrams`
- Pattern: hash map keyed by a sorted-string signature.

### 5. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

- solves: `top_k_frequent`
- Pattern: frequency map plus bucket sort or a heap.

### 6. [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

- solves: `longest_consecutive`
- Pattern: hash set lookup, only start counting from sequence heads.

### 7. [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

- solves: `is_valid_sudoku`
- Pattern: hash sets per row, column, and box.

### 8. [Encode And Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)

- solves: `Codec`
- Pattern: length-prefix encoding to make decoding unambiguous.

### 9. [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)

- solves: `intersect`
- Pattern: frequency-map intersection of two arrays.

### 10. [Majority Element](https://leetcode.com/problems/majority-element/)

- solves: `majority_element`
- Pattern: Boyer-Moore vote counting, or a frequency hash map.

### 11. [Majority Element II](https://leetcode.com/problems/majority-element-ii/)

- solves: `majority_element_ii`
- Pattern: Boyer-Moore with two candidate counters for the n/3 threshold.

### 12. [Design HashMap](https://leetcode.com/problems/design-hashmap/)

- solves: `MyHashMap`
- Pattern: bucket array with separate chaining for collisions.

## Array Manipulation

`array_problems.py` — in-place array and matrix moves: reversals,
prefix/suffix products, sign-flip marking, and index-as-hash placement.

### 13. [Rotate Array](https://leetcode.com/problems/rotate-array/)

- solves: `rotate`
- Pattern: reverse the whole array, then reverse each part in place.

### 14. [Product Of Array Except Self](https://leetcode.com/problems/product-except-self/)

- solves: `product_except_self`
- Pattern: prefix products times suffix products.

### 15. [Find All Duplicates In An Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

- solves: `find_duplicates`
- Pattern: mark visited values in place using index sign flips.

### 16. [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

- solves: `set_zeroes`
- Pattern: use the first row and column as marker storage.

### 17. [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)

- solves: `RandomizedSet`
- Pattern: hash map of value to index paired with a dense array for O(1) random pick.

### 18. [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

- solves: `first_missing_positive`
- Pattern: place each value at its index in place, then scan for the first mismatch.

### 19. [Sort Colors](https://leetcode.com/problems/sort-colors/)

- solves: `sort_colors`
- Pattern: Dutch national flag three-way partition in one pass.

### 20. [Find The Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

- solves: `find_duplicate`
- Pattern: treat values as pointers, Floyd cycle detection to find the repeat.

### 21. [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

- solves: `spiral_order`
- Pattern: shrink top/bottom/left/right bounds while walking the layers.

### 22. [Rotate Image](https://leetcode.com/problems/rotate-image/)

- solves: `rotate_image`
- Pattern: transpose in place, then reverse each row.

## Prefix & Suffix Sums

`prefix_sum_problems.py` — running cumulative sums built from the left
(prefix) and/or the right (suffix). Hash prefixes for O(1) range queries and
subarray-sum counting (including modulo and 2D variants); combine a prefix
pass with a suffix pass for split-point and both-sides problems.

### 23. [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)

- solves: `NumArray`
- Pattern: precompute a prefix sum array for O(1) range queries.

### 24. [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

- solves: `subarray_sum`
- Pattern: running prefix sum plus a count hash map.

### 25. [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

- solves: `check_subarray_sum`
- Pattern: running prefix sum modulo k, hash map of first-seen remainder index.

### 26. [Subarrays Divisible By K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)

- solves: `subarrays_div_by_k`
- Pattern: running prefix sum modulo k, count matching remainders.

### 27. [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)

- solves: `NumMatrix`
- Pattern: 2D prefix sum with inclusion-exclusion.

### 28. [Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)

- solves: `max_sub_array_len`
- Pattern: prefix sum with first-seen index in a hash map to get longest subarray.

### 29. [Contiguous Array](https://leetcode.com/problems/contiguous-array/)

- solves: `find_max_length`
- Pattern: map 0 to -1, track first index of each running prefix sum.

### 30. [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)

- solves: `pivot_index`
- Pattern: the pivot is where the prefix sum on the left equals the suffix sum on the right.

### 31. [Left and Right Sum Differences](https://leetcode.com/problems/left-and-right-sum-differences/)

- solves: `left_right_difference`
- Pattern: build a left prefix-sum array and a right suffix-sum array, then take the absolute difference per index.

### 32. [Maximum Score After Splitting a String](https://leetcode.com/problems/maximum-score-after-splitting-a-string/)

- solves: `max_score`
- Pattern: prefix count of zeros on the left plus suffix count of ones on the right, maximized over every split.

### 33. [Number of Ways to Split Array](https://leetcode.com/problems/number-of-ways-to-split-array/)

- solves: `ways_to_split_array`
- Pattern: sweep the split point comparing the left prefix sum against the remaining suffix sum.

## Kadane

`kadane_problems.py` — one-pass running optimum that extends or restarts at
each index, plus its min/max and circular variants.

### 34. [Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

- solves: `max_profit`
- Pattern: track the running minimum while scanning left to right.

### 35. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

- solves: `max_subarray`
- Pattern: Kadane's algorithm, extend or restart at each index.

### 36. [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

- solves: `max_product_subarray`
- Pattern: Kadane's variant tracking running max and min for sign flips.

### 37. [Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)

- solves: `max_subarray_sum_circular`
- Pattern: Kadane for both max subarray and total-minus-min subarray.

### 38. [Maximum Absolute Sum of Any Subarray](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/)

- solves: `max_absolute_sum`
- Pattern: run Kadane for both the max and min subarray, answer is the larger magnitude.

### 39. [Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/)

- solves: `max_turbulence_size`
- Pattern: Kadane-style up/down run lengths that extend only when the comparison sign alternates.

### 40. [K-Concatenation Maximum Sum](https://leetcode.com/problems/k-concatenation-maximum-sum/)

- solves: `k_concatenation_max_sum`
- Pattern: Kadane over one or two copies plus extra whole-array sums when the total is positive.
  </content>
  </invoke>
