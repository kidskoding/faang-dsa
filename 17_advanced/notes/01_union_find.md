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
Am I storing parent pointers, or ranks/sizes, or both?
Does find() apply path compression, and does union() attach by rank/size?
Am I comparing/merging roots, not the original nodes?
How do I detect a cycle or "already connected" using find(a) == find(b)?
Is the near-O(1) amortized bound actually needed here, or would a plain BFS/DFS be simpler?
```
