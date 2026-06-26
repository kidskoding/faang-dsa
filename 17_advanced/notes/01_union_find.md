# Union Find

## Pattern

Union find tracks connected components under merge operations.

## Intuition

It answers whether two items are in the same group.

## How It Works

Path compression and union by size/rank make it nearly constant time.

## Template

```text
find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
union(a,b):
    connect roots
```

## Example

Merging edges in a graph gradually builds components.

## Complexity

```text
Almost O(1) amortized per operation
Space O(n)
```

## Pitfalls

- Forgetting path compression.
- Unioning nodes instead of roots.
- Using union find when traversal is simpler.

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
