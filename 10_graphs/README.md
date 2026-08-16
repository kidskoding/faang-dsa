# Module 10: Graphs

## Topics

- Graph basics and reachability
- Grid DFS
- Grid BFS and multi-source BFS
- Components, cycles, and bipartite graphs
- Topological sort and DAGs
- Implicit-state BFS
- Weighted shortest paths
- Minimum spanning trees and advanced connectivity

## Notes

1. [Graph Basics And Reachability](notes/01_graph_basics.md)
2. [Grid DFS](notes/02_grid_dfs.md)
3. [Grid BFS And Multi-Source BFS](notes/03_grid_bfs.md)
4. [Components, Cycles, And Bipartite Graphs](notes/04_components_cycles_bipartite.md)
5. [Topological Sort](notes/05_topological_sort.md)
6. [Implicit-State BFS](notes/06_implicit_state_bfs.md)
7. [Weighted Shortest Paths](notes/07_weighted_shortest_paths.md)

## Problem Set

[Graph Problem Set](problem_set/GRAPH_PROBLEM_SET.md) — 72 problems, grouped into **Graph Basics**, **Grid DFS**, **Grid BFS**, **Components, Cycles, And Bipartite**, **Topological Sort**, **Implicit-State BFS**, **Weighted Shortest Paths**. Each entry names the pattern it teaches and the stub function it solves, across 7 solution files in `problem_set/`.

The workbook is the canonical list. It is not duplicated here, so the two
cannot drift apart.

## Additional Notes

- Grids are implicit graphs.
- Each cell is a node and each valid neighboring cell is an edge.
- Deeper graph variants such as minimum spanning trees, advanced union find, and advanced shortest paths live in `17_advanced/`.
