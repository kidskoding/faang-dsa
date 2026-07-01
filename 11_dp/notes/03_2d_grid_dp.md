# 2D And Grid DP

## Pattern

Use row and column as state dimensions.

## Intuition

Grid DP usually moves from top/left to bottom/right or reverse.

## How It Works

Each cell answer depends on neighboring previous cells.

## Template

```text
for r in range(rows):
    for c in range(cols):
        dp[r][c] = combine(dp[r-1][c], dp[r][c-1])
```

## Example

Unique paths adds ways from top and left.

## Complexity

```text
Time: O(rows * cols)
Space: O(rows * cols), sometimes O(cols)
```

## Pitfalls

- Not initializing first row/column.
- Using updated values incorrectly during space optimization.
- Mixing up blocked cells or invalid cells.

## Interview Checklist

Before coding, make sure you can answer:

```text
What does dp[r][c] represent — ways to reach the cell, min/max cost to reach it, or something ending there?
How are the first row and first column initialized, especially with blocked/invalid cells?
Which neighbors feed dp[r][c] (top, left, or both), and in what traversal order?
If space-optimizing to O(cols), am I overwriting a value before reading it in the same pass?
What is the final answer's cell, and does it require a boundary check for unreachable cells?
```
