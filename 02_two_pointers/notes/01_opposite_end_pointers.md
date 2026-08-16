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
            return [left + 1, right + 1]
        if total < target:
            left += 1
        else:
            right -= 1

    return []


assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
assert two_sum_sorted([1, 2, 2, 6], 8) == [2, 4]
assert two_sum_sorted([], 8) == []
```

The strict condition `left < right` prevents one element from being used twice.
Exactly one pointer moves after a rejected pair. Moving both would skip pairs
that were never tested

```text
nums=[1, 2, 2, 6], target=8

left=0 (1)  right=3 (6)  sum=7  too small
    reject every pair using the 1; move left, keep right fixed
left=1 (2)  right=3 (6)  sum=8  accept one-based positions [2, 4]
```

The duplicate `2` causes no problem because the function returns one valid pair.
The returned positions are one-based because Two Sum II explicitly numbers the
first element as position 1. When a problem asks for every unique group,
duplicates need deliberate skipping

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
pointers also works

3Sum With Multiplicity must count positions rather than only unique triples.
After fixing the first value, steer `left` and `right` by their sum as usual. On
a match where the endpoint values differ, count their equal runs. If the left
value appears `left_count` times and the right value appears `right_count` times,
they form `left_count * right_count` pairs. If the endpoint values are equal,
all `k = right - left + 1` remaining values are equal, so any two positions work:
add `k * (k - 1) // 2` and finish that scan. Keep the running answer modulo the
constant required by the problem

```text
remaining=[1, 1, 2, 2, 2], needed sum=3
left value 1 occurs 2 times; right value 2 occurs 3 times
accept 2 * 3 = 6 position pairs, then move past both groups

remaining=[2, 2, 2, 2], needed sum=4
both ends have value 2; choose 2 of 4 positions -> 4 * 3 // 2 = 6
```

Number of Subsequences That Satisfy the Given Sum Condition sorts the values and
tests `nums[left] + nums[right]`. If that sum is too large, `right` is rejected,
because pairing it with any larger minimum would also fail. If it fits,
`nums[left]` is the required minimum and any subset of the `right - left` values
after it may be included. Every included value is at most `nums[right]`, so all
`2 ** (right - left)` subsets are valid. Add that count and move `left`; in code,
precompute the powers of two modulo the value required by the problem

```text
nums=[3, 5, 6, 7], target=9
left=0 (3), right=3 (7) -> 10 is too large, reject 7 and move right
left=0 (3), right=2 (6) -> 9 fits
    keep 3; choose any subset of positions holding 5 and 6
    {}, {5}, {6}, {5, 6} -> 2 ** (2 - 0) = 4 subsequences
```

## Worked Example: [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

You are given non-negative bar heights. Two bars form a container whose width is
the distance between their indices and whose usable height is the shorter bar.
Return the largest area, so a pair `(left, right)` holds
`(right - left) * min(height[left], height[right])`

**Input**: `height`, a `list[int]` of bar heights, where LeetCode guarantees
`2 <= len(height) <= 10^5` and every height is between `0` and `10^4`

**Output**: an `int`, the largest area any single pair of bars can hold, measured
as the distance between their two indices times the shorter of their two heights.
The bars are walls, not a shape to be filled, so nothing between them matters

Trying every pair costs `O(n²)`. Start with the widest possible container
instead. Every inward move loses width, which means a later container can improve
only if its limiting height becomes taller

> "The shorter wall limits the current area. Moving the taller wall keeps that
> same limit and loses width, so it cannot improve the answer. I will move the
> shorter wall because it is the only move that might raise the limit."

This is a forced-movement argument even though the heights are not sorted. If
the bars tie, either one may move because both impose the same limit; the code
below moves `right`

Therefore,

1. Place `left` at index `0` and `right` at the last index, because that pair has
   the largest width available and every later candidate can only be narrower
