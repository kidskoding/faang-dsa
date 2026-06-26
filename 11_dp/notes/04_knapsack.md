# Knapsack

## Pattern

Choose items under a capacity constraint.

## Intuition

State usually tracks item index and remaining capacity or total capacity used.

## How It Works

For 0/1 knapsack, each item is used at most once.

## Template

```text
for item in items:
    for cap from capacity down to weight:
        dp[cap] = max(dp[cap], value + dp[cap - weight])
```

## Example

Descending capacity prevents reusing the same item in 0/1 knapsack.

## Complexity

```text
Time: O(n * capacity)
Space: O(capacity)
```

## Pitfalls

- Looping capacity upward for 0/1 knapsack and reusing items.
- Confusing 0/1 with unbounded knapsack.
- Ignoring capacity as part of state.

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
