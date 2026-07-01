# Merge And Insert Intervals

## Pattern

Merge overlapping intervals into one combined range.

## Intuition

Keep a current merged interval and extend it when the next interval overlaps.

## How It Works

Insert interval is merge intervals with one new interval added.

## Template

```text
sort intervals
merged = []
for start, end in intervals:
    if no overlap:
        append interval
    else:
        extend previous end
```

## Example

`[1,3]` plus `[2,6]` becomes `[1,6]`.

## Complexity

```text
Time: O(n log n) sort or O(n) if already sorted
Space: O(n) output
```

## Pitfalls

- Using `<` instead of `<=` when touching endpoints should merge.
- Forgetting to append the final active interval.
- Not handling insertion before all intervals.

## Interview Checklist

Before coding, make sure you can answer:

```text
What defines the "current merged interval" I'm extending?
Should I use `<` or `<=` when checking if the next interval touches the current one?
For insert-interval, how do I split the work into intervals fully before, overlapping, and fully after the new one?
Am I appending the final active/merged interval after the loop ends?
Is the input already sorted, or do I need to sort first (and does that change the complexity)?
```
