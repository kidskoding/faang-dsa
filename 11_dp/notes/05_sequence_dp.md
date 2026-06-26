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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
