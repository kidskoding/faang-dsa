# Backtracking Problem Set

## Goal

Build backtracking intuition from the choose/explore/unchoose template through
subsets, combinations, permutations, and grid backtracking, then use that
foundation to solve the medium and hard backtracking problems that show up in
LeetCode-style interviews.

## How To Use

Work the file in order. The early sections are the fundamentals. The later
sections are the medium and hard extensions.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Backtracking Basics

These are the basics that teach the choose/explore/unchoose template you should
be able to do without thinking too hard.

### 1. [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

- Pattern: choose one letter per digit position, recurse to the next digit.

### 2. [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

- Pattern: choose `(` or `)` while tracking open/close counts as a pruning constraint.

### 3. [Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/)

- Pattern: place numbers one position at a time, pruning on the divisibility constraint.

## Subsets And Combinations

These build choices in increasing index order to avoid duplicate orderings.

### 4. [Subsets](https://leetcode.com/problems/subsets/)

- Pattern: save the path at every node, advance `start` by one each recursion.

### 5. [Subsets II](https://leetcode.com/problems/subsets-ii/)

- Pattern: sort first, skip repeated values at the same recursion depth.

### 6. [Combinations](https://leetcode.com/problems/combinations/)

- Pattern: save the path only when it reaches size `k`.

### 7. [Combination Sum](https://leetcode.com/problems/combination-sum/)

- Pattern: reuse the same index to allow repeated picks, prune when the running sum exceeds the target.

### 8. [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

- Pattern: sort first, advance past duplicates at the same depth, no reuse of the same index.

### 9. [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)

- Pattern: fixed count and target sum both bound the recursion.

## Permutations

These care about order, so each position can choose any unused item.

### 10. [Permutations](https://leetcode.com/problems/permutations/)

- Pattern: track used values with a boolean array, build the path position by position.

### 11. [Permutations II](https://leetcode.com/problems/permutations-ii/)

- Pattern: sort first, skip a duplicate value at the same depth unless the previous copy was used.

### 12. [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)

- Pattern: choose the next substring cut, only recurse when the prefix is a palindrome.

### 13. [Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)

- Pattern: choose 1-3 digit segments, prune on the 0-255 and leading-zero constraints.

## Grid Backtracking

These are DFS over grid cells with path-specific visited state.

### 14. [Word Search](https://leetcode.com/problems/word-search/)

- Pattern: mark the current cell visited before exploring neighbors, unmark on backtrack.

### 15. [N-Queens](https://leetcode.com/problems/n-queens/)

- Pattern: place one queen per row, prune on column and diagonal conflicts.

### 16. [N-Queens II](https://leetcode.com/problems/n-queens-ii/)

- Pattern: same placement search as N-Queens, count solutions instead of building boards.

## Hards And Extensions

These are the backtracking follow-ups that push beyond the standard medium set.

### 17. [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

- Pattern: fill the next empty cell, prune on row/column/box constraints, backtrack on failure.

### 18. [Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/)

- Pattern: assign each matchstick to one of four sides, prune when a side exceeds the target length.

### 19. [Word Search II](https://leetcode.com/problems/word-search-ii/) (optional)

- Pattern: grid backtracking driven by a trie instead of per-word DFS calls; cross-reference `14_tries`.

## Recommended Order

If you want the shortest path to backtracking fluency, do them in this order:

```text
1. [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
2. [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
3. [Subsets](https://leetcode.com/problems/subsets/)
4. [Subsets II](https://leetcode.com/problems/subsets-ii/)
5. [Combinations](https://leetcode.com/problems/combinations/)
6. [Combination Sum](https://leetcode.com/problems/combination-sum/)
7. [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
8. [Permutations](https://leetcode.com/problems/permutations/)
9. [Permutations II](https://leetcode.com/problems/permutations-ii/)
10. [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
11. [Word Search](https://leetcode.com/problems/word-search/)
12. [N-Queens](https://leetcode.com/problems/n-queens/)
13. [Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)
14. [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)
15. [Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/)
16. [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
```
