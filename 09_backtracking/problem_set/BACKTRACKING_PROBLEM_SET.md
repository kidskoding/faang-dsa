# Backtracking Problem Set

## Goal

Build backtracking intuition across the core shapes — the
choose/explore/unchoose template, subsets and combinations, permutations,
and grid backtracking — then use each shape to solve the medium and hard
backtracking problems that show up in LeetCode-style interviews.

## How To Use

Each section maps to one solution file in this folder and to one
backtracking shape. Work a section top to bottom: problems are ordered
roughly easy to hard, and the implemented ones come first. `solves:` names
the function in that section's file; `solves: (todo)` means the solution is
not written yet.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Backtracking Basics

`backtracking_basics_problems.py` — the choose/explore/unchoose template
you should be able to write without thinking too hard.

### 1. [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

- solves: `letter_combinations`
- Pattern: choose one letter per digit position, recurse to the next digit.

### 2. [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

- solves: `generate_parentheses`
- Pattern: choose `(` or `)` while tracking open/close counts as a pruning constraint.

### 3. [Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/)

- solves: `count_arrangement`
- Pattern: place numbers one position at a time, pruning on the divisibility constraint.

### 4. [Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)

- solves: `letter_case_permutation`
- Pattern: at each letter branch on lower/upper case, pass digits straight through.

### 5. [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

- solves: `binary_tree_paths`
- Pattern: DFS the tree, append the node to the path on the way down and pop it on the way back up.

## Subsets And Combinations

`subsets_combinations_problems.py` — build choices in increasing index
order so no duplicate orderings are generated.

### 6. [Subsets](https://leetcode.com/problems/subsets/)

- solves: `subsets`
- Pattern: save the path at every node, advance `start` by one each recursion.

### 7. [Subsets II](https://leetcode.com/problems/subsets-ii/)

- solves: `subsets_with_dup`
- Pattern: sort first, skip repeated values at the same recursion depth.

### 8. [Combinations](https://leetcode.com/problems/combinations/)

- solves: `combine`
- Pattern: save the path only when it reaches size `k`.

### 9. [Combination Sum](https://leetcode.com/problems/combination-sum/)

- solves: `combination_sum`
- Pattern: reuse the same index to allow repeated picks, prune when the running sum exceeds the target.

### 10. [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

- solves: `combination_sum2`
- Pattern: sort first, advance past duplicates at the same depth, no reuse of the same index.

### 11. [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)

- solves: `combination_sum3`
- Pattern: fixed count and target sum both bound the recursion.

### 12. [Count Sorted Vowel Strings](https://leetcode.com/problems/count-sorted-vowel-strings/)

- solves: `count_vowel_strings`
- Pattern: choose each next vowel in non-decreasing order, count the leaves of the recursion tree.

## Permutations

`permutations_problems.py` — order matters, so each position can choose any
unused item.

### 13. [Permutations](https://leetcode.com/problems/permutations/)

- solves: `permute`
- Pattern: track used values with a boolean array, build the path position by position.

### 14. [Permutations II](https://leetcode.com/problems/permutations-ii/)

- solves: `permute_unique`
- Pattern: sort first, skip a duplicate value at the same depth unless the previous copy was used.

### 15. [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)

- solves: `partition`
- Pattern: choose the next substring cut, only recurse when the prefix is a palindrome.

### 16. [Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)

- solves: `restore_ip_addresses`
- Pattern: choose 1-3 digit segments, prune on the 0-255 and leading-zero constraints.

### 17. [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)

- solves: `get_permutation`
- Pattern: pick each digit by factorial block count rather than enumerating every permutation.

### 18. [Letter Tile Possibilities](https://leetcode.com/problems/letter-tile-possibilities/)

- solves: `num_tile_possibilities`
- Pattern: count sequences from a multiset of tiles, using per-depth counts to skip duplicate letters.

## Grid Backtracking

`grid_backtracking_problems.py` — DFS over grid cells and boards with
path-specific visited state, plus the hard placement/partition follow-ups.

### 19. [Word Search](https://leetcode.com/problems/word-search/)

- solves: `exist`
- Pattern: mark the current cell visited before exploring neighbors, unmark on backtrack.

### 20. [N-Queens](https://leetcode.com/problems/n-queens/)

- solves: `solve_n_queens`
- Pattern: place one queen per row, prune on column and diagonal conflicts.

### 21. [N-Queens II](https://leetcode.com/problems/n-queens-ii/)

- solves: `total_n_queens`
- Pattern: same placement search as N-Queens, count solutions instead of building boards.

### 22. [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

- solves: `solve_sudoku`
- Pattern: fill the next empty cell, prune on row/column/box constraints, backtrack on failure.

### 23. [Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/)

- solves: `makesquare`
- Pattern: assign each matchstick to one of four sides, prune when a side exceeds the target length.

### 24. [Unique Paths III](https://leetcode.com/problems/unique-paths-iii/)

- solves: `unique_paths_iii`
- Pattern: DFS every path that covers all empty cells, marking and unmarking cells as visited.

### 25. [Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/)

- solves: `clean_room`
- Pattern: DFS with a relative-coordinate visited set, turning the robot back to its prior heading on backtrack.

### 26. [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

- solves: `can_partition_k_subsets`
- Pattern: fill one bucket at a time to the target sum, sort descending and skip duplicate starts to prune.

### 27. [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/)

- solves: `add_operators`
- Pattern: choose `+`, `-`, `*`, or concatenation between digits, carrying the last operand to undo multiplication precedence.

### 28. [Word Break II](https://leetcode.com/problems/word-break-ii/)

- solves: `word_break`
- Pattern: choose each next dictionary-word prefix, memoizing suffixes to avoid re-exploring dead ends.

### 29. [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)

- solves: `remove_invalid_parentheses`
- Pattern: compute the minimum removals, then backtrack over which parentheses to drop, deduping at each depth.

### 30. [24 Game](https://leetcode.com/problems/24-game/)

- solves: `judge_point24`
- Pattern: pick two numbers and an operator, recurse on the reduced multiset until one value reaches 24.
