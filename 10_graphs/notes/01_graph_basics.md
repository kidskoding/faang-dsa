# Graph Basics And Reachability

## Pattern

A graph is a set of nodes connected by edges. Problems usually ask whether you can reach nodes, group nodes, or find an optimal path.

## Intuition

Trees have one parent path. Graphs can have cycles and multiple ways to reach the same node, so `visited` state matters.

## How It Works

Represent graphs as adjacency lists for most interviews:

```text
graph[node] = list of neighbors
```

For edge lists, build adjacency first unless the algorithm directly consumes edges.

## Template

```text
build adjacency list
visited = set()

def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for nei in graph[node]:
        dfs(nei)
```

## Example

For edges `(0,1), (1,2), (3,4)`, DFS from `0` reaches `{0,1,2}` but not `{3,4}`.

## Complexity

```text
Time: O(V + E)
Space: O(V + E)
```

## Pitfalls

- Forgetting disconnected components.
- Not marking visited before recursing/enqueuing.
- Treating directed and undirected edges the same.

## Interview Checklist

Before coding, make sure you can answer:

```text
Is the graph directed or undirected, and does that change how edges are traversed?
Am I given an adjacency list, or do I need to build one from an edge list first?
Have I looped over every node, not just node 0, to catch disconnected components?
Do I mark a node visited before recursing into it, to avoid infinite loops on cycles?
Would DFS reach the same conclusion as BFS here, or does the question require shortest path?
```
