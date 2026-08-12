# Time and Space Complexity

**Complexity analysis** describes how an algorithm's work and memory grow as
the input grows. It does not predict an exact number of milliseconds. Instead,
it lets you compare approaches independently of the laptop, programming
language, and particular small input used in a test.

We write that growth with **Big-O notation**. If `n` is the number of input
items, `O(n)` means the work grows in direct proportion to `n`, while `O(n²)`
means it can grow in proportion to the number of pairs of items.

## Start by Naming the Input

The symbol inside Big-O must have a meaning. For a single list, `n` usually
means its length. Two independent inputs may need two symbols: scanning a list
of `n` words and a list of `m` queries costs `O(n + m)`, not automatically
`O(n)`.

Other symbols appear when they describe the input more precisely:

```text
n = number of items in one input
m = number of items in a second independent input
k = requested result size, window width, or another stated quantity
h = height of a tree
V = number of graph vertices
E = number of graph edges
```

Define the symbols when you state the result. "Linear" is incomplete if the
interviewer cannot tell what is being counted.

## Count Work, Not Syntax

Consider a scan that counts positive values:

```python
def count_positive(nums: list[int]) -> int:
    count = 0
    for value in nums:
        if value > 0:
            count += 1
    return count


assert count_positive([-2, 0, 4, 7]) == 2
```

Let `n` be `len(nums)`. The loop inspects every element once, and each inspection
does a fixed amount of work. The runtime is therefore `O(n)`. It does not matter
that the body has a comparison and an addition; doubling `n` still roughly
doubles the number of visits.

Big-O keeps the fastest-growing term and drops constant factors. A function that
makes two complete passes performs `2n` visits, but we write `O(n)`. A function
that performs `n² + n` visits is `O(n²)`, because the square term dominates as
`n` grows.

Sequential loops add their costs:

```python
def totals(a: list[int], b: list[int]) -> tuple[int, int]:
    left_total = 0
    for value in a:
        left_total += value

    right_total = 0
    for value in b:
        right_total += value

    return left_total, right_total


assert totals([1, 2], [10, 20, 30]) == (3, 60)
```

If `a` has `n` items and `b` has `m`, the work is `O(n + m)`. The loops are one
after another, so their costs add. They would multiply only if one loop ran
inside the other.

## Nested Work Depends on What the Loops Actually Visit

This function examines every unordered pair:

```python
def all_pairs(nums: list[int]) -> list[tuple[int, int]]:
    pairs: list[tuple[int, int]] = []
    for left in range(len(nums)):
        for right in range(left + 1, len(nums)):
            pairs.append((nums[left], nums[right]))
    return pairs


assert all_pairs([1, 2, 3]) == [(1, 2), (1, 3), (2, 3)]
```

For `n` values, the result contains `n(n - 1) / 2` pairs. Big-O drops the
constant one-half and lower-order term, leaving `O(n²)` time. This is quadratic
because the code visits pairs, not merely because two loops are visible.

The reverse warning matters too: nested loops are not automatically `O(n²)`.
If an inner `while` advances a pointer that never moves backward, that pointer
can move at most `n` times across the entire run. Later two-pointer and sliding
window notes use this counting argument repeatedly.

## Halving Produces a Logarithm

Suppose the remaining search range has sizes:

```text
64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
```

It takes six halvings to reduce 64 items to one. For 128 items it takes seven.
The number of times you can divide `n` by two before reaching one is `log₂ n`,
so repeatedly halving a search space costs `O(log n)`. Big-O normally writes
`O(log n)` without the base, because changing the logarithm's base changes only
a constant factor.

Sorting comparison-based values costs `O(n log n)` in the general case: there
are logarithmically many levels of organization, and each level handles `n`
items. You may use that cost for Python's `sorted` and `list.sort()` in an
interview unless the problem gives a special value range that supports another
method.

## Worst Case Is the Default

Unless asked otherwise, state the worst-case complexity. A linear search might
find its target at index `0`, but it may inspect every element when the target is
last or absent, so its worst-case time is `O(n)`.

