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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
