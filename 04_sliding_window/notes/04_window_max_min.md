# Window Maximums And Minimums

A running sum survives a slide because the leaving value can be subtracted. A
running maximum does not. If the maximum leaves, one number cannot tell you
which remaining value should replace it.

A **monotonic deque** keeps that replacement order. It stores candidates whose
values move in one direction from front to back:

- A **decreasing deque** keeps the maximum at its front.
- An **increasing deque** keeps the minimum at its front.

The deque is not sorted afterward. Each arrival removes older candidates it
makes permanently useless, then joins the back. The front is the current answer,
and the entries behind it are the successors waiting for that answer to expire.

This is related to the
[monotonic stack](../../03_stacks_and_queues/notes/03_monotonic_stack.md), but a
window adds a second exit. Candidates leave from the back when dominated and
from the front when no longer eligible.

## Why A Later Value Dominates An Earlier One

Suppose `i < j` and `nums[i] <= nums[j]`. For a future maximum window, index
`i` is **dominated** by `j`:

- Any future contiguous window containing the older `i` and reaching `j` also
  contains the newer `j`.
- The newer value is at least as large and survives longer because it lies
  farther right.

Therefore `i` can never become the maximum again and may be deleted now. Repeating
that deletion leaves decreasing values from front to back.

For a minimum, reverse the comparison. A later value no larger than an earlier
one dominates it, leaving increasing values.

## Store Positions When Eligibility Depends On Position

The deque often stores **indices**, not bare values. An index answers both
questions the algorithm asks:

1. What is the candidate's value? Read `nums[dq[0]]`.
2. Is the candidate outside the window? Compare `dq[0]` with the boundary.

A deque of values can work when the outgoing value is handed to you and duplicate
copies are retained carefully. It cannot recover an index for expiry, a length,
or a coordinate gap. Indices are therefore the safer interview default. If the
ordering key is derived, store an index or a tuple containing both the key and
the position.

## Fixed-Width Maximum And Minimum

Sliding Window Maximum asks for the maximum of every width-`k` window. Rescanning
each window costs `O(n * k)`. A decreasing deque reuses the candidates that
survive from the previous window.

```python
from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    dq: deque[int] = deque()
    answer: list[int] = []

    for right, value in enumerate(nums):
        window_left = right - k + 1
        while dq and dq[0] < window_left:
            dq.popleft()

        while dq and nums[dq[-1]] <= value:
            dq.pop()
        dq.append(right)

        if window_left >= 0:
            answer.append(nums[dq[0]])

    return answer
```

Three lines carry the technique:

- Front removals use position: `dq[0] < window_left` means the candidate is
  stale and must be removed before the answer is read.
- Back removals use value: `nums[dq[-1]] <= value` means the arriving value
  dominates that candidate. Using `<=` keeps the newer copy on ties because it
  expires later.
- Output begins only when `window_left >= 0`, because earlier prefixes contain
  fewer than `k` elements.

For `nums = [1, 3, -1, -3, 5]` and `k = 3`:

```text
right=0 value= 1   dq indices=[0]       no full window
right=1 value= 3   DOMINATE index 0     dq=[1] values=[3]
right=2 value=-1   dq=[1,2]             output 3
right=3 value=-3   dq=[1,2,3]           output 3
right=4 value= 5   EXPIRE index 1
                    DOMINATE index 3, then index 2
                    dq=[4]              output 5
```

Index 1 is a **stale deque entry** at `right = 4`. Its value is still larger than
the other stored values, so domination would not remove it; only the boundary
check can. Reading the front before expiry would output 3 for a window that no
longer contains index 1.

When `k = 1`, the previous index expires on every step and each new value becomes
the only candidate, so the output equals the input. Sliding Window Minimum uses
the same code with the back comparison reversed to `>=`.

## Three Ways A Front Becomes Too Old

The domination rule at the back stays the same. What changes across problems is
how the front loses eligibility:

