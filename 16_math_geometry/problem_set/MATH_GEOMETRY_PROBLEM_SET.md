# Math And Geometry Problem Set

## Goal

Build math and geometry intuition across the four core techniques —
in-place matrix transforms, modular and digit arithmetic, gcd/lcm via
Euclid, and coordinate geometry — then use each technique to solve the
math-flavored problems that show up in LeetCode-style interviews.

## How To Use

Each section maps to one solution file in this folder and to one technique
family. Work a section top to bottom: problems are ordered roughly easy to
hard, and the implemented ones come first. `solves:` names the function in
that section's file; `solves: (todo)` means the solution is not written yet.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Matrix

`matrix_problems.py` — in-place matrix transforms using shrinking
boundaries, the grid's own borders as marks, and spare bits for state.

### 1. [Rotate Image](https://leetcode.com/problems/rotate-image/)

- solves: `rotate`
- Pattern: transpose the matrix, then reverse each row in place.

### 2. [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

- solves: `spiral_order`
- Pattern: shrink four boundaries while walking the ring.

### 3. [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)

- solves: `generate_matrix`
- Pattern: fill the same shrinking-boundary ring instead of reading it.

### 4. [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

- solves: `set_zeroes`
- Pattern: mark rows and columns to zero using the matrix's own first
  row/column.

### 5. [Game Of Life](https://leetcode.com/problems/game-of-life/)

- solves: `game_of_life`
- Pattern: encode next state in unused bits so the update stays in place.

## Modular And Digit Arithmetic

`modular_arithmetic_problems.py` — base-26 conversions, binary
exponentiation, and digit/number-theory transforms.

### 6. [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

- solves: `title_to_number`
- Pattern: treat the letters as a base-26 number.

### 7. [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/)

- solves: `convert_to_title`
- Pattern: base-26 conversion with a 1-indexed digit shift.

### 8. [Nim Game](https://leetcode.com/problems/nim-game/)

- solves: `can_win_nim`
- Pattern: find the losing positions via modulo on the pile size.

### 9. [Happy Number](https://leetcode.com/problems/happy-number/)

- solves: `is_happy`
- Pattern: cycle detection over repeated digit-square-sum transforms.

### 10. [Sqrt(x)](https://leetcode.com/problems/sqrtx/)

- solves: `my_sqrt`
- Pattern: binary search the answer space for the integer square root.

### 11. [Pow(x, n)](https://leetcode.com/problems/powx-n/)

- solves: `my_pow`
- Pattern: binary exponentiation halves the exponent each step.

### 12. [Plus One](https://leetcode.com/problems/plus-one/)

- solves: `plus_one`
- Pattern: walk digits right-to-left, carrying, and prepend a leading 1 if
  it overflows.

### 13. [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

- solves: `is_palindrome`
- Pattern: reverse half the digits and compare without converting to a
  string.

### 14. [Add Strings](https://leetcode.com/problems/add-strings/)

- solves: `add_strings`
- Pattern: digit-by-digit bignum addition with carry.

### 15. [Reverse Integer](https://leetcode.com/problems/reverse-integer/)

- solves: `reverse`
- Pattern: reverse digits with 32-bit overflow checking.

### 16. [Count Primes](https://leetcode.com/problems/count-primes/)

- solves: `count_primes`
- Pattern: sieve of Eratosthenes marks multiples as composite.

### 17. [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)

- solves: `trailing_zeroes`
- Pattern: count factors of 5 by summing floor divisions by increasing
  powers of 5.

### 18. [Multiply Strings](https://leetcode.com/problems/multiply-strings/)

- solves: `multiply`
- Pattern: schoolbook multiply into a fixed-size digit buffer indexed by
  position sums.

### 19. [Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

- solves: `int_to_roman`
- Pattern: greedily subtract the largest value-symbol pair, including the
  subtractive cases.

### 20. [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/)

- solves: `nth_ugly_number`
- Pattern: merge three pointer-advanced streams of multiples of 2, 3, and 5.

### 21. [Perfect Squares](https://leetcode.com/problems/perfect-squares/)