Hash-table operations such as dictionary and set lookup are normally described
as `O(1)` average case. Their collision-heavy theoretical worst case is `O(n)`.
Say "average" when that distinction matters; the next note records the common
Python operation costs precisely.

## Space Means Memory That Grows

**Space complexity** counts memory whose amount depends on the input. A few
integer variables use `O(1)` space because their count does not grow with `n`.
A set that may store every input value uses `O(n)` space.

Separate two useful measurements:

- **Output space** holds the result the caller requested.
- **Auxiliary space** is extra working memory used to compute that result.

```python
def doubled(nums: list[int]) -> list[int]:
    result: list[int] = []
    for value in nums:
        result.append(value * 2)
    return result


assert doubled([2, 5, 9]) == [4, 10, 18]
```

The returned list uses `O(n)` output space. Apart from that result, the function
keeps only a fixed number of names, so its auxiliary space is `O(1)`. If the
interviewer asks simply for "space," state which convention you are using.

A recursive call also consumes memory. If at most `h` calls are active at once,
the call stack uses `O(h)` auxiliary space even when no explicit container
appears in the code.

## Amortized Cost Spreads Rare Work Across Many Operations

An **amortized** bound describes the average cost per operation over a sequence,
without assuming random input. Python list append is the standard example.

Most appends place the new value into already allocated room. Occasionally the
list runs out of room and allocates a larger backing array, copying the existing
references. That one append costs `O(n)`, but the extra capacity means the copy
does not happen on every append. Across `n` appends, the total copying remains
`O(n)`, so each append is `O(1)` amortized.

Amortized is not the same as average case:

- **Average-case analysis** depends on assumptions about which inputs occur,
  such as well-distributed hash keys.
- **Amortized analysis** gives a bound for the whole operation sequence, even if
  one particular operation is expensive.

The same idea proves many loops linear. If each item enters a container once and
leaves at most once, there can be at most `n` insertions and `n` removals across
the entire algorithm. An inner removal loop may be expensive on one iteration,
but all removals together are `O(n)`.

## Common Growth Rates

| Growth       | What it usually means                              | Consequence as `n` grows                                |
| ------------ | -------------------------------------------------- | ------------------------------------------------------- |
| `O(1)`       | A fixed amount of work independent of input length | Input size does not add more steps                      |
| `O(log n)`   | The remaining possibilities are repeatedly divided | Growth is slow because doubling `n` adds about one step |
| `O(n)`       | Every item is handled a constant number of times   | Doubling `n` roughly doubles the work                   |
| `O(n log n)` | Sorting or divide-and-combine work                 | Often the best general bound when ordering is required  |
| `O(n²)`      | Many or all pairs are examined                     | Large inputs become expensive quickly                   |
| `O(2ⁿ)`      | Every subset may be explored                       | Practical input sizes must be small                     |
| `O(n!)`      | Every ordering may be explored                     | Growth is even faster than exponential                  |

These are descriptions, not targets. A correct `O(n²)` solution may be the right
starting point, and constraints tell you whether it is fast enough.

## Summary

- Big-O describes how work or memory grows with a named input size; it does not
  predict exact runtime on a particular machine.
- Count what the algorithm visits. Sequential work adds, genuinely nested work
  multiplies, and a pointer that only moves forward can move at most `n` times.
- Drop constants and lower-order terms only after deriving the full count, which
  is why `2n` becomes `O(n)` and `n² + n` becomes `O(n²)`.
- Auxiliary space excludes the required output and includes hidden memory such
  as active recursive calls.
- An amortized `O(1)` operation may occasionally cost `O(n)`; the bound comes
  from spreading that rare work across the complete sequence.

## Complexity Checklist

```text
What does each symbol such as n, m, k, h, V, or E mean here?
What work is repeated, and how many total times can it happen?
Do sequential inputs need O(n + m) instead of collapsing to O(n)?
Is a nested loop revisiting pairs, or are its pointers bounded across the run?
What is the worst input allowed by the problem?
Which containers or call frames grow with the input?
Am I reporting total space, auxiliary space, or both?
If I say amortized, can I bound the total work across the sequence?
```
