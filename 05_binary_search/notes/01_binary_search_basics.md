# Binary Search Basics

**Binary search** finds a value by repeatedly cutting an ordered search space in
half. A left-to-right scan settles one value per comparison. Binary search uses
the order to settle an entire half at once.

Suppose the target is 9:

```text
index   0   1   2   3   4   5   6   7
value  -4   1   3   7   9  12  20  31
        ^           ^               ^
      left         mid            right
```

The values are sorted, so comparing against 7 proves more than “index 3 is not
the answer.” It proves that indices 0 through 3 are all too small. The remaining
positions are the **search space**, meaning the candidates that could still hold
the answer.

The same idea works whenever one probe can rule out a whole side. The probe may
be an array read, a call to an API that says “higher” or “lower,” or a check on a
number that might be the answer.

## When to Use

Binary search is a good fit when:

- The input is sorted and you need to locate a value or position.
- The problem asks for `O(log n)` time, which usually signals that the search
  space should be halved.
- A comparison or API call tells you which side can no longer contain the
  answer.
- A matrix can be viewed as one sorted sequence.

Do not use it merely because an array exists. If the values have no usable order,
a middle probe says nothing about either side. Sorting first costs
`O(n log n)`, so it is not worthwhile for one lookup unless changing the input
is already part of the problem.

Binary search is also different from
[opposite-end pointers](../../02_two_pointers/notes/01_opposite_end_pointers.md).
Two pointers usually move one position at a time for an `O(n)` scan. Binary
search jumps beyond `mid` and gets `O(log n)` because it removes about half of
the remaining candidates.

## The Inclusive Exact-Match Search

