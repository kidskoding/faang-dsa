# Fast And Slow Pointers

## Pattern

Use two pointers moving at different speeds to find middle or detect cycles.

## Intuition

Fast gains on slow. In a cycle, fast eventually catches slow.

## How It Works

For middle, fast reaches the end while slow reaches halfway.

## Template

```text
slow = head
fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

## Example

In a 5-node list, slow lands on the middle when fast exits.

## Complexity

```text
Time: O(n)
Space: O(1)
```

## Pitfalls

- Not checking `fast.next`.
- Using the wrong starting positions for first vs second middle.
- Stopping too late before splitting.

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
