# Sorting Internals

## Pattern

Interviewers occasionally ask you to implement a sort from scratch, or to use a
partition step (quickselect) to answer a Kth-order-statistic question without
sorting everything.

## Intuition

Merge sort and quicksort both attack "sort n items" by shrinking the problem:
merge sort splits blindly and does the work on the merge; quicksort splits
around a pivot and does the work on the partition. Quickselect reuses
quicksort's partition but only recurses into the one side that can contain the
answer, dropping the average case from O(n log n) to O(n).

## How It Works

**Merge sort**: split the array in half, recursively sort each half, then
merge two sorted halves with a linear two-pointer walk. Stable (equal keys
never cross during the merge) and always O(n log n), which is why it is the
safe choice when stability or worst-case guarantees matter, or when sorting a
linked list (merge needs no random access).

**Quicksort**: pick a pivot, partition the array so smaller elements land left
and larger land right, then recursively sort both sides. In place and usually
faster in practice than merge sort due to cache locality, but not stable, and
degrades to O(n^2) on adversarial or already-sorted input unless the pivot is
randomized. The Lomuto partition scheme (single scan, pivot fixed at one end)
is easiest to code correctly under interview pressure; Hoare's is fewer swaps
but trickier to get right.

**Quickselect**: same partition as quicksort, but after partitioning around a
pivot, compare the pivot's final index to the target rank k. Only recurse into
the side that contains index k — never both. Randomize the pivot choice so
adversarial input still runs in expected O(n).

## Template

```text
merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

merge(left, right):
    walk both with two pointers, append the smaller front each step

partition(arr, lo, hi, pivot_index):
    swap pivot to hi
    boundary = lo
    for i in range(lo, hi):
        if arr[i] < pivot_value:
            swap(arr[i], arr[boundary]); boundary += 1
    swap(arr[boundary], arr[hi])
    return boundary  # pivot's final sorted index

quickselect(arr, lo, hi, k):
    pivot_index = random(lo, hi)
    p = partition(arr, lo, hi, pivot_index)
    if p == k: return arr[p]
    if p < k: return quickselect(arr, p + 1, hi, k)
    return quickselect(arr, lo, p - 1, k)
```

## Example

Kth Largest Element In An Array: convert "Kth largest" to "index n-k in
ascending order," then quickselect for that index instead of sorting the
whole array.

## Complexity

```text
Merge sort:  Time O(n log n) always, Space O(n) for the merge buffer
Quicksort:   Time O(n log n) average, O(n^2) worst case, Space O(log n) recursion
Quickselect: Time O(n) average, O(n^2) worst case, Space O(log n) recursion
```

## Pitfalls

- Forgetting to randomize the quicksort/quickselect pivot — sorted or
  reverse-sorted input then triggers the O(n^2) worst case.
- Recursing into both sides in quickselect instead of only the side
  containing k, which silently degrades it back to a full sort.
- Assuming quicksort is stable — it is not, and swapping equal keys can
  reorder them.
- Off-by-one errors in the partition boundary, especially with the Lomuto
  scheme when the array has many duplicate values.

## Interview Checklist

Before coding, make sure you can answer:

```text
Do I need stability or a worst-case guarantee (merge sort), or is average-case
in-place speed enough (quicksort)?
Am I randomizing the pivot so adversarial input can't force O(n^2)?
For a Kth-element question, am I using quickselect instead of a full sort or a heap?
In quickselect, after partitioning, am I recursing into only the side that
contains the target index?
Does my partition scheme correctly handle duplicate values without infinite
recursion?
```
