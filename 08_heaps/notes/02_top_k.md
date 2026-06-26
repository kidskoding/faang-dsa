# Top-K

## Pattern

Use a heap of size `k` to keep only the best `k` candidates.

## Intuition

If you only need k items, do not sort everything.

## How It Works

For k largest, keep a min heap of size k; the smallest kept item is the cutoff.

## Template

```text
heap = []
for x in nums:
    heappush(heap, x)
    if len(heap) > k:
        heappop(heap)
return heap
```

## Example

For k largest, any value popped from the size-k min heap cannot be in the final top k.

## Complexity

```text
Time: O(n log k)
Space: O(k)
```

## Pitfalls

- Using O(n log n) sort when k is small.
- Mixing up min heap vs max heap.
- Returning heap order as sorted order.

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
