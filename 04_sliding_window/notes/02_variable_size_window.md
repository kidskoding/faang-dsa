# Variable-Size Sliding Window

In a [fixed-size window](01_fixed_size_window.md), the problem gives you the
width and both edges move together. A **variable-size window** is different:
the problem gives you a condition, and the two edges move independently to keep
that condition true or to search for the moment it becomes true.

The window is the contiguous range `nums[left : right + 1]`:

```text
index   0   1   2   3   4   5
value   2   3   1   2   4   3
            ^           ^
          left        right

length = right - left + 1
```

`right` expands the window by one element. When the condition requires it,
`left` removes one element at a time. Neither pointer moves backward, so each
index enters once and leaves at most once. That is why a `for` loop containing a
`while` loop can still take `O(n)` total time.

## The Condition Must Move In One Direction

A sliding window is safe only when moving a boundary has a predictable effect.
There are two common shapes:

- For a **longest valid** window, growing can break the rule and shrinking can
  only repair it. A window with at most `k` zeroes has this shape.
- For a **shortest valid** window, growing can only move toward the target and
  shrinking can only move away from it. A window of positive numbers whose sum
  must reach a target has this shape.

The input constraints are part of that proof. With positive values, adding a
number increases a sum and removing one decreases it. Negative values destroy
that direction.

For `nums = [3, -2, 5]` and `target = 5`, an ordinary shortest-window scan first
finds `[3, -2, 5]` with sum 6. Removing 3 drops the sum to 3, so it stops
shrinking and never reaches the valid one-element window `[5]`. The correct
answer is 1, but the positive-only template returns 3.

