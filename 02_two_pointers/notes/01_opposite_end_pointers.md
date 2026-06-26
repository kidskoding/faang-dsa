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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