2. Keep a running `best` that starts at `0`. Starting from zero also settles the
   degenerate input: with fewer than two bars, `right` never sits to the right of
   `left`, the loop body never runs, and `0` is returned instead of an error
3. While `left < right`, measure the current container: its width is
   `right - left` and its usable height is the shorter of the two walls, so its
   area is `(right - left) * min(height[left], height[right])`. Keep it in `best`
   if it beats what has been seen
4. Compare the two walls and move the shorter one inward by one step. That is the
   forced move argued above: the shorter wall caps this area, so keeping it while
   the width falls can never produce a larger container, while replacing it at
   least makes a taller limit possible
5. When the two walls tie, move either one, since both impose the same limit. The
   code moves `right`, which is why the comparison is `height[left] < height[right]`
   rather than `<=`
6. Stop when the pointers meet, since a container needs two distinct bars, and
   return `best`

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

The workbook stretches the same idea in several useful directions. Valid
Palindrome first advances each side past non-alphanumeric characters, since
spaces and punctuation are not part of the comparison. It lowercases the two
remaining characters, rejects a mismatch, and moves both pointers after a match.
For example, the comma in `"A man, a plan"` moves a pointer without triggering a
comparison. Reverse String uses the same two-end movement but swaps instead.
Valid Palindrome II branches once at the first real mismatch and tests the ranges
formed by skipping either the left or the right character

Backspace String Compare scans each string from right to left with its own
`skip` counter. A `#` increments `skip`; an ordinary character is discarded and
decrements `skip` while `skip > 0`; otherwise it is the next visible character
to compare. The two indices move independently until each has found a visible
character, which handles chains such as `"ab##c"` without constructing the
edited strings

Reverse Words in a String must normally remove leading and trailing whitespace
and reduce every internal run to one space. Python strings are immutable, so the
array-style "reverse all characters, then reverse each word" method cannot be
truly in place on a `str`. In Python, `" ".join(reversed(s.split()))` performs
the whitespace normalization and word reversal. In a language with a mutable
character array, the whole-string and per-word reversals reuse the opposite-end
swap directly

- Boats To Save People pairs the heaviest remaining person with the lightest when
  they fit. If they do not fit, the heaviest must travel alone, because no other
  remaining partner is lighter
- Minimize Maximum Pair Sum In Array pairs smallest with largest after sorting.
  Pairing a large value with another large value can only raise the maximum pair
  sum
- Find K Closest Elements starts with the whole sorted array and discards the
  farther endpoint until only `k` values remain. A tie discards the right end
  because the problem prefers smaller values
- 3Sum Closest keeps the closest total while steering toward the target. Four
  Sum adds one more fixed outer index, while the duplicate rules stay the same

Bag of Tokens sorts the token costs and tracks `left`, `right`, `power`, the
current `score`, and the largest score seen. Buy the cheapest remaining token
when affordable, gaining one score, and update `best`. When blocked but holding
a score point, sell the most expensive remaining token for the greatest power
recovery. Selling reduces the current score, so returning the final score is a
rejected shortcut; return `best`, which preserves the peak reached before a
later sale

Trapping Rain Water keeps `left_max` and `right_max`, the tallest walls seen from
the two ends, updating the chosen maximum with the current height before counting
water. When `left_max <= right_max`, the left position is settled because the
right side already supplies a wall at least as tall as its limiting left wall.
Add `left_max - height[left]` when positive, then advance `left`. Otherwise add
`right_max - height[right]` and advance `right`. A future taller wall can raise a
maximum, but it cannot change water already bounded by the lower known side

```text
height=[3, 0, 2, 0, 4]
left_max=3, right_max=4 -> settle from the left
height[1]=0             -> add 3 - 0 = 3
height[2]=2             -> add 3 - 2 = 1
height[3]=0             -> add 3 - 0 = 3
```

The three additions account for all seven trapped units. Each chosen position is
finalized once, which is why the scan remains linear

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
