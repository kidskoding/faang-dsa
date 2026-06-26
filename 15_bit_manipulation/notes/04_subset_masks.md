# Subset Masks

## Pattern

A bitmask can represent a subset.

## Intuition

Each bit says whether an item is included.

## How It Works

Iterate masks from `0` to `2^n - 1` to enumerate subsets.

## Template

```text
for mask in range(1 << n):
    subset = []
    for i in range(n):
        if mask & (1 << i):
            subset.append(items[i])
```

## Example

For n=3, mask `101` means choose items 0 and 2.

## Complexity

```text
Time: O(n * 2^n)
Space: output size
```

## Pitfalls

- Using subset masks when n is too large.
- Mixing item index and bit position.
- Forgetting empty subset mask 0.

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
