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
Do I need strict FIFO order (queue) or insertion/removal at both ends (deque)?
Am I using collections.deque instead of list.pop(0), which would silently make this O(n) per op?
If this is graph/grid BFS, where exactly do I mark visited — on enqueue or on dequeue — and why does that avoid duplicate work?
Does level-order structure matter here (do I need to track level boundaries via queue length snapshots)?
What goes in each queue entry: just a node, or (node, distance/state) for path reconstruction?
```
