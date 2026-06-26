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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
