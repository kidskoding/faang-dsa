# Rotated Arrays

## Pattern

Binary search still works if one side is sorted at every step.

## Intuition

A rotated sorted array has two sorted pieces. Compare endpoints to decide which side is ordered.

## How It Works

At each midpoint, identify the sorted half, then decide if target lies inside it.

## Template

```text
while left <= right:
    mid = ...
    if nums[mid] == target: return mid
    if nums[left] <= nums[mid]:
        handle sorted left half
    else:
        handle sorted right half
```

## Example

In `[4,5,6,7,0,1,2]`, mid `7` means left half `[4,5,6,7]` is sorted.

## Complexity

```text
Time: O(log n)
Space: O(1)
```

## Pitfalls

- Forgetting duplicates can complicate the logic.
- Checking only one sorted side.
- Moving the wrong bound when target is inside the sorted half.

## Interview Checklist

Before coding, make sure you can answer:

```text
How do you decide which half (`nums[left..mid]` or `nums[mid..right]`) is the sorted one at each step?
Once you know the sorted half, how do you check if the target falls inside its range?
How does the logic break with duplicate values (e.g. `nums[left] == nums[mid] == nums[right]`), and how do you recover (linear fallback or shrinking both ends)?
Why is it still O(log n) on distinct values but O(n) worst case with duplicates?
```
