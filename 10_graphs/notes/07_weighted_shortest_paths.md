# Weighted Shortest Paths

## Pattern

When edges have weights, shortest path depends on total cost, not number of edges.

## Intuition

BFS works only when all edges have equal cost. Dijkstra uses a min heap to expand the currently cheapest known state.

## How It Works

Keep best distance per node. Pop the smallest distance from heap. Skip stale entries.

## Template

```text
dist[start] = 0
heap = [(0, start)]
while heap:
    cost, node = heappop(heap)
    if cost > dist[node]: continue
    for nei, weight in graph[node]:
        new_cost = cost + weight
        if new_cost < dist[nei]:
            dist[nei] = new_cost
            heappush(heap, (new_cost, nei))
```

## Example

A path with fewer edges can be more expensive than a longer path with small weights.

## Complexity

```text
Time: O((V + E) log V)
Space: O(V + E)
```

## Pitfalls

- Using BFS on weighted graphs.
- Using Dijkstra with negative weights.
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
