# Graphs Problem Set

## Goal

Build graph intuition from actual LeetCode-style problems. The order follows the module topics: graph basics, reachability, grid traversal, components and cycles, topological sort, implicit-state BFS, weighted shortest paths, and hard graph extensions.

## How To Use

Work the file in order. The problem set follows the topic order from the module README.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Fundamentals

These problems teach graph structure, adjacency traversal, grids as implicit graphs, and BFS/DFS shortest distance.

### 1. [Clone Graph](https://leetcode.com/problems/clone-graph/)

- Pattern: copy nodes with DFS/BFS and a map from original to clone.

### 2. [Flood Fill](https://leetcode.com/problems/flood-fill/)

- Pattern: grid DFS/BFS over cells with the same value.

### 3. [Number Of Islands](https://leetcode.com/problems/number-of-islands/)

- Pattern: count connected components in a grid.

### 4. [Number Of Provinces](https://leetcode.com/problems/number-of-provinces/)

- Pattern: count connected components via union-find or DFS on an adjacency matrix.

### 5. [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)

- Pattern: mark border-connected regions before flipping enclosed cells.

### 6. [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

- Pattern: reverse DFS/BFS from both oceans.

### 7. [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

- Pattern: multi-source BFS over a grid.

### 8. [Shortest Path In Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

- Pattern: BFS shortest path in an unweighted grid.

## Mediums

FAANG-level graph problems across components, cycles, union-find, bipartite coloring, topological sort, implicit-state BFS, and weighted shortest paths.

### 9. [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)

- Pattern: check connectivity and absence of cycles.

### 10. [Redundant Connection](https://leetcode.com/problems/redundant-connection/)

- Pattern: union-find to detect the edge that creates a cycle.

### 11. [Accounts Merge](https://leetcode.com/problems/accounts-merge/)

- Pattern: union-find components through shared identifiers.

### 12. [Is Graph Bipartite](https://leetcode.com/problems/is-graph-bipartite/)

- Pattern: 2-color a graph during BFS/DFS.

### 13. [Shortest Bridge](https://leetcode.com/problems/shortest-bridge/)

- Pattern: mark one island with DFS, then BFS outward to the other island.

### 14. [Course Schedule](https://leetcode.com/problems/course-schedule/)

- Pattern: detect cycles in a directed dependency graph.

### 15. [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

- Pattern: return a topological ordering.

### 16. [Course Schedule IV](https://leetcode.com/problems/course-schedule-iv/)

- Pattern: transitive reachability / all-pairs reachability on a DAG.

### 17. [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/)

- Pattern: detect nodes that cannot reach a cycle.

### 18. [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)

- Pattern: peel leaves to find tree centers.

### 19. [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)

- Pattern: Hierholzer Eulerian path with lexical ordering.

### 20. [Open The Lock](https://leetcode.com/problems/open-the-lock/)

- Pattern: BFS over generated states.

### 21. [Word Ladder](https://leetcode.com/problems/word-ladder/)

- Pattern: BFS shortest path in an implicit graph.

### 22. [Bus Routes](https://leetcode.com/problems/bus-routes/)

- Pattern: BFS over routes as nodes / state compression.

### 23. [Evaluate Division](https://leetcode.com/problems/evaluate-division/)

- Pattern: weighted graph traversal.

### 24. [Network Delay Time](https://leetcode.com/problems/network-delay-time/)

- Pattern: Dijkstra shortest paths in a weighted directed graph.

### 25. [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

- Pattern: shortest paths with an extra stop-count state.

### 26. [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)

- Pattern: Dijkstra where path cost is the maximum edge effort.

## Hards And Extensions

These problems teach path reconstruction, hard topological sort, bitmask BFS, 0-1 BFS, MSTs, low-link DFS, and offline connectivity.

### 27. [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)

- Pattern: BFS shortest layers plus path reconstruction.

### 28. [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)

- Pattern: infer character ordering and topologically sort.

### 29. [Shortest Path To Get All Keys](https://leetcode.com/problems/shortest-path-to-get-all-keys/)

- Pattern: BFS over position plus collected-key bitmask.

### 30. [Minimum Cost To Make At Least One Valid Path In A Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)

- Pattern: 0-1 BFS over grid directions.

### 31. [Min Cost To Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)

- Pattern: minimum spanning tree over complete graph distances.

### 32. [Critical Connections In A Network](https://leetcode.com/problems/critical-connections-in-a-network/)

- Pattern: bridge-finding with DFS low-link values.

### 33. [Bricks Falling When Hit](https://leetcode.com/problems/bricks-falling-when-hit/)

- Pattern: reverse process with union-find connectivity restoration.

### 34. [Longest Increasing Path In A Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

- Pattern: memoized DFS on a directed acyclic grid graph.

## Recommended Order

If you want the shortest path to graph fluency, do these first. This is only the priority path, not the full problem set.

```text
1. [Flood Fill](https://leetcode.com/problems/flood-fill/)
2. [Number Of Islands](https://leetcode.com/problems/number-of-islands/)
3. [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
4. [Shortest Path In Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
5. [Clone Graph](https://leetcode.com/problems/clone-graph/)
6. [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
7. [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
8. [Course Schedule](https://leetcode.com/problems/course-schedule/)
9. [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
10. [Is Graph Bipartite](https://leetcode.com/problems/is-graph-bipartite/)
11. [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)
12. [Redundant Connection](https://leetcode.com/problems/redundant-connection/)
13. [Shortest Bridge](https://leetcode.com/problems/shortest-bridge/)
14. [Word Ladder](https://leetcode.com/problems/word-ladder/)
15. [Network Delay Time](https://leetcode.com/problems/network-delay-time/)
16. [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
17. [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
18. [Min Cost To Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)
19. [Critical Connections In A Network](https://leetcode.com/problems/critical-connections-in-a-network/)
```
