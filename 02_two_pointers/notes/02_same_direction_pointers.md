# Same-Direction Pointers

**Same-direction pointers** move through a sequence in the same general
direction while representing different jobs. The most common pair is a **read
pointer**, which examines each value, and a **write pointer**, which marks where
the next accepted value belongs

```text
              read
                v
index   0   1   2   3   4   5
value   1   2   2   2   3   ?
            ^
          write
```

At the start of an iteration, everything before `write` is finished, everything
from `read` onward is unread, and **`write <= read`**. The gap between the two may
be overwritten. After accepting `nums[read]`, `write` advances and may temporarily
equal `read + 1`; the loop advances `read` before the next iteration. Equivalently,
`write` never passes the next unread position, which is what makes modifying the
input safe

This note also covers the in-place mutation techniques that use the same idea:
swapping instead of overwriting, filling free space from the back, and dividing
an array into three regions

## When To Use

Look for this pattern when the problem says:

- Remove or keep values **in place**, often returning a new logical length
- Preserve the relative order of accepted values while discarding others
- Merge into existing free space without allocating another array
- Divide values into regions such as "less than, equal to, and greater than"
- Advance through one or two sequences without ever needing to move backward

This differs from [opposite-end pointers](01_opposite_end_pointers.md). There,
the endpoints form a candidate together and a comparison eliminates one end.
Here, the pointers usually have separate roles or separate speeds

## Compact Values Without Changing The List Length

Building `[x for x in nums if keep(x)]` is simple, but it uses `O(n)` additional
space and creates a different list. An in-place problem asks you to keep the
original list object and reuse its slots

Remove Duplicates From Sorted Array keeps the first value, then writes only
values different from the last accepted one

```python
def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1

    return write


values = [1, 1, 2, 2, 2, 3]
length = remove_duplicates(values)
assert length == 3
assert values[:length] == [1, 2, 3]

empty: list[int] = []
assert remove_duplicates(empty) == 0

single = [7]
assert remove_duplicates(single) == 1
assert single == [7]
```

The returned length says which prefix is valid. Values after that prefix are
stale and do not need to be cleared

```text
nums=[1, 1, 2, 2, 2, 3]

read=1 (1)  duplicate -> reject it; write stays 1
read=2 (2)  new value -> write at index 1; write becomes 2
read=3 (2)  duplicate -> reject it; write stays 2
read=4 (2)  duplicate -> reject it; write stays 2
read=5 (3)  new value -> write at index 2; write becomes 3

valid prefix=[1, 2, 3]    stale tail=[2, 2, 3]
```

Remove Element uses the same loop with `nums[read] != val` as the keep
condition. If order does not matter, it may instead replace a rejected value
with the final unexamined value and shorten the unchecked region. That version
can avoid writes, but it does not preserve order

## Swap When Rejected Values Must Remain

Move Zeroes cannot simply overwrite zeroes because those zeroes still belong at
the end. Swap each accepted non-zero value into the next `write` slot instead

```python
def move_zeroes(nums: list[int]) -> None:
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


values = [0, 1, 0, 3, 12]
move_zeroes(values)
assert values == [1, 3, 12, 0, 0]

empty: list[int] = []
move_zeroes(empty)
assert empty == []
```

At the start of the iteration, `write <= read`, so the value swapped toward
`read` has already been examined. The swap therefore cannot place an unread
value behind the scan. After an accepted value, `write` may become `read + 1`,
and then the loop advances `read` as well. Use assignment when rejected values
are dead, and use a swap when they still need a place in the final array

## Fill From The Back To Protect Unread Values

Merge Sorted Array gives `nums1` enough empty slots to hold `nums2`. A forward
merge would overwrite real values at the front of `nums1` before reading them.
The largest remaining value belongs at the back, exactly where the free space
already is, so all three pointers should move right to left

```python
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    first = m - 1
    second = n - 1
    write = m + n - 1

    while second >= 0:
        if first >= 0 and nums1[first] > nums2[second]:
            nums1[write] = nums1[first]
            first -= 1
        else:
            nums1[write] = nums2[second]
            second -= 1
        write -= 1


values = [1, 2, 3, 0, 0, 0]
merge(values, 3, [2, 5, 6], 3)
assert values == [1, 2, 2, 3, 5, 6]

values = [4, 5, 6, 0, 0, 0]
merge(values, 3, [1, 2, 3], 3)
assert values == [1, 2, 3, 4, 5, 6]
```

