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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
