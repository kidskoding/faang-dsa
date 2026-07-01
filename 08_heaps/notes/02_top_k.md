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
Am I looking for the k largest or k smallest, and does that flip min heap vs max heap?
Why does keeping a size-k min heap correctly find the k largest (what does the top represent)?
What is the invariant on heap size, and when exactly do I pop after pushing?
Why is this O(n log k) instead of O(n log n), and when does that actually matter?
Do I need the final k items in sorted order, or is the heap's contents enough?
```
