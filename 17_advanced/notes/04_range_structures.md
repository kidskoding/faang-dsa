# Segment Tree And Fenwick Tree

## Pattern

Range structures answer updates and range queries faster than scanning.

## Intuition

Use them when values change and you still need repeated range sums/min/max.

## How It Works

Fenwick is simpler for prefix sums. Segment tree is more general.

## Template

```text
update index
query prefix or range
combine tree nodes
```

## Example

For mutable range sum, update one index and query sums repeatedly.

## Complexity

```text
update/query O(log n)
space O(n)
```

## Pitfalls

- Using prefix sums when updates exist.
- Getting 0-index vs 1-index Fenwick wrong.
- Overbuilding these for normal interview modules.

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
