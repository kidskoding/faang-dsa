# Opposite-End Pointers

**Opposite-end pointers** keep one index at the left end of a sequence and one
at the right, then move them toward each other. The indices are usually called
`left` and `right`, so the basic shape looks like this

```text
index   0   1   2    3    4
value   2   7  11   15   19
        ^                 ^
      left             right
```

A nested loop can inspect every pair, but that costs `O(n²)`. Two pointers
becomes faster only when one comparison can reject many pairs at once. Sorted
order usually provides that proof. If `nums[left] + nums[right]` is too small,
then `nums[left]` is too small with every value at or left of `right`, so moving
`left` is forced. If the sum is too large, moving `right` is forced for the
same reason

The important idea is therefore not "put pointers at both ends." It is **prove
which candidates become impossible before moving a pointer**. Without that
proof, the same-looking loop can silently skip the answer

## When To Use

This pattern is a good candidate when:

- The input is sorted, or sorting is allowed, and you need a pair or a fixed-size
  group
- A comparison tells you that one end cannot participate in a better answer
- The two ends are naturally paired, as in a palindrome, reversal, or widest
  container

Sortedness is not required for every opposite-end problem. A palindrome compares
the ends directly, while Container With Most Water relies on shrinking width.
What all of these problems share is a reason that moving inward is safe

If an unsorted pair problem asks for original indices, use the
[hash-map complement pattern](../../01_arrays_and_hashing/notes/02_hashing.md).
Sorting would cost `O(n log n)` and would destroy those original positions

## Let The Comparison Choose The Pointer

For Two Sum II - Input Array Is Sorted, the numbers already arrive sorted. The
scan is short because each failed sum removes one endpoint from every future
pair

```python
def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1
        else:
            right -= 1

    return []


assert two_sum_sorted([2, 7, 11, 15], 9) == [0, 1]
assert two_sum_sorted([1, 2, 2, 6], 8) == [1, 3]
assert two_sum_sorted([], 8) == []
```

The strict condition `left < right` prevents one element from being used twice.
Exactly one pointer moves after a rejected pair. Moving both would skip pairs
that were never tested

```text
nums=[1, 2, 2, 6], target=8

left=0 (1)  right=3 (6)  sum=7  too small
    reject every pair using the 1; move left, keep right fixed
left=1 (2)  right=3 (6)  sum=8  accept [1, 3]
```

The duplicate `2` causes no problem because the function returns one valid pair.
When a problem asks for every unique group, duplicates need deliberate skipping

## Fix One Value To Turn A Triple Into A Pair

Problems such as 3Sum and 3Sum Closest add one outer choice to the same scan.
Sort the array, fix `nums[i]`, and search the suffix for the remaining two
values. For 3Sum, those two values must add to `-nums[i]`

```python
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    triples: list[list[int]] = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triples.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return triples


assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
assert three_sum([]) == []
```

The outer skip rejects a repeated first value because it would run the same
search again. The inner skips happen only after recording a match, because equal
neighbours would reproduce that same triple. Moving past duplicates before a
match is proven could skip a valid group

4Sum fixes two values before the scan. 3Sum Smaller counts `right - left`
pairs at once when a sum is small enough, because every value between those
pointers also works. 3Sum With Multiplicity makes the same grouped count but
multiplies by the number of equal values. Number of Subsequences That Satisfy the
Given Sum Condition uses the related fact that, once the minimum and maximum
work, every subset of the middle values works, giving a power-of-two count

## Worked Example: [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

You are given non-negative bar heights. Two bars form a container whose width is
the distance between their indices and whose usable height is the shorter bar.
Return the largest area, so a pair `(left, right)` holds
`(right - left) * min(height[left], height[right])`

Trying every pair costs `O(n²)`. Start with the widest possible container
instead. Every inward move loses width, which means a later container can improve
only if its limiting height becomes taller

> "The shorter wall limits the current area. Moving the taller wall keeps that
> same limit and loses width, so it cannot improve the answer. I will move the
> shorter wall because it is the only move that might raise the limit."

This is a forced-movement argument even though the heights are not sorted. If
the bars tie, either one may move because both impose the same limit; the code
below moves `right`

```python
def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        width = right - left
        best = max(best, width * min(height[left], height[right]))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return best


assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert max_area([5, 5, 5]) == 10
assert max_area([]) == 0
```

The standard input begins like this

