# Interval Basics

An **interval** is a pair of numbers `[start, end]` that stands for every point
between them. It is one element of your input, but unlike an integer or a
character it occupies a stretch of the number line rather than a single spot, so
two of them can miss each other, touch, cross, or swallow one another whole.
Every problem in this module is about those relationships

```text
        0    1    2    3    4    5    6    7    8    9
        |    |    |    |    |    |    |    |    |    |
   a         [=========]                                  a = [1, 3]
   b                   [==============]                   b = [3, 6]
   c                                       [====]         c = [7, 8]
```

Everything you already know how to do to an array of numbers still applies, since
an interval list is a list of two-element lists. The new part is that each element
carries **two coordinates that are not interchangeable**. The `start` says when a
thing begins and the `end` says when it stops, and almost every interval bug comes
from sorting by one of them while reasoning about the other

The other thing to pin down before writing code is what the two endpoints
themselves mean. A **closed** interval `[1, 3]` contains both 1 and 3, so `[1, 3]`
and `[3, 5]` share the single point 3. A **half-open** interval `[1, 3)` contains 1
but stops just short of 3, so the same two intervals touch without sharing
anything. LeetCode uses closed intervals for balloons and for interval lists, and
half-open ones for meetings, where a meeting ending at 3 and one starting at 3 do
not clash. Nothing in the code changes except a `<=` becoming a `<`, and getting
that one character wrong is the difference between a correct answer and an
off-by-one that only shows up on touching inputs

> "Before I code, are these endpoints inclusive? If a meeting ends at 3 and the
> next starts at 3, do those count as a conflict? I will assume closed intervals,
> so touching counts as overlapping, and I will flip one comparison if that is
> wrong."

## The Two Ways Two Intervals Can Miss Each Other

Start with the smallest possible question, which is whether intervals `a` and `b`
share any point at all. The direct approach is to enumerate the arrangements, and
there are more of them than people expect: `b` can start inside `a` and end
outside it, `b` can start and end inside `a`, `b` can contain `a` entirely, and
each of those has a mirror image with the roles swapped. Writing that as a chain
of `or`s gives four or five conditions, and under interview pressure at least one
of them comes out with the wrong endpoint

The fix is to ask the opposite question, because the arrangements where they
**miss** each other are not five, they are two. Either `a` finishes before `b`
begins, or `b` finishes before `a` begins

```text
        0    1    2    3    4    5    6    7
   a         [=========]                            a ends at 3
   b                        [=========]             b starts at 4, so a is entirely left of b

   a                        [=========]             the mirror image, which is
   b         [=========]                            the only other way to miss
```

**Disjoint** means `a.end < b.start or b.end < a.start`, and overlapping is the
negation of that. Pushing the `not` inward flips both comparisons and turns the
`or` into an `and`, which leaves one line

```python
def overlaps(a: list[int], b: list[int]) -> bool:
    return a[0] <= b[1] and b[0] <= a[1]


assert overlaps([1, 3], [2, 5]) is True
assert overlaps([1, 3], [3, 5]) is True
assert overlaps([1, 3], [4, 5]) is False
assert overlaps([1, 10], [4, 5]) is True
assert overlaps([4, 5], [1, 10]) is True
assert overlaps([2, 2], [2, 2]) is True
```

Read it as "each one starts before the other one ends". It is symmetric, so the
argument order never matters, and containment needs no special case, which the
`[1, 10]` against `[4, 5]` assertions above check in both directions. The two
`<=` signs are the closed-endpoint policy, and switching to half-open intervals
means writing `a[0] < b[1] and b[0] < a[1]` instead, which is exactly the change
that makes `[1, 3]` and `[3, 5]` stop counting as a conflict

Often you need more than a yes or no, and the shared region itself is just as
short. The overlap begins at the **later** of the two starts, since both intervals
have to have begun, and it finishes at the **earlier** of the two ends, since
either one ending closes it

