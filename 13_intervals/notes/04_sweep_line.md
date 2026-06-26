# Sweep Line

## Pattern

Convert interval starts and ends into events and scan in sorted order.

## Intuition

The active count changes at event boundaries.

## How It Works

This is useful for max overlap, calendars, and range additions.

## Template

```text
events = []
for interval:
    events.append((start, +1))
    events.append((end, -1))
sort events
scan active count
```

## Example

Each start adds one active interval; each end removes one.

## Complexity

```text
Time: O(n log n)
Space: O(n)
```

## Pitfalls

- Wrong tie-breaking for start/end at same coordinate.
- Forgetting endpoint convention.
- Using sweep line when simple merge is enough.

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
