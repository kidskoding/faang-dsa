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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
