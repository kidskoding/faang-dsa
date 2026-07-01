# Shortest Paths

## Pattern

Shortest-path algorithms choose the best next state based on edge weights.

## Intuition

BFS works for unweighted graphs. Dijkstra works for nonnegative weights.

## How It Works

The queue type depends on edge costs.

## Template

```text
BFS: queue
Dijkstra: min heap by distance
0-1 BFS: deque
```

## Example

If every edge costs 1, BFS distance order is already optimal.

## Complexity

```text
BFS O(V+E)
Dijkstra O((V+E) log V)
```

## Pitfalls

- Using BFS on weighted graphs.
- Using Dijkstra with negative edges.
- Not skipping stale heap entries.

## Interview Checklist

Before coding, make sure you can answer:

```text
Are edge weights uniform (BFS), 0/1 (0-1 BFS deque), or general nonnegative (Dijkstra)?
What is my frontier structure: plain queue, deque, or min-heap keyed by distance?
How do I detect and skip a stale/outdated heap entry for an already-finalized node?
Could any edge be negative, and if so, why does Dijkstra break there?
When is a node's distance considered final versus still tentative?
```
