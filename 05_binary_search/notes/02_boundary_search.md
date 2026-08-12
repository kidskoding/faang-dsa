# Boundary Search

An exact binary search stops at any matching value. A **boundary search** keeps
going until it finds the edge of a whole region, such as the first 7, the first
bad version, or the first timestamp after a query.

The search begins with a **predicate**, which is a yes-or-no question `P(i)`
about index `i`. It must be **monotonic**: the answers are all `False` and then
all `True`, with no later return to `False`.

```text
index   0   1   2   3   4   5   6
P(i)    F   F   F   T   T   T   T
                    ^
              first True
```

That first `True` is the **boundary**. Testing `P(mid)` tells you whether the
boundary is at or before `mid`, or strictly after it, which is enough to discard
half of the possible positions.

## Recognizing a Boundary

Look for words such as **first**, **last**, **leftmost**, **rightmost**,
“smallest index such that,” “at or before,” and “at or after.” The edge of a run
of duplicates and a sorted insertion point are both boundaries.

The important step is choosing a monotonic question. On
`[5, 7, 7, 7, 7, 8]`, the predicate `nums[i] == 7` has the shape
`F T T T T F`, so it changes twice and cannot be boundary-searched. The
predicate `nums[i] >= 7` has the shape `F T T T T T`, so its first `True` is
the first 7.

Returning as soon as an exact search lands on 7 is the near miss:

```text
index       0   1   2   3   4   5
value       5   7   7   7   7   8
                    ^
              exact search may return 2
                ^
              first position is 1
```

Finding one copy and walking left is correct, but a list of `n` identical values
makes that walk `O(n)`. The boundary search preserves the required
`O(log n)` time.

## The First-True Template

```python
from collections.abc import Callable


def first_true(n: int, predicate: Callable[[int], bool]) -> int:
    left, right = 0, n

    while left < right:
        mid = left + (right - left) // 2
        if predicate(mid):
            right = mid
        else:
            left = mid + 1

    return left
```

The possible return values are 0 through `n`. Returning `n` means no real index
passed. During the loop:

- The probe interval is **half-open**, `[left, right)`. Therefore, `mid` is
  always a real index below `right`.
- The exact invariant is that the boundary remains in the closed set of possible
  answers `[left, right]`. Every real index below `left` is known `False`, and
  every real index at or above `right` is known `True`. The position `n` acts as
  the answer when there is no true index.
- When `P(mid)` is `True`, `mid` may itself be the first true index. Therefore,
  `right = mid` keeps it as a candidate. Using `mid - 1` could discard the
  answer.
- When `P(mid)` is `False`, `mid` cannot be the boundary, and monotonicity proves
  every earlier index is false too. Therefore, `left = mid + 1` is safe.
- When `left == right`, the invariant leaves exactly one possible boundary, so
  returning `left` needs no extra search.

For `P(i) = nums[i] >= 7`:

```text
left=0 right=6 mid=3  P=True  -> keep mid, right=3
left=0 right=3 mid=1  P=True  -> keep mid, right=1
left=0 right=1 mid=0  P=False -> discard 0, left=1
return 1
```

The first step deliberately rejects index 3 as a final answer even though its
predicate is true. A true midpoint only proves that the boundary is somewhere
at or to its left.

