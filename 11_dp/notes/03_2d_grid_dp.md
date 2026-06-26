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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
