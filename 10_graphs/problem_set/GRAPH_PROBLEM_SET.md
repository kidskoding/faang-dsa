# Graphs Problem Set

## Goal

Build graph intuition from the ground up, then use that foundation to solve the medium and hard graph problems that show up in LeetCode-style interviews.

## How To Use

Work the file in order. The early sections are the fundamentals. The later sections are the medium and hard extensions.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Fundamentals

These are the graph basics you should be able to do without thinking too hard.

### 1. Graph Representations
- Pattern: convert between adjacency lists, adjacency matrices, and edge lists.

### 2. Graph BFS
- Pattern: queue-based traversal with a visited set.

### 3. Graph DFS
- Pattern: recursion or stack-based traversal with a visited set.

### 4. Grid DFS
- Pattern: treat a matrix as an implicit graph and recurse through valid neighbors.

### 5. Grid BFS
- Pattern: treat a matrix as an implicit graph and traverse level by level.

### 6. Multi-Source BFS
- Pattern: seed the queue with many starting nodes and expand outward in layers.

### 7. Topological Sort
- Pattern: order nodes in a directed acyclic graph by dependencies.

### 8. Cycle Detection
- Pattern: detect cycles in directed and undirected graphs.

### 9. Number Of Islands
- Pattern: count connected components in a grid.

### 10. Flood Fill
- Pattern: recolor a connected component in a grid.

### 11. Rotting Oranges
- Pattern: multi-source BFS over a grid.

### 12. Walls And Gates
- Pattern: multi-source BFS to compute shortest distances from many starts.

### 13. Shortest Path In Binary Matrix
- Pattern: BFS for shortest path in an unweighted grid.

## Mediums

These are the graph mediums you should drill for FAANG-style interviews.

### 14. Clone Graph
- Pattern: DFS or BFS copy with a map from original node to clone node.

### 15. Course Schedule
- Pattern: topological sort / cycle detection on prerequisites.

### 16. Course Schedule II
- Pattern: return an actual topological ordering.

### 17. Is Graph Bipartite
- Pattern: 2-color the graph while traversing.

### 18. Find If Path Exists In Graph
- Pattern: reachability via BFS/DFS or union find.

### 19. Number Of Connected Components
- Pattern: count DFS/BFS components in an undirected graph.

### 20. Redundant Connection
- Pattern: detect the first edge that creates a cycle.

### 21. Evaluate Division
- Pattern: graph traversal with weighted edges.

### 22. Accounts Merge
- Pattern: connect accounts through shared identifiers.

### 23. Word Ladder
- Pattern: shortest path in an implicit graph of word transformations.

### 24. Pacific Atlantic Water Flow
- Pattern: reverse BFS/DFS from multiple oceans.

### 25. Surrounded Regions
- Pattern: mark border-connected regions before flipping the rest.

### 26. Reconstruct Itinerary
- Pattern: Eulerian path style traversal with ordering constraints.

### 27. Network Delay Time
- Pattern: shortest paths in a weighted graph.

### 28. Cheapest Flights Within K Stops
- Pattern: shortest paths with a stop constraint.

## Hards And Extensions

These are the graph follow-ups that push beyond the standard medium set.

### 29. Critical Connections In A Network
- Pattern: bridge-finding with DFS low-link values.

### 30. Minimum Height Trees
- Pattern: peel leaves or reason about tree centers.

### 31. Alien Dictionary
- Pattern: infer ordering constraints and topologically sort.

### 32. Longest Increasing Path In A Matrix
- Pattern: graph + memoized DFS over increasing edges.

### 33. Minimum Cost To Make At Least One Valid Path In A Grid
- Pattern: 0-1 BFS / weighted grid traversal.

### 34. Shortest Path To Get All Keys
- Pattern: BFS over grid position plus collected-state bitmask.

### 35. Graph Valid Tree
- Pattern: check acyclicity and connectivity together.

### 36. Parallel Courses
- Pattern: layered topological sort over course dependencies.

### 37. Maximum Probability Path
- Pattern: weighted graph traversal with priority queue logic.

### 38. Swim In Rising Water
- Pattern: shortest path on a grid with a priority queue.

## Recommended Order

If you want the shortest path to graph fluency, do them in this order:

```text
1. Graph Representations
2. Graph BFS
3. Graph DFS
4. Grid DFS
5. Grid BFS
6. Number Of Islands
7. Flood Fill
8. Rotting Oranges
9. Course Schedule
10. Clone Graph
11. Topological Sort
12. Pacific Atlantic Water Flow
13. Word Ladder
14. Network Delay Time
15. Critical Connections In A Network
16. Longest Increasing Path In A Matrix
```

## Mastery Rule

A problem is not done until you can:

1. explain the pattern
2. choose the base case
3. write the helper shape
4. pass the tests
5. explain time and space complexity
