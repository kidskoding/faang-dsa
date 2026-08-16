# Graphs Problem Set

## Goal

Build graph intuition across the core traversal techniques — adjacency
and reachability, grid DFS, grid BFS, components and cycles and bipartite
coloring, topological sort, implicit-state BFS, and weighted shortest
paths — then use each technique to solve the medium and hard graph
problems that show up in LeetCode-style interviews.

## How To Use

Each section maps to one solution file in this folder and to one graph
technique. Work a section top to bottom: problems are ordered roughly
easy to hard, and the implemented ones come first. `solves:` names the
function in that section's file; `solves: (todo)` means the solution is
not written yet.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Graph Basics

`graph_basics_problems.py` — read graph structure from edge lists and
adjacency, then reach nodes with plain DFS/BFS.

### 1. [Find Center Of Star Graph](https://leetcode.com/problems/find-center-of-star-graph/)

- solves: `find_center`
- Pattern: identify graph structure from edge relationships.

### 2. [Find If Path Exists In Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)

- solves: `valid_path`
- Pattern: reachability with BFS or DFS.

### 3. [Employee Importance](https://leetcode.com/problems/employee-importance/)

- solves: `get_importance`
- Pattern: traverse an adjacency list and accumulate values.

### 4. [Keys And Rooms](https://leetcode.com/problems/keys-and-rooms/)

- solves: `can_visit_all_rooms`
- Pattern: reachability through dynamically discovered edges.

### 5. [Clone Graph](https://leetcode.com/problems/clone-graph/)

- solves: `clone_graph`
- Pattern: copy nodes with DFS/BFS and a map from original to clone.

## Grid DFS

`grid_dfs_problems.py` — treat the grid as an implicit graph and use DFS
to count, size, and validate connected regions of cells.

### 6. [Flood Fill](https://leetcode.com/problems/flood-fill/)

- solves: `flood_fill`
- Pattern: grid DFS/BFS over cells with the same value.

### 7. [Number Of Islands](https://leetcode.com/problems/number-of-islands/)

- solves: `num_islands`
- Pattern: count connected components in a grid.

### 8. [Max Area Of Island](https://leetcode.com/problems/max-area-of-island/)

- solves: `max_area_of_island`
- Pattern: compute component size with grid DFS/BFS.

### 9. [Island Perimeter](https://leetcode.com/problems/island-perimeter/)

- solves: `island_perimeter`
- Pattern: reason about grid neighbors and boundaries.

### 10. [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)

- solves: `solve`
- Pattern: mark border-connected regions before flipping enclosed cells.

### 11. [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

- solves: `pacific_atlantic`
- Pattern: reverse DFS/BFS from both oceans.

### 12. [Number Of Enclaves](https://leetcode.com/problems/number-of-enclaves/)

- solves: `num_enclaves`
- Pattern: remove border-connected land before counting trapped land.

### 13. [Number Of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/)

- solves: `closed_island`
- Pattern: DFS a component while tracking whether it touches the boundary.

### 14. [Count Sub Islands](https://leetcode.com/problems/count-sub-islands/)

- solves: `count_sub_islands`
- Pattern: DFS one grid while validating against another grid.

### 15. [Making A Large Island](https://leetcode.com/problems/making-a-large-island/)

- solves: `largest_island`
- Pattern: label components and combine neighboring islands.

## Grid BFS

`grid_bfs_problems.py` — multi-source and single-source BFS over grids to
fill shortest distances and find shortest paths in unweighted cells.

### 16. [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

- solves: `oranges_rotting`
- Pattern: multi-source BFS over a grid.

### 17. [Walls And Gates](https://leetcode.com/problems/walls-and-gates/)

- solves: `walls_and_gates`
- Pattern: multi-source BFS to fill shortest distances from many starts.

### 18. [01 Matrix](https://leetcode.com/problems/01-matrix/)

- solves: `update_matrix`
- Pattern: multi-source BFS from all zero cells.

### 19. [Shortest Path In Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

- solves: `shortest_path_binary_matrix`
- Pattern: BFS shortest path in an unweighted grid.

### 20. [Nearest Exit From Entrance In Maze](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/)

- solves: `nearest_exit`
- Pattern: BFS shortest path to a boundary cell.

### 21. [As Far From Land As Possible](https://leetcode.com/problems/as-far-from-land-as-possible/)

- solves: `max_distance`
- Pattern: multi-source BFS from all land cells.

