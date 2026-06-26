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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
