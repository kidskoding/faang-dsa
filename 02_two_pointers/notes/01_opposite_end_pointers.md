# Opposite-End Pointers

## Pattern

Use one pointer at the left edge and one pointer at the right edge, then move inward based on the condition.

## Intuition

Sorted input gives direction. If the sum is too small, move left up. If the sum is too large, move right down.

## How It Works

The search space shrinks because each move rules out a group of impossible pairs.

## Template

```text
left = 0
right = len(nums) - 1

while left < right:
    evaluate nums[left], nums[right]
    if condition too small:
        left += 1
    elif condition too large:
        right -= 1
    else:
        found answer
```

## Example

For two-sum in a sorted array, a small sum means the left value is too small. Moving right would only make the sum smaller or similar, so move left.

## Complexity

```text
Time: O(n)
Space: O(1)
```

## Pitfalls

- Using this on unsorted input without sorting first.
- Moving both pointers when only one side is justified.
- Forgetting `left < right` when the same element cannot be reused.

## Interview Checklist

Before coding, make sure you can answer:

```text
Is the input actually sorted (or sortable) — does this pattern even apply?
When the sum/condition is too small, why is moving `left` up correct instead of moving `right`?
When the sum/condition is too large, why is moving `right` down correct instead of moving `left`?
Should the loop use `left < right` or `left <= right`, and why (can an element pair with itself)?
On a match, do I move one pointer, both pointers, or return immediately?
If duplicate values are allowed, how do I skip past them without missing a valid pair?
```
