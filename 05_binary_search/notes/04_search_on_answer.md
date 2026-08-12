# Search on the Answer

**Search on the answer** applies binary search to the values an answer could
take instead of to indices in an array. The answer might be an eating speed, a
ship capacity, a waiting time, or a distance. You never build a list of those
candidates. You keep only the lowest and highest possible values.

For each candidate `x`, a **feasibility predicate** answers whether `x` is good
enough. The predicate must be **monotonic**:

```text
candidate    1   2   3   4   5   6   7
feasible     F   F   F   T   T   T   T
                         ^
                  minimum feasible
```

Once one candidate works, every larger candidate must work too. That makes the
answer the first true position in a virtual ordered range, which is the
[boundary search](02_boundary_search.md) from the previous note with values in
place of indices.

## Recognizing the Pattern

The strongest signals are:

- “Find the minimum `x` such that...” or “find the maximum `x` such that...”
- **Minimize the maximum**, such as the largest sum among array pieces.
- **Maximize the minimum**, such as the smallest distance between placed balls.
- Find the kth smallest value without constructing and sorting every possible
  value.
- Checking one candidate is a simple pass, while solving for the best candidate
  directly is difficult.

The predicate is the real algorithm. Before writing the binary-search loop,
state:

1. What one candidate means and what its units are.
2. How to test it.
3. Why passing at `x` implies passing at every larger value, or the mirrored
   rule for a maximum-feasible search.
4. Why the lower and upper bounds cannot exclude the answer.

An “exactly” predicate is often a warning. For example, “Koko finishes in exactly
8 hours” may be true for several speeds and then become false again. “Koko
finishes in at most 8 hours” stays true as speed increases, so it has one
searchable boundary.

## Worked Example: [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

Koko faces several piles and chooses one integer eating speed, measured in
bananas per hour. During an hour she eats from only one pile. A pile of `p`
bananas takes `ceil(p / speed)` hours, and the goal is the smallest speed that
finishes all piles within `h` hours.

Trying speed 1, then 2, then 3 is correct because faster eating never takes more
hours. It is also too slow because the largest pile may contain `10^9` bananas,
so there may be a billion candidates. The same monotonicity that makes the scan
correct lets binary search skip almost all of them.

For one pile, Python can compute ceiling division without floats:

```text
ceil(p / speed) = (p + speed - 1) // speed
```

Python integers do not overflow. In a fixed-width language, use
`p // speed + (p % speed != 0)` when `p + speed - 1` could overflow.

The smallest legal speed is 1. The largest pile is a sufficient upper bound
because at `max(piles)` every pile takes one hour, and the problem guarantees
`h >= len(piles)`. Therefore, the right endpoint is known feasible.

> “My predicate is whether the total ceiling-divided hours are at most `h`.
> Increasing speed cannot increase any pile's hours, so feasibility changes from
> false to true once. I will keep the minimum feasible speed inside an inclusive
> interval.”

```python
def min_eating_speed(piles: list[int], h: int) -> int:
    def feasible(speed: int) -> bool:
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed
        return hours <= h

    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

The bounds are inclusive candidates, and the invariant is that the minimum
feasible answer remains in `[left, right]`. The right endpoint is always known
feasible.

- A feasible `mid` might be the first feasible value, so `right = mid` keeps it.
- An infeasible `mid` proves every smaller speed is also infeasible, so
  `left = mid + 1` safely discards that entire block.
- When the bounds meet, the invariant and the known-feasible right endpoint prove
  the returned value is feasible. Everything below it has been rejected.

For `piles = [3, 6, 7, 11]` and `h = 8`:

```text
left=1 right=11 mid=6  hours=6   feasible   -> right=6
left=1 right=6  mid=3  hours=10  rejected   -> left=4
left=4 right=6  mid=5  hours=8   feasible   -> right=5
left=4 right=5  mid=4  hours=8   feasible   -> right=4
return 4
```

The second probe is the rejected candidate to study. Speed 3 needs 10 hours, so
speeds 1 and 2 cannot work either. One calculation removes three candidates.
The first probe removes speeds 7 through 11 for a different reason: they work,
but none can be the smallest working speed once 6 is known to work.

The boundary can sit at either extreme. `piles = [1, 1], h = 2` returns the low
bound 1. `piles = [3, 6, 7, 11], h = 4` returns the high bound 11 because every
pile must finish in one hour. These cases verify that neither endpoint is
treated as an excluded sentinel.

- **Time Complexity:** `O(n log M)`, where `n` is the number of piles and `M` is
  the largest pile, because each of `O(log M)` candidates requires one `O(n)`
  feasibility pass.
- **Space Complexity:** `O(1)` auxiliary space, because the predicate stores only
  a running hour count.

## The Minimum-Feasible Family

Many problems use Koko's exact loop. Only the candidate, bounds, and predicate
change:

| Problem                                                                                                                   | Candidate and inclusive bounds                            | Feasibility check                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)         | Capacity from `max(weights)` to `sum(weights)`            | Fill days greedily in order; the capacity works when at most `days` groups are needed                             |
| [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)                                         | Maximum allowed piece sum from `max(nums)` to `sum(nums)` | Start a new contiguous piece before the running sum would exceed the cap; at most `k` pieces means the cap works  |
| [Minimum Speed to Arrive on Time](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/)                         | Speed from 1 to the problem's limit `10^7`                | Round every leg except the last up to a full hour and check total time `<= hour`                                  |
| [Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) | Divisor from 1 to `max(nums)`                             | Sum ceiling divisions and check whether the total is at most `threshold`                                          |
| [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)     | Day from `min(bloom_day)` to `max(bloom_day)`             | Count adjacent runs of `k` flowers whose bloom day is at most the candidate; at least `m` bouquets means it works |

The shipping and splitting predicates are the same greedy grouping pass. The
lower bound is `max(...)` because a group must contain the largest single item.
The upper bound `sum(...)` places everything in one group and is therefore known
feasible.

```python
def ship_feasible(weights: list[int], days: int, capacity: int) -> bool:
    used_days, load = 1, 0
    for weight in weights:
        if load + weight > capacity:
            used_days += 1
            load = 0
        load += weight
    return used_days <= days


