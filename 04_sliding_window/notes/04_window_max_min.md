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
Am I storing indices in the deque, not values, so I can detect and evict expired entries?
For a max window, why is it safe to pop smaller values from the back before pushing nums[right]?
What check evicts the front of the deque when deque[0] falls outside the current window bounds?
Am I using `<=` vs `<` consistently when popping, and how does that choice handle duplicate values?
Why does this run in amortized O(n) despite the nested while loop (each index pushed and popped at most once)?
```
