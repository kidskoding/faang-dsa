# Subsets And Combinations

## Pattern

Build choices in increasing index order to avoid duplicates and permutations.

## Intuition

The `start` index prevents reusing earlier choices.

## How It Works

Subsets save at every node; combinations often save only when size or target is reached.

## Template

```text
def backtrack(start, path):
    save path if needed
    for i in range(start, n):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
```

## Example

For `[1,2,3]`, starting later prevents `[2,1]` after `[1,2]`.

## Complexity

```text
Time: O(2^n) for subsets, output dominated
Space: O(n) path
```

## Pitfalls

- Using `0` as next start and creating duplicate orders.
- Saving path without copying.
- Not sorting when duplicate-skipping requires it.

## Interview Checklist

Before coding, make sure you can answer:

```text
Am I passing `i + 1` (not `0` or `i`) as the next `start` to avoid reordered duplicates?
Do subsets need to be saved at every node, or only when a size/target condition is met?
If the input has duplicate values, did I sort first and skip repeated values at the same recursion depth?
Is the path being copied (`path[:]` or `list(path)`) at save time, not saved by reference?
What terminates the loop early — running out of indices, or exceeding a target sum?
```
