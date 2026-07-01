# Heap Basics

## Pattern

A heap is a priority queue that quickly returns the smallest or largest priority item.

## Intuition

Use a heap when you repeatedly need the next best item, not full sorted order.

## How It Works

Python `heapq` is a min heap. Use negative values for max-heap behavior.

## Template

```text
heap = []
heappush(heap, item)
best = heappop(heap)
```

## Example

If tasks have priorities, popping returns the smallest priority first.

## Complexity

```text
push/pop: O(log n)
peek: O(1)
heapify: O(n)
```

## Pitfalls

- Expecting heap iteration to be sorted.
- Forgetting Python has min heap only by default.
- Putting tuples in heap with incomparable tie fields.

## Interview Checklist

Before coding, make sure you can answer:

```text
Do I need repeated access to the next-best item, or just one min/max lookup?
Do I need a min heap or a max heap, and how do I simulate max heap in Python?
What exactly goes in each heap entry, and are tuple fields comparable if priorities tie?
Should I build the heap with heapify (O(n)) or push items one at a time (O(n log n))?
Am I relying on heap iteration/order being sorted anywhere (it isn't)?
```
