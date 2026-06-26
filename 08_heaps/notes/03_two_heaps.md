# Two Heaps

## Pattern

Use one max heap for the lower half and one min heap for the upper half.

## Intuition

This keeps a stream split around the median.

## How It Works

Balance heap sizes so their tops expose the median.

## Template

```text
lower = max heap
upper = min heap
add number to one heap
rebalance sizes
median from heap tops
```

## Example

For odd count, the larger heap top is median. For even count, average the two tops.

## Complexity

```text
insert: O(log n)
find median: O(1)
space: O(n)
```

## Pitfalls

- Not rebalancing sizes.
- Forgetting max heap needs negated values in Python.
- Letting lower max exceed upper min.

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