### 22. [Map Of Highest Peak](https://leetcode.com/problems/map-of-highest-peak/)

- solves: `highest_peak`
- Pattern: multi-source BFS from all water cells.

### 23. [Shortest Bridge](https://leetcode.com/problems/shortest-bridge/)

- solves: `shortest_bridge`
- Pattern: mark one island, then BFS outward to the other island.

### 24. [Detect Cycles In 2D Grid](https://leetcode.com/problems/detect-cycles-in-2d-grid/)

- solves: `contains_cycle`
- Pattern: DFS/BFS grid cycle detection with parent tracking.

## Components, Cycles, And Bipartite

`components_cycles_bipartite_problems.py` — count components, detect
cycles, 2-color graphs, and reason about directed edge orientation.

### 25. [Number Of Connected Components In An Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

- solves: `count_components`
- Pattern: count components with DFS/BFS.

### 26. [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)

- solves: `valid_tree`
- Pattern: check connectivity and absence of cycles.

### 27. [Redundant Connection](https://leetcode.com/problems/redundant-connection/)

- solves: `find_redundant_connection`
- Pattern: detect the edge that creates a cycle.

### 28. [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)

- solves: `is_bipartite`
- Pattern: 2-color a graph during BFS/DFS.

### 29. [Possible Bipartition](https://leetcode.com/problems/possible-bipartition/)

- solves: `possible_bipartition`
- Pattern: 2-color a conflict graph.

### 30. [Accounts Merge](https://leetcode.com/problems/accounts-merge/)

- solves: `accounts_merge`
- Pattern: build components through shared identifiers.

### 31. [Reorder Routes To Make All Paths Lead To The City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)

- solves: `min_reorder`
- Pattern: DFS/BFS with directed edge orientation.

### 32. [Minimum Number Of Vertices To Reach All Nodes](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/)

- solves: `find_smallest_set_of_vertices`
- Pattern: nodes with zero indegree are required starts.

### 33. [Find Closest Node To Given Two Nodes](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/)

- solves: `closest_meeting_node`
- Pattern: compare distances from two starts in a directed graph.

### 34. [Number Of Provinces](https://leetcode.com/problems/number-of-provinces/)

- solves: `find_circle_num`
- Pattern: count connected components via union-find or DFS on an
  adjacency matrix.

### 35. [Critical Connections In A Network](https://leetcode.com/problems/critical-connections-in-a-network/)

- solves: `critical_connections`
- Pattern: bridge-finding with DFS low-link values.

### 36. [Bricks Falling When Hit](https://leetcode.com/problems/bricks-falling-when-hit/)

- solves: `hit_bricks`
- Pattern: reverse process with union-find connectivity restoration.

### 37. [Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/)

- solves: (todo)
- Pattern: directed version of cycle removal; a node with two parents and a cycle
  are separate cases, so find the candidate edges first and test which removal
  leaves a valid rooted tree.

### 38. [Count Subtrees With Max Distance Between Cities](https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/)

- solves: (todo)
- Pattern: enumerate every subset of nodes as a bitmask, keep the connected ones,
  and take the diameter of each induced subtree.

## Topological Sort

`topological_sort_problems.py` — order and reason about directed acyclic
graphs via Kahn's algorithm, cycle detection, and DAG DP.

### 39. [Course Schedule](https://leetcode.com/problems/course-schedule/)

- solves: `can_finish`
- Pattern: detect cycles in a directed dependency graph.

### 40. [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

- solves: `find_order`
- Pattern: return a topological ordering.

### 41. [All Paths From Source To Target](https://leetcode.com/problems/all-paths-from-source-to-target/)

- solves: `all_paths_source_target`
- Pattern: backtrack through a DAG.

### 42. [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/)

- solves: `eventual_safe_nodes`
- Pattern: detect nodes that cannot reach a cycle.

### 43. [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)

- solves: `find_min_height_trees`
- Pattern: peel leaves to find tree centers.

### 44. [Time Needed To Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/)

- solves: `num_of_minutes`
- Pattern: DFS/BFS over a management tree.

### 45. [Course Schedule IV](https://leetcode.com/problems/course-schedule-iv/)

- solves: `check_if_prerequisite`
- Pattern: transitive prerequisite reachability.

### 46. [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)

- solves: `find_itinerary`
- Pattern: graph traversal with lexical ordering constraints.

