# Monotonic Queue

## Pattern

A monotonic queue keeps candidates for window max/min in sorted usefulness order.

## Intuition

It combines queue expiry with monotonic stack-style candidate removal.

## How It Works

For sliding window maximum, smaller values behind a larger new value can never be max while the larger value remains.

## Template

```text
dq = deque()
for i, x in enumerate(nums):
    while dq and dq[0] <= i - k:
        dq.popleft()
    while dq and nums[dq[-1]] <= x:
        dq.pop()
    dq.append(i)
```

## Example

The front is the best candidate for the current window.

## Complexity

```text
Time: O(n)
Space: O(k)
```

## Pitfalls

- Forgetting to expire old indices.
- Using values instead of indices.
- Reading the answer before the first full window.

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
