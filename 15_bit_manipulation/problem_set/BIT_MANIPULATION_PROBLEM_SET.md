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

### 6. [Hamming Distance](https://leetcode.com/problems/hamming-distance/)

- Pattern: popcount of `x ^ y` counts the differing bit positions.

### 7. [Complement Of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/)

- Pattern: XOR against an all-ones mask sized to the number's bit length.

### 8. [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

- Pattern: subtract shifted (doubled) divisors to build the quotient bit by bit.

## Masks

### 9. [Sum Of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)

- Pattern: XOR for sum without carry, AND-and-shift for the carry, repeat.

### 10. [Bitwise AND Of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

- Pattern: the answer is the shared prefix mask of `left` and `right`.

### 11. [Minimum Flips To Make A Or B Equal To C](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)

- Pattern: compare `a`, `b`, and `c` bit by bit and count required flips.

### 12. [UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/)

- Pattern: mask the leading bits of each byte to decode and verify continuation counts.

### 13. [Gray Code](https://leetcode.com/problems/gray-code/)

- Pattern: generate the sequence with `i ^ (i >> 1)` so consecutive codes differ by one bit.

## XOR Patterns

### 14. [Single Number](https://leetcode.com/problems/single-number/)

- Pattern: XOR every value together so paired duplicates cancel.

### 15. [Single Number II](https://leetcode.com/problems/single-number-ii/)

- Pattern: count bits mod 3 across all numbers to isolate the singleton.

### 16. [Single Number III](https://leetcode.com/problems/single-number-iii/)

- Pattern: XOR everything, then split by a distinguishing bit.

### 17. [Missing Number](https://leetcode.com/problems/missing-number/)

- Pattern: XOR indices against values so every present pair cancels.

### 18. [Find The Difference](https://leetcode.com/problems/find-the-difference/)

- Pattern: XOR both strings together so shared characters cancel out.

### 19. [Decode XORed Array](https://leetcode.com/problems/decode-xored-array/)

- Pattern: recover each element by XORing the previous decoded value with the encoded one.

## Subset Masks And Bitmask DP

### 20. [Subsets](https://leetcode.com/problems/subsets/)

- Pattern: enumerate every mask from `0` to `2^n - 1` (see also `09_backtracking`).

### 21. [Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance/)

- Pattern: sum per-bit contributions across all pairs instead of comparing pairs directly.

### 22. [Maximum XOR Of Two Numbers In An Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

- Pattern: build candidate prefixes bit by bit, greedily checking for a complement in a prefix set.

### 23. [Partition To K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

- Pattern: memoize over a used-elements bitmask while filling buckets to the target sum.

### 24. [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)

- Pattern: BFS over `(node, visited-mask)` states until every bit is set.

### 25. [Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam/)

- Pattern: DP over per-row seating bitmasks that are compatible with the row above.

### 26. [Fair Distribution of Cookies](https://leetcode.com/problems/fair-distribution-of-cookies/)

- Pattern: submask enumeration / bitmask DP assigning subsets to buckets.

## Recommended Order

If you want the shortest path to bit manipulation fluency, do them in this order:

```text
1. [Number Of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
2. [Counting Bits](https://leetcode.com/problems/counting-bits/)
3. [Power Of Two](https://leetcode.com/problems/power-of-two/)
4. [Power Of Four](https://leetcode.com/problems/power-of-four/)
5. [Hamming Distance](https://leetcode.com/problems/hamming-distance/)
6. [Complement Of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/)
7. [Reverse Bits](https://leetcode.com/problems/reverse-bits/)
8. [Missing Number](https://leetcode.com/problems/missing-number/)
9. [Single Number](https://leetcode.com/problems/single-number/)
10. [Find The Difference](https://leetcode.com/problems/find-the-difference/)
11. [Single Number II](https://leetcode.com/problems/single-number-ii/)
12. [Single Number III](https://leetcode.com/problems/single-number-iii/)
13. [Decode XORed Array](https://leetcode.com/problems/decode-xored-array/)
14. [Sum Of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)
15. [Bitwise AND Of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)
16. [Minimum Flips To Make A Or B Equal To C](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)
17. [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)
18. [Gray Code](https://leetcode.com/problems/gray-code/)
19. [UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/)
20. [Subsets](https://leetcode.com/problems/subsets/)
21. [Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance/)
22. [Maximum XOR Of Two Numbers In An Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)
23. [Partition To K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)
24. [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)
25. [Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam/)
26. [Fair Distribution of Cookies](https://leetcode.com/problems/fair-distribution-of-cookies/)
```
