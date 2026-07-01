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
Is n small enough (roughly <= 20) that 2^n enumeration is feasible?
Am I distinguishing bit position (item index) from the mask's integer value?
Does my loop correctly include the empty subset (mask 0)?
For each mask, am I checking `mask & (1 << i)` against the right item i?
```
