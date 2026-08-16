# Rotated Arrays

A **rotated sorted array** starts sorted, then moves some prefix from the front
to the back. Nothing inside either piece changes order.

```text
sorted     [ 0   1   2   4   5   6   7 ]
cut                     |
rotated    [ 4   5   6   7 ][ 0   1   2 ]
             sorted run       sorted run
```

The seam where 7 is followed by 0 is the **rotation point**, also called the
**pivot**. A rotation of zero is allowed, so `[0, 1, 2, 4, 5, 6, 7]` is also a
valid input.

Ordinary binary search fails because the whole array is no longer sorted. On the
rotated array above, comparing target 0 with midpoint 7 and moving left discards
the target immediately. The useful property is narrower: because there is only
one rotation point, it can lie in at most one half of the current interval.
Therefore, **at least one half is always sorted**.

## Searching by the Sorted Half

For distinct values, `nums[left] <= nums[mid]` proves that the left half is
sorted. If it is false, the rotation point lies in the left half, so the right
half must be sorted.

Once a sorted half is known, both of its ends tell you whether `target` belongs
inside it:

```text
left half sorted:   nums[left] <= target < nums[mid]
right half sorted:  nums[mid] < target <= nums[right]
```

The midpoint is excluded from both tests because equality is checked first.

```python
def search_rotated(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert search_rotated([0, 1, 2, 4, 5, 6, 7], 4) == 3
assert search_rotated([1], 0) == -1
```

The bounds are inclusive. The invariant is that, if the target exists, it remains
inside `nums[left:right + 1]`. Every branch preserves it because it either keeps
the sorted half whose endpoint range contains the target, or rejects that entire
half and keeps the other one.

Two details prevent common failures:

- The sorted-half test uses `<=`. When two candidates remain, `mid == left`, so
  the left half is one element and is still sorted. Using `<` misclassifies
  `[1, 0]` when searching for 0.
- The containment test needs both endpoints. Checking only
  `target < nums[mid]` repeats the ordinary-search mistake because a small
  target may live in the wrapped run on the right.

## Worked Example: [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

Given a rotated sorted array of distinct integers, return the target's index or
`-1` if it is absent. The required `O(log n)` time rules out scanning.

**Input**: `nums`, a `list[int]` that was sorted in ascending order and then
rotated at some unknown pivot, where `1 <= len(nums) <= 5000` and every value is
distinct, together with `target`, a single `int` to look for. The rotation amount
may be zero, so an unrotated sorted array is a legal input

**Output**: an `int`, the index into `nums` at which `target` sits, or `-1` when
`target` does not appear anywhere in `nums`. The index is into the rotated array
as given, not into the sorted order it came from, which is why sorting a copy
first would answer the wrong question

> “Plain binary search cannot act on `nums[mid]` alone because the smaller run
> may have wrapped to the right. I will first identify a sorted half, then use
> both endpoints of that half to decide whether it can contain the target.”

Therefore,

1. Set `left = 0` and `right = len(nums) - 1`, and loop while `left <= right`.
   The bounds are inclusive because a single remaining index still has to be
   probed, and a one-element input is a legal case that must reach its own
   comparison
2. Compute `mid = left + (right - left) // 2` and compare `nums[mid]` with
   `target` first. Returning here is what lets both containment tests below
   exclude `mid` from their ranges
3. Decide which half is sorted with `nums[left] <= nums[mid]`. Only one rotation
   point exists, so it can sit in at most one half, which makes this single
   comparison enough to name a fully sorted side. The `<=` matters because when
   two candidates remain `mid == left`, and that one-element left half is sorted
4. If the left half is sorted, keep it only when
   `nums[left] <= target < nums[mid]`, since a sorted run's two endpoints decide
   membership exactly. Keeping it means `right = mid - 1`; otherwise the answer
   can only be in the other half, so `left = mid + 1`
