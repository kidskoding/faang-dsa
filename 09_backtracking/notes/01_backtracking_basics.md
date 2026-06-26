# Backtracking Basics

## Pattern

Backtracking explores a decision tree and undoes choices when returning.

## Intuition

It is controlled brute force: choose, explore, unchoose.

## How It Works

Use it when you must enumerate valid combinations, permutations, paths, or assignments.

## Template

```text
def backtrack(state):
    if complete(state):
        save answer
        return
    for choice in choices:
        make choice
        backtrack(state)
        undo choice
```

## Example

For subsets, each number creates a choose/skip decision.

## Complexity

```text
Time: often exponential
Space: recursion depth plus output
```

## Pitfalls

- Forgetting to undo a choice.
- Appending mutable state without copying.
- Not pruning invalid branches early.

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
