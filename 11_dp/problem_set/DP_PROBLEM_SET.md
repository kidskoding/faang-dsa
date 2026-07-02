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

### 6. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

- Pattern: Kadane — best subarray ending at i is either extend or restart.

### 7. [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

- Pattern: track both max and min products ending at i since negatives flip signs.

### 8. [Delete and Earn](https://leetcode.com/problems/delete-and-earn/)

- Pattern: bucket values into points, then it reduces to House Robber over the value line.

## 2D Grid DP

State is a row and column, usually built from the top and left neighbors.

### 9. [Unique Paths](https://leetcode.com/problems/unique-paths/)

- Pattern: sum the ways from the top and left cells.

### 10. [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)

- Pattern: same as Unique Paths but obstacles zero out a cell.

### 11. [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

- Pattern: take the cheaper of the top and left paths into each cell.

### 12. [Triangle](https://leetcode.com/problems/triangle/)

- Pattern: min path sum on a triangular grid, bottom-up.

### 13. [Maximal Square](https://leetcode.com/problems/maximal-square/)

- Pattern: `dp[r][c]` is the largest square side ending at that cell.

### 14. [Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/)

- Pattern: each cell takes the min of the three cells above it.

### 15. [Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)

- Pattern: same recurrence as Maximal Square, but sum every side length to count squares.

## Knapsack

State tracks item index and remaining or used capacity.

### 16. [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

- Pattern: 0/1 knapsack — can a subset hit exactly half the total sum.

### 17. [Target Sum](https://leetcode.com/problems/target-sum/)

- Pattern: 0/1 knapsack reframed as counting sign assignments that hit a target.

### 18. [Coin Change](https://leetcode.com/problems/coin-change/)

- Pattern: unbounded knapsack — fewest coins to reach an amount.

### 19. [Coin Change II](https://leetcode.com/problems/coin-change-ii/)

- Pattern: unbounded knapsack — count combinations that reach an amount.

### 20. [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)

- Pattern: unbounded knapsack counting ordered sequences, so loop target outside items.

### 21. [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/)

- Pattern: 0/1 knapsack with two capacities, the counts of zeros and ones.

## Sequence DP

State compares positions within one or two sequences.

### 22. [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

- Pattern: `dp[i]` is the longest increasing subsequence ending at i.

### 23. [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)

- Pattern: sort then O(n log n) LIS on the second dimension.

### 24. [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

- Pattern: `dp[i][j]` over prefixes of two strings, matching characters extend the diagonal.

### 25. [Edit Distance](https://leetcode.com/problems/edit-distance/)

- Pattern: `dp[i][j]` is the min operations to convert one prefix into another.

### 26. [Word Break](https://leetcode.com/problems/word-break/)

- Pattern: `dp[i]` is true if the prefix ending at i can be segmented into dictionary words.

### 27. [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

- Pattern: `dp[i][j]` is true if the substring is a palindrome, expand from the diagonal.

### 28. [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)

- Pattern: count every palindromic substring using the same table shape as above.

### 29. [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/)

- Pattern: min-cut partition DP with precomputed palindrome table.

### 30. [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

- Pattern: state machine DP over held, sold, and cooldown states.

### 31. [Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

- Pattern: state machine DP over held and not-held states, fee charged on sell.

### 32. [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

- Pattern: state DP over (day, transactions-remaining, holding).

## Hards And Extensions

These push sequence DP into three inputs, counting subsequences, and interval DP.

### 33. [Interleaving String](https://leetcode.com/problems/interleaving-string/)

- Pattern: `dp[i][j]` tracks whether prefixes of two strings interleave into a third.

### 34. [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)

- Pattern: `dp[i][j]` counts ways one string's prefix appears as a subsequence of another.

### 35. [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

- Pattern: `dp[i][j]` handles literal, `.`, and `*` transitions between string and pattern.

### 36. [Burst Balloons](https://leetcode.com/problems/burst-balloons/)

- Pattern: interval DP — choose the last balloon to burst in a range.

### 37. [Minimum Cost to Merge Stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/)

- Pattern: interval DP over merge ranges.

### 38. [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

- Pattern: `dp[i]` is the longest valid substring ending at i, closing bracket looks back.

### 39. [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)

- Pattern: build per-row histogram heights, then largest-rectangle-in-histogram each row.

### 40. [Cherry Pickup](https://leetcode.com/problems/cherry-pickup/)

- Pattern: two walks at once, `dp` over both positions on a shared diagonal.

## Recommended Order

If you want the shortest path to DP fluency, do them in this order:

```text
1. [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
2. [House Robber](https://leetcode.com/problems/house-robber/)
3. [House Robber II](https://leetcode.com/problems/house-robber-ii/)
4. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
5. [Decode Ways](https://leetcode.com/problems/decode-ways/)
6. [Unique Paths](https://leetcode.com/problems/unique-paths/)
7. [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
8. [Triangle](https://leetcode.com/problems/triangle/)
9. [Maximal Square](https://leetcode.com/problems/maximal-square/)
10. [Coin Change](https://leetcode.com/problems/coin-change/)
11. [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
12. [Target Sum](https://leetcode.com/problems/target-sum/)
13. [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
14. [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)
15. [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
16. [Edit Distance](https://leetcode.com/problems/edit-distance/)
17. [Word Break](https://leetcode.com/problems/word-break/)
18. [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
19. [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
20. [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
21. [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
22. [Burst Balloons](https://leetcode.com/problems/burst-balloons/)
```