def bouquet_feasible(
    bloom_day: list[int], bouquets: int, size: int, day: int
) -> bool:
    made, adjacent = 0, 0
    for bloom in bloom_day:
        if bloom <= day:
            adjacent += 1
            if adjacent == size:
                made += 1
                adjacent = 0
        else:
            adjacent = 0
    return made >= bouquets
```

Resetting `adjacent` on an unbloomed flower is essential because bouquets require
consecutive flowers. Before searching, the bouquet problem must reject
`bouquets * size > len(bloom_day)` as impossible.

For Minimum Speed to Arrive on Time, the first `n - 1` legs each consume at least
one full hour regardless of speed. If `hour <= n - 1`, no answer exists and the
function returns `-1` before searching. The final leg is not rounded, which is
the detail that distinguishes this predicate from Koko.

## Maximum-Feasible Search

[Sqrt(x)](https://leetcode.com/problems/sqrtx/),
[Arranging Coins](https://leetcode.com/problems/arranging-coins/), and
[Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/)
want the **largest** candidate that works:

```text
candidate    0   1   2   3   4   5
feasible     T   T   T   T   F   F
                         ^
                    last True
```

Now a feasible midpoint stays on the left. The midpoint must round upward,
because with adjacent bounds 3 and 4, a rounded-down midpoint of 3 followed by
`left = mid` would make no progress.

```python
def my_sqrt(x: int) -> int:
    left, right = 0, x
    while left < right:
        mid = left + (right - left + 1) // 2
        if mid <= x // mid:
            left = mid
        else:
            right = mid - 1
    return left
```

The comparison `mid <= x // mid` avoids overflow from `mid * mid` in a
fixed-width language. The invariant is that the largest feasible answer remains
inside inclusive `[left, right]`, with `left` known feasible. On success,
`left = mid` keeps the candidate. On failure, `right = mid - 1` discards it and
every larger value.

Arranging Coins changes the predicate to whether
`rows * (rows + 1) // 2 <= n`. Magnetic Force sorts basket positions, then tests
a gap by placing the first ball at the leftmost basket and every later ball at
the earliest basket at least `gap` away. Choosing an earlier valid basket leaves
at least as much room for every later ball, so this greedy test is exact.

For Magnetic Force, the bounds are 1 through
`position[-1] - position[0]` after sorting. A feasible gap moves `left` up, and
an infeasible gap moves `right` down. The sort costs `O(p log p)` time and up to
`O(p)` auxiliary space in Python for `p` positions; the later search costs
`O(p log D)` for position span `D`.

## Searching a Value by Counting

The kth-smallest problems use a candidate value `x` and the predicate:

```text
count(values <= x) >= k
```

The predicate is monotonic because raising `x` can add qualifying values but can
never remove one.

[Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
searches from the top-left value to the bottom-right value. One staircase pass
counts entries at most `x` in `O(n)` for an `n x n` matrix:

```python
def kth_smallest(matrix: list[list[int]], k: int) -> int:
    n = len(matrix)

    def count_at_most(value: int) -> int:
        count, col = 0, n - 1
        for row in matrix:
            while col >= 0 and row[col] > value:
                col -= 1
            count += col + 1
        return count

    left, right = matrix[0][0], matrix[-1][-1]
    while left < right:
        mid = left + (right - left) // 2
        if count_at_most(mid) >= k:
            right = mid
        else:
            left = mid + 1
    return left
```

The column pointer is not reset for each row. Since columns increase downward,
the last qualifying column can only stay put or move left, so the whole count
uses `n` row steps and at most `n` column moves.

The returned candidate is guaranteed to be a matrix value even though a tested
`mid` may not be. If the smallest value whose count reaches `k` were absent,
the previous integer would have the same count and would be a smaller feasible
answer, which is a contradiction.

The other counting problems change only how `count_at_most(mid)` is computed:

- [Kth Smallest Number in Multiplication Table](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/)
  adds `min(mid // row, n)` for each row because row `r` contains
  `r, 2r, 3r, ...`.
- [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
  searches values 1 through `n`. If more than `mid` input values are
  `<= mid`, the pigeonhole principle places the duplicate at or below `mid`.
  This version does not modify the array and uses constant auxiliary space.
- [Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/)
  sorts the numbers and searches distances from 0 through
  `nums[-1] - nums[0]`. A same-direction window counts pairs with distance
  `<= mid`: for every `right`, advance `left` until the window fits, then add
  `right - left` pairs.

For pair distance, sorting costs `O(n log n)` time and up to `O(n)` auxiliary
space in Python. Each count is `O(n)` because both pointers move only forward,
so the complete search is `O(n log D)` after sorting for distance range `D`.

## Searching for a Partition

[Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
searches a cut position rather than the median value. Search the shorter array
`a`. If its cut puts `i` values on the left, the cut in `b` is forced to be
`j = half - i` so the combined left side has the required size.

The partition is correct when both cross-boundary inequalities hold:

```text
a_left <= b_right
b_left <= a_right
```

If `a_left > b_right`, the cut in `a` is too far right. If
`b_left > a_right`, it is too far left.

```python
def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    a, b = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
    total = len(a) + len(b)
    half = (total + 1) // 2
    left, right = 0, len(a)

    while left <= right:
        i = left + (right - left) // 2
        j = half - i

        a_left = a[i - 1] if i > 0 else float("-inf")
        a_right = a[i] if i < len(a) else float("inf")
        b_left = b[j - 1] if j > 0 else float("-inf")
        b_right = b[j] if j < len(b) else float("inf")

        if a_left > b_right:
            right = i - 1
        elif b_left > a_right:
            left = i + 1
        else:
            if total % 2 == 1:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2

    raise ValueError("inputs must be sorted and not both empty")
```

The infinities represent a missing value beyond an end and keep it from winning
the wrong `max` or `min`. Searching the shorter array guarantees the cut in the
longer array stays valid and gives `O(log min(m, n))` time with `O(1)`
auxiliary space.

## Time and Space Complexity

Let `R` be the number of integer candidates in the searched answer range.

| Approach                               | Time                                                                               | Space                                                       |
| -------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Search with an `O(n)` feasibility pass | `O(n log R)`: the range halves `O(log R)` times and each candidate scans `n` items | `O(1)` auxiliary when the predicate keeps only counters     |
| Scan every candidate                   | `O(nR)`: each of the `R` values triggers a full `n`-item check                     | `O(1)` auxiliary because it can reuse the same predicate    |
| Kth value in an `n x n` sorted matrix  | `O(n log R)`: each value probe uses an `O(n)` staircase count                      | `O(1)` auxiliary because the matrix is only read            |
| Sort all matrix values                 | `O(n² log n)`: all `n²` entries are ordered to return one value                    | `O(n²)`: flattening duplicates the entire matrix            |
| Median partition                       | `O(log min(m, n))`: only cuts in the shorter array are searched                    | `O(1)`: four boundary values and two cut indices are stored |

The reusable formula is `O(log R)` multiplied by the cost of one predicate call.
`R` is a value range, not necessarily the input length.

## Summary

- **Search on the answer** binary-searches a numeric candidate range and uses a
  monotonic predicate to grade one candidate at a time.
- A minimum-feasible search keeps the answer in inclusive `[left, right]`, uses a
  lower midpoint, keeps success with `right = mid`, and rejects failure with
  `left = mid + 1`.
- A maximum-feasible search uses an upper midpoint, keeps success with
  `left = mid`, and rejects failure with `right = mid - 1`.
- Bounds are part of the proof. The low end must be legal, the high end must not
  exclude the answer, and a loop that returns without validation needs a known
  feasible endpoint or an earlier impossible-case check.
- Integer ceiling division avoids float rounding, and overflow-safe midpoint and
  comparison forms matter in fixed-width interview languages.
- Kth-smallest searches use `count(values <= mid) >= k`, while the median problem
  searches a valid partition of the shorter array.
- The total time is the cost of one predicate multiplied by `O(log R)`, where
  `R` is the width of the candidate range.

## Interview Checklist

```text
What number am I searching for, and what are its units?
What exactly does feasible(mid) mean?
Why can feasibility change only once?
Am I finding the minimum feasible or maximum feasible value?
Can I prove both inclusive bounds contain the answer?
Is one endpoint known feasible, or must I reject an impossible case first?
Does a successful mid stay in the candidate region?
Does every failed mid leave the candidate region?
Does my maximizing midpoint round upward so the loop cannot stall?
Am I using integer-safe midpoint, multiplication, and ceiling-division forms?
What does one predicate call cost?
Have I tested answers at both the low and high bounds?
```
