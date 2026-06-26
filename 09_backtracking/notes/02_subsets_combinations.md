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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
