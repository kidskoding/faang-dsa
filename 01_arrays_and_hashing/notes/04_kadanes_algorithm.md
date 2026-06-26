# Kadane's Algorithm

## Pattern

Kadane's algorithm finds the best subarray ending at each position and keeps the best overall answer.

It is a dynamic programming pattern optimized into constant space.

## Intuition

At each number, you decide:

```text
Should I extend the previous subarray, or start fresh here?
```

If the previous sum hurts more than it helps, drop it.

## How It Works

Maintain:

```text
current = best subarray sum ending at current index
best = best subarray sum seen anywhere
```

Transition:

```text
current = max(nums[i], current + nums[i])
best = max(best, current)
```

## Template

```text
current = nums[0]
best = nums[0]

for x in nums[1:]:
    current = max(x, current + x)
    best = max(best, current)

return best
```

## Example

For `[-2, 1, -3, 4, -1, 2, 1]`:

```text
at 4: starting fresh is better than extending a negative sum
then extend: 4 + -1 + 2 + 1 = 6
```

Best answer is `6`.

## Complexity

```text
Time: O(n)
Space: O(1)
```

## Pitfalls

- Initializing best to `0` when all numbers can be negative.
- Forgetting the subarray must be contiguous.
- Confusing subsequence with subarray.
- Returning current instead of best.

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