The loop watches only `second`. Once `nums2` is exhausted, any remaining prefix
of `nums1` is already in its correct place, so copying it would be rejected as
unnecessary work. If `nums1` is exhausted first, the remaining `nums2` values
still have to be written

Squares of a Sorted Array uses the same backward-write decision. The largest
absolute value is at one of the original ends, so compare their squares and
write the larger one into the answer from right to left. [Rotate Array](../../01_arrays_and_hashing/notes/01_dynamic_arrays.md)
also uses opposite-end swaps, but its three-reversal derivation was established
in the previous module

## When Same Direction Means Different Speeds

Find the Duplicate Number uses indices differently. For an array of `n + 1`
values where every value is from `1` through `n`, read `nums[index]` as the next
index to visit. There are more starting positions than possible next positions,
so repeatedly following the values must eventually enter a loop

This is **Floyd's cycle detection**. A `slow` pointer moves one step at a time and
`fast` moves two, so they must meet inside the loop. To see why the second phase
works, call the distance from index 0 to the loop entry `d`. At the first meeting,
the extra distance traveled by `fast` is a whole number of loop lengths. That
leaves the loop entry exactly `d` forward steps from the meeting point when
distance is measured around the loop. Therefore, a pointer restarted at index 0
and the meeting pointer will reach the entry together when both move one step at
a time

```python
def find_duplicate(nums: list[int]) -> int:
    slow = fast = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    finder = 0
    while finder != slow:
        finder = nums[finder]
        slow = nums[slow]

    return finder


assert find_duplicate([1, 3, 4, 2, 2]) == 2
assert find_duplicate([3, 1, 3, 4, 2]) == 3
```

The first meeting is not automatically the answer, so returning there is a
rejected shortcut. The distance alignment is why the restart phase finds the
entry rather than merely producing another arbitrary meeting inside the loop

## Boundaries That Only Move Forward

Some workbook problems use two forward-moving boundaries without modifying the
array. They still belong to the same family because processed positions never
need to be revisited

- Partition Labels records each character's last position. As `read` advances,
  the current partition end becomes the furthest last position seen; a cut is
  accepted only when `read` reaches that boundary
- Longest Mountain In Array walks up a strictly increasing slope and then down a
  strictly decreasing slope. A flat pair rejects the current mountain because
  both a climb and a descent are required
- Interval List Intersections keeps one pointer in each sorted list of closed
  intervals `[start, end]`. After recording an overlap, move the interval that
  ends first because it cannot overlap any later interval from the other list

Subarray Product Less Than K maintains a contiguous region between `left` and
`right`. All values are positive, so removing values from the left can only
decrease the product. After shrinking until the product is below `k`, every
suffix ending at `right` and starting from `left` through `right` is also valid.
There are `right - left + 1` such suffixes

Number of Subarrays With Bounded Maximum uses two last-seen boundaries.
`last_too_large` is the latest index whose value exceeded `upper`, and
`last_in_range` is the latest index whose value was between `lower` and `upper`.
For the current right end, valid starts run from `last_too_large + 1` through
`last_in_range`, so add `max(0, last_in_range - last_too_large)`

Subarrays With K Different Integers uses a **frequency map**, which stores how
many times each value occurs in the current region. `at_most(k)` adds the new
right value, then shrinks from the left while the map has more than `k` keys.
Each removal decrements a count and deletes the key at zero, because a zero-count
key must not count as distinct. Once valid, it also adds `right - left + 1`.
Every region with exactly `k` distinct values appears in `at_most(k)` but not in
`at_most(k - 1)`, giving `exactly(k) = at_most(k) - at_most(k - 1)`

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


def num_subarray_bounded_max(
    nums: list[int], lower: int, upper: int
) -> int:
    last_too_large = -1
    last_in_range = -1
    total = 0

    for right, value in enumerate(nums):
        if value > upper:
            last_too_large = right
        if lower <= value <= upper:
            last_in_range = right
        total += max(0, last_in_range - last_too_large)

    return total


def subarrays_with_k_distinct(nums: list[int], k: int) -> int:
    def at_most(limit: int) -> int:
        counts: dict[int, int] = {}
        left = 0
        total = 0

        for right, value in enumerate(nums):
            counts[value] = counts.get(value, 0) + 1
            while len(counts) > limit:
                outgoing = nums[left]
                counts[outgoing] -= 1
                if counts[outgoing] == 0:
                    del counts[outgoing]
                left += 1
            total += right - left + 1

        return total

    return at_most(k) - at_most(k - 1)


