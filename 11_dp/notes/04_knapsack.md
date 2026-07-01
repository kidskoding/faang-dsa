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
Is this 0/1 (each item used at most once) or unbounded (items reusable)?
Why does 0/1 knapsack require iterating capacity from high to low, while unbounded goes low to high?
What does dp[cap] mean after processing the current item — best value using items seen so far with this capacity?
Do I need the 2D dp[item][cap] form, or is the capacity-only 1D rolling array sufficient here?
What is the base case for dp[0] (zero capacity) and for an empty item set?
```