```python
def intersect(a: list[int], b: list[int]) -> list[int] | None:
    lo = max(a[0], b[0])
    hi = min(a[1], b[1])
    return [lo, hi] if lo <= hi else None


assert intersect([1, 3], [2, 5]) == [2, 3]
assert intersect([1, 3], [3, 5]) == [3, 3]
assert intersect([1, 3], [4, 5]) is None
assert intersect([1, 10], [4, 5]) == [4, 5]
assert intersect([7, 7], [7, 7]) == [7, 7]
```

`lo <= hi` is the overlap test again in a different costume, since `max(starts)`
being at most `min(ends)` says precisely that each start is at or before both ends.
Computing `lo` and `hi` first and testing them afterwards is usually shorter than
testing for overlap and then recomputing the bounds, and it is why the worked
example at the end of this topic never calls `overlaps` at all

**Determine if Two Events Have Conflict** is the overlap test with no arithmetic
at all, because the times arrive as `"HH:MM"` strings. Those are fixed-width and
zero-padded, so comparing them as strings compares them character by character and
gives the same ordering as comparing the clock times, and no parsing is needed

```python
def have_conflict(event1: list[str], event2: list[str]) -> bool:
    return event1[0] <= event2[1] and event2[0] <= event1[1]


assert have_conflict(["01:15", "02:00"], ["02:00", "03:00"]) is True
assert have_conflict(["01:00", "02:00"], ["01:20", "03:00"]) is True
assert have_conflict(["10:00", "11:00"], ["14:00", "15:00"]) is False
assert have_conflict(["09:00", "09:00"], ["09:00", "09:00"]) is True
```

Say the zero-padding out loud, because the trick fails the moment a time arrives
as `"9:00"` instead of `"09:00"`, since `"9"` sorts after `"1"` and a nine o'clock
event would look later than an eleven o'clock one

## Sorting Turns A Global Question Into A Local One

Scale the question up from two intervals to `n` of them. "Could a person attend
every one of these meetings", which is the same as asking whether any two of them
overlap, has an obvious answer: run `overlaps` on every pair. That is `O(n²)`
comparisons, and on the `10^4` intervals these problems hand you that is the
`n * (n - 1) / 2` pairs, about `5 * 10^7` tests, for a question that needs one
pass

The reason it feels wasteful is that most of those pairs are absurd. You compare
the 9am meeting against the 5pm one when there are six meetings in between. What
you want is a rule that lets you ignore all the far-apart pairs, and **sorting by
start time** is that rule

Suppose the intervals are sorted so their starts are non-decreasing, and suppose
some pair `i < j` overlaps, meaning `starts[j] <= ends[i]`. The interval at `i + 1`
starts at or after `i` and at or before `j`, because the list is sorted, so
`starts[i + 1] <= starts[j] <= ends[i]`, which is exactly the statement that `i`
and `i + 1` overlap. So if **any** pair overlaps, then some **adjacent** pair
overlaps, and checking the `n - 1` adjacent pairs is enough

```python
def any_overlap(intervals: list[list[int]]) -> bool:
    ordered = sorted(intervals)
    for i in range(1, len(ordered)):
        if ordered[i][0] <= ordered[i - 1][1]:
            return True
    return False


assert any_overlap([[0, 30], [5, 10], [15, 20]]) is True
assert any_overlap([[7, 10], [2, 4]]) is False
assert any_overlap([[1, 3], [3, 5]]) is True
assert any_overlap([]) is False
assert any_overlap([[1, 5]]) is False
```

`sorted(intervals)` with no key sorts by start first and by end as a tiebreak,
since Python compares lists element by element, and that is normally what you
want. The comparison inside the loop is one-sided rather than the full `overlaps`
call, because sorting has already guaranteed `ordered[i - 1][0] <= ordered[i][0]`,
so half of the two-sided test is true by construction

That lemma is the reason this whole module opens with a sort. Once the intervals
are in start order, every question about the *whole* set becomes a question about
each interval and the state left behind by the ones before it, which is a single
left-to-right scan. Merging overlapping intervals, inserting a new one, counting
concurrent meetings, and sweeping events all inherit this move from here

