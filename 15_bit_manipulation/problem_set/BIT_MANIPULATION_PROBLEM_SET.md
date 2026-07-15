# Bit Manipulation Problem Set

## Goal

Build fluency with the four bit-manipulation techniques — raw bit operators,
mask arithmetic, XOR identities, and subset/bitmask enumeration — then use
each technique to solve the counting, parity, and subset problems that show
up in FAANG-style interviews.

## How To Use

Each section maps to one solution file in this folder and to one bit
technique. Work a section top to bottom: problems are ordered roughly easy
to hard, and the implemented ones come first. `solves:` names the function
in that section's file; `solves: (todo)` means the solution is not written
yet.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Bitwise Basics

`bitwise_basics_problems.py` — raw bit operators: clear the lowest set bit,
shift bits in and out, and test single-bit properties.

### 1. [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

- solves: `hamming_weight`
- Pattern: repeatedly clear the lowest set bit with `n & (n - 1)` and count steps.

### 2. [Counting Bits](https://leetcode.com/problems/counting-bits/)

- solves: `count_bits`
- Pattern: build a DP table where `ans[i] = ans[i >> 1] + (i & 1)`.

### 3. [Power of Two](https://leetcode.com/problems/power-of-two/)

- solves: `is_power_of_two`
- Pattern: a positive power of two has exactly one set bit, so `n & (n - 1) == 0`.

### 4. [Power of Four](https://leetcode.com/problems/power-of-four/)

- solves: `is_power_of_four`
- Pattern: one set bit plus that bit sitting at an even position.

### 5. [Reverse Bits](https://leetcode.com/problems/reverse-bits/)

- solves: `reverse_bits`
- Pattern: shift bits out of `n` while shifting them into the result.

### 6. [Hamming Distance](https://leetcode.com/problems/hamming-distance/)

- solves: `hamming_distance`
- Pattern: popcount of `x ^ y` counts the differing bit positions.

### 7. [Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/)

- solves: `bitwise_complement`
- Pattern: XOR against an all-ones mask sized to the number's bit length.

### 8. [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

- solves: `divide`
- Pattern: subtract shifted (doubled) divisors to build the quotient bit by bit.

## Masks

`masks_problems.py` — mask arithmetic: add without a `+`, collapse a range to
its shared prefix, and reconcile bits across operands.

### 9. [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)

- solves: `get_sum`
- Pattern: XOR gives the sum without carry, AND-and-shift gives the carry, repeat until no carry.

### 10. [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

- solves: `range_bitwise_and`
- Pattern: shift both bounds right together until they match, then shift the shared prefix back.

### 11. [Minimum Flips to Make a OR b Equal to c](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)

- solves: `min_flips`
- Pattern: compare `a`, `b`, and `c` bit by bit and count the flips needed to fix each mismatch.

### 12. [Gray Code](https://leetcode.com/problems/gray-code/)

- solves: `gray_code`
- Pattern: generate the sequence with `i ^ (i >> 1)` so consecutive codes differ by one bit.

### 13. [UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/)

- solves: `valid_utf8`
- Pattern: mask the leading bits of each byte to decode and verify continuation counts.

## XOR Patterns

`xor_problems.py` — XOR identities: paired values cancel, so the survivor is
the singleton, the missing element, or the distinguishing bit.

### 14. [Single Number](https://leetcode.com/problems/single-number/)

- solves: `single_number`
- Pattern: XOR every value together so paired duplicates cancel, leaving the singleton.

### 15. [Missing Number](https://leetcode.com/problems/missing-number/)

- solves: `missing_number`
- Pattern: XOR every index and every value together so present pairs cancel, leaving the missing one.

### 16. [Single Number II](https://leetcode.com/problems/single-number-ii/)

- solves: `single_number_ii`
- Pattern: sum each bit position mod 3 across all numbers to isolate the singleton's bits.

### 17. [Single Number III](https://leetcode.com/problems/single-number-iii/)

- solves: `single_number_iii`
- Pattern: XOR everything to get the diff of the two singles, then split by a set bit in diff.

### 18. [Find the Difference](https://leetcode.com/problems/find-the-difference/)

- solves: `find_the_difference`
- Pattern: XOR both strings together so shared characters cancel out.

### 19. [Decode XORed Array](https://leetcode.com/problems/decode-xored-array/)

- solves: `decode`
- Pattern: recover each element by XORing the previous decoded value with the encoded one.

## Subset Masks and Bitmask DP

`subset_masks_problems.py` — treat an integer as a set: enumerate masks, sum
per-bit contributions, and build answers bit by bit.

### 20. [Subsets](https://leetcode.com/problems/subsets/)

- solves: `subsets`
- Pattern: enumerate every mask from `0` to `2^n - 1` and read off included items (see also `09_backtracking`).

### 21. [Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance/)

- solves: `total_hamming_distance`
- Pattern: sum, per bit position, `ones * zeros` across all numbers instead of comparing pairs.

### 22. [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

- solves: `max_xor_of_two_numbers`
- Pattern: build the answer bit by bit, greedily checking for a complement prefix in a seen set.

### 23. [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

- solves: `can_partition_k_subsets`
- Pattern: memoize over a used-elements bitmask while filling buckets to the target sum.

### 24. [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)

- solves: `shortest_path_length`
- Pattern: BFS over `(node, visited-mask)` states until every bit is set.

### 25. [Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam/)

- solves: `max_students`
- Pattern: DP over per-row seating bitmasks that are compatible with the row above.

### 26. [Fair Distribution of Cookies](https://leetcode.com/problems/fair-distribution-of-cookies/)

- solves: `distribute_cookies`
- Pattern: submask enumeration / bitmask DP assigning subsets to buckets.
