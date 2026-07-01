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
Why does the deque store indices, not values, and what does that let me check (window expiry via i - k)?
In what order do I expire out-of-window entries vs pop dominated entries vs append the new index each iteration — and why does that order matter?
Why can smaller values behind a larger new value be safely discarded forever, not just for this window?
At what point in the loop is the front of the deque a valid answer (only once the first full window is formed)?
Am I tracking window max or window min, and is the pop condition (<=  vs >=) correct for that direction?
```
