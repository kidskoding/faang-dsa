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
Am I answering "can everyone attend" (boolean) or "how many rooms needed" (max concurrency)?
Do back-to-back meetings (one ends exactly when another starts) require a new room?
Should I use separate sorted start/end arrays with two pointers, or a min-heap of end times — and why?
If using a heap, when do I pop a finished meeting versus push a new one?
What does the peak value of my counter represent in terms of the answer?
```
