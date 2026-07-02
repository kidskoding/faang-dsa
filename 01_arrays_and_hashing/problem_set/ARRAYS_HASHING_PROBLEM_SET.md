# Arrays And Hashing Problem Set

## Goal

Build array and hash-table intuition from the ground up, then use that foundation to solve the medium and hard array/hashing problems that show up in LeetCode-style interviews.

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

These are the array and hashing basics you should be able to do without thinking too hard.

### 1. [Two Sum](https://leetcode.com/problems/two-sum/)

- Pattern: complement lookup in a hash map.

### 2. [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

- Pattern: seen set membership check.

### 3. [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

- Pattern: compare character frequency maps.

### 4. [Rotate Array](https://leetcode.com/problems/rotate-array/)

- Pattern: reverse the whole array, then reverse each part in place.

### 5. [Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

- Pattern: track the running minimum while scanning left to right.

### 6. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

- Pattern: Kadane's algorithm, extend or restart at each index.

### 7. [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)

- Pattern: precompute a prefix sum array for O(1) range queries.

### 8. [Majority Element](https://leetcode.com/problems/majority-element/)

- Pattern: Boyer-Moore vote counting, or a frequency hash map.

### 9. [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)

- Pattern: frequency-map intersection of two arrays.

## Mediums

These are the array and hashing mediums you should drill for FAANG-style interviews.

### 10. [Group Anagrams](https://leetcode.com/problems/group-anagrams/)

- Pattern: hash map keyed by a sorted-string signature.

### 11. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

- Pattern: frequency map plus bucket sort or a heap.

### 12. [Product Of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

- Pattern: prefix products times suffix products.

### 13. [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

- Pattern: hash set lookup, only start counting from sequence heads.

### 14. [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

- Pattern: running prefix sum plus a count hash map.

### 15. [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

- Pattern: Kadane's variant tracking running max and min for sign flips.

### 16. [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

- Pattern: hash sets per row, column, and box.

### 17. [Encode And Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)

- Pattern: length-prefix encoding to make decoding unambiguous.

### 18. [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

- Pattern: use the first row and column as marker storage.

### 19. [Find All Duplicates In An Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

- Pattern: mark visited values in place using index sign flips.

### 20. [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

- Pattern: running prefix sum modulo k, hash map of first-seen remainder index.

### 21. [Contiguous Array](https://leetcode.com/problems/contiguous-array/)

- Pattern: map 0 to -1, track first index of each running prefix sum.

### 22. [Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)

- Pattern: Kadane for both max subarray and total-minus-min subarray.

### 23. [Sort Colors](https://leetcode.com/problems/sort-colors/)

- Pattern: Dutch national flag three-way partition in one pass.

### 24. [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

- Pattern: shrink top/bottom/left/right bounds while walking the layers.

### 25. [Rotate Image](https://leetcode.com/problems/rotate-image/)

- Pattern: transpose in place, then reverse each row.

### 26. [Find The Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

- Pattern: treat values as pointers, Floyd cycle detection to find the repeat.

### 27. [Majority Element II](https://leetcode.com/problems/majority-element-ii/)

- Pattern: Boyer-Moore with two candidate counters for the n/3 threshold.

### 28. [Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)

- Pattern: prefix sum with first-seen index in a hash map to get longest subarray.

## Hards And Extensions

These are the array and hashing follow-ups that push beyond the standard medium set.

### 29. [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

- Pattern: place each value at its index in place, then scan for the first mismatch.

### 30. [Design HashMap](https://leetcode.com/problems/design-hashmap/)

- Pattern: bucket array with separate chaining for collisions.

### 31. [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)

- Pattern: 2D prefix sum with inclusion-exclusion.

### 32. [Subarrays Divisible By K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)

- Pattern: running prefix sum modulo k, count matching remainders.

### 33. [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)

- Pattern: hash map of value to index paired with a dense array for O(1) random pick.

### 34. [Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)

- Pattern: prefix sums with merge sort or a BIT to count sums inside a range.

## Recommended Order

If you want the shortest path to array and hashing fluency, do them in this order:

```text
1. [Two Sum](https://leetcode.com/problems/two-sum/)
2. [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
3. [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
4. [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
5. [Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
6. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
7. [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
8. [Majority Element](https://leetcode.com/problems/majority-element/)
9. [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
10. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
11. [Product Of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
12. [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
13. [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
14. [Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)
15. [Contiguous Array](https://leetcode.com/problems/contiguous-array/)
16. [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
17. [Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)
18. [Sort Colors](https://leetcode.com/problems/sort-colors/)
19. [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
20. [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
21. [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)
22. [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)
```
