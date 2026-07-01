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
Am I sorting edges by weight before scanning them (Kruskal)?
How does union-find with path compression tell me an edge would create a cycle?
Why is greedily taking the cheapest non-cycle edge always safe (cut property)?
Does the graph need to be connected for a true spanning tree to exist?
Am I conflating this with shortest-path (single source) instead of minimum total connection cost?
```