## Choosing The Sort Key: Start Versus End

Two sort keys cover nearly every interval problem, and picking the wrong one is
the most expensive mistake available, because the resulting code looks reasonable
and produces wrong answers on inputs you will not think to test

- **Sort by start** when you are walking the timeline and building something as
  you go. Merging a run of overlapping intervals, inserting into a sorted set, and
  detecting a conflict all want start order, because a left-to-right scan needs to
  meet intervals in the order they begin
- **Sort by end** when you are **choosing** a subset and want to leave as much
  room as possible for the choices you have not made yet. The interval that
  finishes earliest blocks the least future space, so committing to it is never
  worse than committing to any other candidate. That exchange argument is
  developed in [greedy algorithms](../../12_greedy_algorithms/notes/01_greedy_fundamentals.md),
  and its interval form in [interval greedy](../../12_greedy_algorithms/notes/03_interval_greedy.md)

**Minimum Number Of Arrows To Burst Balloons** is the second kind. Each balloon is
a horizontal interval, an arrow fired at coordinate `x` pops every balloon whose
interval contains `x`, and you want the fewest arrows. Sorting by end and firing
each arrow at the earliest end you have not yet covered is optimal, because that
arrow pops the balloon that had the least room to be popped in, and any arrow that
pops it can be slid rightward to that end without losing anything

```python
def find_min_arrow_shots(points: list[list[int]]) -> int:
    if not points:
        return 0
    ordered = sorted(points, key=lambda p: p[1])
    arrows = 1
    arrow_x = ordered[0][1]
    for start, end in ordered[1:]:
        if start > arrow_x:
            arrows += 1
            arrow_x = end
    return arrows


assert find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
assert find_min_arrow_shots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
assert find_min_arrow_shots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
assert find_min_arrow_shots([[1, 2]]) == 1
assert find_min_arrow_shots([]) == 0
```

**Three details in those eleven lines**:

- `key=lambda p: p[1]` sorts by end and nothing else, which is the entire
  algorithm. Keeping the same loop but sorting by start answers
  `[[1, 10], [2, 3], [8, 9]]` with one arrow, because the wide first balloon drags
  `arrow_x` out to 10 and every later balloon then passes the `start > arrow_x`
  test, even though no single coordinate lies in all three intervals and the true
  answer is 2. The wrong key produces a wrong number rather than a slow one
- `start > arrow_x` is strict, because a balloon starting exactly at the current
  arrow's coordinate is pierced by that arrow under closed endpoints. Writing
  `>=` fires a redundant arrow at every touching balloon, and the third assertion
  above, which expects 2 rather than 4, is the case that catches it
- `sorted` rather than `points.sort()` leaves the caller's list alone. Mutating an
  argument is not wrong here, but it is worth a sentence out loud, since a grader
  or a caller that reuses the input will see it reordered

Tracing the first assertion shows where the work is skipped. Sorting by end turns
`[[10, 16], [2, 8], [1, 6], [7, 12]]` into `[[1, 6], [2, 8], [7, 12], [10, 16]]`

```text
balloon    arrow_x before   start > arrow_x   action                arrows
[1, 6]         -                  -           first arrow at 6         1
[2, 8]         6            2 > 6 is false    SKIPPED, already popped  1
[7, 12]        6            7 > 6 is true     new arrow at 12          2
[10, 16]      12           10 > 12 is false   SKIPPED, already popped  2
```

The two skipped rows are the point. `[2, 8]` is a wide balloon that stretches well
past the arrow, and it still needs no arrow of its own, because the arrow at 6
already passes through it. Notice also that `arrow_x` is only ever moved when a
new arrow is fired, never when a balloon is skipped. Updating it to the skipped
balloon's end would push it to 8 on row two, which makes `7 > 8` false so
`[7, 12]` gets skipped as well and pushes it on to 12 and then to 16, and the
whole input comes back as 1 arrow instead of 2