| Window boundary       | Front-removal rule                                                                         | Why                                                                         |
| --------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| Fixed width `k`       | `dq[0] < right - k + 1`                                                                    | The index lies before the current window's first position.                  |
| Moving `left` pointer | Pop when `dq[0] == left` before advancing `left`, or remove every `dq[0] < left` afterward | The validity condition, not a fixed width, decides which position leaves.   |
| Coordinate distance   | `x[right] - x[dq[0]] > k`                                                                  | Eligibility is measured by coordinates rather than by array-index distance. |

Do not copy a fixed-width expiry expression into a variable or coordinate
window. The back still means “dominated,” but the front must be tied to the
actual definition of “outside.”

## Worked Example: [Longest Continuous Subarray With Absolute Difference At Most Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-difference-less-than-or-equal-to-limit/)

Given an integer array and `limit`, return the longest contiguous subarray whose
maximum minus minimum is at most `limit`.

The width is not given, so this is a
[variable window](02_variable_size_window.md). Growing can only keep or widen
the spread, while shrinking can only keep or narrow it. The missing state is an
efficient maximum and minimum.

Scanning the indices from `left` through `right` for a new maximum and minimum
after every move is correct and quadratic in the worst case. Instead, keep one
decreasing deque for the maximum and one increasing deque for the minimum.

> “Both deques store indices for the same `[left, right]` window. I will feed
> `right` to both, shrink while their front values differ by more than `limit`,
> and retire a front only when its index is exactly the position leaving.”

```python
from collections import deque


def longest_subarray(nums: list[int], limit: int) -> int:
    max_dq: deque[int] = deque()
    min_dq: deque[int] = deque()
    left = 0
    best = 0

    for right, value in enumerate(nums):
        while max_dq and nums[max_dq[-1]] <= value:
            max_dq.pop()
        max_dq.append(right)

        while min_dq and nums[min_dq[-1]] >= value:
            min_dq.pop()
        min_dq.append(right)

        while nums[max_dq[0]] - nums[min_dq[0]] > limit:
            if max_dq[0] == left:
                max_dq.popleft()
            if min_dq[0] == left:
                min_dq.popleft()
            left += 1

        best = max(best, right - left + 1)

    return best
```

The two front checks are written as separate `if` statements because each deque
owns its expiry independently. In this exact loop an invalid window has
different maximum and minimum positions, so an `elif` also works, but two checks
remain correct when the pattern is reused with another condition. The answer is
recorded after the shrink loop because this is a longest-valid problem.

Trace `nums = [8, 2, 4, 7]` and `limit = 4`:

```text
right=0 value=8   max=[8]      min=[8]      left=0  best=1
right=1 value=2   max=[8,2]    min=[2]
                  spread 6 is INVALID
                  left=0 holds max 8 -> remove it; min stays
                  window=[2]                left=1  best=1
right=2 value=4   max drops dominated 2
                  max=[4]      min=[2,4]    spread 2  best=2
right=3 value=7   max drops dominated 4
                  max=[7]      min=[2,4,7]  spread 5 is INVALID
                  left=1 holds min 2 -> remove it; max stays
                  window=[4,7]              left=2  best=2
```

The invalid windows are repaired by different deques. At `right = 1` the old
maximum expires; at `right = 3` the old minimum expires. Popping both fronts on
either shrink would discard an extreme that remains inside the window.

- **Time Complexity:** `O(n)`, because each of the `n` indices enters each deque
  once and leaves at most once, while `left` also advances at most `n` times.
- **Space Complexity:** `O(n)` in the worst case, because a variable window may
  span the entire array and a monotonic input can leave one deque holding every
  index.

Continuous Subarrays uses the same two deques with `limit = 2`, but counts all
valid windows. After repair, add `right - left + 1` because every suffix ending
at `right` also has spread at most 2.

## Negative Values Need Prefix-Sum Boundaries

Shortest Subarray With Sum At Least K allows negative values. The ordinary
positive-number shrink fails because removing a negative value can increase the
sum, so “the first invalid shrink means stop” is no longer true.