[Binary Search](https://leetcode.com/problems/binary-search/) returns any index
holding `target`, or `-1` when the target is absent.

```python
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

This loop uses **inclusive bounds**, so both `left` and `right` are live
candidates. Its invariant is:

> If `target` exists, it is somewhere inside `nums[left:right + 1]`.

Every update must preserve that statement:

- When `nums[mid] < target`, sortedness proves every index through `mid` is too
  small. Setting `left = mid + 1` cannot discard the answer.
- When `nums[mid] > target`, every index from `mid` onward is too large. Setting
  `right = mid - 1` is safe for the mirrored reason.
- Both moves exclude `mid` because it was just tested and rejected. Writing
  `left = mid` can repeat the same midpoint forever on a two-element window.
- The condition is `left <= right` because `left == right` represents one
  candidate, not an empty search space.

On `[-4, 1, 3, 7, 9, 12, 20, 31]` with target 9:

```text
left=0 right=7 mid=3 value=7   too small -> discard 0..3
left=4 right=7 mid=5 value=12  too large -> discard 5..7
left=4 right=4 mid=4 value=9   found -> return 4
```

The rejected probe at index 5 is the useful step. Comparing only with 12 removes
12, 20, and 31, so those last two values are never read. For an absent target,
the bounds eventually cross. At that point the candidate region is empty, and
the invariant proves that returning `-1` is correct.

The subtraction form of the midpoint is worth using by habit. Python integers do
not overflow, but `left + right` can overflow a fixed-width integer in languages
such as Java or C++. The expression
`left + (right - left) // 2` avoids that addition while choosing the same lower
midpoint.

## Where the Left Bound Lands

[Search Insert Position](https://leetcode.com/problems/search-insert-position/)
asks where `target` belongs if it is missing. The exact loop already computes
that position:

```python
def search_insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left
```

The equality case moves `right` because an equal value is a valid insertion
position, but an earlier equal value may exist. On exit, every index below
`left` is smaller than `target` and every index above `right` is greater than or
equal to it. Since `left == right + 1`, `left` is the first legal insertion
position.

An empty list returns 0. A target smaller than every value also returns 0, while
a target larger than every value returns `len(nums)`. The next note generalizes
this “first position where a condition holds” idea into
[boundary search](02_boundary_search.md).

## Searching Through a Comparison API

[Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)
shows that an array is optional. The function `guess(value)` returns 0 for a
match, 1 when the hidden number is higher, and -1 when it is lower.

```python
from collections.abc import Callable


def guess_number(n: int, guess: Callable[[int], int]) -> int:
    left, right = 1, n

    while left <= right:
        mid = left + (right - left) // 2
        verdict = guess(mid)
        if verdict == 0:
            return mid
        if verdict > 0:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

The candidates are the values 1 through `n` rather than array indices. The
invariant is unchanged: the hidden number, if it exists under the API contract,
remains inside the inclusive range `[left, right]`.

## Worked Example: [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

The matrix has two ordering guarantees. Every row is sorted, and the first value
of each row is greater than the last value of the previous row. Therefore,
reading row by row produces one sorted sequence:

```text
                 flat index
[  1   3   5   7 ]    0  1  2  3
[ 10  11  16  20 ]    4  5  6  7
[ 23  30  34  60 ]    8  9 10 11
```

Copying those values into a new list would make ordinary binary search obvious,
but it would spend `O(mn)` time and space before a logarithmic search even
began. The better move is to search the **virtual flattened indices** from 0
through `rows * cols - 1`.

A flat index `i` maps back to the matrix with
`row, col = divmod(i, cols)`. Division counts how many full rows fit before
`i`, and the remainder gives the column. The divisor must be the number of
columns, which is easy to get wrong on a rectangular matrix.

> “I will treat the matrix as one sorted array without copying it. My bounds are
> inclusive flat indices, and if the target exists it remains inside that flat
> interval. Each probe converts back with `divmod(mid, cols)`.”

```python
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = left + (right - left) // 2
        row, col = divmod(mid, cols)
        value = matrix[row][col]

        if value == target:
            return True
        if value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
```

Searching the matrix above for 16 gives:

```text
left=0 right=11 mid=5 -> (1,1)=11  too small -> discard flat 0..5
left=6 right=11 mid=8 -> (2,0)=23  too large -> discard flat 8..11
left=6 right=7  mid=6 -> (1,2)=16  found
```

The second probe is the rejected candidate to notice. It lands in another row
and discards the entire bottom row from flat index 8 onward. The code never
needs to treat a row boundary specially because the problem's two guarantees
make that boundary part of one sorted order.

- **Time Complexity:** `O(log(mn))` for `m` rows and `n` columns, because the
  virtual range contains `mn` positions and halves each iteration.
- **Space Complexity:** `O(1)` auxiliary space, because the coordinate is
  computed on demand and no flattened copy is built.

## When Rows Do Not Chain Together

[Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)
only promises that each row and each column is sorted. Flattening is invalid
because the end of one row may be larger than the start of the next.

Start at the top-right corner instead. It is the largest value in its row and the
smallest value in its column. A value larger than `target` removes the whole
column by moving left, while a smaller value removes the whole row by moving
down.

```python
def search_matrix_ii(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        value = matrix[row][col]
        if value == target:
            return True
        if value > target:
            col -= 1
        else:
            row += 1

    return False
```

Starting at the top-left is the near miss. When that smallest corner is below the
target, the answer could be either right or down, so no side can be discarded.
Top-right works because its two legal moves change the value in opposite
directions.

## Time and Space Complexity

| Approach                 | Time                                                                                   | Space                                                            |
| ------------------------ | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Exact binary search      | `O(log n)`: the inclusive candidate interval halves after each probe                   | `O(1)`: the loop keeps only `left`, `right`, and `mid`           |
| Linear search            | `O(n)`: an absent target forces every one of the `n` values to be read                 | `O(1)`: one loop index is enough                                 |
| Flattened matrix search  | `O(log(mn))`: binary search halves `mn` virtual positions for `m` rows and `n` columns | `O(1)`: `divmod` computes coordinates without copying the matrix |
| Matrix staircase         | `O(m + n)`: each probe permanently removes one row or one column                       | `O(1)`: only a row and column index are stored                   |
| Copy matrix, then search | `O(mn)`: copying every cell dominates the later logarithmic search                     | `O(mn)`: the flattened list duplicates all matrix values         |

## Summary

- **Binary search** keeps a search space of possible answers, probes its middle,
  and discards a whole side when ordering proves that side cannot contain the
  target.
- Exact search uses inclusive bounds `[left, right]` and the invariant that, if
  the target exists, it remains inside those bounds.
  - The loop condition is `left <= right` because a one-element range still has
    to be tested.
  - Both updates step past `mid` because it was already rejected, which also
    guarantees that the range shrinks.
- Returning `left` after the bounds cross gives the first position whose value
  is greater than or equal to the target, which is its sorted insertion point.
- A comparison API can replace an array read because binary search needs an
  ordered candidate space and a direction, not necessarily stored values.
- A matrix whose rows chain together can be searched as `mn` virtual positions
  with `divmod(mid, cols)`. A matrix whose rows and columns are only
  independently sorted needs the `O(m + n)` staircase instead.

## Interview Checklist

```text
Why can one probe discard an entire side?
Are my bounds inclusive or half-open, and what candidates remain possible?
Does the loop test a one-element search space?
Does every update remove mid and therefore guarantee progress?
What do left and right mean after an unsuccessful search?
Should absence return -1, False, or the insertion position?
Could left + right overflow in the interview language?
For a matrix, do the rows chain into one sorted sequence?
Does divmod use the column count?
Have I checked empty, one-element, hit, and absent cases?
```