## Intervals That Nobody Handed You

The problems above arrive as a list of pairs. The harder recognition step is a
problem whose input is a flat array or a string, where the intervals are something
you construct. Two of them are worth knowing by shape

**Summary Ranges** gives a sorted array of distinct integers and asks for the
compressed ranges, so `[0, 1, 2, 4, 5, 7]` becomes `["0->2", "4->5", "7"]`. The
intervals are the maximal runs of consecutive values, and you build each one by
holding onto where the run started while an inner loop walks forward as long as
each value is exactly one more than the one before it

```python
def summary_ranges(nums: list[int]) -> list[str]:
    out: list[str] = []
    i = 0
    while i < len(nums):
        start = i
        while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
            i += 1
        out.append(str(nums[start]) if start == i else f"{nums[start]}->{nums[i]}")
        i += 1
    return out


assert summary_ranges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
assert summary_ranges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
assert summary_ranges([-1]) == ["-1"]
assert summary_ranges([]) == []
```

`start == i` after the inner loop means the run never advanced, so it holds one
number and gets formatted without an arrow, which is the case the trailing `7` in
the first assertion and the lone `-1` in the third exist to check. The inner `while` reads `nums[i + 1]` only
after confirming `i + 1 < len(nums)`, and Python's `and` short-circuits, so the
bounds check has to come first or the last run walks off the end

**Partition Labels** hides its intervals one level deeper. Given a string, cut it
into as many pieces as possible so that no letter appears in two pieces. Each
letter `c` defines an interval from its first occurrence to its last, and a piece
is legal exactly when it fully contains the interval of every letter inside it.
Because you scan left to right, the first occurrence is wherever you meet the
letter, so the only thing you need in advance is each letter's **last** index,
which is one pass into a [hash map](../../01_arrays_and_hashing/notes/02_hashing.md)

```python
def partition_labels(s: str) -> list[int]:
    last = {ch: i for i, ch in enumerate(s)}
    out: list[int] = []
    start = 0
    end = 0
    for i, ch in enumerate(s):
        end = max(end, last[ch])
        if i == end:
            out.append(end - start + 1)
            start = i + 1
    return out


assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]
assert partition_labels("eccbbbbdec") == [10]
assert partition_labels("a") == [1]
assert partition_labels("") == []
```

`end` is the right edge of the piece being built, and every letter you pass can
only push it rightward, never pull it back, which is why the update is a `max`
rather than an assignment. When the scan reaches the position `end` is pointing at,
every letter seen so far ends at or before here, so the piece can close

Tracing `"abacdc"`, whose last-index map is `{a: 2, b: 1, c: 5, d: 4}`

```text
i  char  last[char]   end before -> after   i == end?
0   a        2            0 -> 2            no
1   b        1            2 -> 2            no, DISCARDED: b ends at 1, left of end
2   a        2            2 -> 2            yes, cut, piece "aba" of length 3
3   c        5            2 -> 5            no
4   d        4            5 -> 5            no, DISCARDED: d ends at 4, left of end
5   c        5            5 -> 5            yes, cut, piece "cdc" of length 3
```

The two discarded rows are letters whose intervals sit strictly inside the piece
already under construction, so they demand nothing and the `max` throws their
value away. Only a letter that reaches further right than anything before it moves
the boundary, and `b` at row 1 shows why the `max` cannot be dropped: assigning
`end = last[ch]` there would pull the boundary back from 2 to 1 and cut after
`"ab"`, splitting the two `a`s across two pieces

## Worked Example: [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)

You get two lists of closed intervals, each list already sorted and internally
non-overlapping, and you return every interval that appears in both, meaning the
region each pair of them shares

**Input**:

- `first_list`, a `list[list[int]]` where each entry is `[start, end]` with
  `start <= end`. The list is sorted by start and its intervals are pairwise
  disjoint, so it describes a set of separated stretches of the number line
