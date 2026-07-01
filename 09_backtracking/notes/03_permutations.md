# Permutations

## Pattern

Permutations care about order, so each position can choose any unused item.

## Intuition

Track used values or swap in place.

## How It Works

The recursion depth is the current position in the permutation.

## Template

```text
def backtrack(path):
    if len(path) == n:
        save copy
    for i in range(n):
        if used[i]: continue
        used[i] = True
        path.append(nums[i])
        backtrack(path)
        path.pop()
        used[i] = False
```

## Example

For three numbers, there are `3 * 2 * 1 = 6` permutations.

## Complexity

```text
Time: O(n! * n) including output copies
Space: O(n)
```

## Pitfalls

- Confusing permutations with combinations.
- Not marking values unused after recursion.
- Duplicate handling when input has repeated values.

## Interview Checklist

Before coding, make sure you can answer:

```text
Am I tracking "used" items with a boolean array/set, or swapping in place — and why that choice here?
Does the base case check `len(path) == n`, not an index bound?
If values repeat, how do I skip duplicate permutations (sort + skip same value at same depth when previous unused)?
Is `used[i]` reset to `False` right after popping the path, on every branch including early returns?
How does this differ from combinations in terms of what "order matters" costs in branching factor?
```
