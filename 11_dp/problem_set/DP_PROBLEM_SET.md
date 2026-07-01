# DP Problem Set

## Goal

Build DP intuition from single-index state through grid state, capacity-constrained
knapsack state, and two-sequence state, then use that foundation to solve the
medium and hard DP problems that show up in LeetCode-style interviews.

## How To Use

Work the file in order. Each band adds a new state shape on top of the last.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## 1D DP

State is a single index, usually the best answer up to or ending at that index.

### 1. [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

- Pattern: `dp[i] = dp[i - 1] + dp[i - 2]`.

### 2. [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)

- Pattern: choose the cheaper of the last one or two steps.

### 3. [House Robber](https://leetcode.com/problems/house-robber/)

- Pattern: rob or skip the current house.

### 4. [House Robber II](https://leetcode.com/problems/house-robber-ii/)

- Pattern: houses form a circle, so run House Robber twice excluding one end each time.

### 5. [Decode Ways](https://leetcode.com/problems/decode-ways/)

- Pattern: `dp[i]` depends on whether the last one or two digits form a valid letter code.

## 2D Grid DP

State is a row and column, usually built from the top and left neighbors.

### 6. [Unique Paths](https://leetcode.com/problems/unique-paths/)

- Pattern: sum the ways from the top and left cells.

### 7. [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)

- Pattern: same as Unique Paths but obstacles zero out a cell.

### 8. [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

- Pattern: take the cheaper of the top and left paths into each cell.

### 9. [Triangle](https://leetcode.com/problems/triangle/)

- Pattern: min path sum on a triangular grid, bottom-up.

### 10. [Maximal Square](https://leetcode.com/problems/maximal-square/)

- Pattern: `dp[r][c]` is the largest square side ending at that cell.

## Knapsack

State tracks item index and remaining or used capacity.

### 11. [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

- Pattern: 0/1 knapsack — can a subset hit exactly half the total sum.

### 12. [Target Sum](https://leetcode.com/problems/target-sum/)

- Pattern: 0/1 knapsack reframed as counting sign assignments that hit a target.

### 13. [Coin Change](https://leetcode.com/problems/coin-change/)

- Pattern: unbounded knapsack — fewest coins to reach an amount.

### 14. [Coin Change II](https://leetcode.com/problems/coin-change-ii/)

- Pattern: unbounded knapsack — count combinations that reach an amount.

## Sequence DP

State compares positions within one or two sequences.

### 15. [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

- Pattern: `dp[i]` is the longest increasing subsequence ending at i.

### 16. [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

- Pattern: `dp[i][j]` over prefixes of two strings, matching characters extend the diagonal.

### 17. [Edit Distance](https://leetcode.com/problems/edit-distance/)

- Pattern: `dp[i][j]` is the min operations to convert one prefix into another.

### 18. [Word Break](https://leetcode.com/problems/word-break/)

- Pattern: `dp[i]` is true if the prefix ending at i can be segmented into dictionary words.

### 19. [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

- Pattern: `dp[i][j]` is true if the substring is a palindrome, expand from the diagonal.

### 20. [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)

- Pattern: count every palindromic substring using the same table shape as above.

### 21. [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

- Pattern: state machine DP over held, sold, and cooldown states.

### 22. [Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

- Pattern: state machine DP over held and not-held states, fee charged on sell.

## Hards And Extensions

These push sequence DP into three inputs, counting subsequences, and interval DP.

### 23. [Interleaving String](https://leetcode.com/problems/interleaving-string/)

- Pattern: `dp[i][j]` tracks whether prefixes of two strings interleave into a third.

### 24. [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)

- Pattern: `dp[i][j]` counts ways one string's prefix appears as a subsequence of another.

### 25. [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

- Pattern: `dp[i][j]` handles literal, `.`, and `*` transitions between string and pattern.

### 26. [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)

- Pattern: `dp[i][j]` handles literal, `?`, and `*` transitions between string and pattern.

### 27. [Burst Balloons](https://leetcode.com/problems/burst-balloons/)

- Pattern: interval DP — choose the last balloon to burst in a range.

## Recommended Order

If you want the shortest path to DP fluency, do them in this order:

```text
1. [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
2. [House Robber](https://leetcode.com/problems/house-robber/)
3. [House Robber II](https://leetcode.com/problems/house-robber-ii/)
4. [Decode Ways](https://leetcode.com/problems/decode-ways/)
5. [Unique Paths](https://leetcode.com/problems/unique-paths/)
6. [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
7. [Triangle](https://leetcode.com/problems/triangle/)
8. [Coin Change](https://leetcode.com/problems/coin-change/)
9. [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
10. [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
11. [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
12. [Edit Distance](https://leetcode.com/problems/edit-distance/)
13. [Word Break](https://leetcode.com/problems/word-break/)
14. [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
15. [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
16. [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
17. [Burst Balloons](https://leetcode.com/problems/burst-balloons/)
```