assert num_subarray_product_less_than_k([10, 5, 2, 6], 100) == 8
assert num_subarray_product_less_than_k([], 100) == 0
assert num_subarray_bounded_max([2, 1, 4, 3], 2, 3) == 3
assert subarrays_with_k_distinct([1, 2, 1, 2, 3], 2) == 7
```

Each helper takes `O(n)` time because both boundaries move only forward; a
shrinking `while` loop advances `left` at most `n` times across the whole run.
The product and bounded-maximum versions use `O(1)` auxiliary space. The
exact-distinct version uses `O(k)` space for at most `k` live frequency keys, and
running `at_most` twice changes neither asymptotic bound

Module 04 develops this moving-region idea under its usual name, **sliding
window**, but these equations are enough to implement the workbook problems here

## Worked Example: [Sort Colors](https://leetcode.com/problems/sort-colors/)

The array contains only `0`, `1`, and `2`. Sort it in place in one pass without
calling a sorting function. A normal sort is correct but costs `O(n log n)`,
while the three possible values let us maintain three finished regions and one
unknown region

**Input**: `nums`, a `list[int]` in which every value is `0`, `1`, or `2`, where
`1 <= len(nums) <= 300`

**Output**: `None`. The function returns nothing and instead **mutates `nums` in
place**, so that after the call the list holds all of its `0` values first, then
all of its `1` values, then all of its `2` values

```text
[ 0 region ][ 1 region ][       unknown       ][ 2 region ]
              low        mid                 high
```

`low` is the next slot for a 0, `mid` examines the unknown value, and `high` is
the next slot for a 2. Before every iteration:

- Everything before `low` is 0
- Everything from `low` through `mid - 1` is 1
- Everything from `mid` through `high` is unclassified
- Everything after `high` is 2

This arrangement is called a **three-way partition**. The unknown region shrinks
on every iteration, which proves the loop terminates

> "A 0 swaps to the low side and both forward boundaries advance. A 1 is already
> in its region, so only mid advances. A 2 swaps to the high side, but mid stays
> because the incoming value has not been classified yet."

Therefore,

1. Start `low` and `mid` at index 0 and `high` at the last index, because before
   any value has been examined the finished `0` and `2` regions are both empty and
   the unknown region covers the whole array
2. Loop while `mid <= high`, since that condition says exactly that the unknown
   region still holds at least one value. For an empty list `high` starts at `-1`,
   so the loop body never runs and the list is left untouched
3. When `nums[mid]` is `0`, swap it with `nums[low]` and advance both `low` and
   `mid`. The value arriving at `mid` is safe to skip because `low` either equals
   `mid`, making the swap a self-swap, or points into the classified `1` region
4. When `nums[mid]` is `2`, swap it with `nums[high]` and decrease `high`, but
   leave `mid` where it is. The value arriving from `high` comes out of the unknown
   region and has never been examined, so it must be classified on the next
   iteration
5. Otherwise the value is `1`, which already belongs between `low` and `mid`, so
   advance `mid` alone and leave both swaps undone
6. Stop once `mid` passes `high`. Every position has then been assigned to one of
   the three regions, so `nums` is sorted and there is nothing to return

```python
def sort_colors(nums: list[int]) -> None:
    low = mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        else:
            mid += 1


values = [2, 0, 2, 1, 1, 0]
sort_colors(values)
assert values == [0, 0, 1, 1, 2, 2]

all_equal = [2, 2, 2, 2]
sort_colors(all_equal)
assert all_equal == [2, 2, 2, 2]

empty: list[int] = []
sort_colors(empty)
assert empty == []
```

The first transition is the branch that matters most

```text
start       [2, 0, 2, 1, 1, 0]   low=0 mid=0 high=5
see 2       [0, 0, 2, 1, 1, 2]   low=0 mid=0 high=4
             ^
             mid does not move; the incoming 0 is still unknown