- `second_list`, a `list[list[int]]` with the same guarantees. Either list may be
  empty, and each holds up to 1000 intervals, with coordinates that fit
  comfortably in an `int`

**Output**: a `list[list[int]]` of the intersections, sorted by start. Each entry
is the region covered by one interval from each input list, and single-point
intersections such as `[5, 5]` are real answers rather than degenerate cases to be
filtered out, since the intervals are closed. Two intervals that do not meet
contribute nothing, so the output can be shorter than either input and is empty
when the lists never meet

The phrase that identifies the technique is "each list is already sorted", which
means the answer should cost one linear walk rather than a sort. The naive version
compares every interval in the first list against every interval in the second and
keeps the non-empty intersections, which is `O(m * n)` and, worse, throws away the
one fact the problem went out of its way to give you. Most of those pairs are
hopeless, since an interval in the first list that ends at 10 can never meet one in
the second list that starts at 40

Walk both lists at once with a pointer into each, the same two-cursor shape as
[merging two sorted lists](../../06_linked_lists/notes/04_merge_split.md). At every
step you hold one interval from each side, and the region they share is
`[max(starts), min(ends)]` from earlier in this topic, which you keep when it is
non-empty. Then exactly one pointer advances, and which one is the whole decision:
the interval that **ends first** can never intersect anything later in the other
list, because everything later there starts even further right, so it is finished
and its pointer moves

> "Both lists are sorted, so I will use one pointer per list instead of comparing
> all pairs. At each step I take `max` of the starts and `min` of the ends, emit
> that when it is non-empty, and advance the pointer whose interval ends first,
> because that interval cannot meet anything further along in the other list."

1. Set both pointers to zero and loop while both are still in range. The moment
   either list is exhausted no further intersection is possible, since an
   intersection needs one interval from each side, and that condition also handles
   an empty input list without a separate guard
2. At each step take the current interval from each list and compute
   `lo = max` of the two starts and `hi = min` of the two ends, which is the
   candidate shared region
3. Append `[lo, hi]` when `lo <= hi`. When `lo > hi` the two intervals miss each
   other entirely, so nothing is emitted and the step still counts as progress,
   because a pointer moves either way
4. Compare the two ends and advance the pointer belonging to the interval that
   ends first. That interval has been fully compared against everything it could
   possibly reach, since every remaining interval in the other list starts at or
   after the current one, which starts at or after this interval's end
5. Break ties either way when the two ends are equal, because both intervals
   finish at the same coordinate, so both are exhausted and whichever one you
   advance now leaves the other to be advanced on the following step with no
   intersection missed in between
6. Return the collected list, which is already in sorted order because both
   pointers only move rightward, so each emitted region starts at or after the one
   before it

```python
def interval_intersection(
    first_list: list[list[int]], second_list: list[list[int]]
) -> list[list[int]]:
    out: list[list[int]] = []
    i = 0
    j = 0
    while i < len(first_list) and j < len(second_list):
        lo = max(first_list[i][0], second_list[j][0])
        hi = min(first_list[i][1], second_list[j][1])
        if lo <= hi:
            out.append([lo, hi])
        if first_list[i][1] < second_list[j][1]:
            i += 1
        else:
            j += 1
    return out


assert interval_intersection(
    [[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]
) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
assert interval_intersection([[1, 7]], [[3, 10]]) == [[3, 7]]
assert interval_intersection([[1, 3], [5, 9]], []) == []
assert interval_intersection([], [[4, 8], [10, 12]]) == []
```

Tracing the first three intervals of each list shows both the emitted and the
rejected steps

```text
A = [0,2]   B = [1,5]    lo=1  hi=2   emit [1, 2]    2 < 5, advance i
A = [5,10]  B = [1,5]    lo=5  hi=5   emit [5, 5]    5 < 10 is false, advance j
A = [5,10]  B = [8,12]   lo=8  hi=10  emit [8, 10]   10 < 12, advance i
A = [13,23] B = [8,12]   lo=13 hi=12  REJECTED       12 < 23 is false, advance j
A = [13,23] B = [15,24]  lo=15 hi=23  emit [15, 23]  23 < 24, advance i
```

