# Two Pointers Problem Set

## Goal

Build array two-pointer intuition from the ground up, then use that foundation to solve the medium and hard opposite-end, same-direction, and in-place mutation problems that show up in LeetCode-style interviews.

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

These are the two-pointer basics you should be able to do without thinking too hard.

### 1. [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

- Pattern: shrink from both ends while skipping non-alphanumeric characters.

### 2. [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

- Pattern: move `left` up or `right` down based on whether the sum is too small or too large.

### 3. [Reverse String](https://leetcode.com/problems/reverse-string/)

- Pattern: swap opposite ends in place until the pointers cross.

### 4. [Remove Element](https://leetcode.com/problems/remove-element/)

- Pattern: `write` pointer only advances when `read` finds a value to keep.

### 5. [Remove Duplicates From Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

- Pattern: `write` advances only when `nums[read]` differs from `nums[write - 1]`.

### 6. [Move Zeroes](https://leetcode.com/problems/move-zeroes/)

- Pattern: same-direction compaction, then backfill the tail with zeroes.

### 7. [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

- Pattern: write from the back so unread values are never overwritten.

### 8. [Squares Of A Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

- Pattern: the largest square is always at one of the two ends; fill the result from the back.

## Mediums

These are the two-pointer mediums you should drill for FAANG-style interviews.

### 9. [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

- Pattern: shrink from both ends, always moving the shorter wall.

### 10. [3Sum](https://leetcode.com/problems/3sum/)

- Pattern: fix one value, then run opposite-end pointers on the rest while skipping duplicates.

### 11. [3Sum Closest](https://leetcode.com/problems/3sum-closest/)

- Pattern: fix one value, then track the closest sum seen while narrowing with opposite-end pointers.

### 12. [Boats To Save People](https://leetcode.com/problems/boats-to-save-people/)

- Pattern: pair the lightest and heaviest person when they fit under the limit together.

### 13. [Sort Colors](https://leetcode.com/problems/sort-colors/)

- Pattern: Dutch national flag partitioning with low, mid, and high pointers.

### 14. [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)

- Pattern: shrink from both ends, and on the first mismatch try skipping either the left or the right character.

### 15. [3Sum Smaller](https://leetcode.com/problems/3sum-smaller/)

- Pattern: fix one value, then count all pairs at once when the opposite-end sum drops below the target.

### 16. [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

- Pattern: Floyd's cycle detection treating values as next-index pointers.

### 17. [Partition Labels](https://leetcode.com/problems/partition-labels/)

- Pattern: expand the current partition until the scan pointer reaches the last occurrence of every letter inside it.

### 18. [Reverse Words In A String](https://leetcode.com/problems/reverse-words-in-a-string/)

- Pattern: reverse the whole string, then reverse each word span with opposite-end pointers.

### 19. [Rotate Array](https://leetcode.com/problems/rotate-array/)

- Pattern: reverse-based rotation using opposite-end swaps on three ranges.

### 20. [Longest Mountain In Array](https://leetcode.com/problems/longest-mountain-in-array/)

- Pattern: walk up then down from each peak, extending a base pointer to measure the widest mountain.

### 21. [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)

- Pattern: scan both strings from the back, skipping characters consumed by backspaces before comparing.

### 22. [Bag Of Tokens](https://leetcode.com/problems/bag-of-tokens/)

- Pattern: sort, then spend the cheapest token for score and cash in the most expensive for power at the ends.

### 23. [Minimize Maximum Pair Sum In Array](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/)

- Pattern: sort, then pair smallest with largest from opposite ends to flatten the max pair sum.

### 24. [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

- Pattern: shrink a window from both ends, dropping whichever end is farther from the target.

### 25. [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)

- Pattern: advance two pointers across both sorted lists, emitting the overlap and moving the one that ends first.

## Hards And Extensions

These are the two-pointer follow-ups that push beyond the standard medium set.

### 26. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

- Pattern: track the running max height from each end and trap water against the shorter side.

### 27. [4Sum](https://leetcode.com/problems/4sum/)

- Pattern: fix two values, then run opposite-end pointers on the remaining pair while skipping duplicates.

### 28. [3Sum With Multiplicity](https://leetcode.com/problems/3sum-with-multiplicity/)

- Pattern: fix one value and count opposite-end pairs, handling equal-value multiplicities with combinatorics.

### 29. [Number Of Subsequences That Satisfy The Given Sum Condition](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

- Pattern: sort, then use opposite-end pointers to count valid min/max windows via powers of two.

### 30. [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)

- Pattern: same-direction window that shrinks from the left whenever the running product hits the limit.

### 31. [Number Of Subarrays With Bounded Maximum](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/)

- Pattern: count subarrays whose max lands in range by tracking the last out-of-range index with two pointers.

### 32. [Subarrays With K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)

- Pattern: exactly-K equals at-most-K minus at-most-(K-1), each computed with a same-direction window.

### 33. [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/)

- Pattern: partition around the median, then interleave halves with three-way pointer indexing.

## Recommended Order

If you want the shortest path to two-pointer fluency, do them in this order:

```text
1. [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
2. [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
3. [Reverse String](https://leetcode.com/problems/reverse-string/)
4. [Remove Element](https://leetcode.com/problems/remove-element/)
5. [Remove Duplicates From Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
6. [Move Zeroes](https://leetcode.com/problems/move-zeroes/)
7. [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
8. [Squares Of A Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)
9. [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)
10. [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
11. [3Sum](https://leetcode.com/problems/3sum/)
12. [3Sum Closest](https://leetcode.com/problems/3sum-closest/)
13. [3Sum Smaller](https://leetcode.com/problems/3sum-smaller/)
14. [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
15. [Sort Colors](https://leetcode.com/problems/sort-colors/)
16. [Partition Labels](https://leetcode.com/problems/partition-labels/)
17. [Boats To Save People](https://leetcode.com/problems/boats-to-save-people/)
18. [Bag Of Tokens](https://leetcode.com/problems/bag-of-tokens/)
19. [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)
20. [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)
21. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
22. [4Sum](https://leetcode.com/problems/4sum/)
23. [Subarrays With K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)
```
