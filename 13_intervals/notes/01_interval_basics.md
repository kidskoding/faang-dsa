# Interval Basics

## Pattern

Intervals represent ranges with start and end points.

## Intuition

Most interval problems become easier after sorting by start or end.

## How It Works

You compare the next interval against the current active interval.

## Template

```text
sort intervals by start
for interval in intervals:
    compare interval.start with current_end
```

## Example

`[1,3]` and `[2,5]` overlap because `2 <= 3`.

## Complexity

```text
Time usually O(n log n) due to sorting
Space depends on output
```

## Pitfalls

- Not clarifying inclusive vs exclusive endpoints.
- Forgetting empty input.
- Sorting by the wrong key.

## Interview Checklist

Before coding, make sure you can answer:

```text
Are endpoints inclusive or exclusive, and does that change what "overlap" means?
Should I sort by start or by end for this problem?
What is the exact condition that decides two intervals overlap vs. are disjoint?
Do touching intervals (e.g. [1,3] and [3,5]) count as overlapping here?
How do I handle an empty input or a single interval?
```
