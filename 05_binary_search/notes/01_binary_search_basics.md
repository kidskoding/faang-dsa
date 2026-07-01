# Binary Search Basics

## Pattern

Repeatedly cut a sorted search space in half.

## Intuition

Sorted order tells you which half cannot contain the answer.

## How It Works

Maintain `left` and `right` as the remaining possible answer range.

## Template

```text
left = 0
right = len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

## Example

Searching for `7` in `[1,3,5,7,9]` checks middle `5`, then moves right.

## Complexity

```text
Time: O(log n)
Space: O(1)
```

## Pitfalls

- Using binary search on unsorted data.
- Infinite loops from not moving bounds.
- Overflow in some languages from `(l+r)//2`.

## Interview Checklist

Before coding, make sure you can answer:

```text
Is the array actually sorted (or sorted enough) for binary search to apply?
Why does `left <= right` (not `<`) match an exact-match search?
Why is `mid + 1` / `mid - 1` correct here instead of `mid` when narrowing?
How would you rewrite `(left + right) // 2` to avoid overflow in a language without arbitrary-precision ints?
What do you return if the target is never found?
```
