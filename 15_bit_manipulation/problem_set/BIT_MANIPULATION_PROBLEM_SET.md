# Bit Manipulation Problem Set

## Goal

Build fluency with raw bit operators, then use masks and XOR identities to
solve the counting, parity, and subset-enumeration problems that show up in
FAANG-style interviews.

## How To Use

Work the file in order. Bitwise basics and masks are the fundamentals. XOR
patterns and subset masks are the mediums and hard extensions.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Bitwise Basics

### 1. [Number Of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

- Pattern: repeatedly clear the lowest set bit with `n & (n - 1)`.

### 2. [Counting Bits](https://leetcode.com/problems/counting-bits/)

- Pattern: build a DP table from the popcount of `i >> 1`.

### 3. [Reverse Bits](https://leetcode.com/problems/reverse-bits/)

- Pattern: shift bits out of one integer while shifting them into another.

### 4. [Power Of Two](https://leetcode.com/problems/power-of-two/)

- Pattern: a power of two has exactly one set bit, so `n & (n - 1) == 0`.

### 5. [Power Of Four](https://leetcode.com/problems/power-of-four/)

- Pattern: one set bit plus a parity check on the bit's position.

## Masks

### 6. [Sum Of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)

- Pattern: XOR for sum without carry, AND-and-shift for the carry, repeat.

### 7. [Bitwise AND Of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

- Pattern: the answer is the shared prefix mask of `left` and `right`.

### 8. [Minimum Flips To Make A Or B Equal To C](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)

- Pattern: compare `a`, `b`, and `c` bit by bit and count required flips.

## XOR Patterns

### 9. [Single Number](https://leetcode.com/problems/single-number/)

- Pattern: XOR every value together so paired duplicates cancel.

### 10. [Single Number II](https://leetcode.com/problems/single-number-ii/)

- Pattern: count bits mod 3 across all numbers to isolate the singleton.

### 11. [Single Number III](https://leetcode.com/problems/single-number-iii/)

- Pattern: XOR everything, then split by a distinguishing bit.

### 12. [Missing Number](https://leetcode.com/problems/missing-number/)

- Pattern: XOR indices against values so every present pair cancels.

## Subset Masks And Bitmask DP

### 13. [Subsets](https://leetcode.com/problems/subsets/)

- Pattern: enumerate every mask from `0` to `2^n - 1` (see also `09_backtracking`).

### 14. [Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance/)

- Pattern: sum per-bit contributions across all pairs instead of comparing pairs directly.

### 15. [Maximum XOR Of Two Numbers In An Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

- Pattern: build candidate prefixes bit by bit, greedily checking for a complement in a prefix set.

## Recommended Order

If you want the shortest path to bit manipulation fluency, do them in this order:

```text
1. [Number Of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
2. [Counting Bits](https://leetcode.com/problems/counting-bits/)
3. [Power Of Two](https://leetcode.com/problems/power-of-two/)
4. [Power Of Four](https://leetcode.com/problems/power-of-four/)
5. [Reverse Bits](https://leetcode.com/problems/reverse-bits/)
6. [Missing Number](https://leetcode.com/problems/missing-number/)
7. [Single Number](https://leetcode.com/problems/single-number/)
8. [Single Number II](https://leetcode.com/problems/single-number-ii/)
9. [Single Number III](https://leetcode.com/problems/single-number-iii/)
10. [Sum Of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)
11. [Bitwise AND Of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)
12. [Subsets](https://leetcode.com/problems/subsets/)
13. [Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance/)
14. [Minimum Flips To Make A Or B Equal To C](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)
15. [Maximum XOR Of Two Numbers In An Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)
```