[First Bad Version](https://leetcode.com/problems/first-bad-version/) is the
same contract over versions numbered 1 through `n`. If `mid` is bad, keep it
with `right = mid` because it could be the first bad version. Otherwise discard
it with `left = mid + 1`.

```python
from collections.abc import Callable


def first_bad_version(n: int, is_bad_version: Callable[[int], bool]) -> int:
    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        if is_bad_version(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

This version assumes the problem's guarantee that at least one bad version
exists. Without that guarantee, the search needs a sentinel position or a
post-loop call that confirms the returned version is actually bad.

## Last True and Python's bisect

For a predicate shaped `T T T F F`, the last true index is one position before
the first false:

```python
from collections.abc import Callable


def last_true(n: int, predicate: Callable[[int], bool]) -> int:
    left, right = 0, n
    while left < right:
        mid = left + (right - left) // 2
        if not predicate(mid):
            right = mid
        else:
            left = mid + 1
    return left - 1
```

The return is `-1` when nothing is true and `n - 1` when everything is true.
Check `-1` before indexing because Python would interpret it as the last
element.

The standard library packages the two most common sorted-array predicates:

```python
from bisect import bisect_left, bisect_right

values = [5, 7, 7, 7, 7, 8]

assert bisect_left(values, 7) == 1   # first value >= 7
assert bisect_right(values, 7) == 5  # first value > 7
```

| Call                 | Equal values count as  | Returned boundary                     |
| -------------------- | ---------------------- | ------------------------------------- |
| `bisect_left(a, x)`  | `True` for `a[i] >= x` | Before the run of values equal to `x` |
| `bisect_right(a, x)` | `False` for `a[i] > x` | After the run of values equal to `x`  |

Therefore, `bisect_right(a, x) - bisect_left(a, x)` counts copies of `x`, and
`bisect_right(a, x) - 1` finds the last value at or before `x`.

## Worked Example: [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

Given a non-decreasing array, return the first and last index holding `target`,
or `[-1, -1]` if it is absent. Duplicates are the reason an exact search is
insufficient, and the required `O(log n)` time rules out walking outward after a
match.

The first occurrence is the boundary `nums[i] >= target`. The position after
the last occurrence is the boundary `nums[i] > target`. The only extra work is
validating the first boundary, because it may be `n` or may land on a larger
value when the target sits in a gap.

> “I will run the same first-true search twice. The first pass keeps equality on
> the true side, while the second pass requires a strictly larger value. Before
> indexing the first boundary, I will confirm that it is real and actually holds
> the target.”

```python
def search_range(nums: list[int], target: int) -> list[int]:
    def lower_bound(strict: bool) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            passes = nums[mid] > target if strict else nums[mid] >= target
            if passes:
                right = mid
            else:
                left = mid + 1
        return left

    first = lower_bound(strict=False)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]

    last = lower_bound(strict=True) - 1
    return [first, last]
```

For `nums = [5, 7, 7, 8, 8, 10]` and `target = 8`:

```text
first search, nums[i] >= 8:
  mid=3 value=8 True  -> right=3
  mid=1 value=7 False -> left=2
  mid=2 value=7 False -> left=3
  first=3

second search, nums[i] > 8:
  mid=3 value=8 False -> left=4
  mid=5 value=10 True -> right=5
  mid=4 value=8 False -> left=5
  one-past-last=5, so last=4
```

The first probe is the near miss: index 3 holds the target, but returning
`[3, 3]` there would miss the duplicate at index 4. Each match narrows a
boundary instead of ending the search.

Searching for 6 makes the first boundary land at index 1 on value 7. The
post-loop validation rejects that candidate and returns `[-1, -1]`. An empty
list makes the boundary equal 0, which is also `len(nums)`, so the short-circuit
guard returns safely without indexing.

- **Time Complexity:** `O(log n)` for `n` elements, because two halving searches
  still take `2 log n = O(log n)`.
- **Space Complexity:** `O(1)` auxiliary space, because both passes keep a fixed
  number of indices and the two-element result has fixed size.

## Boundary Problems in Different Clothes

The predicate does not need to be a direct comparison. It only needs one
permanent change.

**Nearest timestamp and wraparound.**
[Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)
stores each key's timestamps in increasing order. A query uses
`bisect_right(times, timestamp) - 1` to find the last write at or before the
requested time. [Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)
uses `bisect_right` and wraps index `n` back to 0 with modulo.

```python
from bisect import bisect_right
class TimeMap:
    def __init__(self) -> None:
        self.times: dict[str, list[int]] = {}
        self.values: dict[str, list[str]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times.setdefault(key, []).append(timestamp)
        self.values.setdefault(key, []).append(value)

    def get(self, key: str, timestamp: int) -> str:
        times = self.times.get(key)
        if not times:
            return ""
        i = bisect_right(times, timestamp) - 1
        return self.values[key][i] if i >= 0 else ""


def next_greatest_letter(letters: list[str], target: str) -> str:
    return letters[bisect_right(letters, target) % len(letters)]
```

The two parallel lists avoid building timestamp tuples or copying timestamps on
every query. The problem guarantees increasing timestamps for each `set` call,
so appending preserves the order that `bisect_right` needs.

**Searching a derived count.**
[Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/)
uses `arr[i] - (i + 1)`, the number of positive integers missing before
`arr[i]`. Find the first index where that count is at least `k`, then return
`left + k`.

[Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/)
groups positions as pairs `(2i, 2i + 1)`. Before the single value, the pair
matches. At and after it, the pair is broken. Search the first broken pair and
return `nums[2 * boundary]`. If no pair breaks, the single value is the last
element.

**Searching a window edge.**
[Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)
searches possible left edges from 0 through `n - k`. For edge `mid`, compare
the value that would leave, `arr[mid]`, with the value that would enter,
`arr[mid + k]`:

```python
def find_closest_elements(arr: list[int], k: int, x: int) -> list[int]:
    left, right = 0, len(arr) - k
    while left < right:
        mid = left + (right - left) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left : left + k]
