# Sequence DP

## Pattern

Model relationships between positions in one or two sequences.

## Intuition

LIS and LCS are classic examples of state over sequence prefixes or endings.

## How It Works

For LCS, `dp[i][j]` means best answer using prefixes of both strings.

## Template

```text
if chars match:
    dp[i][j] = 1 + dp[i-1][j-1]
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

## Example

For LCS of `abc` and `adc`, matching `a` and `c` contribute to answer length 2.

## Complexity

```text
Often O(n^2) or O(n*m)
Space depends on table size
```

## Pitfalls

- Confusing substring with subsequence.
- For LIS, using O(n^2) when O(n log n) may be expected.
- Wrong prefix indexing.

## Interview Checklist

Before coding, make sure you can answer:

```text
Am I solving for a subsequence (order preserved, gaps allowed) or a substring/subarray (contiguous)?
What does dp[i][j] mean — best answer over prefixes ending at i and j, or comparing two full sequences?
When characters/elements match, why does the transition pull from dp[i-1][j-1] rather than dp[i-1][j] or dp[i][j-1]?
When they don't match, which of dp[i-1][j] or dp[i][j-1] (or both) carries the answer forward, and why?
Does this problem admit an O(n log n) alternative (e.g., patience sorting for LIS) instead of the O(n^2) table?
```
