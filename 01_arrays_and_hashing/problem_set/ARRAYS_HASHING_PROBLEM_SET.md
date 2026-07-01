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

## Mediums

These are the array and hashing mediums you should drill for FAANG-style interviews.

### 8. [Group Anagrams](https://leetcode.com/problems/group-anagrams/)

- Pattern: hash map keyed by a sorted-string signature.

### 9. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

- Pattern: frequency map plus bucket sort or a heap.

### 10. [Product Of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

- Pattern: prefix products times suffix products.

### 11. [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

- Pattern: hash set lookup, only start counting from sequence heads.

### 12. [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

- Pattern: running prefix sum plus a count hash map.

### 13. [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

- Pattern: Kadane's variant tracking running max and min for sign flips.

### 14. [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

- Pattern: hash sets per row, column, and box.

### 15. [Encode And Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)

- Pattern: length-prefix encoding to make decoding unambiguous.

### 16. [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

- Pattern: use the first row and column as marker storage.

### 17. [Find All Duplicates In An Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

- Pattern: mark visited values in place using index sign flips.

### 18. [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

- Pattern: running prefix sum modulo k, hash map of first-seen remainder index.

## Hards And Extensions

These are the array and hashing follow-ups that push beyond the standard medium set.

### 19. [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

- Pattern: place each value at its index in place, then scan for the first mismatch.

### 20. [Design HashMap](https://leetcode.com/problems/design-hashmap/)

- Pattern: bucket array with separate chaining for collisions.

### 21. [Design HashSet](https://leetcode.com/problems/design-hashset/)

- Pattern: bucket array storing keys only, no values.

### 22. [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)

- Pattern: 2D prefix sum with inclusion-exclusion.

### 23. [Subarrays Divisible By K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)

- Pattern: running prefix sum modulo k, count matching remainders.

### 24. [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)

- Pattern: hash map of value to index paired with a dense array for O(1) random pick.

## Recommended Order

If you want the shortest path to array and hashing fluency, do them in this order:

```text
1. [Two Sum](https://leetcode.com/problems/two-sum/)
2. [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
3. [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
4. [Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
5. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
6. [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
7. [Rotate Array](https://leetcode.com/problems/rotate-array/)
8. [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
9. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
10. [Product Of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
11. [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
12. [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
13. [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
14. [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
15. [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
16. [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)
17. [Design HashMap](https://leetcode.com/problems/design-hashmap/)
18. [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)
```
