# Merging And Inserting Intervals

A **disjoint interval set** is a list of intervals in which no two of them
overlap, kept sorted by their start. It is the interval world's version of a
normalized form: the same stretch of the number line can be described by a
hundred different overlapping intervals, but only one disjoint set describes it,
so once you have that set, questions like "how much total length is covered" or
"is the point 7 inside" become a single scan or a single binary search

**Merging** is the operation that produces one. You hand it a bag of intervals in
any order, possibly overlapping, possibly nested inside one another, and it hands
back the disjoint set covering exactly the same points

Think of a highlighter on a number line. You drag it across 1 to 3, then across 2
to 6, then across 8 to 10. Look at the paper afterwards and the first two strokes
are indistinguishable from one long stroke from 1 to 6, because ink over ink is
just ink. Three strokes went down and two marks came out. Merging is asking the
code to see what your eye sees

```text
           1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18
[1, 3]     [-------]
[2, 6]         [---------------]
[3, 4]             [---]
[8, 10]                                [-------]
[15, 18]                                                           [-----------]
```

Four of those five strokes are stacked over the region from 1 to 6, and the
disjoint set for the whole picture is `[[1, 6], [8, 10], [15, 18]]`. This topic
covers how to build that set, how to add one more interval to a set that is
already disjoint, and the two counting problems that are the same scan with the
output thrown away

## Why Comparing Every Pair Of Intervals Fails

The obvious idea uses the overlap test from
[interval basics](01_interval_basics.md) directly. Walk over every pair, and when
two intervals overlap, replace them with their union and delete one of them

```python
def merge_pairwise(intervals: list[list[int]]) -> list[list[int]]:
    out = [list(interval) for interval in intervals]
    i = 0
    while i < len(out):
        j = i + 1
        while j < len(out):
            if out[i][0] <= out[j][1] and out[j][0] <= out[i][1]:
                out[i] = [min(out[i][0], out[j][0]), max(out[i][1], out[j][1])]
                out.pop(j)
            else:
                j += 1
        i += 1
    return out


assert merge_pairwise([[1, 3], [2, 7], [6, 8]]) == [[1, 8]]
assert merge_pairwise([[1, 3], [6, 8], [2, 7]]) == [[1, 7], [6, 8]]
assert merge_pairwise([]) == []
```

Those two asserts hold the same three intervals in a different order, and the
second answer is wrong. `[1, 7]` and `[6, 8]` plainly overlap, so the output is
not a disjoint set at all

```text
         1   2   3   4   5   6   7   8
[1, 3]   [-------]
[6, 8]                       [-------]
[2, 7]       [-------------------]
```

Watch what the run does. It compares `[1, 3]` against `[6, 8]`, which do not
overlap, so nothing happens. It then compares `[1, 3]` against `[2, 7]`, which do
overlap, so those two collapse into `[1, 7]`. That merge has **created an overlap
that did not exist in the input**, because `[1, 7]` reaches 7 while neither `[1, 3]`
nor `[2, 7]` alone reached far enough to touch `[6, 8]`. The pair that now needs
merging is one the loop has already walked past

The failure is specific and it hands you the fix. Merging is not a local property
of a pair, because absorbing an interval pushes an endpoint outward and can wake
up a conflict behind you. Patching it by rerunning the whole sweep until nothing
changes is correct and costs `O(n³)`, since each sweep compares `O(n²)` pairs and
may retire only one interval

The real fix is to process the intervals in an order where **an endpoint can only
ever move to the right, and everything to the right is still ahead of you**

## Sorting By Start Makes Overlap A Local Question

Sort the intervals by their start. Now suppose you are partway through, holding
one **active block** that you are still growing, and you look at the next interval
in sorted order

- Its start is at least the active block's start, because that is what sorting by
  start guarantees, so it can never stick out on the left. The only way it can
  interact with the block is by overlapping its right end
- If its start is past the active block's end, the two are disjoint. Every
  interval after it has a start at least as large, so every one of those is past
  the block's end too. **The block can never grow again**, so you can close it and
  never look back
