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

### Graph Basics And Reachability

These problems teach graph structure, adjacency traversal, and visited-set reasoning.

### 1. [Find Center Of Star Graph](https://leetcode.com/problems/find-center-of-star-graph/)

- Pattern: identify graph structure from edge relationships.

### 2. [Find If Path Exists In Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)

- Pattern: reachability with BFS or DFS.

### 3. [Employee Importance](https://leetcode.com/problems/employee-importance/)

- Pattern: traverse an adjacency list and accumulate values.

### 4. [Keys And Rooms](https://leetcode.com/problems/keys-and-rooms/)

- Pattern: reachability through dynamically discovered edges.

### 5. [Clone Graph](https://leetcode.com/problems/clone-graph/)

- Pattern: copy nodes with DFS/BFS and a map from original to clone.

### Grid DFS

These problems teach matrices as implicit graphs and recursive component exploration.

### 6. [Flood Fill](https://leetcode.com/problems/flood-fill/)

- Pattern: grid DFS/BFS over cells with the same value.

### 7. [Number Of Islands](https://leetcode.com/problems/number-of-islands/)

- Pattern: count connected components in a grid.

### 8. [Max Area Of Island](https://leetcode.com/problems/max-area-of-island/)

- Pattern: compute component size with grid DFS/BFS.

### 9. [Island Perimeter](https://leetcode.com/problems/island-perimeter/)

- Pattern: reason about grid neighbors and boundaries.

### 10. [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)

- Pattern: mark border-connected regions before flipping enclosed cells.

### 11. [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

- Pattern: reverse DFS/BFS from both oceans.

### 12. [Number Of Enclaves](https://leetcode.com/problems/number-of-enclaves/)

- Pattern: remove border-connected land before counting trapped land.

### 13. [Number Of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/)

- Pattern: DFS a component while tracking whether it touches the boundary.

### 14. [Count Sub Islands](https://leetcode.com/problems/count-sub-islands/)

- Pattern: DFS one grid while validating against another grid.

### 15. [Making A Large Island](https://leetcode.com/problems/making-a-large-island/)

- Pattern: label components and combine neighboring islands.

### Grid BFS And Multi-Source BFS

These problems teach level-order expansion, shortest distance in grids, and many-source starts.

### 16. [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

- Pattern: multi-source BFS over a grid.

### 17. [Walls And Gates](https://leetcode.com/problems/walls-and-gates/)

- Pattern: multi-source BFS to fill shortest distances from many starts.

### 18. [01 Matrix](https://leetcode.com/problems/01-matrix/)

- Pattern: multi-source BFS from all zero cells.

### 19. [Shortest Path In Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

- Pattern: BFS shortest path in an unweighted grid.

### 20. [Nearest Exit From Entrance In Maze](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/)

- Pattern: BFS shortest path to a boundary cell.

### 21. [As Far From Land As Possible](https://leetcode.com/problems/as-far-from-land-as-possible/)

- Pattern: multi-source BFS from all land cells.

### 22. [Map Of Highest Peak](https://leetcode.com/problems/map-of-highest-peak/)

- Pattern: multi-source BFS from all water cells.

### 23. [Shortest Bridge](https://leetcode.com/problems/shortest-bridge/)

- Pattern: mark one island, then BFS outward to the other island.

### 24. [Detect Cycles In 2D Grid](https://leetcode.com/problems/detect-cycles-in-2d-grid/)

- Pattern: DFS/BFS grid cycle detection with parent tracking.

### Components, Cycles, And Bipartite Graphs

These problems teach connected components, cycle detection, coloring, and tree validity.

### 25. [Number Of Connected Components In An Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

- Pattern: count components with DFS/BFS.

### 26. [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)

- Pattern: check connectivity and absence of cycles.

### 27. [Redundant Connection](https://leetcode.com/problems/redundant-connection/)

- Pattern: detect the edge that creates a cycle.

### 28. [Is Graph Bipartite](https://leetcode.com/problems/is-graph-bipartite/)

