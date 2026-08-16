# Prefix and Suffix Sums

A **prefix** is everything from the beginning through some boundary. For
`[3, -1, 4, 2]`, the prefix ending after the first three values is
`[3, -1, 4]`. A **prefix sum** stores that prefix's total.

A **suffix** is the matching idea from the other direction: everything from a
boundary through the end. These names matter because many array questions ask
about a range, a split, or "everything except here." If you recompute each part
from scratch, the same values are added again and again.

## One Leading Zero Removes the Boundary Case

Build a prefix array with one extra entry:

```text
nums      [  3 ][ -1 ][  4 ][  2 ]
index         0     1     2     3
prefix   [  0 ][  3 ][  2 ][  6 ][  8 ]
             ^ sum of zero values
```

Define `prefix[i]` as the sum of values strictly before index `i`. Then
`prefix[0] = 0`, and each new entry is
`prefix[i + 1] = prefix[i] + nums[i]`.

The sum from index `left` through `right`, including both ends, is:

```text
prefix[right + 1] - prefix[left]
```

The larger prefix contains the wanted range plus everything before `left`.
Subtracting the smaller prefix cancels that unwanted beginning.

```text
sum nums[1..3] = (-1) + 4 + 2
               = prefix[4] - prefix[1]
               = 8 - 3
               = 5
```

Using `prefix[right]` is the rejected lookup because it stops before `right`.
The extra leading zero is what makes `right + 1` correct even when `left = 0`.

```python
class NumArray:
    def __init__(self, nums: list[int]) -> None:
        self.prefix = [0]
        for value in nums:
            self.prefix.append(self.prefix[-1] + value)

    def sum_range(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


totals = NumArray([3, -1, 4, 2])
assert totals.sum_range(1, 3) == 5
assert totals.sum_range(0, 0) == 3
assert NumArray([7]).sum_range(0, 0) == 7
```

This is the direct solution to
[Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/).
Construction spends `O(n)` time and space once, then every query is `O(1)`.
That trade is useful only when there are repeated queries; for one total, a
single running variable is enough.

## Split Points Need Only a Running Side

At a split, storing both a prefix array and a suffix array often works, but it is
more memory than necessary. Compute the total once. During a left-to-right scan,
the left sum is a running prefix and the right sum is `total - left`.

For [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/), index
`i` is accepted when the sum strictly to its left equals the sum strictly to its
right:

```python
def pivot_index(nums: list[int]) -> int:
    total = sum(nums)
    left_sum = 0

    for index, value in enumerate(nums):
        right_sum = total - left_sum - value
        if left_sum == right_sum:
            return index
        left_sum += value

    return -1


assert pivot_index([1, 7, 3, 6, 5, 6]) == 3
assert pivot_index([2, 1, -1]) == 0
assert pivot_index([]) == -1
```

The current `value` is subtracted because neither side includes the pivot. At
index `0` in `[2, 1, -1]`, the empty left side has sum zero and the right side
also has sum zero, so rejecting empty sides would miss a valid pivot.