Use the [prefix-sum definition](../../01_arrays_and_hashing/notes/03_prefix_suffix_sums.md):
`prefix[j] - prefix[i]` is the sum of `nums[i : j]`. For each end boundary `j`,
we want the latest start `i` whose difference is at least `k`, because a later
start gives a shorter subarray.

Keep prefix indices in increasing order of prefix value. Two removal rules now
apply:

- From the front, while `prefix[j] - prefix[dq[0]] >= k`, record that length and
  consume the start. A later end paired with the same start would only be longer.
- From the back, remove any start whose prefix value is at least the current
  prefix. The current boundary is later and no larger, so it gives every future
  end a larger sum and a shorter length.

```python
from collections import deque


def shortest_subarray(nums: list[int], k: int) -> int:
    prefix = [0]
    for value in nums:
        prefix.append(prefix[-1] + value)

    dq: deque[int] = deque()
    best = len(nums) + 1

    for end, total in enumerate(prefix):
        while dq and total - prefix[dq[0]] >= k:
            best = min(best, end - dq.popleft())

        while dq and prefix[dq[-1]] >= total:
            dq.pop()

        dq.append(end)

    return -1 if best == len(nums) + 1 else best
```

For `nums = [2, -1, 2, 3]` and `k = 4`, the prefix values are
`[0, 2, 1, 3, 6]`:

```text
end=0 total=0   deque prefixes=[0]
end=1 total=2   deque prefixes=[0,2]
end=2 total=1   BACK DROP prefix 2; prefix 1 is later and smaller
                  deque prefixes=[0,1]
end=3 total=3   deque prefixes=[0,1,3]
end=4 total=6   FRONT prefix 0 qualifies -> length 4
                  FRONT prefix 1 qualifies -> length 2, improve
                  prefix 3 does not qualify; stop
answer=2, the subarray [2,3]
```

The negative `-1` makes the prefix fall from 2 to 1, creating the domination
step a positive-only window cannot represent. Each prefix is still appended once
and removed at most once, so both inner loops total `O(n)` work.

## Coordinate Windows And Mixed State

Max Value of Equation gives points sorted by `x`. For `i < j`, rewrite
`yi + yj + |xi - xj|` as `(yi - xi) + (yj + xj)`. For each right point, the
deque keeps the largest `y - x` among earlier points satisfying
`xj - xi <= k`.

```python
from collections import deque


def find_max_value_of_equation(points: list[list[int]], k: int) -> int:
    dq: deque[int] = deque()
    best = -(10**18)

    for right, (x, y) in enumerate(points):
        while dq and x - points[dq[0]][0] > k:
            dq.popleft()

        if dq:
            left = dq[0]
            best = max(best, points[left][1] - points[left][0] + x + y)

        while dq and points[dq[-1]][1] - points[dq[-1]][0] <= y - x:
            dq.pop()
        dq.append(right)

    return best
```

The query happens before appending `right` so a point cannot pair with itself.
Several earlier points may cross the coordinate limit at once, so coordinate
expiry uses a `while`.

Maximum Number of Robots Within Budget combines deque state with a running sum.
For `[left, right]`, its cost is the maximum charge time plus the window width
times the sum of running costs. The max deque supplies the first term; a running
total supplies the second. During every shrink, expire the max index if it is
leaving, subtract its running cost, and advance `left`. The window may become
empty when one robot alone exceeds the budget, so guard the cost test with a
nonempty deque.

```python
from collections import deque


def maximum_robots(
    charge_times: list[int], running_costs: list[int], budget: int
) -> int:
    max_dq: deque[int] = deque()
    left = 0
    running_sum = 0
    best = 0

    for right, charge in enumerate(charge_times):
        while max_dq and charge_times[max_dq[-1]] <= charge:
            max_dq.pop()
        max_dq.append(right)
        running_sum += running_costs[right]

        while (
            max_dq
            and charge_times[max_dq[0]]
            + (right - left + 1) * running_sum
            > budget
        ):
            if max_dq[0] == left:
                max_dq.popleft()
            running_sum -= running_costs[left]
            left += 1

        best = max(best, right - left + 1)

    return best
```

