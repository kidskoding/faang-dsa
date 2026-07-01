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
Do I actually have mutable updates interleaved with range queries (not just static prefix sums)?
Fenwick or segment tree: do I need arbitrary range min/max, or just prefix sums?
Is my Fenwick tree consistently 1-indexed, and does lowbit(i) = i & (-i) drive both update and query?
For a segment tree, how do child nodes combine into a parent, and is that operation associative?
What is the log n update/query cost buying me over an O(n) rescan per query?
```
