# Minimum Spanning Tree

## Pattern

An MST connects all nodes with minimum total edge cost.

## Intuition

Kruskal sorts edges and adds safe edges that connect new components.

## How It Works

Union find detects whether an edge creates a cycle.

## Template

```text
sort edges by weight
for edge in edges:
    if find(u) != find(v):
        union(u,v)
        add cost
```

## Example

Always adding the cheapest non-cycle edge is safe by cut property.

## Complexity

```text
Kruskal O(E log E)
Space O(V)
```

## Pitfalls

- Adding edges that form cycles.
- Forgetting graph must be connected for full MST.
- Confusing shortest path with MST.

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
