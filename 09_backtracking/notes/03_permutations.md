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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