## Counting Fixed Bounds Without A Deque

Count Subarrays With Fixed Bounds appears in this workbook section because it
tracks a window's allowed minimum and maximum, but a deque is unnecessary. The
problem fixes the only permitted extremes as `min_k` and `max_k`.

Track the most recent index of each required bound and the most recent value
outside the allowed range. For each `right`, a valid start must be after the bad
index and no later than both required-bound indices:

```python
def count_subarrays(nums: list[int], min_k: int, max_k: int) -> int:
    last_bad = -1
    last_min = -1
    last_max = -1
    total = 0

    for right, value in enumerate(nums):
        if value < min_k or value > max_k:
            last_bad = right
        if value == min_k:
            last_min = right
        if value == max_k:
            last_max = right

        total += max(0, min(last_min, last_max) - last_bad)

    return total
```

The formula counts start indices from `last_bad + 1` through the earlier of
`last_min` and `last_max`. If either bound has not appeared since the last bad
value, the contribution is zero.

## Time and Space Complexity

Let `n` be the input length and `k` a fixed width or coordinate budget where
the problem defines one.

| Technique                         | Time                                                                           | Space                                                             |
| --------------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| Rescan every fixed window extreme | `O(n * k)`: each window searches up to `k` values again                        | `O(1)` auxiliary space                                            |
| Fixed-width monotonic deque       | `O(n)`: each index is appended once and removed at most once                   | `O(k)` auxiliary space, plus `O(n - k + 1)` for the returned list |
| Variable max/min deques           | `O(n)`: all domination, expiry, and left-pointer moves total linear work       | `O(n)` worst case because the valid window may be the whole array |
| Prefix-sum monotonic deque        | `O(n)`: each of the `n + 1` prefix indices enters once and leaves at most once | `O(n)` for the prefix array and deque                             |
| Last-position fixed-bounds count  | `O(n)`: each right edge updates three positions and one formula                | `O(1)`: only the three last positions and total are stored        |

## Summary

- A **monotonic deque** keeps successor candidates in value order. A decreasing
  deque exposes the maximum; an increasing deque exposes the minimum.
- Candidates leave from the back when a later value dominates them and from the
  front when the problem's window rule makes them ineligible.
- Store indices when expiry, distance, length, or coordinates matter. A bare
  value cannot prove whether a duplicate copy is inside or outside the window.
- The three normal expiry rules are fixed index width, a moving `left` pointer,
  and coordinate distance. Match the front check to the problem's boundary.
- Two deques maintain a window's spread in `O(1)` amortized work per move. Count
  all valid spread windows by adding `right - left + 1` after repair.
- Negative values invalidate ordinary shortest-sum shrinking. Prefix sums plus
  an increasing deque compare all useful start boundaries without assuming the
  sum moves monotonically.
- Count Subarrays With Fixed Bounds needs only last positions because the
  required minimum and maximum are known values, not arbitrary live extremes.
- Every deque version is linear because each index is appended once and removed
  at most once, even when one arrival pops many candidates.

## Interview Checklist

```text
Do I need a window sum/count, or an extreme that cannot be undone?
Should the deque decrease for a maximum or increase for a minimum?
What does one deque entry store, and can it prove when the candidate expires?
What dominates an entry at the back?
What retires the front: fixed width, left pointer, coordinate distance, or use?
Do stale fronts get removed before I read the answer?
If two deques share a window, can the same index leave both?
Do negative values make ordinary sum shrinking unsafe?
For prefix sums, do qualifying starts leave the front and dominated starts leave the back?
Can the window become empty, requiring a guard before reading dq[0]?
Can I justify O(n) by counting one append and at most one removal per index?
```
