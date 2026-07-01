# Grid DFS

## Pattern

A grid is an implicit graph. Each cell is a node, and neighboring cells are edges.

## Intuition

You do not need to build an adjacency list. Compute neighbors with direction arrays.

## How It Works

For each cell, check bounds, value validity, and visited state. DFS explores the full connected region.

## Template

```text
def dfs(r, c):
    if r/c out of bounds:
        return
    if cell is invalid or visited:
        return

    mark visited
    for each direction:
        dfs(nr, nc)
```

## Example

In number of islands, DFS from one land cell marks the entire island so it is counted once.

## Complexity

```text
Time: O(rows * cols)
Space: O(rows * cols) worst-case recursion/visited
```

## Pitfalls

- Bad bounds checks.
- Forgetting to mark visited.
- Recursing diagonally when only 4-direction movement is allowed.

## Interview Checklist

Before coding, make sure you can answer:

```text
What are my bounds checks, and do I check them before or after indexing into the grid?
Is movement restricted to 4 directions, or does the problem allow diagonals?
Am I marking a cell visited (or mutating it in place) before or after recursing into it?
Can I reuse the input grid as the visited set, or do I need a separate structure?
Does the recursion depth risk a stack overflow on large grids, and would BFS be safer?
```