```

The comparison uses `>` rather than `>=` because a distance tie favors the
smaller values and therefore keeps the earlier window. The returned slice
allocates `O(k)` output space.

**Searching once per query.**
[Successful Pairs of Spells and Potions](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/)
sorts the `m` potions once. For spell `s`, the minimum potion is
`ceil(success / s) = (success + s - 1) // s`. A `bisect_left` finds the first
qualifying potion, and `m - boundary` gives the count. Sorting costs
`O(m log m)`, the `q` spells cost `O(q log m)`, the answer uses `O(q)` output
space, and Python's sort may use `O(m)` auxiliary space.

## Searching for a Peak

[Find Peak Element](https://leetcode.com/problems/find-peak-element/) is a
related halving search, but `nums[i] > nums[i + 1]` does not need to be
monotonic when multiple peaks exist. The invariant is instead that **some peak
remains inside the inclusive interval**.

```python
def find_peak_element(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left
```

A descending step means a peak exists at `mid` or to its left, so `mid` stays.
An ascending step means a peak exists strictly to the right, so `mid` leaves.
The loop reads `mid + 1` safely because `left < right` guarantees
`mid < right`.

[Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/)
combines three searches: use the slope rule to find the peak, exact-search the
ascending side, and then exact-search the descending side with the comparison
directions reversed. Search the ascending side first because the problem asks
for the smallest matching index. The limited API changes array reads into
`mountain_arr.get(i)` calls but does not change the bounds.

## Time and Space Complexity

| Approach                                 | Time                                                                                   | Space                                                                           |
| ---------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| One boundary search                      | `O(log n)`: the possible boundary positions halve each iteration                       | `O(1)`: only three indices are stored                                           |
| Exact search, then walk duplicates       | `O(n)`: an all-equal array forces the walk across all `n` values                       | `O(1)`: two walking indices are enough                                          |
| Find K Closest Elements                  | `O(log(n - k) + k)`: search the legal window starts, then copy `k` values              | `O(k)` output and `O(1)` auxiliary: the returned slice owns `k` references      |
| Successful Pairs                         | `O(m log m + q log m)`: sort `m` potions once, then search once for each of `q` spells | `O(m)` auxiliary for Python's sort and `O(q)` output for the counts             |
| TimeMap `get` with stored timestamp list | `O(log t)`: search the `t` writes for one key                                          | `O(1)` auxiliary per query, while the complete store uses `O(T)` for `T` writes |

## Summary

- A **boundary search** finds the first index where a monotonic predicate changes
  from `False` to `True`.
- The first-true template searches possible boundary positions 0 through `n`.
  Its probe interval is `[left, right)`, while the boundary remains a candidate
  in `[left, right]`.
  - A true midpoint stays with `right = mid` because it may be the first true
    index.
  - A false midpoint leaves with `left = mid + 1` because it and everything
    before it cannot be the boundary.
- `bisect_left(a, x)` finds the first value `>= x`, while
  `bisect_right(a, x)` finds the first value `> x`. Their difference counts
  copies of `x`.
- A returned boundary may be `n` or may point at a larger value, so callers must
  validate it before treating it as an exact match.
- Derived counts, window edges, timestamps, and local slopes can all supply the
  one-direction decision even when the problem does not ask for a plain value.

## Interview Checklist

```text
What yes-or-no predicate am I searching?
Can I prove its answers change only once?
What does left mean, what does right mean, and is n a valid returned boundary?
On True, do I keep mid with right = mid?
On False, do I discard mid with left = mid + 1?
Does equality belong on the left side or the right side of the boundary?
Am I asking for first True, or first False minus one?
Could the result be n or -1, and do I validate before indexing?
If I read mid + 1, does the loop guarantee it exists?
Do empty input, duplicates, all-true, and all-false predicates work?
```
