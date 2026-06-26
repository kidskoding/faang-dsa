# Meeting Rooms

## Pattern

Meeting room problems track how many intervals are active at once.

## Intuition

If a meeting starts before another ends, you need another room.

## How It Works

Use sorted starts/ends or a min heap of end times.

## Template

```text
sort starts
sort ends
rooms = 0
move through starts and ends
```

## Example

A start before earliest end increases active rooms; otherwise one room frees.

## Complexity

```text
Time: O(n log n)
Space: O(n) or O(1) depending method
```

## Pitfalls

- Treating back-to-back meetings as overlapping.
- Using merge logic when max overlap is needed.
- Forgetting to pop all ended meetings in heap approach.

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
