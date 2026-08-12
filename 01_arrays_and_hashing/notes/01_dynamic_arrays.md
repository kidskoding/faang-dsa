# Dynamic Arrays

An **array** stores values in numbered positions called **indices**. Python's
`list` is a **dynamic array**, which means it keeps those positions while also
being able to grow and shrink.

```text
index    0    1    2    3
value   10   20   30   40
                    ^
                 nums[2]
```

An index gives Python the exact slot to visit, so reading or replacing
`nums[i]` takes `O(1)` time. That direct access is the reason arrays are the
default container for scans, in-place changes, and answers that must preserve an
order.

Dynamic does not mean every position is equally cheap to change. The end can
grow without disturbing the current values, but inserting or deleting in the
middle changes which value belongs at every later index.

## Size, Capacity, and Why Append Is Amortized

A dynamic array tracks two different quantities:

- Its **size** is the number of live elements that the program can access.
- Its **capacity** is the number of slots already allocated in the backing
  array.

When `size < capacity`, an append writes into the next unused slot. When the
array is full, it allocates a larger backing array, copies the existing
references, and then writes the new value.

```text
size=2 capacity=4    [ 10 ][ 20 ][    ][    ]   append 30 in place
size=4 capacity=4    [ 10 ][ 20 ][ 30 ][ 40 ]   append 50 cannot fit
                                              X rejected old capacity
size=5 capacity=8    [ 10 ][ 20 ][ 30 ][ 40 ][ 50 ][    ][    ][    ]
                     copy old values, then append
```

The resize is an expensive `O(n)` append, but capacity grows by a constant
factor rather than by one slot. Across `n` appends, the copied amounts form a
geometric series such as `1 + 2 + 4 + ...`, whose total is `O(n)`. The complete
sequence therefore costs `O(n)`, or `O(1)` **amortized** per append. This is the
same amortized analysis introduced in
[time and space complexity](../../00_fundamentals/notes/03_time_and_space_complexity.md).

> "A list append is `O(1)` amortized. Most appends use spare capacity, while an
> occasional resize copies the current elements. Geometric growth keeps all of
> those copies linear across the full sequence."

## Mutation Keeps the Same Array

An **in-place** algorithm changes the input array instead of building another
array of the same size. Assignment and swapping are the two basic moves:

```python
def reverse_in_place(nums: list[int]) -> None:
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


values = [10, 20, 30, 40]
reverse_in_place(values)
assert values == [40, 30, 20, 10]

empty: list[int] = []
reverse_in_place(empty)
assert empty == []

single = [7]
reverse_in_place(single)
assert single == [7]
```

The condition is `left < right`, not `<=`, because the middle element of an
odd-length array is already in its final place. Rejecting that unnecessary
self-swap also makes the stopping condition easy to explain.

Changing the list's length while scanning it is more dangerous. Removing index
`i` shifts every later element one slot left, so the next value may move into an
index the loop has already passed.

```text
start                 [ 2 ][ 4 ][ 6 ][ 8 ]
remove index 1        [ 2 ][ 6 ][ 8 ]
                              ^ 6 moved left; incrementing i skips it
```

When order must be preserved, the next module derives a separate read position
and write position in
[same-direction pointers](../../02_two_pointers/notes/02_same_direction_pointers.md).
For now, keep the consequence in mind: changing the length during a scan can
skip a value. When order does not matter, there is a cheaper deletion.

## Delete Without Shifting When Order Does Not Matter

Suppose you need to remove index `i`, but the remaining values may appear in any
order. Move the last value into slot `i`, then pop the last slot. This is called
**swap-delete**.

```python
def remove_unordered(values: list[int], index: int) -> int:
    removed = values[index]
    values[index] = values[-1]
    values.pop()
    return removed


values = [10, 20, 30, 40]
assert remove_unordered(values, 1) == 20
assert values == [10, 40, 30]

single = [7]
assert remove_unordered(single, 0) == 7
assert single == []
```

The last value, 40, is a valid replacement candidate because order was declared
irrelevant. Values 30 and 40 are not shifted. If order must remain
`[10, 30, 40]`, that candidate is rejected and a normal deletion costs `O(n)`.

Swap-delete is one half of
[Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/).
The other half is a mapping from each value to its current index, which the next
note introduces. Whenever the last value moves, its stored index must be updated
as well.

## Reusing Indices as State

Array constraints sometimes make the array itself usable as bookkeeping. If an
input of length `n` contains only values from `1` through `n`, value `x` can map
to index `x - 1`. Problems use that fact in several ways:

- [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)
  negates the value at index `abs(x) - 1`. A position that is already negative
  means `x` was seen before.
- [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)
  repeatedly swaps each useful value `x` toward index `x - 1`, then finds the
  first index whose value is wrong.
