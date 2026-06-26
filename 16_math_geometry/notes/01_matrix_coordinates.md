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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
