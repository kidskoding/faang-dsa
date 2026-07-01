# Matrix Coordinates

## Pattern

Represent grid positions as `(row, col)` and move with direction arrays.

## Intuition

Most matrix bugs are boundary bugs.

## How It Works

Use consistent row/column naming and bounds checks.

## Template

```text
directions = [(1,0),(-1,0),(0,1),(0,-1)]
for dr, dc in directions:
    nr = r + dr
    nc = c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        process
```

## Example

From `(2,3)`, `(2,4)` is right and `(3,3)` is down.

## Complexity

```text
Usually O(rows * cols)
Space depends on visited/output
```

## Pitfalls

- Swapping rows and columns.
- Using `len(grid[0])` when grid may be empty.
- Bad bounds checks.

## Interview Checklist

Before coding, make sure you can answer:

```text
Am I consistently treating the first coordinate as row and the second as col?
Which direction set does this problem need: 4-directional, 8-directional, or diagonals only?
Do I bounds-check `0 <= nr < rows and 0 <= nc < cols` before touching grid[nr][nc]?
Could the grid be empty or ragged, and does my `len(grid[0])` call handle that?
Am I marking cells visited in place or with a separate set, and could that double-count or infinite-loop?
What is the time and space complexity in terms of rows * cols?
```
