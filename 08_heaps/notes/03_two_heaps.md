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
What is the size invariant between the lower max heap and upper min heap?
Which heap does a new number go into first, and how/when do I rebalance?
Why does the lower heap's max always stay <= the upper heap's min?
How do I compute the median differently for even vs odd total counts?
How am I negating values for the max heap without corrupting comparisons?
```
