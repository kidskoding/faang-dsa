# Components, Cycles, And Bipartite Graphs

## Pattern

Component problems group reachable nodes. Cycle problems detect repeated structure. Bipartite problems color nodes into two groups.

## Intuition

DFS/BFS traversal gives structure. Extra state tells you what structure you found.

## How It Works

For components, start traversal from every unvisited node. For bipartite, assign alternating colors. For cycles, track parent in undirected graphs or visiting states in directed graphs.

## Template

```text
for node in all nodes:
    if node not visited:
        start traversal
        update component/cycle/color answer
```

## Example

A graph is bipartite if every edge connects opposite colors. If an edge connects same colors, fail.

## Complexity

```text
Time: O(V + E)
Space: O(V)
```

## Pitfalls

- Only traversing from node 0.
- Using undirected cycle logic for directed graphs.
- Forgetting isolated nodes.

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