- Pattern: 2-color a graph during BFS/DFS.

### 29. [Possible Bipartition](https://leetcode.com/problems/possible-bipartition/)

- Pattern: 2-color a conflict graph.

### 30. [Accounts Merge](https://leetcode.com/problems/accounts-merge/)

- Pattern: build components through shared identifiers.

### 31. [Reorder Routes To Make All Paths Lead To The City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)

- Pattern: DFS/BFS with directed edge orientation.

### 32. [Minimum Number Of Vertices To Reach All Nodes](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/)

- Pattern: nodes with zero indegree are required starts.

### 33. [Find Closest Node To Given Two Nodes](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/)

- Pattern: compare distances from two starts in a directed graph.

## Mediums

### Topological Sort And DAGs

These problems teach prerequisite ordering, directed cycle detection, and DAG propagation.

### 34. [Course Schedule](https://leetcode.com/problems/course-schedule/)

- Pattern: detect cycles in a directed dependency graph.

### 35. [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

- Pattern: return a topological ordering.

### 36. [All Paths From Source To Target](https://leetcode.com/problems/all-paths-from-source-to-target/)

- Pattern: backtrack through a DAG.

### 37. [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/)

- Pattern: detect nodes that cannot reach a cycle.

### 38. [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)

- Pattern: peel leaves to find tree centers.

### 39. [Time Needed To Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/)

- Pattern: DFS/BFS over a management tree.

### 40. [Course Schedule IV](https://leetcode.com/problems/course-schedule-iv/)

- Pattern: transitive prerequisite reachability.

### 41. [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)

- Pattern: graph traversal with lexical ordering constraints.

### 42. [All Ancestors Of A Node In A Directed Acyclic Graph](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/)

- Pattern: propagate ancestor sets through topological order.

### 43. [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)

- Pattern: infer character ordering and topologically sort.

### 44. [Parallel Courses III](https://leetcode.com/problems/parallel-courses-iii/)

- Pattern: longest path in a DAG.

### 45. [Largest Color Value In A Directed Graph](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/)

- Pattern: topological DP with cycle detection.

### Implicit-State BFS

These problems teach generated neighbors, state compression, and BFS over non-obvious graph nodes.

### 46. [Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)

- Pattern: BFS over generated string states.

### 47. [Open The Lock](https://leetcode.com/problems/open-the-lock/)

- Pattern: BFS over generated states.

### 48. [Word Ladder](https://leetcode.com/problems/word-ladder/)

- Pattern: BFS shortest path in an implicit graph.

### 49. [Snakes And Ladders](https://leetcode.com/problems/snakes-and-ladders/)

- Pattern: BFS over board positions with transitions.

### 50. [Shortest Path To Get All Keys](https://leetcode.com/problems/shortest-path-to-get-all-keys/)

- Pattern: BFS over position plus collected-key bitmask.

### 51. [Bus Routes](https://leetcode.com/problems/bus-routes/)

- Pattern: BFS over route/state compression.

### 52. [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)

- Pattern: BFS shortest layers plus path reconstruction.

### 53. [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)

- Pattern: BFS over node plus visited-bitmask state.

### 54. [Minimum Moves To Reach Target With Rotations](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/)

- Pattern: BFS over grid position plus orientation.

### Weighted Shortest Paths

These problems teach weighted edges, priority queues, 0-1 BFS, and shortest-path state.

### 55. [Evaluate Division](https://leetcode.com/problems/evaluate-division/)

- Pattern: weighted graph traversal.

### 56. [Network Delay Time](https://leetcode.com/problems/network-delay-time/)

- Pattern: shortest paths in a weighted directed graph.

### 57. [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

- Pattern: shortest paths with an extra stop-count state.

### 58. [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)

- Pattern: shortest path where path cost is the maximum edge effort.

### 59. [Path With Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/)

- Pattern: Dijkstra-style traversal maximizing probability.

### 60. [The Maze](https://leetcode.com/problems/the-maze/)

