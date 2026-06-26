# Grid Backtracking

## Pattern

Move through grid cells while marking the current path as visited.

## Intuition

Grid backtracking is DFS with path-specific visited state.

## How It Works

You mark a cell before exploring neighbors and unmark it after.

## Template

```text
def dfs(r, c, index):
    if out of bounds or invalid: return false
    if complete: return true
    mark visited
    explore four directions
    unmark visited
```

## Example

In word search, one cell cannot be reused in the same word path, but can be used in a different attempted path.

## Complexity

```text
Time: O(rows * cols * branching^word_length)
Space: O(word_length)
```

## Pitfalls

- Using global visited across all starts.
- Forgetting to unmark.
- Checking completion after rejecting the final valid character.

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