### 47. [All Ancestors Of A Node In A Directed Acyclic Graph](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/)

- solves: `get_ancestors`
- Pattern: propagate ancestor sets through topological order.

### 48. [Parallel Courses III](https://leetcode.com/problems/parallel-courses-iii/)

- solves: `minimum_time`
- Pattern: longest path in a DAG.

### 49. [Largest Color Value In A Directed Graph](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/)

- solves: `largest_path_value`
- Pattern: topological DP with cycle detection.

### 50. [Longest Increasing Path In A Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

- solves: `longest_increasing_path`
- Pattern: memoized DFS on a directed acyclic grid graph.

## Implicit-State BFS

`implicit_state_bfs_problems.py` — BFS shortest paths where nodes are
generated states (strings, board positions, bitmask combinations).

### 51. [Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)

- solves: `min_mutation`
- Pattern: BFS over generated string states.

### 52. [Open The Lock](https://leetcode.com/problems/open-the-lock/)

- solves: `open_lock`
- Pattern: BFS over generated states.

### 53. [Word Ladder](https://leetcode.com/problems/word-ladder/)

- solves: `ladder_length`
- Pattern: BFS shortest path in an implicit graph.

### 54. [Snakes And Ladders](https://leetcode.com/problems/snakes-and-ladders/)

- solves: `snakes_and_ladders`
- Pattern: BFS over board positions with transitions.

### 55. [Shortest Path To Get All Keys](https://leetcode.com/problems/shortest-path-to-get-all-keys/)

- solves: `shortest_path_all_keys`
- Pattern: BFS over position plus collected-key bitmask.

### 56. [Bus Routes](https://leetcode.com/problems/bus-routes/)

- solves: `num_buses_to_destination`
- Pattern: BFS over route/state compression.

### 57. [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)

- solves: `shortest_path_length`
- Pattern: BFS over node plus visited-bitmask state.

### 58. [Minimum Moves To Reach Target With Rotations](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/)

- solves: `minimum_moves`
- Pattern: BFS over grid position plus orientation.

## Weighted Shortest Paths

`weighted_shortest_paths_problems.py` — Dijkstra, 0-1 BFS, and
state-augmented shortest paths over weighted graphs and grids.

### 59. [Evaluate Division](https://leetcode.com/problems/evaluate-division/)

- solves: `calc_equation`
- Pattern: weighted graph traversal.

### 60. [Network Delay Time](https://leetcode.com/problems/network-delay-time/)

- solves: `network_delay_time`
- Pattern: shortest paths in a weighted directed graph.

### 61. [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

- solves: `find_cheapest_price`
- Pattern: shortest paths with an extra stop-count state.

### 62. [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)

- solves: `minimum_effort_path`
- Pattern: shortest path where path cost is the maximum edge effort.

### 63. [Path With Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/)

- solves: `max_probability`
- Pattern: Dijkstra-style traversal maximizing probability.

### 64. [The Maze](https://leetcode.com/problems/the-maze/)

- solves: `has_path`
- Pattern: DFS/BFS with rolling movement until walls.

### 65. [The Maze II](https://leetcode.com/problems/the-maze-ii/)

- solves: `shortest_distance`
- Pattern: Dijkstra over rolling-movement distances.

### 66. [Find The City With The Smallest Number Of Neighbors At A Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

- solves: `find_the_city`
- Pattern: all-pairs or repeated shortest paths.

### 67. [Minimum Obstacle Removal To Reach Corner](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/)

- solves: `minimum_obstacles`
- Pattern: 0-1 BFS over a grid.

### 68. [Minimum Cost To Make At Least One Valid Path In A Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)

- solves: `min_cost`
- Pattern: 0-1 BFS over grid directions.

### 69. [Swim In Rising Water](https://leetcode.com/problems/swim-in-rising-water/)

- solves: `swim_in_water`
- Pattern: priority-queue traversal over a weighted grid.

### 70. [Minimum Cost To Reach Destination In Time](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/)

- solves: `minimum_cost`
- Pattern: shortest path with time as part of the state.

### 71. [Second Minimum Time To Reach Destination](https://leetcode.com/problems/second-minimum-time-to-reach-destination/)

- solves: `second_minimum_time`
- Pattern: track first and second shortest arrival times.

### 72. [Min Cost To Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)

- solves: `min_cost_connect_points`
- Pattern: minimum spanning tree over complete graph distances.
