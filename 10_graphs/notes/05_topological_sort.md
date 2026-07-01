# Topological Sort

## Pattern

Topological sort orders directed acyclic graph nodes so every prerequisite appears before dependent nodes.

## Intuition

If a course has prerequisites, you cannot take it until incoming edges are resolved.

## How It Works

Kahn's algorithm uses indegrees. Start with nodes that have indegree 0, then remove their outgoing edges.

## Template

```text
build graph and indegree
queue = all nodes with indegree 0
order = []
while queue:
    node = queue.popleft()
    order.append(node)
    for nei in graph[node]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            queue.append(nei)
```

## Example

If `A -> B`, A appears before B in the order.

## Complexity

```text
Time: O(V + E)
Space: O(V + E)
```

## Pitfalls

- Forgetting cycles mean no valid ordering.
- Reversing edge direction.
- Returning an order before checking all nodes were processed.

## Interview Checklist

Before coding, make sure you can answer:

```text
Which direction do the edges point: prerequisite -> dependent, and did I build the adjacency list in that direction?
How do I compute indegree for every node before starting the queue?
How do I detect a cycle: by comparing the length of my output order to the total node count?
What do I return if the graph has a cycle (no valid ordering) versus a valid full ordering?
Why does starting from indegree-0 nodes guarantee prerequisites are processed first?
```