The same running-split idea handles
[Number of Ways to Split Array](https://leetcode.com/problems/number-of-ways-to-split-array/)
and [Maximum Score After Splitting a String](https://leetcode.com/problems/maximum-score-after-splitting-a-string/).
The only extra rule is whether the problem allows a split at the ends. If both
parts must be nonempty, stop before the last index.

[Left and Right Sum Differences](https://leetcode.com/problems/left-and-right-sum-differences/)
asks for an answer at every index, so either full prefix/suffix arrays or one
running left total plus a decreasing right total works.

## Prefix From the Left, Suffix From the Right

[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
uses multiplication rather than addition, but the boundary idea is identical.
For each index, multiply everything to its left by everything to its right.

The answer array can first store left products. A backward pass carries one
running suffix product, so no second array is needed:

```python
def product_except_self(nums: list[int]) -> list[int]:
    answer = [1] * len(nums)

    prefix_product = 1
    for index, value in enumerate(nums):
        answer[index] = prefix_product
        prefix_product *= value

    suffix_product = 1
    for index in range(len(nums) - 1, -1, -1):
        answer[index] *= suffix_product
        suffix_product *= nums[index]

    return answer


assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
assert product_except_self([0, 1, 2, 3]) == [6, 0, 0, 0]
assert product_except_self([5]) == [1]
assert product_except_self([]) == []
```

The current value is deliberately rejected from both running products. It joins
the prefix only after `answer[index]` is written, and it joins the suffix only
after that answer is multiplied. That ordering is the entire "except self"
condition.

## Turn a Subarray Sum Into a Prefix Lookup

A **subarray** is one contiguous slice. Let `running` be the prefix sum through
the current index. If a previous prefix had sum `running - k`, then the values
between that earlier boundary and the current boundary sum to `k`:

```text
current prefix - earlier prefix = wanted subarray
running        - (running - k)  = k
```

This turns "which earlier starting points work?" into one hash-map lookup. The
map stores `prefix_sum -> number of times seen`, because duplicate prefix sums
represent different starting boundaries and each one creates a different
subarray.

## Worked Example: [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

Given an integer array `nums` and integer `k`, return the number of contiguous,
nonempty subarrays whose values sum to `k`. Values may be negative, so the
running sum can rise, fall, or repeat.

**Input**: `nums`, a `list[int]` where `1 <= len(nums) <= 2 * 10^4` and each
value satisfies `-1000 <= nums[i] <= 1000`, and `k`, an `int` target sum with
`-10^7 <= k <= 10^7`

**Output**: an `int`, the number of contiguous nonempty slices of `nums` whose
values add up to exactly `k`. Slices that overlap are counted separately, so the
same index may belong to many counted subarrays, and the answer is `0` when no
slice reaches `k`

Checking every start and extending every end is `O(n²)` because many overlapping
ranges are summed repeatedly. Two moving boundaries do not fix that for negative
values: adding `-5` can make a too-large total smaller, so there is no safe rule
that says which boundary must move. Prefix sums avoid that assumption entirely.

Seed the map with `{0: 1}`. This represents one empty prefix before index `0`,
which lets a subarray starting at index `0` be counted by the same lookup as
every other subarray.

> "At each index I know the current prefix sum. A subarray ending here sums to
> `k` for every earlier prefix equal to `running - k`, so I will add that stored
> frequency before recording the current prefix."

Therefore,

1. Start `prefix_count` as `{0: 1}`, `running` at `0`, and `answer` at `0`. The
   seeded zero is the empty prefix before index `0`, and without it every
   subarray that starts at the very beginning would go uncounted
2. Walk the array left to right, adding each value to `running`, so `running` is
   always the prefix sum through the current index and no earlier boundary has to
   be re-added
3. Compute `needed = running - k`, which is the prefix sum an earlier boundary
   must have had for the values between it and here to total exactly `k`
4. Add `prefix_count.get(needed, 0)` to `answer`, taking the stored frequency
   rather than a yes-or-no answer, because each earlier boundary with that same
   prefix sum starts a different valid subarray. A missing key contributes `0`,
   which is the rejection case
5. Record the current prefix by incrementing `prefix_count[running]`, and do it
   only after the lookup. Recording first would let `running` match its own
   `needed` when `k` is `0` and count the empty subarray ending here
6. Return `answer` once the scan finishes. An empty array never enters the loop,
   so the seeded map is never consulted and the count stays `0`

```python
def subarray_sum(nums: list[int], k: int) -> int:
    prefix_count: dict[int, int] = {0: 1}
    running = 0
    answer = 0

    for value in nums:
        running += value
        needed = running - k
        answer += prefix_count.get(needed, 0)
        prefix_count[running] = prefix_count.get(running, 0) + 1

    return answer


assert subarray_sum([1, 1, 1], 2) == 2
assert subarray_sum([1, -1, 0], 0) == 3
assert subarray_sum([], 0) == 0
assert subarray_sum([5], 5) == 1
assert subarray_sum([5], 2) == 0
```

- **Time Complexity:** `O(n)` average time, where `n` is the array length,
  because each value performs one average-constant-time lookup and update.
- **Space Complexity:** `O(n)` auxiliary space, because all `n + 1` prefix
  boundaries may have different sums.

The negative example exercises repeated and falling prefixes:

```text
start            running=0   count={0: 1}             answer=0
value=1          running=1   need=1 -> REJECT         add prefix 1
value=-1         running=0   need=0 -> 1 match        answer=1, count[0]=2
value=0          running=0   need=0 -> 2 matches      answer=3, count[0]=3
```

At the first step, the needed prefix `1` has not appeared before the current
boundary, so the lookup is correctly rejected. Recording `running` after the
lookup also prevents an empty subarray ending at the current boundary from being
counted.

## Counts, Earliest Indices, and Remainders

The map value changes with the question:

- Store a **count** when the problem asks how many subarrays work, as in
  Subarray Sum Equals K.
- Store the **earliest index** when the problem asks for the longest subarray.
  A later occurrence of the same prefix is rejected because the earlier index
  always creates an equal or longer range. This solves
  [Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)
  and, after treating `0` as `-1`,
  [Contiguous Array](https://leetcode.com/problems/contiguous-array/).

Some problems ask whether a sum is divisible by `k`. The **remainder** `x % k`
is what remains after taking out whole groups of `k`. Two prefix sums with the
same remainder differ by a multiple of `k`, so the subarray between them is
divisible by `k`.

- [Subarrays Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)
  stores a frequency of each remainder because it counts every valid range.
- [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)
  stores the first index of each remainder because it needs a range of length at
  least two. A repeated remainder one position later is rejected as too short.

Python's `%` already produces a consistent nonnegative remainder for positive
`k`. In languages where negative totals can produce negative remainders,
normalize with `(remainder + k) % k`.

## Two-Dimensional Prefix Sums

For repeated rectangle queries, a 2D prefix table stores the sum above and to
the left of every boundary. To get one rectangle, take the large prefix, remove
the area above it, remove the area to its left, then add back the top-left corner
because it was removed twice. This add-back is called **inclusion-exclusion**.

```text
rectangle sum = whole prefix - above - left + removed-twice corner
```

That is the complete idea behind
[Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/).
The extra zero row and zero column play the same role as the leading zero in the
1D array: rectangle edges need no special branch.

## Time and Space Complexity

| Approach                          | Time                                                                                        | Space                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Re-sum every range                | `O(qn)`: each of `q` queries may scan `n` values again                                      | `O(1)` auxiliary: no precomputed sums are stored                        |
| Build a prefix array, then query  | `O(n + q)`: construction scans `n` values and each query is `O(1)`                          | `O(n)`: one prefix entry is stored per boundary                         |
| Running prefix with a hash map    | `O(n)` average: every boundary performs one constant-average-time lookup                    | `O(n)`: up to `n + 1` distinct prefix states may be stored              |
| Prefix and running suffix product | `O(n)`: one forward and one backward pass touch each value                                  | `O(1)` auxiliary excluding the required `O(n)` answer array             |
| 2D prefix table                   | `O(rows * columns)` to build and `O(1)` per query: four table entries determine a rectangle | `O(rows * columns)`: one cumulative value is stored per matrix boundary |

## Summary

- A prefix sum stores the total before a boundary. With `prefix[0] = 0`, the
  inclusive range `left..right` is `prefix[right + 1] - prefix[left]`.
- Prefix arrays spend `O(n)` preprocessing time and space to make repeated range
  queries `O(1)`. A single running prefix is enough when answers are produced in
  one scan.
- At a split point, `right_sum = total - left_sum - current_value`, because the
  current index belongs to neither side.
- Prefix and suffix passes combine information from both sides without division,
  which is why Product of Array Except Self still works when zeros appear.
- A subarray ending at the current boundary sums to `k` when an earlier prefix
  equals `running - k`; store counts for how many answers and earliest indices
  for the longest answer.
- Negative values break any boundary rule based only on a sum growing or
  shrinking, but they do not break prefix subtraction.
- Equal prefix remainders mark a difference divisible by `k`, while a 2D prefix
  table answers rectangles by subtracting two regions and adding back their
  overlap.

## Interview Checklist

```text
Am I answering repeated ranges, one running scan, or every split point?
Does prefix[i] include nums[i], or does it stop before index i?
For an inclusive range, am I using prefix[right + 1] - prefix[left]?
Should the map store a frequency or the earliest index?
Did I seed the empty prefix so ranges beginning at index 0 can be found?
Am I recording the current prefix only after looking for an earlier one?
Can negative values invalidate a moving-boundary shortcut?
For a remainder problem, is there also a minimum-length requirement?
In 2D, did I add back the corner that was subtracted twice?
```