- If its start is not past the block's end, the two overlap, so the block absorbs
  it. Absorbing extends the block's end to the right at most, which is safe,
  because everything to the right is still unprocessed

That third bullet is exactly what killed the pairwise version, and it is now
harmless. Pushing the end rightward can only affect intervals you have not
reached yet, and you are about to reach them anyway

The block therefore only ever needs to be compared against one thing at a time,
which makes the whole job one linear pass after the sort

## The Merge Loop

```python
def merge(intervals: list[list[int]]) -> list[list[int]]:
    merged: list[list[int]] = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge([[1, 4], [4, 5]]) == [[1, 5]]
assert merge([[1, 10], [2, 3]]) == [[1, 10]]
assert merge([]) == []
```

**Four decisions in five lines**, and three of them are where the bugs live

- `sorted(intervals)` with no key sorts by start first and by end as a tie-break,
  because Python compares lists element by element. Only the start ordering is
  load-bearing here, since the argument above never used the end
- `merged[-1]` is the active block. There is no separate `current_start` and
  `current_end` pair to keep in sync, because the last element of the output *is*
  the block being grown, and finishing it means doing nothing more to it
- `max(merged[-1][1], end)` rather than plain `end` is the line people drop. When
  the next interval is entirely swallowed by the block, as `[2, 3]` is by
  `[1, 10]` in the third assert, its end is smaller and assigning it would shrink
  the block and lose coverage. Sorting by start says nothing about the ends, so a
  contained interval can appear at any point
- `merged and ...` guards the very first interval, since `merged[-1]` on an empty
  list raises `IndexError`. The empty-input assert is what catches this

## Tracing The Merge Over Five Intervals

Run `merge` on `[[8, 10], [1, 3], [2, 6], [3, 4], [15, 18]]`, which arrives
unsorted and contains one interval nested inside another. Sorting turns it into
`[[1, 3], [2, 6], [3, 4], [8, 10], [15, 18]]`, and each line below is one loop
iteration:

```text
interval    start <= block end?     action                     merged after
[1, 3]      no block yet            open the first block       [[1,3]]
[2, 6]      2 <= 3, overlaps        extend end 3 -> 6          [[1,6]]
[3, 4]      3 <= 6, overlaps        DISCARDED, max keeps 6     [[1,6]]
[8, 10]     8 > 6, disjoint         close block, open a new    [[1,6],[8,10]]
[15, 18]    15 > 10, disjoint       close block, open a new    [[1,6],[8,10],[15,18]]
```

The third line is the one worth remembering. `[3, 4]` passes the overlap test and
enters the merging branch, and then its end loses the `max` comparison and changes
nothing, so it is absorbed without a trace. Had that line been
`merged[-1][1] = end`, the block would have become `[1, 4]`, and the run would go
on to report `[8, 10]` and `[15, 18]` correctly while silently having lost the
region from 4 to 6

The fourth line is the other half of the argument. `[8, 10]` closes the block at
`[1, 6]` permanently, and the code expresses that permanence by simply appending a
new list and never touching `merged[-2]` again

## Whether Touching Intervals Merge Is A Question, Not A Fact

