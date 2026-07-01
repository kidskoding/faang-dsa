# K-Way Merge

## Pattern

Use a heap to merge k sorted streams by always taking the smallest current head.

## Intuition

Each stream is sorted internally. The heap chooses the global next value.

## How It Works

Push the first item from each list, then push the next item from the list you popped.

## Template

```text
heap = first item from each list
while heap:
    value, list_id, index = heappop(heap)
    append value
    push next from same list
```

## Example

This is the heap version of merging two sorted lists generalized to k lists.

## Complexity

```text
Time: O(N log k)
Space: O(k)
```

## Pitfalls

- Pushing all N values instead of one per list.
- Losing which list an item came from.
- Not handling empty lists.

## Interview Checklist

Before coding, make sure you can answer:

```text
Why does the heap only ever hold one candidate per list, not all N values?
What info do I store per heap entry so I know which list/index to advance next?
What do I do when a list is exhausted or empty from the start?
Why is this O(N log k) rather than O(N log N), and what does k represent here?
How would this change if merging linked lists instead of arrays (no index, use node.next)?
```