- solves: `num_squares`
- Pattern: DP over the fewest squares, or BFS on remaining-value states.

### 22. [Implement Rand10() Using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7/)

- solves: `rand10`
- Pattern: rejection sampling to build a uniform distribution.

### 23. [Pow(x, n)](https://leetcode.com/problems/powx-n/)

- solves: (todo)
- Pattern: binary exponentiation, squaring the base and halving the exponent, with
  the negative exponent handled by inverting once at the end.

## GCD And LCM

`gcd_lcm_problems.py` — Euclid's gcd applied to factor counts, repeated
strings, and reduced fractions.

### 24. [Number of Common Factors](https://leetcode.com/problems/number-of-common-factors/)

- solves: `common_factors`
- Pattern: the common factors of a and b are exactly the divisors of
  gcd(a, b).

### 25. [Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/)

- solves: `gcd_of_strings`
- Pattern: a common divisor exists only if `str1 + str2 == str2 + str1`;
  its length is gcd(len1, len2).

### 26. [Fraction To Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/)

- solves: `fraction_to_decimal`
- Pattern: use gcd to reduce the fraction, then track remainders to detect
  a repeating cycle.

### 27. [Smallest Even Multiple](https://leetcode.com/problems/smallest-even-multiple/)

- solves: `smallest_even_multiple`
- Pattern: the answer is lcm(n, 2) — `n` if it is already even, else `2 * n`.

### 28. [Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/)

- solves: `find_gcd`
- Pattern: gcd of the array equals gcd of only its smallest and largest
  elements.

### 29. [Water and Jug Problem](https://leetcode.com/problems/water-and-jug-problem/)

- solves: `can_measure_water`
- Pattern: by Bezout's identity, target is reachable iff it fits in the two
  jugs and is a multiple of gcd(jug1, jug2).

## Geometry

`geometry_problems.py` — coordinate geometry with squared distances,
interval overlap, reduced slopes, and area sweeps.

### 30. [Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/)

- solves: `is_rectangle_overlap`
- Pattern: check that both axis intervals overlap.

### 31. [Valid Square](https://leetcode.com/problems/valid-square/)

- solves: `valid_square`
- Pattern: compare squared distances between all point pairs.

### 32. [Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/)

- solves: `min_area_rect`
- Pattern: hash points and pair up diagonals that share a center and radius.

### 33. [Max Points On A Line](https://leetcode.com/problems/max-points-on-a-line/)

- solves: `max_points`
- Pattern: group points by reduced-slope key relative to each anchor point.

### 34. [Largest Triangle Area](https://leetcode.com/problems/largest-triangle-area/)

- solves: `largest_triangle_area`
- Pattern: apply the shoelace cross-product area over every triple of
  points.

### 35. [Rectangle Area](https://leetcode.com/problems/rectangle-area/)

- solves: `compute_area`
- Pattern: sum both areas and subtract the overlap of the two axis
  intervals.

### 36. [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

- solves: `k_closest`
- Pattern: keep the k smallest squared distances with a heap or quickselect.

### 37. [Basic Calculator](https://leetcode.com/problems/basic-calculator/)

- solves: `calculate`
- Pattern: evaluate with a running sign and a stack for parenthesized
  subexpressions.

### 38. [Self Crossing](https://leetcode.com/problems/self-crossing/)

- solves: `is_self_crossing`
- Pattern: compare each move against the prior few segments for the three
  crossing cases.

### 39. [Erect the Fence](https://leetcode.com/problems/erect-the-fence/)

- solves: `outer_trees`
- Pattern: build the convex hull (Andrew's monotone chain) via cross-product
  turns.

### 40. [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

- solves: `get_skyline`
- Pattern: sweep building edges and track the current max height with a heap.

### 41. [Perfect Rectangle](https://leetcode.com/problems/perfect-rectangle/)

- solves: `is_rectangle_cover`
- Pattern: check total area equals the bounding box and every interior
  corner cancels.

### 42. [Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/)

- solves: `rectangle_area`
- Pattern: coordinate-compress and sweep a line, summing active covered
  width.
