# Queue And Deque

## Pattern

A queue is first-in, first-out. A deque supports efficient operations at both ends.

## Intuition

Queues model level-order processing and shortest-path BFS. Deques also power monotonic queues.

## How It Works

Use `collections.deque` in Python for efficient `popleft`.

## Template

```text
queue = deque([start])
while queue:
    item = queue.popleft()
    process item
    add neighbors
```

## Example

In BFS, items added earlier are processed earlier, which preserves distance order.

## Complexity

```text
append/popleft: O(1)
space: O(n)
```

## Pitfalls

- Using list `pop(0)`, which is O(n).
- Mixing queue and stack behavior accidentally.
- Not marking visited when enqueuing in graph BFS.

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
