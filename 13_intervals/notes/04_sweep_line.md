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
How do I encode each interval as (position, delta) events, and what deltas do I use?
When a start and an end land on the same coordinate, which event should be processed first, and why does that matter?
What does the running active-count variable represent at each point in the scan?
Am I tracking a running sum (max overlap / calendar) or a running total (range addition), and does that change the event encoding?
Is a full sweep line overkill here, or would a simpler sort-and-merge pass solve it?
```