5. If instead the right half is sorted, apply the mirrored test
   `nums[mid] < target <= nums[right]`, moving `left = mid + 1` to keep that half
   and `right = mid - 1` to reject it
6. If the loop drains the interval so that `left > right`, no half ever contained
   the target, so return `-1`. Rotation zero needs no special case here, because
   every half chosen along the way is just a slice of the original sorted array

The code is the sorted-half search above. For
`nums = [4, 5, 6, 7, 0, 1, 2]` and `target = 0`:

```text
left=0 right=6 mid=3 value=7
  left half [4,5,6,7] is sorted
  0 is NOT in [4,7) -> reject that half, left=4

left=4 right=6 mid=5 value=1
  left half [0,1] is sorted
  0 IS in [0,1) -> keep it, right=4

left=4 right=4 mid=4 value=0 -> return 4
```

The first candidate is the near miss. Ordinary binary search sees `0 < 7` and
moves left, which loses the answer. The rotated search first proves that
`[4, 5, 6, 7]` is sorted, then rejects it because 0 lies below its lower
endpoint.

Searching the same array for 3 rejects a half on every iteration until
`left > right`, so the invariant proves absence and the function returns `-1`.
A one-element input either returns index 0 or empties the interval after one
probe. A rotation of zero works without a special case because each chosen half
is simply part of the original sorted array.

- **Time Complexity:** `O(log n)` for `n` distinct values, because each
  iteration removes about half of the inclusive interval.
- **Space Complexity:** `O(1)` auxiliary space, because the search stores only
  three indices.

## Finding the Rotation Point

