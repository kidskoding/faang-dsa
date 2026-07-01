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

## Hards And Extensions

These are the two-pointer follow-ups that push beyond the standard medium set.

### 14. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

- Pattern: track the running max height from each end and trap water against the shorter side.

### 15. [4Sum](https://leetcode.com/problems/4sum/)

- Pattern: fix two values, then run opposite-end pointers on the remaining pair while skipping duplicates.

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
9. [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
10. [3Sum](https://leetcode.com/problems/3sum/)
11. [3Sum Closest](https://leetcode.com/problems/3sum-closest/)
12. [Sort Colors](https://leetcode.com/problems/sort-colors/)
13. [Boats To Save People](https://leetcode.com/problems/boats-to-save-people/)
14. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
15. [4Sum](https://leetcode.com/problems/4sum/)
```
