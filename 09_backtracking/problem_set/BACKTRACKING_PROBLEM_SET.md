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

### 4. [Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)

- Pattern: at each letter branch on lower/upper case, pass digits straight through.

### 5. [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

- Pattern: DFS the tree, append the node to the path on the way down and pop it on the way back up.

## Subsets And Combinations

These build choices in increasing index order to avoid duplicate orderings.

### 6. [Subsets](https://leetcode.com/problems/subsets/)

- Pattern: save the path at every node, advance `start` by one each recursion.

### 7. [Subsets II](https://leetcode.com/problems/subsets-ii/)

- Pattern: sort first, skip repeated values at the same recursion depth.

### 8. [Combinations](https://leetcode.com/problems/combinations/)

- Pattern: save the path only when it reaches size `k`.

### 9. [Combination Sum](https://leetcode.com/problems/combination-sum/)

- Pattern: reuse the same index to allow repeated picks, prune when the running sum exceeds the target.

### 10. [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

- Pattern: sort first, advance past duplicates at the same depth, no reuse of the same index.

### 11. [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)

- Pattern: fixed count and target sum both bound the recursion.

### 12. [Count Sorted Vowel Strings](https://leetcode.com/problems/count-sorted-vowel-strings/)

- Pattern: choose each next vowel in non-decreasing order, count the leaves of the recursion tree.

## Permutations

These care about order, so each position can choose any unused item.

### 13. [Permutations](https://leetcode.com/problems/permutations/)

- Pattern: track used values with a boolean array, build the path position by position.

### 14. [Permutations II](https://leetcode.com/problems/permutations-ii/)

- Pattern: sort first, skip a duplicate value at the same depth unless the previous copy was used.

### 15. [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)

- Pattern: choose the next substring cut, only recurse when the prefix is a palindrome.

### 16. [Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)

- Pattern: choose 1-3 digit segments, prune on the 0-255 and leading-zero constraints.

### 17. [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)

- Pattern: pick each digit by factorial block count rather than enumerating every permutation.

### 18. [Letter Tile Possibilities](https://leetcode.com/problems/letter-tile-possibilities/)

- Pattern: count sequences from a multiset of tiles, using per-depth counts to skip duplicate letters.

## Grid Backtracking

These are DFS over grid cells with path-specific visited state.

### 19. [Word Search](https://leetcode.com/problems/word-search/)

- Pattern: mark the current cell visited before exploring neighbors, unmark on backtrack.

### 20. [N-Queens](https://leetcode.com/problems/n-queens/)

- Pattern: place one queen per row, prune on column and diagonal conflicts.

### 21. [N-Queens II](https://leetcode.com/problems/n-queens-ii/)

- Pattern: same placement search as N-Queens, count solutions instead of building boards.

### 22. [Unique Paths III](https://leetcode.com/problems/unique-paths-iii/)

- Pattern: DFS every path that covers all empty cells, marking and unmarking cells as visited.

### 23. [Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/)

- Pattern: DFS with a relative-coordinate visited set, turning the robot back to its prior heading on backtrack.

## Hards And Extensions

These are the backtracking follow-ups that push beyond the standard medium set.

### 24. [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

- Pattern: fill the next empty cell, prune on row/column/box constraints, backtrack on failure.

### 25. [Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/)

- Pattern: assign each matchstick to one of four sides, prune when a side exceeds the target length.

### 26. [Word Search II](https://leetcode.com/problems/word-search-ii/) (optional)

- Pattern: grid backtracking driven by a trie instead of per-word DFS calls; cross-reference `14_tries`.

### 27. [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/)

- Pattern: choose `+`, `-`, `*`, or concatenation between digits, carrying the last operand to undo multiplication precedence.

### 28. [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)

- Pattern: compute the minimum removals, then backtrack over which parentheses to drop, deduping at each depth.

### 29. [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

- Pattern: fill one bucket at a time to the target sum, sort descending and skip duplicate starts to prune.

### 30. [Word Break II](https://leetcode.com/problems/word-break-ii/)

- Pattern: choose each next dictionary-word prefix, memoizing suffixes to avoid re-exploring dead ends.

### 31. [24 Game](https://leetcode.com/problems/24-game/)

- Pattern: pick two numbers and an operator, recurse on the reduced multiset until one value reaches 24.

## Recommended Order

If you want the shortest path to backtracking fluency, do them in this order:

```text
1. [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
2. [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
3. [Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)
4. [Subsets](https://leetcode.com/problems/subsets/)
5. [Subsets II](https://leetcode.com/problems/subsets-ii/)
6. [Combinations](https://leetcode.com/problems/combinations/)
7. [Combination Sum](https://leetcode.com/problems/combination-sum/)
8. [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
9. [Permutations](https://leetcode.com/problems/permutations/)
10. [Permutations II](https://leetcode.com/problems/permutations-ii/)
11. [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
12. [Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)
13. [Word Search](https://leetcode.com/problems/word-search/)
14. [N-Queens](https://leetcode.com/problems/n-queens/)
15. [Unique Paths III](https://leetcode.com/problems/unique-paths-iii/)
16. [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
17. [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)
18. [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/)
19. [Word Break II](https://leetcode.com/problems/word-break-ii/)
20. [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)
```
