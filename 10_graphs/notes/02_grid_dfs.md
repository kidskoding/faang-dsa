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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