`[1, 4]` and `[4, 5]` share the single point 4. Merging them into `[1, 5]` is what
`start <= merged[-1][1]` does, and it is what
[Merge Intervals](https://leetcode.com/problems/merge-intervals/) wants. Change
that one character to `start < merged[-1][1]` and the two stay separate

Neither is right in general. The comparison encodes whether the endpoints are
**inclusive**, meaning the interval owns the point at its end, or **exclusive**,
meaning it stops just short of it. A meeting from 1 to 4 and a meeting from 4 to 5
do not conflict, because you walk out as the next person walks in, and a stretch
of road painted from 1 to 4 and another from 4 to 5 do form one painted stretch

> "Before I pick the comparison I want to check one case with you. If one interval
> ends at 4 and the next starts at 4, do those count as overlapping? For merging
> ranges I would use `<=` so they combine, but for booking a room I would use `<`
> so back-to-back bookings are allowed. I will go with `<=` unless you tell me
> otherwise."

Ask it once, in one sentence, and then write the operator you agreed on. Silently
picking one is how a solution that is entirely correct fails a third of the test
cases

## Dropping Intervals That Are Already Inside Another

[Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/)
asks how many intervals survive after deleting every interval that is contained
in another one. Interval `[c, d]` is **covered** by `[a, b]` when `a <= c` and
`d <= b`

```text
          1   2   3   4   5   6   7   8   9   10
kept      [-----------------------------------]
covered       [---]
```

This is the merge scan with the union step removed. Sort by start, keep a running
`kept_end` for the widest interval kept so far, and an interval survives only if
it reaches strictly further right than that

```python
def remove_covered_intervals(intervals: list[list[int]]) -> int:
    kept = 0
    kept_end = float("-inf")
    for start, end in sorted(intervals, key=lambda interval: (interval[0], -interval[1])):
        if end > kept_end:
            kept += 1
            kept_end = end
    return kept


assert remove_covered_intervals([[1, 4], [3, 6], [2, 8]]) == 2
assert remove_covered_intervals([[1, 4], [2, 3]]) == 1
assert remove_covered_intervals([[1, 4], [1, 10]]) == 1
assert remove_covered_intervals([]) == 0
```

The test is only `end > kept_end` and never mentions the starts, because sorting
by start already guarantees `kept_start <= start` for everything that comes after,
which is half of the covering condition. The scan only has to check the other half

**The `-interval[1]` tie-break is the whole difficulty of this problem.** Two
intervals can share a start, and then plain start-order leaves their relative
position to whatever `sorted` happens to do. The third assert is the case:
sorting `[[1, 4], [1, 10]]` by start alone can put `[1, 4]` first, which sets
`kept_end` to 4, and then `[1, 10]` has `10 > 4` and is also kept, giving 2 when
the answer is 1, since `[1, 4]` sits entirely inside `[1, 10]`. Sorting the ends
descending within a shared start puts the widest interval first, so everything it
covers arrives afterwards and fails the test

## Counting Removals Instead Of Building A Set

[Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
asks for the smallest number of intervals to delete so that the rest are pairwise
disjoint. Deleting the fewest is the same as **keeping the most**, which is the
earliest-finish-first scheduling problem that
[interval greedy](../../12_greedy_algorithms/notes/03_interval_greedy.md) proves
by an exchange argument: whatever an optimal schedule does first, swapping in the
interval that finishes soonest leaves at least as much room, so it is never worse

So sort by end, keep an interval whenever it starts at or after the last kept end,
and subtract

```python
def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    kept = 0
    kept_end = float("-inf")
    for start, end in sorted(intervals, key=lambda interval: interval[1]):
        if start >= kept_end:
            kept += 1
            kept_end = end
    return len(intervals) - kept


assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
assert erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2
assert erase_overlap_intervals([[1, 2], [2, 3]]) == 0
assert erase_overlap_intervals([]) == 0
```

**This is the near-miss to `merge`, and confusing the two is the standard mistake
in this module.** Both sort, both scan once, both hold a single running end, and
they answer opposite questions

- `merge` sorts by **start**, and on an overlap it **grows** the block with
  `max`, because it must not lose coverage
- `erase_overlap_intervals` sorts by **end**, and on an overlap it **drops** the
  new interval entirely, because keeping the one that finishes earliest is what
  leaves the most room for the rest

Note the third assert. `[1, 2]` and `[2, 3]` are back-to-back, and here `start >= kept_end` treats them as compatible, which is the opposite endpoint convention
from the `<=` in `merge`. That is not an inconsistency, it is the same question
from the previous section answered differently by two different problems, which is
why it is worth asking

## Keeping The Set Disjoint As Numbers Arrive One At A Time

[Data Stream As Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)
turns merging into a **design problem**. Integers arrive one at a time through
`add_num`, and `get_intervals` must return the disjoint set summarizing everything
seen so far. Collecting the numbers and merging from scratch on every query is
correct and re-does all the work each time

The better version keeps the disjoint set as the only state and repairs it at each
insertion. A single number `v` is the interval `[v, v]`, and it can interact with
at most two stored intervals, the one immediately to its left and the one
immediately to its right, since everything else is strictly further away. So find
that position by binary search and check both neighbours

Two integers merge when they are **adjacent**, not only when they overlap: adding
2 to a set holding `[1, 1]` and `[3, 3]` must produce `[1, 3]`, because these are
integers and there is nothing between 1 and 3 left uncovered. That is why the
tests below compare against `value - 1` and `value + 1` rather than against
`value`

```python
from bisect import bisect_left


class SummaryRanges:
    def __init__(self) -> None:
        self.intervals: list[list[int]] = []

    def add_num(self, value: int) -> None:
        intervals = self.intervals
        i = bisect_left(intervals, value, key=lambda interval: interval[0])
        if i < len(intervals) and intervals[i][0] == value:
            return
        if i > 0 and intervals[i - 1][1] >= value:
            return
        if i > 0 and intervals[i - 1][1] == value - 1:
            i -= 1
            intervals[i][1] = value
        else:
            intervals.insert(i, [value, value])
        if i + 1 < len(intervals) and intervals[i][1] + 1 == intervals[i + 1][0]:
            intervals[i][1] = intervals[i + 1][1]
            intervals.pop(i + 1)

    def get_intervals(self) -> list[list[int]]:
        return [list(interval) for interval in self.intervals]


stream = SummaryRanges()
stream.add_num(1)
assert stream.get_intervals() == [[1, 1]]
stream.add_num(3)
assert stream.get_intervals() == [[1, 1], [3, 3]]
stream.add_num(7)
assert stream.get_intervals() == [[1, 1], [3, 3], [7, 7]]
stream.add_num(2)
assert stream.get_intervals() == [[1, 3], [7, 7]]
stream.add_num(6)
assert stream.get_intervals() == [[1, 3], [6, 7]]

repeated = SummaryRanges()
repeated.add_num(5)
repeated.add_num(5)
assert repeated.get_intervals() == [[5, 5]]
assert SummaryRanges().get_intervals() == []
```

`bisect_left` with `key=lambda interval: interval[0]` returns the index of the
first stored interval whose start is at least `value`, so `intervals[i - 1]` is
the neighbour on the left and `intervals[i]` is the neighbour on the right. The
`key` parameter searches by start without building a parallel list of starts, and
it needs Python 3.10 or later

**The two early returns are the duplicate handling**, and this is the case
interviewers add on purpose. A repeated number must leave the set untouched, and
it can already be present in two ways: `intervals[i][0] == value` means it is the
start of an existing interval, and `intervals[i - 1][1] >= value` means it is
somewhere inside the interval on the left. Without both checks, adding 5 twice
either duplicates `[5, 5]` or widens a neighbour it was already inside

**The `i -= 1` is what makes the second half work.** Once the left neighbour has
absorbed the value, the interval to keep growing is that neighbour rather than
anything at the original index, so the index moves back to point at it. The final
block then runs identically whether the value extended a neighbour or was inserted
as its own interval, which is why there is one right-side check and not two

Adding 2 to `[[1, 1], [3, 3], [7, 7]]` exercises every branch at once. The search
puts `i` at 1, the left neighbour ends at 1 which is `value - 1`, so `i` becomes 0
and `[1, 1]` grows to `[1, 2]`. Then the right check sees `2 + 1 == 3`, so
`[1, 2]` swallows `[3, 3]` into `[1, 3]` and the now-duplicate entry is popped.
Three stored intervals become two from a single insertion

## Worked Example: [Insert Interval](https://leetcode.com/problems/insert-interval/)

You are given a list of intervals that is **already sorted by start and already
disjoint**, plus one new interval. Return the list you would get by adding the new
interval and merging whatever it now overlaps

**Input**:

- `intervals`, a `list[list[int]]` where each element is a two-element list
  `[start, end]` with `start <= end`. The list is sorted by start, no two of its
  intervals overlap, and it may be empty
- `new_interval`, a `list[int]` of the form `[start, end]`, also with
  `start <= end`, under no constraint about where it falls relative to the others

**Output**: a `list[list[int]]` that is again sorted by start and disjoint, and
that covers exactly the points covered by `intervals` together with
`new_interval`. Its length is between 1 and `len(intervals) + 1`, since the new
interval either merges with something or becomes a new entry of its own

The phrase that decides the approach is "already sorted and disjoint". Appending
`new_interval` and calling `merge` returns the right answer, and it throws away
that guarantee to pay `O(n log n)` for a sort of a list that arrived sorted. An
input that is already in the order you wanted is an invitation to a single linear
pass

Because the stored intervals are disjoint and sorted, they split into exactly
three runs relative to the new interval: the ones that finish before it starts,
then a contiguous run that touches it, then the ones that begin after it ends.
Those runs are contiguous, so one left-to-right walk handles each in its own loop
with no branching inside

> "The input is already sorted and disjoint, so I do not need to sort. I will
> walk it once in three phases: copy everything that ends before the new interval
> starts, then absorb everything that touches it by widening my working interval
> with `min` on the start and `max` on the end, then append the working interval
> and copy the rest."

1. Take `start, end` out of `new_interval` into two local variables. These are the
   **working interval**, and they will widen as intervals are absorbed, so the
   original list is never mutated and the caller's data survives
2. In the first phase, copy across every interval whose end is strictly less than
   `start`. Those sit entirely to the left with a gap, and no later interval can
   change that, so they go into the output untouched and in order
3. Stop that phase at the first interval whose end reaches `start`. This is where
   the overlapping run begins, and it may be empty, which is the case where the
   new interval drops into a gap
4. In the second phase, absorb every interval whose **start** is at most `end`.
   Each absorbed interval widens the working interval with `min` on the start and
   `max` on the end, and the `max` matters for the same reason it did in `merge`,
   because a stored interval can be entirely swallowed and must not shrink the
   working end
5. The `end` being tested in that loop condition is the widening one, not the
   original. That is what lets the absorption chain: swallowing one interval can
   push `end` far enough right to reach the next, exactly the effect that broke
   the pairwise merge and that a left-to-right walk handles for free
6. Stop that phase at the first interval whose start is beyond the current `end`.
   Everything from there on starts later still, because the input is sorted, so
   nothing further can touch the working interval
7. Append the working interval, which is now the union of the new interval and
   everything it reached, then copy the remaining tail across unchanged

```python
def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    start, end = new_interval
    out: list[list[int]] = []
    i, n = 0, len(intervals)
    while i < n and intervals[i][1] < start:
        out.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    out.append([start, end])
    out.extend(intervals[i:])
    return out


assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
assert insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
assert insert([], [5, 7]) == [[5, 7]]
assert insert([[1, 5]], [2, 3]) == [[1, 5]]
assert insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
```

Tracing the second assert, where `[4, 8]` goes into
`[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]`:

```text
phase  interval    test                       working interval   action
1      [1, 2]      end 2 < start 4            [4, 8]             copied out, still to the left
1      [3, 5]      end 5 not < 4              [4, 8]             phase 1 ends here
2      [3, 5]      start 3 <= end 8           [3, 8]             absorbed, start pulled left
2      [6, 7]      start 6 <= end 8           [3, 8]             DISCARDED, max keeps 8
2      [8, 10]     start 8 <= end 8           [3, 10]            absorbed, end pushed right
2      [12, 16]    start 12 > end 10          [3, 10]            phase 2 ends here
-      -           -                          [3, 10]            append, then copy the tail
```

`[6, 7]` is the discarded step. It sits entirely inside the working interval, so
both `min` and `max` keep what they had and the absorption is invisible in the
state. Replacing `max(end, intervals[i][1])` with `intervals[i][1]` would set the
working end to 7 here, and the very next line would then test `8 <= 7`, fail, and
stop the phase early, leaving `[8, 10]` in the output beside `[3, 7]` when the two
should have been one interval

`[8, 10]` is the line that proves the loop condition must read the widening `end`.
Against the original `[4, 8]` the test `8 <= 8` only passes because `end` is still
8, and after absorbing it the working interval reaches 10, which is what makes
`[12, 16]` the correct stopping point rather than the second thing absorbed

- **Time Complexity:** `O(n)` for `n` stored intervals, because each interval is
  examined by exactly one of the three phases and copied at most once, and the
  input arriving sorted is what removes the `O(n log n)` a sort would cost
- **Space Complexity:** `O(n)` for the output list, which holds at most `n + 1`
  intervals when the new one overlaps nothing. Beyond the output nothing is
  allocated, since the working interval is two integers and the tail is copied by
  reference into the same list

## Time and Space Complexity

Throughout, `n` is the number of intervals. `sorted` allocates a new list of `n`
references and so contributes `O(n)` space in every row that uses it

**Building a disjoint set from a bag of intervals**

| Approach                                                  | Time                                                                                                                           | Space                                                                                      |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Sort by start, one pass (`merge`)                         | `O(n log n)`: the sort dominates, since the pass after it visits each of the `n` intervals once and does `O(1)` work per visit | `O(n)`: the output holds all `n` intervals when none of them overlap, plus the sorted copy |
| Merging overlapping pairs in one sweep (`merge_pairwise`) | `O(n²)`: every pair is compared, and this is the version that returns a non-disjoint answer, so the cost buys a wrong result   | `O(n)`: one working copy of the list, shrinking as intervals are absorbed                  |
| Repeating that sweep until nothing changes                | `O(n³)`: each sweep is `O(n²)` and may retire only one interval, so up to `n` sweeps run before the list stabilises            | `O(n)`: the same single working copy, since the cost is repeated work rather than storage  |

**Inserting one interval into a set that is already sorted and disjoint**

| Approach                                          | Time                                                                                                                | Space                                                                                         |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Three-phase single pass (`insert`)                | `O(n)`: each interval falls in exactly one phase and is touched once, with no sort because the input arrives sorted | `O(n)`: the output list, holding up to `n + 1` intervals when the new one merges with nothing |
| Appending the new interval and re-running `merge` | `O(n log n)`: correct, but it pays for a sort of a list that was already in order                                   | `O(n)`: the same output, plus the sort's copy of `n + 1` references                           |

**Counting scans over the same sorted pass**

| Approach                                               | Time                                                                                              | Space                                                                                     |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `erase_overlap_intervals`, sorting by end              | `O(n log n)`: the sort, then one pass doing a comparison and at most two assignments per interval | `O(n)`: only the sorted copy, since the state is two integers and no output list is built |
| `remove_covered_intervals`, sorting by `(start, -end)` | `O(n log n)`: the same shape, with a tuple key that costs `O(1)` per comparison                   | `O(n)`: only the sorted copy, for the same reason                                         |

**`SummaryRanges` over a stream**, where `n` is the number of disjoint intervals
currently stored, which is at most the number of `add_num` calls so far

| Operation                                              | Time                                                                                                                                                     | Space                                                                                          |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `add_num`                                              | `O(n)`: `bisect_left` locates the position in `O(log n)`, but `list.insert` and `list.pop` shift every element after it, and that shift is the real cost | `O(1)`: it mutates the stored list in place and allocates at most one new two-element interval |
| `get_intervals`                                        | `O(n)`: it copies each stored interval so the caller cannot mutate the internal state                                                                    | `O(n)`: the returned copy, which is the output rather than auxiliary space                     |
| Storing every number and merging on each query instead | `O(m log m)` per query for `m` numbers seen: it re-sorts and re-merges the entire history every time `get_intervals` is called                           | `O(m)`: the full history is kept rather than only the `n` intervals summarizing it             |

## Summary

- A **disjoint interval set** is a list of non-overlapping intervals kept sorted
  by start, and it is the canonical form of a region of the number line. Merging
  is the operation that turns an arbitrary bag of intervals into one, which is why
  it is the first thing most interval problems do
  - Think of overlapping highlighter strokes, where ink over ink is
    indistinguishable from one longer stroke
- Merging cannot be done by comparing pairs, because absorbing an interval pushes
  an endpoint outward and can create an overlap with an interval the loop has
  already passed. Sorting by start removes that possibility, since an endpoint can
  then only ever move right, and everything to the right is still unprocessed
  - Concretely, `[1, 3]` and `[2, 7]` merge into `[1, 7]`, which now overlaps a
    `[6, 8]` that neither of them touched before
- The merge loop keeps the active block as `merged[-1]` rather than as a separate
  pair of variables, extends it with `merged[-1][1] = max(merged[-1][1], end)` on
  an overlap, and appends a fresh block otherwise
  - The `max` is not decoration. Sorting by start says nothing about the ends, so
    a fully contained interval such as `[2, 3]` inside `[1, 10]` can arrive at any
    time, and assigning its end directly would shrink the block and lose coverage
  - The `merged and ...` guard exists only for the first iteration, and an empty
    input is what exposes its absence
- Whether `[1, 4]` and `[4, 5]` merge is a clarifying question rather than a rule.
  `start <= merged[-1][1]` treats touching endpoints as overlapping, which is what
  Merge Intervals wants, while `<` keeps them apart, which is what a room booking
  wants. Ask it in one sentence before writing the comparison
- **Insert Interval** exploits an input that is already sorted and disjoint to run
  in `O(n)` with no sort, by splitting the list into three contiguous runs: the
  intervals ending before the new one starts, the run touching it, and the
  intervals starting after it ends
  - The second loop tests against the *widening* `end`, which is what lets one
    absorption reach the next interval, and it uses `min` on the start and `max`
    on the end for the same containment reason as `merge`
  - Appending the new interval and re-running `merge` is a correct answer that
    costs `O(n log n)` and throws away the guarantee the problem handed you
- The same sorted single pass answers counting questions when the output set is
  discarded, and the sort key is what distinguishes them
  - **Non-overlapping Intervals** sorts by **end** and drops any interval starting
    before the last kept end, because earliest-finish-first keeps the most
    intervals by the exchange argument, and the answer is `len(intervals) - kept`
  - **Remove Covered Intervals** sorts by `(start, -end)` and keeps an interval
    only when its end is strictly past the widest end kept so far. The descending
    end tie-break is mandatory, since two intervals sharing a start would otherwise
    both be counted when one contains the other
- **Data Stream As Disjoint Intervals** maintains the set incrementally. A single
  integer touches at most its two neighbours, found with `bisect_left` on the
  starts, so each insertion is a local repair rather than a full re-merge
  - Integers merge when **adjacent**, so the checks compare against `value - 1` and
    `value + 1`, and adding 2 to `[1, 1]` and `[3, 3]` must yield `[1, 3]`
  - Duplicates must leave the set untouched, and a repeated value can be either the
    start of a stored interval or somewhere inside the interval on its left, so
    both cases need an early return
  - `add_num` is `O(n)` and not `O(log n)`, because `list.insert` shifts the tail
    even though the binary search that found the position was logarithmic

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
Am I building a disjoint set (merge), adding one interval to an existing one (insert), or just counting?
Do touching endpoints like [1,4] and [4,5] merge here, and have I asked rather than guessed?
Am I sorting by start (merging, covering) or by end (keeping the most intervals)?
Do equal starts need a descending-end tie-break so a wider interval is seen first?
On an overlap, do I extend with max(current_end, end) rather than assigning end directly?
Is the input already sorted and disjoint, which turns an O(n log n) sort into an O(n) walk?
Does my loop condition read the widening end, so one absorption can chain into the next?
What does my code do on empty input, on a single interval, and on two identical intervals?
For a streaming version, which neighbours can a new value touch, and are adjacent integers merged?
Did I state that the sort dominates the time, and that the output list is the space?
```