see 0       [0, 0, 2, 1, 1, 2]   low=1 mid=1 high=4
see 0       [0, 0, 2, 1, 1, 2]   low=2 mid=2 high=4
see 2       [0, 0, 1, 1, 2, 2]   low=2 mid=2 high=3
```

Advancing `mid` after the first swap is rejected because it would skip the
unseen 0 that arrived from `high`. The 0 branch has two safe cases. When
`low == mid`, the swap is a self-swap, so both pointers simply advance. When
`low < mid`, the region from `low` through `mid - 1` contains only classified
1s, so the swap pulls a known 1 into `mid` and both pointers may still advance.
For example, `[1, 0]` first advances `mid` over the 1, then swaps the 0 with
`low`; the incoming 1 is already classified, producing `[0, 1]`

- **Time Complexity:** `O(n)`, because either `mid` increases or `high`
  decreases on every iteration, shrinking the unknown region once per value
- **Space Complexity:** `O(1)`, because the three regions are stored inside the
  input and only three indices are added

Wiggle Sort II asks for `nums[0] < nums[1] > nums[2] < ...`. Choose the median,
then run the same three-way partition through **virtual indices** rather than
physical indices. For an array of length `n`, logical position `i` maps to
`(1 + 2 * i) % (n | 1)`. This visits odd positions first and then even positions:
for `n = 6`, the order is `1, 3, 5, 0, 2, 4`

Treat that virtual order as the array used by the partition. Values greater than
the median swap toward the virtual `low` end, values smaller than the median swap
toward virtual `high`, and values equal to the median advance through the middle.
The result places large values in physical odd slots and small values in physical
even slots, while the median values fill the gaps

```text
nums=[1, 5, 1, 1, 6, 4], median=1
virtual order of slots: 1, 3, 5, 0, 2, 4
move values > 1 toward the start of that virtual order
one valid physical result: [1, 5, 1, 6, 1, 4]
                         1 < 5 > 1 < 6 > 1 < 4
```

Selecting the median with in-place Quickselect takes `O(n)` expected time and
`O(1)` auxiliary space, and the virtual three-way partition is another `O(n)`
pass with constant state. The simpler starting solution sorts a copy and
interleaves reversed halves; that costs `O(n log n)` time and `O(n)` auxiliary
space, but it makes the placement rule easier to explain before the follow-up

## Time and Space Complexity

`n` is the input length, while `m` is the number of live values initially stored
in the first array of a merge

| Approach                          | Time                                                                            | Space                                                                            |
| --------------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Read/write compaction or swapping | `O(n)`: `read` examines each position once and `write` never moves backward     | `O(1)`: the input slots hold the accepted values, with only two indices added    |
| Backward merge                    | `O(m + n)`: each live value from the two arrays is written at most once         | `O(1)`: the unused tail of the first array is the output space                   |
| Fast/slow duplicate search        | `O(n)`: both phases traverse a number of links proportional to the array length | `O(1)`: only the slow, fast, and finder indices are stored                       |
| Three-way partition               | `O(n)`: each iteration shrinks the unknown region by moving `mid` or `high`     | `O(1)`: swaps reuse the input and only three boundaries are stored               |
| Build a filtered list             | `O(n)`: every input value is still examined once                                | `O(n)`: the new list may store every value and violates the in-place requirement |

## Summary

- **Same-direction pointers** often split reading from writing. At the start of
  each iteration, everything before `write` is final, everything from `read`
  onward is unread, and `write <= read`. After accepting a value, `write` may
  equal `read + 1`, but it never passes the next unread position
- In-place filtering returns a logical length, so values beyond that prefix may
  remain stale. Swap instead of overwrite when rejected values must still appear
  somewhere in the final array
- Fill from the back when free space is at the back, because a forward write could
  destroy values that have not yet been read
- Fast and slow pointers can traverse a value-to-index chain at different speeds.
  Find the Duplicate Number uses one phase to meet inside the loop and a second
  phase to locate its entry
- A three-way partition maintains finished low and high regions around an unknown
  middle. After swapping from the high end, do not advance `mid`, because the
  incoming value has not been classified
- Compaction, backward merging, and three-way partitioning all take linear time
  and constant auxiliary space because they reuse the input rather than allocate
  another full array

## Interview Checklist

Before coding, make sure you can answer each of these

```text
What does each pointer mean, and which region is already final?
Why can write never pass the next unread position?
Does a rejected value disappear, remain stale, or need to be swapped elsewhere?
Does the caller read the whole array or only the returned logical prefix?
Would writing forward overwrite unread data, meaning I should write backward?
When may a pointer stay still after a swap, and what remains unclassified?
Does the problem preserve relative order, or may I swap from an end?
For two sequences, which pointer is safe to advance after a comparison?
Can I explain both phases of a fast/slow loop-entry search?
Can I name the finished and unknown regions before coding a partition?
```
