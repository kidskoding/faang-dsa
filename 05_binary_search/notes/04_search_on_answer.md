# Search On Answer

## Pattern

Binary search over possible answer values instead of array indices.

## Intuition

If you can test whether an answer candidate is feasible, and feasibility is monotonic, binary search the answer.

## How It Works

Common for minimum capacity, minimum speed, maximum minimum value.

## Template

```text
left = smallest_possible
right = largest_possible
while left < right:
    mid = (left + right) // 2
    if feasible(mid):
        right = mid
    else:
        left = mid + 1
return left
```

## Example

For shipping capacity, if capacity `x` works, any larger capacity also works.

## Complexity

```text
Time: O(log(answer_range) * cost(feasible))
Space: depends on feasible check
```

## Pitfalls

- Not defining the answer range correctly.
- Using binary search without monotonic feasibility.
- Getting min-valid vs max-valid update direction wrong.

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
