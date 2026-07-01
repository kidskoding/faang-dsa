# Math And Geometry Problem Set

## Goal

Build the coordinate, modular, gcd/lcm, and geometry intuition needed for the math-flavored problems that show up in LeetCode-style interviews.

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

These are the matrix/coordinate and modular-arithmetic basics you should be able to do without thinking too hard.

### 1. [Rotate Image](https://leetcode.com/problems/rotate-image/)

- Pattern: transpose the matrix, then reverse each row in place.

### 2. [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

- Pattern: shrink four boundaries while walking the ring.

### 3. [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)

- Pattern: fill the same shrinking-boundary ring instead of reading it.

### 4. [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

- Pattern: mark rows and columns to zero using the matrix's own first row/column.

### 5. [Pow(x, n)](https://leetcode.com/problems/powx-n/)

- Pattern: binary exponentiation halves the exponent each step.

### 6. [Sqrt(x)](https://leetcode.com/problems/sqrtx/)

- Pattern: binary search the answer space for the integer square root.

## Mediums

These are the matrix, modular arithmetic, and gcd/lcm mediums you should drill for FAANG-style interviews.

### 7. [Game Of Life](https://leetcode.com/problems/game-of-life/)

- Pattern: encode next state in unused bits so the update stays in place.

### 8. [Fraction To Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/)

- Pattern: use gcd to reduce the fraction, then track remainders to detect a repeating cycle.

### 9. [Nim Game](https://leetcode.com/problems/nim-game/)

- Pattern: find the losing positions via modulo on the pile size.

### 10. [Happy Number](https://leetcode.com/problems/happy-number/)

- Pattern: cycle detection over repeated digit-square-sum transforms.

### 11. [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

- Pattern: treat the letters as a base-26 number.

### 12. [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/)

- Pattern: base-26 conversion with a 1-indexed digit shift.

## Geometry Basics

These are the coordinate-geometry problems that build on slopes, distances, and orientation.

### 13. [Valid Square](https://leetcode.com/problems/valid-square/)

- Pattern: compare squared distances between all point pairs.

### 14. [Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/)

- Pattern: check that both axis intervals overlap.

### 15. [Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/)

- Pattern: hash points and pair up diagonals that share a center and radius.

## Hards And Extensions

These are the math and geometry follow-ups that push beyond the standard medium set.

### 16. [Max Points On A Line](https://leetcode.com/problems/max-points-on-a-line/)

- Pattern: group points by reduced-slope key relative to each anchor point.

## Recommended Order

If you want the shortest path to math and geometry fluency, do them in this order:

```text
1. [Rotate Image](https://leetcode.com/problems/rotate-image/)
2. [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
3. [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)
4. [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
5. [Pow(x, n)](https://leetcode.com/problems/powx-n/)
6. [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
7. [Happy Number](https://leetcode.com/problems/happy-number/)
8. [Nim Game](https://leetcode.com/problems/nim-game/)
9. [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)
10. [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/)
11. [Fraction To Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/)
12. [Game Of Life](https://leetcode.com/problems/game-of-life/)
13. [Valid Square](https://leetcode.com/problems/valid-square/)
14. [Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/)
15. [Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/)
16. [Max Points On A Line](https://leetcode.com/problems/max-points-on-a-line/)
```
