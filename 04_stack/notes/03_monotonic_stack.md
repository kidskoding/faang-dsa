# Monotonic Stack

## Pattern

A monotonic stack keeps values in increasing or decreasing order to find next greater/smaller relationships.

## Intuition

When a new value makes old values useless, pop them and resolve their answers.

## How It Works

Each element is pushed once and popped once, so the total work is linear.

## Template

```text
stack = indices
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] < x:
        j = stack.pop()
        answer[j] = x
    stack.append(i)
```

## Example

For daily temperatures, a warmer day resolves all previous colder unresolved days.

## Complexity

```text
Time: O(n)
Space: O(n)
```

## Pitfalls

- Thinking the nested while loop makes it O(n^2).
- Storing values when indices are needed for distances.
- Choosing increasing vs decreasing order backwards.

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
