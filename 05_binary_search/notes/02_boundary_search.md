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
What is the monotonic predicate, and can you prove it's false...false, true...true (or vice versa)?
Why does this template use `right = n` and `left < right` instead of `right = n - 1` and `left <= right`?
Why do you set `right = mid` instead of `mid - 1` when the condition is true?
Does `left` land on the first-true or last-false index, and how would you flip it to find the other boundary?
What happens if no index satisfies the condition — what does `left` equal on exit?
```