- [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
  reuses the first row and first column as marker arrays. Separate flags are
  still needed for those two marker regions themselves.

These techniques are valid only when the constraints define a safe index. A
value of `0`, `-3`, or `n + 1` is rejected as a position in the `1..n` scheme;
blindly using it as an index changes the wrong cell or leaves the array.

Matrix problems use the same idea with two indices. [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
shrinks four boundaries after completing each side, while
[Rotate Image](https://leetcode.com/problems/rotate-image/) transposes
`matrix[row][column]` with `matrix[column][row]` before reversing each row.
The important skill is to say what every boundary or index represents before
mutating it.

[Sort Colors](https://leetcode.com/problems/sort-colors/) uses boundaries to
divide one array into three regions. `left` marks the next slot for a `0`,
`right` marks the next slot for a `2`, and `current` examines the unknown region.
After swapping a `2` with `nums[right]`, do not advance `current`, because the
incoming value has not been classified yet. That incoming value is a rejected
candidate for the finished middle region until it is examined.

[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
has a stricter follow-up: do not mutate the input and use constant extra space.
Its values are valid indices, so repeatedly moving from `index` to `nums[index]`
creates a chain of positions. Since `n + 1` positions point into only `n`
possible next positions, that chain must repeat, and the entry into the repeated
cycle identifies the duplicate. The fast/slow method for locating that entry is
derived fully in [cycle detection](../../06_linked_lists/notes/02_fast_slow.md).
This is a recognition preview rather than a technique to use yet; the later note
derives the constant-space search from the repeated chain.

## Worked Example: [Rotate Array](https://leetcode.com/problems/rotate-array/)

Given an integer array `nums`, rotate it to the right by `k` positions in place.
For example, rotating `[1, 2, 3, 4, 5, 6, 7]` right by three produces
`[5, 6, 7, 1, 2, 3, 4]`. An empty array is normally excluded by the problem
constraints, but guarding it makes the helper safe to reuse.

Moving the last value to the front `k` times works, but each front insertion
shifts the array. That costs `O(kn)` time in the worst case. The array already
contains the right two groups; they are merely in the wrong order:

```text
original groups       [ 1  2  3  4 ][ 5  6  7 ]
wanted order          [ 5  6  7 ][ 1  2  3  4 ]
```

Three reversals put those groups in place without allocating another array:

1. Reverse everything, producing `[7, 6, 5, 4, 3, 2, 1]`.
2. Reverse the first `k` values, producing `[5, 6, 7, 4, 3, 2, 1]`.
3. Reverse the remaining values, producing `[5, 6, 7, 1, 2, 3, 4]`.

First reduce `k` with `k %= n`. A full rotation changes nothing, so on a
seven-element array `k = 10` has the same effect as `k = 3`; the other seven
positions are rejected as a complete cycle.

> "Repeated front insertion would redo shifting. I can instead view the array
> as two groups, reverse the whole array to swap their order, and reverse each
> group to restore its internal order."

```python
def rotate(nums: list[int], k: int) -> None:
    if not nums:
        return

    k %= len(nums)

    def reverse(left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)


values = [1, 2, 3, 4, 5, 6, 7]
rotate(values, 3)
assert values == [5, 6, 7, 1, 2, 3, 4]

single = [9]
rotate(single, 100)
assert single == [9]

empty: list[int] = []
rotate(empty, 4)
assert empty == []
```

- **Time Complexity:** `O(n)`, where `n` is the array length, because the three
  reversals touch each position a constant number of times.
- **Space Complexity:** `O(1)` auxiliary space, because the algorithm keeps only
  indices and swaps values inside `nums`.

## Time and Space Complexity

| Operation or approach          | Time                                                                                                     | Space                                                                        |
| ------------------------------ | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Read or assign `nums[i]`       | `O(1)`: the index identifies one direct slot                                                             | `O(1)`: the operation creates no growing structure                           |
| Append to a dynamic array      | `O(1)` amortized and `O(n)` for one resize: geometric capacity growth spreads copies across the sequence | `O(n)`: the backing array holds capacity proportional to the `n` live values |
| Insert or delete in the middle | `O(n)`: up to all later values shift to preserve order                                                   | `O(1)` auxiliary: the existing array is changed in place                     |
| Swap-delete                    | `O(1)`: one assignment and one end pop avoid shifting                                                    | `O(1)` auxiliary: no second array is created                                 |
| Rotate by repeated front moves | `O(kn)`: each of `k` moves can shift `n` values                                                          | `O(1)` auxiliary: the work can still mutate the same array                   |
| Rotate with three reversals    | `O(n)`: every position participates in a constant number of swaps                                        | `O(1)` auxiliary: only boundary indices are stored                           |

## Summary

- A **dynamic array** stores values by index and keeps spare capacity so it can
  grow. Python's `list` is the dynamic array used throughout this book.
- Indexing and replacement take `O(1)` time because an index identifies one
  slot, while middle insertion and deletion take `O(n)` because later values
  must shift.
- Appending is `O(1)` amortized because rare resize copies form a geometric
  series whose total stays linear across many appends.
- In-place algorithms mutate the existing array with indices and swaps. State
  what each index represents before changing values, especially in a matrix.
- Swap-delete replaces a removed value with the last value and pops the end in
  `O(1)`, but it is valid only when the remaining order does not matter.
- Constraints can let values map to array positions for marking or placement,
  but values outside the promised range must not be treated as indices.

## Interview Checklist

```text
Does the problem require the original order to remain unchanged?
Will an insertion or deletion shift later values inside my loop?
Can I mutate the input, or must I allocate a separate result?
If order does not matter, can swap-delete avoid a linear shift?
Does every value I turn into an index fall inside the promised range?
What does each matrix boundary or array index represent before I update it?
Can I explain why append is amortized O(1), not worst-case O(1)?
Have I tested an empty array, a singleton, and a no-op mutation?
```
