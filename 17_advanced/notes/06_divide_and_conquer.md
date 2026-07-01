# Divide And Conquer

Binary search (`05_binary_search`) is the simplest relative of this paradigm —
it halves the input but solves only one side with no combine step
("decrease and conquer"). This note covers the full paradigm and its advanced
problems: Different Ways To Add Parentheses, The Skyline Problem, Closest Pair
Of Points, Beautiful Array.

## Pattern

Break a problem into independent subproblems of the same shape, solve each
recursively, then combine their results into the answer for the whole
problem.

## Intuition

Merge sort is the canonical example: divide (split the array in half),
conquer (recursively sort each half), combine (merge two sorted halves).
The same divide/conquer/combine shape shows up whenever a problem can be
split into non-overlapping pieces where the combine step is cheap relative to
solving each piece — that is what separates divide and conquer from dynamic
programming, where subproblems overlap and get cached instead of recombined.

## How It Works

1. **Divide**: split the input into smaller, independent pieces (usually
   halves, sometimes an operator or a spatial partition).
2. **Conquer**: recursively solve each piece down to a trivial base case.
3. **Combine**: merge the sub-results into the answer for the current level —
   this is usually where the real algorithmic work happens.

Divide and conquer beats brute force when the combine step can exploit
structure that a naive nested loop can't — e.g. merging two already-sorted
halves is O(n) instead of re-sorting, and merging two spatially-sorted point
strips only needs to check a narrow band instead of every pair.

## Template

```text
solve(problem):
    if problem is trivially small: return base_case_answer
    left, right = divide(problem)
    left_result = solve(left)
    right_result = solve(right)
    return combine(left_result, right_result)
```

## Example

Different Ways To Add Parentheses: split the expression on each operator,
recursively compute all results for the left and right substrings, then
combine every pair with that operator. The Skyline Problem: divide buildings
in half, recursively get each half's skyline, then merge two skylines with a
line-sweep merge (like merging two sorted lists, but tracking max height
instead of picking the smaller value).

## Master Theorem (brief)

For recurrences of the form `T(n) = a*T(n/b) + O(n^d)`, compare `d` to
`log_b(a)`: if `d > log_b(a)` the combine step dominates (e.g. merge sort:
`T(n) = 2T(n/2) + O(n)` gives O(n log n)); if `d < log_b(a)` the recursive
branching dominates; if they're equal you get an extra log factor. In
interviews it's enough to recognize the recurrence shape and state the
resulting complexity — deriving the theorem from scratch is low yield.

## Complexity

```text
Depends on the combine step: T(n) = a*T(n/b) + O(n^d) per the Master Theorem
Merge sort:      T(n) = 2T(n/2) + O(n)       -> O(n log n)
Closest pair:    T(n) = 2T(n/2) + O(n)       -> O(n log n)
Different Ways:  exponential in expression length (no shared subproblems)
```

## Pitfalls

- Reaching for divide and conquer when subproblems overlap — that's a DP
  signal, and D&C without memoization would redo the same work
  exponentially (Different Ways To Add Parentheses is the exception where
  overlap is rare enough that plain recursion is fine).
- Making the combine step as expensive as brute force, which erases the
  benefit of dividing in the first place (e.g. an O(n^2) skyline merge).
- Forgetting the base case, causing infinite recursion on size-0 or size-1
  inputs.
- Over-investing in Master Theorem derivations instead of just recognizing
  the recurrence shape and citing the known result.

## Interview Checklist

Before coding, make sure you can answer:

```text
Can this problem be split into independent, non-overlapping pieces? If the
pieces overlap, is DP a better fit than divide and conquer?
What is the base case, and does recursion actually reach it?
What does the combine step need to do, and can it exploit structure from the
divide step (sorted halves, spatial partition) to stay cheap?
What is the recurrence T(n) = a*T(n/b) + O(n^d), and what complexity does
that imply?
```