When negative values are allowed in a shortest-sum problem, do not patch the
shrink loop. Use prefix sums with the
[monotonic-deque method](04_window_max_min.md#negative-values-need-prefix-sum-boundaries),
which does not assume the sum moves in one direction.

## Longest And Shortest Use Opposite Shrink Loops

For a **longest** answer, expand first, shrink **while invalid**, and record only
after the repair:

```text
add nums[right]
while window is invalid:
    remove nums[left]
    left += 1
record right - left + 1
```

Minimum Size Subarray Sum is the standard **shortest** version. Expand until
valid, then shrink **while valid** and record before each removal, because every
successful shrink is a shorter candidate:

```python
def min_sub_array_len(target: int, nums: list[int]) -> int:
    left = 0
    window_sum = 0
    best = len(nums) + 1

    for right, value in enumerate(nums):
        window_sum += value
        while window_sum >= target:
            best = min(best, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return 0 if best == len(nums) + 1 else best
```

`best` starts above every possible length, so the first real answer can replace
it. If no window reaches `target`, the sentinel survives and becomes 0. The
order inside the loop also matters: record while the window is still valid,
then remove `nums[left]`, then advance `left`.

On `[2, 3, 1, 2, 4, 3]` with target 7, `right = 4` first gives `[3, 1, 2, 4]`
with length 4. Removing 3 leaves `[1, 2, 4]`, which is still valid and improves
the answer to 3. The loop must continue after the first valid window or it misses
the shorter one. At `right = 5`, it eventually finds `[4, 3]` and returns 2.

## Budgets Become Counts Or Costs

Wording such as “change at most `k` values” usually means the window may contain
at most `k` units of something bad. The budget is not the window width.

- Max Consecutive Ones III counts zeroes and shrinks while `zeroes > k`.
- Get Equal Substrings Within Budget adds
  `abs(ord(s[i]) - ord(t[i]))` and shrinks while the running conversion cost
  exceeds `maxCost`.
- Longest Subarray of 1's After Deleting One Element allows at most one zero,
  but records `window_width - 1`. The subtraction is required even when the
  array contains only ones because the problem says one element must be deleted.
- Maximum Erasure Value uses a set for membership and a running sum. It removes
  from both until the entering value is no longer duplicated, then adds the
  unique window's sum as a candidate.

Frequency of the Most Frequent Element first sorts the values. Within a sorted
window, the rightmost value is the target to which every smaller value is
raised. If the window sum is `total`, the required increments are
`nums[right] * window_width - total`; shrink while that cost exceeds `k`.
Sorting is what makes “raise everything to the right edge” a safe one-direction
condition.

Longest Nice Subarray describes its condition with bits. `a & b` is nonzero
when integers `a` and `b` share a binary 1 position, while `a | b` records all
binary positions present in either value. Keep an OR mask for the current
window. Before adding `nums[right]`, shrink while `mask & nums[right]` is
nonzero, removing a departing value with `mask ^= nums[left]`. XOR removal is
safe because a valid nice window never has one bit owned by two stored values.

Best Time to Buy and Sell Stock is the smallest member of this family. `right`
is the selling day and the best earlier buying price is the state. A new lower
price replaces the left candidate; otherwise `price - minimum_so_far` is a
profit candidate. There is no shrink loop because only the cheapest earlier
price matters.

## Counting Every Valid Window

After an at-most window is repaired, every suffix ending at `right` and starting
between `left` and `right` is also valid. There are `right - left + 1` such
windows.

Subarray Product Less Than K applies that rule to positive integers:

```python
def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
    if k <= 1:
        return 0

    left = 0
    product = 1
    total = 0

    for right, value in enumerate(nums):
        product *= value
        while product >= k:
            product //= nums[left]
            left += 1
        total += right - left + 1

    return total
```

The `k <= 1` guard is necessary because a product of positive integers cannot
be less than 1. Without it, an immediately invalid one-element window would keep
shrinking past itself. For `[10, 5, 2, 6]` and `k = 100`, the repaired window
ending at value 6 is `[5, 2, 6]`, so its three valid suffixes are `[6]`,
`[2, 6]`, and `[5, 2, 6]`.

Counting an **exact** amount is less direct. The
[`at_most(k) - at_most(k - 1)`](03_frequency_map_windows.md#turn-exactly-k-into-two-at-most-questions)
transformation is developed in the next note.

## Worked Example: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Given a string, return the length of its longest contiguous substring with no
repeated character. The empty string is allowed and should return 0.

Trying every start and growing until a duplicate appears repeats the same work
and costs `O(n^2)`. This is a longest-valid window: the new character at `right`
may create a duplicate, removing characters from the left can only remove that
duplicate, and neither boundary needs to move backward.

A set with a shrink loop works. A map from character to its **last seen index**
lets `left` jump directly past the earlier copy. This problem needs membership
and position, not multiplicity, so a full frequency map would carry more state
than the condition asks for.

> “My window contains no duplicate. If the next character last appeared inside
> the current window, I will move `left` one past that index. I will never move
> `left` backward, because the map also contains old occurrences that have
> already expired.”

```python
def length_of_longest_substring(s: str) -> int:
    last_seen: dict[str, int] = {}
    left = 0
    best = 0

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        best = max(best, right - left + 1)

    return best
```

Trace `"abba"`:

```text
right=0  a  last_seen={}       window="a"   left=0  best=1
right=1  b  no duplicate      window="ab"  left=0  best=2
right=2  b  previous b at 1   jump left=2   window="b"   best=2
right=3  a  previous a at 0 is STALE because 0 < left
             reject moving left backward    window="ba"  best=2
```

The second `b` makes the window invalid as soon as it enters, and the jump
repairs it before the length is recorded. The final `a` is the rejected move:
using `left = last_seen['a'] + 1` without the `>= left` guard would move `left`
from 2 back to 1 and accept `"bba"`.

On duplicate-heavy input such as `"bbbb"`, every character after the first
makes an immediately invalid width-2 window, then moves `left` forward by one.
The answer remains 1, and both pointers still cross the string only once.

- **Time Complexity:** `O(n)` average time, because the scan performs one
  average-constant-time map lookup and update for each of the `n` characters.
- **Space Complexity:** `O(d)`, where `d` is the number of distinct characters
  seen, because the map keeps one latest index per character.

## Time and Space Complexity

Let `n` be the input length and `d` the number of distinct values held in hash
state.

| Approach                                  | Time                                                                                 | Space                                                                                                  |
| ----------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| Restart `right` for every `left`          | `O(n^2)`: overlapping ranges are rebuilt from each start                             | `O(1)` when only a numeric state is recomputed                                                         |
| Variable window with numeric or bit state | `O(n)`: `right` advances `n` times and `left` advances at most `n` times total       | `O(1)`: the state is a sum, product, count, or integer mask                                            |
| Variable window with a set or map         | `O(n)` average: pointer movement stays linear and hash operations are average `O(1)` | `O(d)`: one entry may be stored per distinct live or previously seen value                             |
| Sort, then use a raise-cost window        | `O(n log n)`: sorting dominates the linear window scan                               | `O(n)` in Python: `sorted()` copies the input, while `list.sort()` may still use linear working memory |

## Summary

- A **variable-size sliding window** receives a validity condition rather than a
  width. `right` expands it, `left` shrinks it, and the answer often is the
  width `right - left + 1`.
- A longest-valid problem shrinks while invalid and records after repair. A
  shortest-valid problem shrinks while valid and records before removal because
  each successful shrink is a shorter candidate.
- The technique requires a one-direction condition. Positive sum and product
  inputs often provide it, while negative values can make shrinking increase a
  sum and invalidate the ordinary boundary logic.
- “At most `k` changes” usually becomes a budget inside the window, such as a
  zero count, conversion cost, or replacement count. `k` is not necessarily a
  width.
- Counting at-most windows adds `right - left + 1` after repair because every
  suffix of a valid window ending at the same `right` is also valid.
- A nested shrink loop remains `O(n)` total because `left` has only `n` forward
  moves across the entire scan.

## Interview Checklist

```text
Is the width given, or does a condition decide it?
Does growing and shrinking change validity in a predictable direction?
Do the constraints allow negatives or zeroes that break that direction?
Am I finding the longest valid window, the shortest, or counting all valid windows?
Should I shrink while invalid or while valid?
Should the answer update happen after repair or before removal?
What state enters on the right and what exact operation removes the left value?
Does k mean a width, a budget, or an exact count?
Can I justify O(n) by counting all left and right movements?
Does stale state in a map ever move left backward?
```
