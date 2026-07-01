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
Am I checking `fast and fast.next` (or just `fast`), and does that match whether I want the first or second middle?
If I'm detecting a cycle, do I also need to find its entry point, and do I know why the second pointer starts at head for that?
Why does fast catching slow prove a cycle, rather than just looping forever?
Where exactly do slow and fast start, and does that choice shift which node counts as "the middle" for even-length lists?
What is the time and space complexity, and why is this preferred over a hash-set-of-visited-nodes approach?
```
