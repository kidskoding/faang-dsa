# Fast And Slow Pointers

## Pattern

Move one pointer faster than another to detect cycles, find middles, or compare positions with a gap.

## Intuition

Different speeds reveal structure. If there is a cycle, fast eventually catches slow. If fast reaches the end, slow is near the middle.

## How It Works

This pattern is common in linked lists, but it also appears in arrays modeled as pointer jumps.

## Template

```text
slow = start
fast = start

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

## Example

In a linked list of length 5, fast moves two steps at a time. When fast reaches the end, slow has moved about half as many steps.

## Complexity

```text
Time: O(n)
Space: O(1)
```

## Pitfalls

- Not checking `fast` and `fast.next` before moving two steps.
- Using fast/slow when a simple two-pointer scan is enough.
- For cycle entry, forgetting the second phase after detection.

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
