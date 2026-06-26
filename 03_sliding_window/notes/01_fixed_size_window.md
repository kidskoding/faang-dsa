# Fixed-Size Sliding Window

## Pattern

Maintain a window of exactly `k` elements while moving one step at a time.

## Intuition

Instead of recomputing each window from scratch, remove the outgoing value and add the incoming value.

## How It Works

The window size stays constant after the first `k` elements.

## Template

```text
window_sum = 0
for right in range(len(nums)):
    window_sum += nums[right]
    if right >= k:
        window_sum -= nums[right - k]
    if right >= k - 1:
        update answer
```

## Example

For max average subarray of length `k`, keep the sum of the current `k` elements and update the max.

## Complexity

```text
Time: O(n)
Space: O(1)
```

## Pitfalls

- Updating the answer before the first full window exists.
- Removing the wrong outgoing index.
- Using variable-window logic for a fixed-size problem.

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
