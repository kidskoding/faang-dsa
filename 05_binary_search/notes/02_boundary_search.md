# Boundary Search

## Pattern

Find the first or last position where a condition becomes true.

## Intuition

Many problems are not direct equality search; they ask for an edge.

## How It Works

Use a monotonic predicate: false false false true true.

## Template

```text
left = 0
right = n
while left < right:
    mid = (left + right) // 2
    if condition(mid):
        right = mid
    else:
        left = mid + 1
return left
```

## Example

Lower bound finds the first index with value >= target.

## Complexity

```text
Time: O(log n)
Space: O(1)
```

## Pitfalls

- Using `<=` template when half-open bounds are cleaner.
- Returning mid instead of final boundary.
- Not proving the predicate is monotonic.

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