```text
height=[1, 8, 6, 2, 5, 4, 8, 3, 7]

left=0 (1)  right=8 (7)  width=8  area=8
    moving right is rejected: height 1 would still cap the area while width fell
    move left; right stays at 8

left=1 (8)  right=8 (7)  width=7  area=49  best=49
    right is shorter, so move right

left=1 (8)  right=7 (3)  width=6  area=18  best stays 49
    this candidate is discarded; move right again because height 3 is the limit
```

The scan never needs to revisit a removed bar. When a shorter bar is discarded,
every container using it at a smaller width has an area no larger than the one
already checked

- **Time Complexity:** `O(n)`, because one pointer moves inward on every
  iteration and the pointers can cross only once
- **Space Complexity:** `O(1)`, because the scan stores two indices and the best
  area rather than another array

## Other Shapes In This Family

The workbook stretches the same idea in several useful directions:

- Valid Palindrome and Reverse String compare or swap the two ends, then move
  both pointers. Valid Palindrome II branches once at the first mismatch and
  tests skipping either end, because only one deletion is allowed
- Backspace String Compare scans both strings from right to left. Before comparing
  visible characters, each pointer skips characters erased by a `#`
- Reverse Words in a String reverses the whole sequence and then reverses each
  word range, reusing the same opposite-end swap on several boundaries
- Boats To Save People pairs the heaviest remaining person with the lightest when
  they fit. If they do not fit, the heaviest must travel alone, because no other
  remaining partner is lighter
- Minimize Maximum Pair Sum In Array pairs smallest with largest after sorting.
  Pairing a large value with another large value can only raise the maximum pair
  sum
- Bag of Tokens spends the cheapest token to gain score and, only when blocked,
  sells the most expensive token to recover the most power per lost point
- Find K Closest Elements starts with the whole sorted array and discards the
  farther endpoint until only `k` values remain. A tie discards the right end
  because the problem prefers smaller values
- 3Sum Closest keeps the closest total while steering toward the target. Four
  Sum adds one more fixed outer index, while the duplicate rules stay the same
- Trapping Rain Water tracks the tallest wall seen from each side. The side with
  the smaller running boundary can be finalized, because the opposite boundary
  is already tall enough and a future wall cannot lower the trapped amount there

Each variant still needs its own rejection sentence. "Move the pointer that the
template says to move" is not a correctness argument

## Time and Space Complexity

`n` is the number of input values

| Approach                                         | Time                                                                                   | Space                                                                                                                            |
| ------------------------------------------------ | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Opposite-end scan on prepared input              | `O(n)`: at least one pointer moves inward each iteration, so no index is crossed twice | `O(1)`: the scan stores only indices and a small amount of state                                                                 |
| Sort, then scan                                  | `O(n log n)`: comparison sorting dominates the following linear scan                   | `O(n)`: `sorted()` copies the values; an in-place `list.sort()` avoids that copy but may still use implementation working memory |
| Fix one value, then scan for 3Sum-style problems | `O(n²)`: each of `n` outer choices can run one linear suffix scan                      | `O(n)` beyond the output in Python: the scan stores constant state, but `list.sort()` may use linear working memory              |
| Check every pair                                 | `O(n²)`: nested loops inspect candidates that the movement proof could reject together | `O(1)`: only two loop indices are needed                                                                                         |

## Summary

- **Opposite-end pointers** place `left` and `right` at the extremes and move
  inward only after proving that one endpoint cannot belong to a better answer
- Sorted pair problems use a forced rule: a sum that is too small moves `left`,
  while a sum that is too large moves `right`, because the opposite move makes
  the error worse
- Symmetric problems such as palindromes and reversals do not need sorted input,
  because the two ends are compared directly and both can move after a match
- Container With Most Water always moves the shorter wall, because moving the
  taller wall preserves the limiting height while shrinking the width
- 3Sum fixes one value and scans the remaining suffix. Duplicate first values and
  duplicate values after a match must be skipped so the output stays unique
- A single prepared scan costs `O(n)` time and `O(1)` auxiliary space. Sorting
  first changes the time to `O(n log n)`, and fixing an outer value for 3Sum
  changes it to `O(n²)`

## Interview Checklist

Before coding, make sure you can answer each of these

```text
What property lets me reject an endpoint instead of checking every pair?
Is the input sorted, or is the movement proof based on something else?
If I sort, do I destroy original indices that the answer must return?
When a candidate fails, which pointer moves, which pointer stays, and why?
Should the loop use left < right, and may one element be used twice?
Do duplicates require skipping, counting, or no special handling?
For a triple or quadruple, how many values should I fix before the pair scan?
Can I justify moving the shorter wall in Container With Most Water?
Can I state the cost of sorting separately from the cost of the scan?
```