[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
asks for the first value in the wrapped run. There is no target to recognize, so
the loop keeps one possible minimum until the bounds meet.

```python
def find_min_rotated(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


assert find_min_rotated([3, 4, 5, 1, 2]) == 1
assert find_min_rotated([4, 5, 6, 7, 0, 1, 2]) == 0
assert find_min_rotated([11, 13, 15, 17]) == 11
assert find_min_rotated([1]) == 1
```

The bounds are inclusive and the invariant is that the minimum remains in
`[left, right]`.

- If `nums[mid] > nums[right]`, `mid` is in the larger run and the minimum is
  strictly to its right. Therefore, `left = mid + 1` cannot discard the answer.
- Otherwise, `mid` and `right` are in the same sorted run, or `mid` is the
  minimum itself. Therefore, `right = mid` keeps `mid` as a candidate.
- When the bounds meet, the invariant identifies that one remaining index as the
  minimum. An unrotated array repeatedly moves `right` left and correctly lands
  at index 0.

Comparing against `nums[left]` is the tempting near miss. On an unrotated array,
`nums[mid] > nums[left]` is true, but moving right would walk away from the
minimum. Comparing against the right endpoint separates the larger run from the
wrapped smaller run without that ambiguity.

```text
nums = [4, 5, 6, 7, 0, 1, 2]

left=0 right=6 mid=3  7 > 2 -> minimum strictly right, left=4
left=4 right=6 mid=5  1 <=2 -> mid may be minimum, right=5
left=4 right=5 mid=4  0 <=1 -> mid may be minimum, right=4
return nums[4] = 0
```

## What Duplicates Remove

Distinct values made the sorted-half test decisive. With duplicates,
`nums[left] == nums[mid] == nums[right]` reveals nothing:

```text
[1, 0, 1, 1, 1]    rotation point is left of mid
[1, 1, 1, 0, 1]    rotation point is right of mid
```

The three inspected values are identical in both arrays, but the correct moves
are different. No comparison can recover information that is not present, so
[Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)
shrinks the ambiguous ends by one.

```python
def search_rotated_with_duplicates(nums: list[int], target: int) -> bool:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True

        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False


assert search_rotated_with_duplicates([2, 5, 6, 0, 0, 1, 2], 0) is True
assert search_rotated_with_duplicates([2, 5, 6, 0, 0, 1, 2], 3) is False
assert search_rotated_with_duplicates([1, 0, 1, 1, 1], 0) is True
assert search_rotated_with_duplicates([1, 1, 1, 1], 0) is False
```

Dropping the ends is safe because they equal `nums[mid]`, which remains in the
interval. If that shared value were the target, the equality check would already
have returned.

[Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)
compares only against `right`. On equality it can discard `right` because
`mid` keeps an equal value in play:

```python
def find_min_rotated_with_duplicates(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1

    return nums[left]


assert find_min_rotated_with_duplicates([1, 3, 5]) == 1
assert find_min_rotated_with_duplicates([2, 2, 2, 0, 1]) == 0
assert find_min_rotated_with_duplicates([3, 3, 1, 3]) == 1
assert find_min_rotated_with_duplicates([2, 2, 2]) == 2
```

Duplicates degrade the worst case to `O(n)`. An all-equal array with an absent
target sheds only one or two positions per iteration instead of half. The
algorithm is still correct; the input no longer provides enough information for
a guaranteed logarithmic choice.

## Mountain Arrays Use the Local Slope

[Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)
rises to one peak and then falls. It also has two sorted runs, but neither end
identifies the peak because both ends are small. The useful comparison is the
**local slope** between `mid` and `mid + 1`.

```python
def peak_index_in_mountain_array(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


assert peak_index_in_mountain_array([0, 1, 0]) == 1
assert peak_index_in_mountain_array([0, 2, 1, 0]) == 1
assert peak_index_in_mountain_array([0, 10, 5, 2]) == 1
assert peak_index_in_mountain_array([3, 4, 5, 1]) == 2
```

An upward slope proves the peak is strictly right of `mid`. A downward slope
means `mid` might be the peak, so it stays with `right = mid`. The read at
`mid + 1` is safe because `left < right` guarantees `mid < right`.

## Time and Space Complexity

| Approach                               | Time                                                                                                  | Space                                                   |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Rotated target search, distinct values | `O(log n)`: each sorted-half decision discards about half of `n` values                               | `O(1)`: only inclusive bounds and a midpoint are stored |
| Find minimum, distinct values          | `O(log n)`: the interval containing the rotation point halves each iteration                          | `O(1)`: the input is only read                          |
| Rotated search with duplicates         | `O(n)` worst case: equal endpoints may force one-position shrinking                                   | `O(1)`: ambiguity is handled by moving existing bounds  |
| Linear scan                            | `O(n)`: every position may be tested, which misses the required logarithmic target on distinct values | `O(1)`: one loop index is enough                        |
| Sort before searching                  | `O(n log n)`: sorting dominates and destroys the original index the target problem asks for           | `O(n)` auxiliary in Python's sort in the worst case     |

## Summary

- A **rotated sorted array** contains two sorted runs separated by one rotation
  point, so at least one half of every search interval is sorted.
- A target search first identifies the sorted half and then tests the target
  against both endpoints of that half.
  - The inclusive invariant is that the target, if present, remains in
    `[left, right]`.
  - Equality with `mid` is checked before containment, so both half ranges may
    exclude `mid`.
- Finding the minimum compares `nums[mid]` with `nums[right]` and keeps a
  possible answer with `right = mid`.
- Duplicate endpoints can make the two halves indistinguishable. Shrinking an
  ambiguous end preserves correctness but allows an `O(n)` worst case.
- A mountain array is split by direction rather than rotation, so its searchable
  signal is the local slope `arr[mid] < arr[mid + 1]`.

## Interview Checklist

```text
Am I searching for a target or for the rotation point?
Can I explain why at least one half is sorted?
Does the sorted-half test use <= so a one-element half counts?
Does target containment compare against both endpoints?
Do I test nums[mid] == target before excluding mid?
For the minimum, do I compare against nums[right]?
For the minimum, do I keep mid with right = mid?
Are duplicates allowed, and what makes the decision ambiguous?
Can I state the O(n) duplicate worst case?
Do rotation zero, one element, two elements, and an absent target work?
```
