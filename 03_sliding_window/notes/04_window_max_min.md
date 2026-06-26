# Window Max And Min

## Pattern

Use a monotonic deque to query the max or min of each sliding window efficiently.

## Intuition

A normal queue cannot tell the max quickly. A monotonic queue keeps candidates in useful order.

## How It Works

For max windows, keep values decreasing. The front is always the max.

## Template

```text
deque = candidate indices
for right in range(n):
    remove indices outside window
    while deque and nums[deque[-1]] <= nums[right]:
        deque.pop()
    deque.append(right)
    if window formed:
        answer.append(nums[deque[0]])
```

## Example

For `[1,3,-1]` with window size 3, index of `3` stays at the front because smaller later values cannot beat it.

## Complexity

```text
Time: O(n)
Space: O(k)
```

## Pitfalls

- Storing values instead of indices, making expiry hard.
- Using `<` vs `<=` inconsistently with duplicates.
- Forgetting to remove expired indices before reading the front.

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
