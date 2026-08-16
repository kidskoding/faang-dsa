# DP Problem Set

## Goal

Build DP intuition across the four state shapes — single-index (1D) state,
grid (row/column) state, capacity-constrained knapsack state, and
one-or-two-sequence state — then use each shape to solve the medium and hard
DP problems that show up in LeetCode-style interviews.

## How To Use

Each section maps to one solution file in this folder and to one DP state
shape. Work a section top to bottom: problems are ordered roughly easy to
hard, and the implemented ones come first. `solves:` names the function in
that section's file; `solves: (todo)` means the solution is not written yet.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## 1D DP

`one_d_dp_problems.py` — state is a single index, usually the best answer up
to or ending at that index.

### 1. [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

- solves: `climbing_stairs`
- Pattern: `dp[i] = dp[i - 1] + dp[i - 2]`, ways to reach step i.

### 2. [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)

- solves: `min_cost_climbing_stairs`
- Pattern: `dp[i]` is the cheapest cost to reach step i from one or two steps back.

### 3. [House Robber](https://leetcode.com/problems/house-robber/)

- solves: `rob`
- Pattern: `dp[i] = max(skip house i, rob house i + dp[i - 2])`.

### 4. [House Robber II](https://leetcode.com/problems/house-robber-ii/)

- solves: `rob_ii`
- Pattern: houses form a circle; run House Robber twice, excluding one end each time.

### 5. [Decode Ways](https://leetcode.com/problems/decode-ways/)

- solves: `num_decodings`
- Pattern: `dp[i]` sums the ways using the last one digit and the last two digits.

### 6. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

- solves: `max_subarray`
- Pattern: Kadane — best subarray ending at i either extends or restarts.

### 7. [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

- solves: `max_product`
- Pattern: track both max and min products ending at i since negatives flip signs.

### 8. [Delete and Earn](https://leetcode.com/problems/delete-and-earn/)

- solves: `delete_and_earn`
- Pattern: bucket values into points, then it reduces to House Robber over the value line.

## 2D Grid DP

`grid_dp_problems.py` — state is a row and column, usually built from the top
and left neighbors.

### 9. [Unique Paths](https://leetcode.com/problems/unique-paths/)

- solves: `unique_paths`
- Pattern: `dp[r][c] = dp[r - 1][c] + dp[r][c - 1]`.

### 10. [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)

- solves: `unique_paths_with_obstacles`
- Pattern: same recurrence as Unique Paths, but an obstacle cell is forced to 0.

### 11. [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

- solves: `min_path_sum`
- Pattern: `dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])`.

### 12. [Triangle](https://leetcode.com/problems/triangle/)

- solves: `minimum_total`
- Pattern: min path sum from the bottom row upward on a triangular grid.

### 13. [Maximal Square](https://leetcode.com/problems/maximal-square/)

- solves: `maximal_square`
- Pattern: `dp[r][c]` is the largest square side ending at that cell.

### 14. [Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/)

- solves: `min_falling_path_sum`
- Pattern: each cell takes the min of the three cells above it.

### 15. [Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)

- solves: `count_squares`
- Pattern: same recurrence as Maximal Square, but sum every side length to count squares.

## Knapsack

`knapsack_problems.py` — state tracks item index and remaining or used
capacity.

### 16. [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

- solves: `can_partition`
- Pattern: 0/1 knapsack — can a subset of nums sum to exactly half the total.

### 17. [Target Sum](https://leetcode.com/problems/target-sum/)

- solves: `find_target_sum_ways`
- Pattern: 0/1 knapsack reframed — count sign assignments that hit target.

### 18. [Coin Change](https://leetcode.com/problems/coin-change/)

- solves: `coin_change`
- Pattern: unbounded knapsack — fewest coins whose sum is amount.

### 19. [Coin Change II](https://leetcode.com/problems/coin-change-ii/)

- solves: `change`
- Pattern: unbounded knapsack — count combinations of coins that sum to amount.

### 20. [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)

- solves: `combination_sum4`
- Pattern: unbounded knapsack counting ordered sequences, so loop target outside items.

### 21. [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/)

- solves: `find_max_form`
- Pattern: 0/1 knapsack with two capacities, the counts of zeros and ones.

## Sequence DP

`sequence_dp_problems.py` — state compares positions within one or two
sequences, then pushes into three inputs, subsequence counting, and interval
DP.

### 22. [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

- solves: `length_of_lis`
- Pattern: `dp[i]` is the longest increasing subsequence ending at index i.

### 23. [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

- solves: `longest_common_subsequence`
- Pattern: `dp[i][j]` over prefixes; matching characters extend the diagonal.

### 24. [Word Break](https://leetcode.com/problems/word-break/)

- solves: `word_break`
- Pattern: `dp[i]` is true if the prefix ending at i splits into dictionary words.

### 25. [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)

- solves: `count_substrings`
- Pattern: count every palindromic substring using a `dp[i][j]` palindrome table.

### 26. [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

- solves: `longest_palindrome`
- Pattern: `dp[i][j]` is true if s[i..j] is a palindrome, built from shorter spans.

### 27. [Edit Distance](https://leetcode.com/problems/edit-distance/)

- solves: `min_distance`
- Pattern: `dp[i][j]` is the min insert/delete/replace ops to convert one prefix to another.

### 28. [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

- solves: `max_profit_with_cooldown`
- Pattern: state machine DP over held, sold-today, and cooldown states.

### 29. [Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

- solves: `max_profit_with_fee`
- Pattern: state machine DP over held and not-held states, fee charged on sell.

### 30. [Interleaving String](https://leetcode.com/problems/interleaving-string/)

- solves: `is_interleave`
- Pattern: `dp[i][j]` tracks whether prefixes of s1 and s2 interleave into s3's prefix.

### 31. [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)

- solves: `num_distinct`
- Pattern: `dp[i][j]` counts ways t's prefix appears as a subsequence of s's prefix.

### 32. [Burst Balloons](https://leetcode.com/problems/burst-balloons/)

- solves: `max_coins`
- Pattern: interval DP — choose the last balloon to burst within a range.

### 33. [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

- solves: `is_match_regex`
- Pattern: `dp[i][j]` handles literal, `.`, and `*` transitions between s and p.

### 34. [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)

- solves: `is_match_wildcard`
- Pattern: `dp[i][j]` handles literal, `?`, and `*` transitions between s and p.

### 35. [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/)

- solves: `min_cut`
- Pattern: min-cut partition DP with a precomputed palindrome table.

### 36. [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

- solves: `max_profit_iv`
- Pattern: state DP over (day, transactions-remaining, holding).

### 37. [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

- solves: `longest_valid_parentheses`
- Pattern: `dp[i]` is the longest valid substring ending at i, closing bracket looks back.

### 38. [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)

- solves: `maximal_rectangle`
- Pattern: build per-row histogram heights, then largest-rectangle-in-histogram each row.

### 39. [Minimum Cost to Merge Stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/)

- solves: `merge_stones`
- Pattern: interval DP over merge ranges.

### 40. [Cherry Pickup](https://leetcode.com/problems/cherry-pickup/)

- solves: `cherry_pickup`
- Pattern: two walks at once, `dp` over both positions on a shared diagonal.

### 41. [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)

- solves: `longest_palindrome_subseq`
- Pattern: the LCS recurrence run against the reversed string, or `dp[i][j]` over
  a widening interval where matching ends add two.
