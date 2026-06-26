# Frequency Map Windows

## Pattern

Use counts inside the current window to track duplicates, required characters, or distinct values.

## Intuition

A set only says present or missing. A frequency map tells how many copies are inside the window.

## How It Works

This matters when duplicate characters or values are allowed.

## Template

```text
counts = {}
left = 0
for right, x in enumerate(items):
    counts[x] = counts.get(x, 0) + 1

    while invalid(counts):
        y = items[left]
        counts[y] -= 1
        if counts[y] == 0:
            del counts[y]
        left += 1
```

## Example

For permutation-in-string, counts track whether the window has exactly the target character frequencies.

## Complexity

```text
Time: O(n)
Space: O(distinct values in window)
```

## Pitfalls

- Leaving zero-count keys in the map when distinct count matters.
- Comparing entire maps too often when a matched counter would be cleaner.
- Confusing required count with current window count.

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