- Pattern: DFS/BFS with rolling movement until walls.

### 61. [The Maze II](https://leetcode.com/problems/the-maze-ii/)

- Pattern: Dijkstra over rolling-movement distances.

### 62. [Find The City With The Smallest Number Of Neighbors At A Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

- Pattern: all-pairs or repeated shortest paths.

### 63. [Minimum Obstacle Removal To Reach Corner](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/)

- Pattern: 0-1 BFS over a grid.

### 64. [Minimum Cost To Make At Least One Valid Path In A Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)

- Pattern: 0-1 BFS over grid directions.

### 65. [Swim In Rising Water](https://leetcode.com/problems/swim-in-rising-water/)

- Pattern: priority-queue traversal over a weighted grid.

### 66. [Minimum Cost To Reach Destination In Time](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/)

- Pattern: shortest path with time as part of the state.

### 67. [Second Minimum Time To Reach Destination](https://leetcode.com/problems/second-minimum-time-to-reach-destination/)

- Pattern: track first and second shortest arrival times.

## Hards And Extensions

### Minimum Spanning Trees And Advanced Connectivity

These problems teach MSTs, low-link DFS, offline connectivity, and advanced graph follow-ups.

### 68. [Min Cost To Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)

- Pattern: minimum spanning tree over complete graph distances.

### 69. [Critical Connections In A Network](https://leetcode.com/problems/critical-connections-in-a-network/)

- Pattern: bridge-finding with DFS low-link values.

### 70. [Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/)

- Pattern: directed cycle detection with indegree conflict handling.

### 71. [Bricks Falling When Hit](https://leetcode.com/problems/bricks-falling-when-hit/)

- Pattern: reverse process with connectivity restoration.

### 72. [Find Critical And Pseudo-Critical Edges In Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)

- Pattern: compare MST costs with forced and banned edges.

### 73. [Count Subtrees With Max Distance Between Cities](https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/)

- Pattern: enumerate subsets and validate tree distances.

### 74. [Checking Existence Of Edge Length Limited Paths](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/)

- Pattern: offline queries with sorted edges.

### 75. [Longest Increasing Path In A Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

- Pattern: memoized DFS on a directed acyclic grid graph.

## Recommended Order

If you want the shortest path to graph fluency, do these first. This is only the priority path, not the full problem set.

```text
1. [Flood Fill](https://leetcode.com/problems/flood-fill/)
2. [Number Of Islands](https://leetcode.com/problems/number-of-islands/)
3. [Max Area Of Island](https://leetcode.com/problems/max-area-of-island/)
4. [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
5. [Walls And Gates](https://leetcode.com/problems/walls-and-gates/)
6. [01 Matrix](https://leetcode.com/problems/01-matrix/)
7. [Shortest Path In Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
8. [Find If Path Exists In Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)
9. [Clone Graph](https://leetcode.com/problems/clone-graph/)
10. [Course Schedule](https://leetcode.com/problems/course-schedule/)
11. [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
12. [Is Graph Bipartite](https://leetcode.com/problems/is-graph-bipartite/)
13. [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)
14. [Redundant Connection](https://leetcode.com/problems/redundant-connection/)
15. [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
16. [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
17. [Shortest Bridge](https://leetcode.com/problems/shortest-bridge/)
18. [Word Ladder](https://leetcode.com/problems/word-ladder/)
19. [Evaluate Division](https://leetcode.com/problems/evaluate-division/)
20. [Network Delay Time](https://leetcode.com/problems/network-delay-time/)
21. [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
22. [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
23. [Min Cost To Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)
24. [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)
25. [Critical Connections In A Network](https://leetcode.com/problems/critical-connections-in-a-network/)
26. [Longest Increasing Path In A Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)
27. [Minimum Cost To Make At Least One Valid Path In A Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
28. [Shortest Path To Get All Keys](https://leetcode.com/problems/shortest-path-to-get-all-keys/)
29. [Bus Routes](https://leetcode.com/problems/bus-routes/)
30. [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)
```