Row two is the single-point intersection `[5, 5]`, which the closed-endpoint rule
makes a genuine answer, and which any code that tests `lo < hi` instead of
`lo <= hi` silently drops. Row four is the rejected step, where `[13, 23]` starts
after `[8, 12]` has already ended, so `lo` overshoots `hi` and nothing is emitted.
Advancing `j` there is what unblocks the walk, and advancing `i` instead would move
past `[13, 23]` and lose its real intersection with `[15, 24]` on the next row

- **Time Complexity:** `O(m + n)` for lists of `m` and `n` intervals, because each
  iteration does constant work and advances exactly one of the two pointers, so
  the loop runs at most `m + n` times
- **Space Complexity:** `O(1)` auxiliary beyond the output, since only the two
  integer pointers are kept. The returned list holds at most `m + n - 1`
  intersections, because every iteration emits at most one and the final iteration
  ends the loop

## Time and Space Complexity

Throughout, `n` is the number of intervals, and in the two-list problem `m` and `n`
are the lengths of the two lists

**Comparing a single pair of intervals**

| Approach                                     | Time                                                                                    | Space                                                            |
| -------------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `a[0] <= b[1] and b[0] <= a[1]`              | `O(1)`: two comparisons and one `and`, with no dependence on how wide the intervals are | `O(1)`: nothing is allocated, since the test reads four integers |
| Enumerating the arrangement cases separately | `O(1)`: the same constant work, so the cost of the mistake is bugs rather than time     | `O(1)`: also allocation-free                                     |

**Deciding whether any two of `n` intervals overlap**

| Approach                                | Time                                                                                                            | Space                                                                                                                                    |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Sort by start, then scan adjacent pairs | `O(n log n)`: the sort dominates, since the scan afterwards is `O(n)` with one comparison per neighbouring pair | `O(n)`: `sorted` builds a new list of `n` references, and Python's sort needs `O(n)` scratch in the worst case even when called in place |
| `overlaps` on every pair                | `O(n²)`: there are `n * (n - 1) / 2` pairs and each is tested in constant time                                  | `O(1)`: no sorted copy and no auxiliary structure, which is the only thing this version wins                                             |

**The three scanning problems in this topic**

| Problem                                      | Time                                                                                                      | Space                                                                                                                                                 |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Minimum arrows, sorting by end then scanning | `O(n log n)`: sorting `n` balloons dominates the single `O(n)` pass that fires the arrows                 | `O(n)`: the sorted copy of the balloon list, since the scan itself keeps only `arrows` and `arrow_x`                                                  |
| Summary Ranges                               | `O(n)`: the outer and inner loops together advance `i` exactly `n` times, so no element is examined twice | `O(n)` for the output strings, and `O(1)` auxiliary, because only `i` and `start` are carried                                                         |
| Partition Labels                             | `O(n)`: one pass to build the last-index map and one pass to cut, over a string of length `n`             | `O(a)`: where `a` is the alphabet size, at most 26 for lowercase input, since the map holds one entry per distinct character rather than per position |

**Intersecting two sorted interval lists**

| Approach                                | Time                                                                                                                                  | Space                                                                                          |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Two pointers, one per list              | `O(m + n)`: every iteration advances exactly one pointer, and neither pointer ever moves backwards                                    | `O(1)` auxiliary plus `O(m + n)` for the output, which holds at most `m + n - 1` intersections |
| Testing every pair across the two lists | `O(m * n)`: each of the `m` intervals is compared against all `n` of the others, which discards the sortedness the problem guarantees | `O(1)` auxiliary plus the same output, so the sortedness buys time and not space               |

## Summary

- An **interval** `[start, end]` stands for every point between its two endpoints,
  so unlike a plain number it can overlap, touch, or contain another one. The two
  coordinates are not interchangeable, and mixing up which one you sorted by and
  which one you are reasoning about is where most interval bugs come from
