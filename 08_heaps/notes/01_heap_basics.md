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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
