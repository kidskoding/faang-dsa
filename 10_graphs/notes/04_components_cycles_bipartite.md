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
Am I counting components, detecting a cycle, or coloring a bipartition, and does that change what state I track per node?
For cycle detection, is the graph directed (need a "visiting" vs "visited" state) or undirected (need to track the parent edge)?
For bipartite coloring, what do I do when an edge connects two nodes that already have the same color?
Have I started a fresh traversal from every unvisited node, so isolated nodes and other components aren't skipped?
What does the algorithm output when the graph is already disconnected — is that itself a valid or invalid case?
```
