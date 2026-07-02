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

### 7. [Plus One](https://leetcode.com/problems/plus-one/)

- Pattern: walk digits right-to-left, carrying, and prepend a leading 1 if it overflows.

### 8. [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

- Pattern: reverse half the digits and compare without converting to a string.

### 9. [Add Strings](https://leetcode.com/problems/add-strings/)

- Pattern: digit-by-digit bignum addition with carry.

### 10. [Reverse Integer](https://leetcode.com/problems/reverse-integer/)

- Pattern: reverse digits with 32-bit overflow checking.

## Mediums

These are the matrix, modular arithmetic, and gcd/lcm mediums you should drill for FAANG-style interviews.

### 11. [Game Of Life](https://leetcode.com/problems/game-of-life/)

- Pattern: encode next state in unused bits so the update stays in place.

### 12. [Fraction To Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/)

- Pattern: use gcd to reduce the fraction, then track remainders to detect a repeating cycle.

### 13. [Happy Number](https://leetcode.com/problems/happy-number/)

- Pattern: cycle detection over repeated digit-square-sum transforms.

### 14. [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

- Pattern: treat the letters as a base-26 number.

### 15. [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/)

- Pattern: base-26 conversion with a 1-indexed digit shift.

### 16. [Multiply Strings](https://leetcode.com/problems/multiply-strings/)

- Pattern: schoolbook multiply into a fixed-size digit buffer indexed by position sums.

### 17. [Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

- Pattern: greedily subtract the largest value-symbol pair, including the subtractive cases.

### 18. [Count Primes](https://leetcode.com/problems/count-primes/)

- Pattern: sieve of Eratosthenes marks multiples as composite.

### 19. [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/)

- Pattern: merge three pointer-advanced streams of multiples of 2, 3, and 5.

### 20. [Perfect Squares](https://leetcode.com/problems/perfect-squares/)

- Pattern: DP over the fewest squares, or BFS on remaining-value states.

### 21. [Rectangle Area](https://leetcode.com/problems/rectangle-area/)

- Pattern: sum both areas and subtract the overlap of the two axis intervals.

### 22. [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)

- Pattern: count factors of 5 by summing floor divisions by increasing powers of 5.

### 23. [Implement Rand10() Using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7/)

- Pattern: rejection sampling to build a uniform distribution.

## Geometry Basics

These are the coordinate-geometry problems that build on slopes, distances, and orientation.

### 24. [Valid Square](https://leetcode.com/problems/valid-square/)

- Pattern: compare squared distances between all point pairs.

### 25. [Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/)

- Pattern: check that both axis intervals overlap.

### 26. [Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/)

- Pattern: hash points and pair up diagonals that share a center and radius.

### 27. [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

- Pattern: keep the k smallest squared distances with a heap or quickselect.

### 28. [Largest Triangle Area](https://leetcode.com/problems/largest-triangle-area/)

- Pattern: apply the shoelace cross-product area over every triple of points.

## Hards And Extensions

These are the math and geometry follow-ups that push beyond the standard medium set.

### 29. [Max Points On A Line](https://leetcode.com/problems/max-points-on-a-line/)

- Pattern: group points by reduced-slope key relative to each anchor point.

### 30. [Erect the Fence](https://leetcode.com/problems/erect-the-fence/)

- Pattern: build the convex hull (Andrew's monotone chain) via cross-product turns.

### 31. [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

- Pattern: sweep building edges and track the current max height with a heap.

### 32. [Perfect Rectangle](https://leetcode.com/problems/perfect-rectangle/)

- Pattern: check total area equals the bounding box and every interior corner cancels.

### 33. [Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/)

- Pattern: coordinate-compress and sweep a line, summing active covered width.

### 34. [Self Crossing](https://leetcode.com/problems/self-crossing/)

- Pattern: compare each move against the prior few segments for the three crossing cases.

### 35. [Basic Calculator](https://leetcode.com/problems/basic-calculator/)

- Pattern: evaluate with a running sign and a stack for parenthesized subexpressions.

## Recommended Order

If you want the shortest path to math and geometry fluency, do them in this order:

```text
1. [Rotate Image](https://leetcode.com/problems/rotate-image/)
2. [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
3. [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
4. [Plus One](https://leetcode.com/problems/plus-one/)
5. [Palindrome Number](https://leetcode.com/problems/palindrome-number/)
6. [Add Strings](https://leetcode.com/problems/add-strings/)
7. [Reverse Integer](https://leetcode.com/problems/reverse-integer/)
8. [Pow(x, n)](https://leetcode.com/problems/powx-n/)
9. [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
10. [Happy Number](https://leetcode.com/problems/happy-number/)
11. [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)
12. [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/)
13. [Count Primes](https://leetcode.com/problems/count-primes/)
14. [Multiply Strings](https://leetcode.com/problems/multiply-strings/)
15. [Integer to Roman](https://leetcode.com/problems/integer-to-roman/)
16. [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)
17. [Game Of Life](https://leetcode.com/problems/game-of-life/)
18. [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
19. [Rectangle Area](https://leetcode.com/problems/rectangle-area/)
20. [Max Points On A Line](https://leetcode.com/problems/max-points-on-a-line/)
21. [Erect the Fence](https://leetcode.com/problems/erect-the-fence/)
22. [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)
```