- **Closed** endpoints include both ends, so `[1, 3]` and `[3, 5]` share the point
  3, while **half-open** endpoints exclude the right end, so the same two only
  touch. Ask which convention applies before writing code, because the entire
  difference is a `<=` against a `<`
  - LeetCode uses closed intervals for balloons and interval lists, and half-open
    ones for meetings, where a meeting ending at 3 does not clash with one
    starting at 3
- Two intervals overlap exactly when `a.start <= b.end and b.start <= a.end`,
  which is derived by negating the only two ways they can miss each other, namely
  one finishing entirely before the other begins
  - Read it out loud as "each one starts before the other one ends". It is
    symmetric, so argument order never matters, and full containment needs no
    separate case
  - The shared region is `[max(starts), min(ends)]`, and it is non-empty exactly
    when `lo <= hi`, which is the same test wearing different clothes. Computing
    the bounds first and testing them afterwards is shorter than testing and then
    recomputing
- Asking whether any two of `n` intervals overlap by comparing all pairs is
  `O(n²)`, and sorting by start replaces it with a single `O(n)` scan of adjacent
  pairs. If any pair overlaps then some adjacent pair does, because the interval
  sitting between them starts no later than the second one and therefore also
  lands inside the first one
  - This is why almost every interval solution begins with a sort. Ordering the
    intervals turns a question about the whole set into a question about each
    interval and the state the previous ones left behind
- **Sort by start** when scanning the timeline and building something as you go,
  as in merging, inserting, or conflict detection. **Sort by end** when choosing a
  subset, because the interval that finishes earliest blocks the least future room
  - Minimum Arrows is the sort-by-end family. Fire an arrow at the earliest end,
    skip every balloon that arrow already pierces, and move `arrow_x` only when a
    new arrow is fired, never when a balloon is skipped
  - The skip test is the strict `start > arrow_x`, because a balloon beginning
    exactly at the arrow's coordinate is already popped under closed endpoints
- Some problems supply an array or a string rather than a list of pairs, and the
  intervals are yours to construct. Recognising them is the harder half of the
  pattern
  - Summary Ranges builds each interval as a maximal run of consecutive integers,
    remembering where the run began and formatting a one-element run without an
    arrow
  - Partition Labels treats each letter's first and last occurrence as an
    interval, precomputes the last index of every character in one pass, extends
    the current piece's right edge with `max`, and cuts when the scan position
    reaches that edge. The `max` is load-bearing, since assigning instead would
    let a letter that ends early pull the boundary backwards
- Walking two sorted interval lists together uses one pointer per list, emits
  `[max(starts), min(ends)]` whenever it is non-empty, and advances the pointer
  whose interval **ends first**, since that interval cannot reach anything further
  along in the other list. That is `O(m + n)` rather than the `O(m * n)` of
  comparing all pairs
- The cost of an interval problem is usually `O(n log n)` because of the sort,
  with an `O(n)` scan after it, so the sort is the thing to quote when asked. When
  the input arrives already sorted, as in Interval List Intersections, the whole
  problem drops to linear and failing to notice that is the missed optimisation

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
Are the endpoints closed or half-open, and do touching intervals count as overlapping?
Can I state the overlap test in one line, and defend it as the negation of the two disjoint cases?
Do I need a yes/no overlap, or the shared region [max(starts), min(ends)] itself?
Am I sorting by start because I am scanning, or by end because I am choosing a subset?
If I sort by end, what is the exchange argument for why the earliest finisher is safe?
Is the input already sorted, which would make an O(n log n) answer needlessly slow?
Does sorting mutate the caller's list, and have I said so or used sorted() instead?
Which pointer advances when I walk two lists, and why can the other one wait?
What are the intervals here if the input is a raw array or a string rather than pairs?
What happens on an empty list, a single interval, and a zero-width interval like [4, 4]?
```
