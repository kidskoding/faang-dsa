# Interval Greedy

## Pattern

Sort intervals by the property that makes future choices easiest.

## Intuition

Often earliest end time is better than earliest start time.

## How It Works

For non-overlap, choose the interval that ends soonest.

## Template

```text
sort by end
end = -inf
count = 0
for interval in intervals:
    if interval.start >= end:
        choose it
        end = interval.end
```

## Example

Choosing a shorter/earlier-ending interval leaves more room for the rest.

## Complexity

```text
Time: O(n log n)
Space: O(1) or sorting space
```

## Pitfalls

- Sorting by start when end time is the real greedy key.
- Not defining overlap boundary carefully.
- Forgetting to prove exchange argument.

## Interview Checklist

Before coding, make sure you can answer:

```text
Why sort by end time instead of start time or duration for this problem?
What is my exchange argument for why the earliest-ending interval is never a worse choice?
How exactly am I defining the overlap boundary — is `start >= end` or `start > end` correct here?
What does `end` represent between iterations, and when does it get updated?
Would this problem change (e.g. to erase/merge count) if I kept the same sort but changed what I track?
```
