# Interval Greedy

An **interval** is a pair `[start, end]` that claims a stretch of a line. A
meeting that runs from 1 o'clock to 4 is the interval `[1, 4]`, a balloon
floating across x-coordinates 2 through 8 is `[2, 8]`, and a chunk of a string
covering positions 3 through 9 is `[3, 9]`. Two intervals **overlap** when they
share at least one point of that line, which is the only relationship this whole
topic cares about

The windows in [sliding window](../../04_sliding_window/notes/02_variable_size_window.md)
were ranges too, but you owned them: you decided where the left and right edges
went, and the range was always a contiguous block of one array. Intervals arrive
as *data*. They are handed to you in whatever order the input file happened to
list them, they sit anywhere on the line, and your only power is deciding which
ones to keep

**Interval greedy** is the shape that follows from that. Sort the input on one
carefully chosen field, then sweep it once from left to right while holding a
single number, almost always the end of the last item you committed to. Each
item is accepted or thrown away on the spot, with no lookahead and no undo

Picture one conference room and a stack of booking requests on your desk. You
cannot see the future and you cannot un-book a room, so the only decision you
actually control is **what order you read the stack in**. That is the entire
technique. Everything difficult about interval greedy is choosing the sort key,
because the right key is the one that makes "decide on the spot" enough
information to be optimal

## Fitting The Most Meetings Into One Room

Start with the cleanest version, called **activity selection**: given a list of
meetings, keep as many as possible such that no two of the kept ones overlap.
[Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
asks the mirror-image question, the minimum number to *remove*, and removing the
fewest is the same as keeping the most

Here are six meetings on a timeline

```text
time   0    1    2    3    4    5    6    7    8    9
A           [--------------]
B                     [---------]
C      [-----------------------------]
D                               [---------]
E                     [------------------------]
F                                              [----]
```

The first instinct is to read them in the order the day happens, so sort by
**start time** and take every meeting that still fits. That instinct is wrong,
and one tiny example kills it

```text
time   0    1    2    3    4
X      [-------------------]         a single all-day meeting [0, 4]
Y           [----]                   [1, 2]
Z                     [----]         [2, 3]
```

Sorting by start puts `X` first, and `X` is accepted because nothing has been
booked yet. It then blocks both `Y` and `Z`, so the answer comes out as 1 when
the true answer is 2. Nothing about `X` was expensive to look at; the damage was
that committing to it **consumed the rest of the line**. Sorting by start ranks
meetings by when they begin, but what a greedy sweep is spending is the part of
the line still available afterwards, and a start time says nothing about that

Once the failure is stated that way the fix names itself. The resource being
spent is *remaining line*, so rank the meetings by how little of it they consume,
which is their **end time**. Take the meeting that finishes earliest, then the
earliest-finishing meeting that starts at or after that, and so on

Why that is not just a better guess is the [exchange argument](01_greedy_fundamentals.md)
applied to this specific rule. Take any optimal schedule and look at its first
meeting `M`. Let `G` be the earliest-ending meeting overall, which is what the
greedy rule picks first. Since `G` ends no later than `M` ends, swapping `M` out
for `G` leaves every other meeting in that optimal schedule still compatible,
because they all started at or after `M`'s end and therefore also start at or
after `G`'s end. The swap changes the count by zero, so there is an optimal
schedule that begins with the greedy choice. Delete `G` and everything it
overlaps, and the same argument runs again on what is left

> "I will sort by end time rather than start time. The greedy choice is the
> meeting that finishes earliest, and it is safe because any optimal schedule's
> first meeting can be exchanged for it without breaking anything later — the
> earliest finisher leaves at least as much of the timeline free."

```python
def max_non_overlapping(intervals: list[list[int]]) -> int:
    kept = 0
    last_end = float("-inf")
    for start, end in sorted(intervals, key=lambda pair: pair[1]):
        if start >= last_end:
            kept += 1
            last_end = end
    return kept


def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    return len(intervals) - max_non_overlapping(intervals)


assert max_non_overlapping([[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [8, 9]]) == 3
assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
assert erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2
assert erase_overlap_intervals([[1, 2], [2, 3]]) == 0
assert erase_overlap_intervals([]) == 0
```

**Four details in five lines**:

- `last_end` is the whole memory of the sweep. It means "the earliest moment the
  room is free again", so `start >= last_end` is literally the question "has the
  room been handed back by the time this meeting wants it?"
- `float("-inf")` is the seed rather than `0`, because interval coordinates can be
  negative and seeding at `0` would silently reject every meeting that starts
  before zero
- `last_end` is only written when a meeting is **kept**. Updating it on a rejected
  meeting is the standard bug, and it is invisible on small inputs: rejecting
  `[0, 6]` while setting `last_end = 6` would then also refuse `[5, 7]`, which was
  perfectly bookable
- `sorted(...)` builds a new list instead of calling `intervals.sort()`, which
  mutates the caller's input. That matters in a real codebase and interviewers
  occasionally ask about it, so it is a free point

The mirror-image framing is worth saying out loud because it is what turns the
counting answer into the LeetCode answer. Every interval is either kept or
erased, so `erased = n - kept`, and there is never a reason to write a second
algorithm for the removal version

**A near miss that breaks the whole thing**: if each interval also carried a
value and you wanted the maximum total value rather than the maximum count,
earliest-end greedy is wrong. Given `[0, 10]` worth 100, `[0, 1]` worth 1, and
`[2, 3]` worth 1, the greedy rule takes the two cheap intervals for a total of 2
and never looks at the one worth 100. That version is **weighted interval
scheduling**, and it needs
[dynamic programming](../../11_dp/notes/01_dp_fundamentals.md) instead — sort by
end, then `dp[i] = max(dp[i - 1], value[i] + dp[latest compatible])`. Greedy is
safe here only because every interval is worth exactly one

## Tracing The Sweep, Rejections Included

Run the six meetings from the timeline above, which sort by end into
`[1,4], [3,5], [0,6], [5,7], [3,8], [8,9]`

```text
interval   start >= last_end?      decision   last_end   kept
[1, 4]     1 >= -inf               KEEP              4      1
[3, 5]     3 >= 4  is false        REJECT            4      1
[0, 6]     0 >= 4  is false        REJECT            4      1
[5, 7]     5 >= 4                  KEEP              7      2
[3, 8]     3 >= 7  is false        REJECT            7      2
[8, 9]     8 >= 7                  KEEP              9      3
```

Three kept, three erased. The interesting lines are the rejections rather than
the acceptances

`[0, 6]` is the one to stare at. It is the *longest-running* meeting in the whole
set except for `[3, 8]`, it starts before anything else, and the sweep throws it
away without a second thought because `last_end` is already 4. That is the
sorting decision paying off: had the list been ordered by start time, `[0, 6]`
would have been examined first, accepted, and would have blocked both `[1, 4]`
and `[5, 7]`

`[3, 5]` shows why the update has to be conditional. It is rejected while
`last_end` stays at 4, not 5. Bumping `last_end` to 5 on a rejection would have
made `[5, 7]` look fine but would have been meaningless bookkeeping, and on other
inputs it silently loses intervals

## One Arrow For A Whole Cluster, And Where The Boundary Sits

[Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)
looks like a different problem and is the same sweep with two characters
changed. Balloons are intervals on the x-axis, an arrow fired at coordinate `x`
pops every balloon whose interval contains `x`, and you want the fewest arrows

Sort by end again. Fire the first arrow at the *end* of the earliest-ending
balloon, since that is the rightmost point that still pops it and therefore the
point that catches the most other balloons for free. Every later balloon that
starts at or before that coordinate is already popped, so it is skipped. The
first balloon that starts strictly after it needs a fresh arrow

The counting flips: the previous problem counted the intervals it kept, and this
one counts the moments it was **forced to start a new group**. Those are the same
number here, because each arrow corresponds to exactly one earliest-ending
balloon, but the framing generalises better to any "how few groups" question

```python
def find_min_arrow_shots(points: list[list[int]]) -> int:
    if not points:
        return 0
    ordered = sorted(points, key=lambda pair: pair[1])
    arrows = 1
    last_end = ordered[0][1]
    for start, end in ordered[1:]:
        if start > last_end:
            arrows += 1
            last_end = end
    return arrows


assert find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
assert find_min_arrow_shots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
assert find_min_arrow_shots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
assert find_min_arrow_shots([]) == 0
```

**The comparison is `start > last_end`, and in the scheduling version it was
`start >= last_end`.** That single character is the **overlap boundary**, and
getting it backwards is the most common way to fail one of these on a hidden test
case. The rule comes from the problem's own physics rather than from taste

- Two meetings `[1, 2]` and `[2, 3]` do **not** conflict, because one room is
  vacated at 2 and the next is occupied from 2. Touching endpoints are fine, so
  the keep test admits equality with `>=`
- Two balloons `[1, 2]` and `[2, 3]` **do** share the point `x = 2`, and one arrow
  at 2 pops both. Touching endpoints count as overlapping, so a new arrow is only
  needed when `start > last_end`

The third assert is the case that tells them apart. The chain
`[1,2], [2,3], [3,4], [4,5]` needs 2 arrows, at `x = 2` and `x = 4`, while the
same four intervals treated as meetings are all mutually bookable. Ask which
convention the problem uses before writing the comparison, and if the statement
is vague, say out loud which one you are assuming

[Eliminate Maximum Number of Monsters](https://leetcode.com/problems/eliminate-maximum-number-of-monsters/)
is the same sort-by-deadline instinct with the intervals hidden. Each monster is
described by a distance and a speed, so its arrival time is `dist / speed`, and
you get one kill per minute starting at minute 0. Sort the arrival times and walk
them: the monster you must shoot at minute `k` is the `k`-th soonest to arrive,
because delaying the most urgent one to save a less urgent one can only lose

```python
def eliminate_maximum(dist: list[int], speed: list[int]) -> int:
    arrivals = sorted(d / s for d, s in zip(dist, speed))
    for minute, arrival in enumerate(arrivals):
        if arrival <= minute:
            return minute
    return len(arrivals)


assert eliminate_maximum([1, 3, 4], [1, 1, 1]) == 3
assert eliminate_maximum([1, 1, 2, 3], [1, 1, 1, 1]) == 1
assert eliminate_maximum([3, 2, 4], [5, 3, 2]) == 1
assert eliminate_maximum([1], [1]) == 1
```

The boundary question shows up here too, as `arrival <= minute` rather than
`arrival < minute`. A monster arriving exactly at minute `k` has already reached
the city when the minute-`k` shot would be fired, so equality is a loss

## Cutting A Line Where Nothing Reaches Across

Some problems hand you no intervals at all and expect you to build them, then
sweep the same way. [Partition Labels](https://leetcode.com/problems/partition-labels/)
gives a string and asks for the sizes of the largest possible pieces such that
every letter appears in exactly one piece

Each distinct letter defines an interval, from its first occurrence to its last,
and a cut is only legal at a position that no letter's interval spans. There is
no sorting step, because scanning the string left to right already visits the
positions in order. What is carried instead is a running `end`, meaning "the
furthest position any letter seen so far reaches", and the moment the scan index
catches up to it, everything opened has been closed and the piece can be sealed

```python
def partition_labels(s: str) -> list[int]:
    last = {ch: i for i, ch in enumerate(s)}
    sizes: list[int] = []
    start = end = 0
    for i, ch in enumerate(s):
        end = max(end, last[ch])
        if i == end:
            sizes.append(end - start + 1)
            start = i + 1
    return sizes


assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]
assert partition_labels("eccbbbbdec") == [10]
assert partition_labels("a") == [1]
assert partition_labels("") == []
```

The dictionary comprehension `{ch: i for i, ch in enumerate(s)}` records the
*last* index of each character rather than the first, since a later assignment to
the same key overwrites the earlier one. That is a
[frequency-map](../../01_arrays_and_hashing/notes/02_hashing.md) idiom worth
recognising on sight, because writing an explicit loop to find last occurrences
costs three extra lines

The first nine characters of the official example show the boundary extending and
then holding

```text
i= 0 ch=a  last[a]= 8   end  0 ->  8
i= 1 ch=b  last[b]= 5   end  8 ->  8    b closes inside the piece already open
i= 4 ch=c  last[c]= 7   end  8 ->  8    c closes inside it too
i= 8 ch=a  last[a]= 8   end  8 ->  8    CUT, size 9
i= 9 ch=d  last[d]=14   end  8 -> 14    a new piece opens
```

Rows `i = 1` and `i = 4` are the discarded candidates. Both `b` and `c` reach
further right than the current index, so both are tempting places to think about
cutting, and both are rejected because `end` is already 8 and `max` refuses to
shrink it. `end` only ever moves right, which is the invariant that makes one
pass sufficient

[Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals/)
is the same running-boundary idea with the condition changed from "every letter
is contained" to "every left value is at most every right value". Two maxima are
needed rather than one: `left_max` is the maximum of the committed prefix, and
`running_max` is the maximum of everything seen. When a value smaller than
`left_max` turns up, the prefix must swallow it and everything before it, so the
boundary moves and `left_max` catches up to `running_max`

```python
def partition_disjoint(nums: list[int]) -> int:
    left_max = running_max = nums[0]
    boundary = 0
    for i in range(1, len(nums)):
        if nums[i] < left_max:
            boundary = i
            left_max = running_max
        else:
            running_max = max(running_max, nums[i])
    return boundary + 1


assert partition_disjoint([5, 0, 3, 8, 6]) == 3
assert partition_disjoint([1, 1, 1, 0, 6, 12]) == 4
assert partition_disjoint([1, 1]) == 1
```

On `[5, 0, 3, 8, 6]` the value `6` at the end is smaller than `8`, but `8` was
never promoted into `left_max`, so `6` is not a violation and the boundary stays
at index 2. That distinction between "the biggest thing committed" and "the
biggest thing seen" is the entire problem

## Pairing The Lightest Person With The Heaviest

[Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) sorts
by a plain weight instead of an endpoint, and it is here because the reasoning is
identical: sort so that the most constrained decision becomes obvious, then
commit without revisiting. Each boat carries at most two people and at most
`limit` total weight, and you want the fewest boats

The heaviest person is the constraint. They are going on *some* boat, and the
only question is who rides with them. If the lightest remaining person cannot fit
beside them, then nobody can, so that boat sails alone. If the lightest does fit,
pairing them is never worse than pairing anyone else, because any heavier partner
you could have used still fits everywhere the lightest one did

That is two pointers converging from the ends of a sorted array, which is exactly
the [opposite-end pointer](../../02_two_pointers/notes/01_opposite_end_pointers.md)
movement, applied to a greedy commitment instead of a search

```python
def num_rescue_boats(people: list[int], limit: int) -> int:
    ordered = sorted(people)
    left, right, boats = 0, len(ordered) - 1, 0
    while left <= right:
        if ordered[left] + ordered[right] <= limit:
            left += 1
        right -= 1
        boats += 1
    return boats


assert num_rescue_boats([1, 2], 3) == 1
assert num_rescue_boats([3, 2, 2, 1], 3) == 3
assert num_rescue_boats([3, 5, 3, 4], 5) == 4
assert num_rescue_boats([2], 3) == 1
```

`right -= 1` and `boats += 1` sit outside the `if`, and that placement is the
whole loop. Every pass launches exactly one boat and always loads the heaviest
remaining person, whether or not a companion was found, so the loop runs at most
`n` times. `left += 1` fires only on a successful pairing. The condition is
`left <= right` and not `left < right`, because the final person, when an odd
number remain, still needs a boat

[Advantage Shuffle](https://leetcode.com/problems/advantage-shuffle/) uses the
same two ends of a sorted list for a different commitment. You are matching your
cards against an opponent's fixed lineup and want to win as many head-to-head
comparisons as possible. Handle the opponent's **strongest** card first: if your
best card beats it, spend your best card, since no weaker card of yours could
have; if your best card cannot beat it, that comparison is unwinnable, so throw
your **worst** card at it and keep everything useful

```python
def advantage_count(nums1: list[int], nums2: list[int]) -> list[int]:
    ours = sorted(nums1)
    strongest_first = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
    result = [0] * len(nums2)
    left, right = 0, len(ours) - 1
    for i in strongest_first:
        if ours[right] > nums2[i]:
            result[i] = ours[right]
            right -= 1
        else:
            result[i] = ours[left]
            left += 1
    return result


assert advantage_count([2, 7, 11, 15], [1, 10, 4, 11]) == [2, 11, 7, 15]
assert advantage_count([12, 24, 8, 32], [13, 25, 32, 11]) == [24, 32, 8, 12]
assert advantage_count([1], [1]) == [1]
```

The output has to line up with the opponent's **original** positions, so the sort
is over *indices* rather than over the values themselves, and `result[i]` writes
back into the original slot. Sorting `nums2` directly and returning the answer in
sorted order is a correct algorithm producing a wrong-shaped answer, and it is a
mistake that survives every hand-check on paper

## Committing To The Most Constrained Item First

The three problems in this group share one move: find the item that has the
fewest options left, settle it completely, and let everything else be decided by
what remains

[Hand of Straights](https://leetcode.com/problems/hand-of-straights/) asks whether
a hand of cards can be split into groups of `group_size` consecutive values. The
smallest card left in the hand is the most constrained item in the problem,
because nothing smaller exists to sit below it, so it *must* be the bottom of a
group. That forces the whole group, and repeating the argument on what remains
decides everything

```python
from collections import Counter


def is_n_straight_hand(hand: list[int], group_size: int) -> bool:
    if len(hand) % group_size:
        return False
    counts = Counter(hand)
    for card in sorted(counts):
        need = counts[card]
        if need <= 0:
            continue
        for step in range(group_size):
            if counts[card + step] < need:
                return False
            counts[card + step] -= need
    return True


assert is_n_straight_hand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) is True
assert is_n_straight_hand([1, 2, 3, 4, 5], 4) is False
assert is_n_straight_hand([1, 1, 2, 2, 3, 3], 3) is True
assert is_n_straight_hand([], 3) is True
```

Starting `need` copies of the run at once, rather than one run at a time, is what
keeps this fast, since a hand with a thousand identical cards would otherwise
loop a thousand times. Tracing `[1,2,3,6,2,3,4,7,8]` with `group_size = 3` shows
the discarded starting points

```text
card 1  need 1  has [1, 2, 2] of values 1,2,3   run built   counts left {2:1, 3:1, 4:1, 6:1, 7:1, 8:1}
card 2  need 1  has [1, 1, 1] of values 2,3,4   run built   counts left {6:1, 7:1, 8:1}
card 3  need 0                                  SKIPPED, already consumed by an earlier run
card 4  need 0                                  SKIPPED, already consumed
card 6  need 1  has [1, 1, 1] of values 6,7,8   run built   counts left {}
```

Cards 3 and 4 are the rejected steps. They are still in the sorted key list, and
the `if need <= 0: continue` guard is what stops them from starting a second run
out of cards that have already been spent. Deleting exhausted keys instead of
guarding is equally fine, but mutating a dictionary while iterating its sorted
key list is not, so the guard is the safer habit

[Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/)
asks the same shape of question about a sorted input, with the twist that groups
must be length 3 *or more*. Now there is a real choice at each value: extend an
existing run, or start a new one. Extending is always at least as good, because a
run that is already length 3 stays legal when extended, while a fresh run
immediately owes two more values

```python
def is_possible(nums: list[int]) -> bool:
    remaining = Counter(nums)
    ends_at: Counter[int] = Counter()
    for value in nums:
        if remaining[value] == 0:
            continue
        remaining[value] -= 1
        if ends_at[value - 1] > 0:
            ends_at[value - 1] -= 1
            ends_at[value] += 1
        elif remaining[value + 1] > 0 and remaining[value + 2] > 0:
            remaining[value + 1] -= 1
            remaining[value + 2] -= 1
            ends_at[value + 2] += 1
        else:
            return False
    return True


assert is_possible([1, 2, 3, 3, 4, 5]) is True
assert is_possible([1, 2, 3, 3, 4, 4, 5, 5]) is True
assert is_possible([1, 2, 3, 4, 4, 5]) is False
assert is_possible([1, 2, 3]) is True
```

Two counters are needed and they answer different questions. `remaining` says how
many copies of a value are still unplaced, and `ends_at` says how many runs are
currently waiting for exactly that value plus one. The `elif` branch reserves the
next two values immediately rather than hoping they turn up later, which is what
makes `[1, 2, 3, 4, 4, 5]` fail correctly: the second `4` can neither extend the
finished run nor find a `5` and a `6` to open a new one

[Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/)
inverts the direction. Each person is `[height, k]`, where `k` counts how many
people **at least as tall** stand in front of them, and you rebuild the queue. The
most constrained people here are the tallest, because for them `k` counts
everybody in front, so their position is fully determined. Place the tallest
first, then the next tallest, and so on. Every later insertion is of a strictly
shorter person, who is invisible to everyone already placed, so no earlier
person's `k` can be disturbed

```python
def reconstruct_queue(people: list[list[int]]) -> list[list[int]]:
    queue: list[list[int]] = []
    for person in sorted(people, key=lambda p: (-p[0], p[1])):
        queue.insert(person[1], person)
    return queue


assert reconstruct_queue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]) == [
    [5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]
]
assert reconstruct_queue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]) == [
    [4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]
]
assert reconstruct_queue([[1, 0]]) == [[1, 0]]
```

The key `(-p[0], p[1])` is tallest first with **ascending `k` inside a tie**, and
both halves are load-bearing. People of equal height *do* count each other, so
among the 7s, `[7, 0]` has to be placed before `[7, 1]` for the second one to land
behind it. Reverse that tie-break and the equal-height pairs come out swapped,
which passes the small examples and fails the real tests

`queue.insert(person[1], person)` is the greedy commitment: `k` is read directly
as an index into the partially built queue, because every person already sitting
there is at least as tall

## Two Passes When One Cannot See Both Neighbours

[Candy](https://leetcode.com/problems/candy/) breaks the one-sweep habit for a
reason worth understanding. Children stand in a line with ratings, everyone gets
at least one candy, and any child rated higher than an immediate neighbour must
get more candy than that neighbour. Minimise the total

A single left-to-right pass can satisfy the left-neighbour rule, since when you
reach index `i` you already know what index `i - 1` received. It cannot satisfy
the right-neighbour rule, because index `i + 1` has not been decided yet. On the
official example `[1, 0, 2]` the left pass produces `[1, 1, 2]`, totalling 4,
which is illegal: the child rated 1 at index 0 outranks the child rated 0 beside
them and yet holds the same single candy

Rather than inventing a cleverer single rule, run the greedy twice, once in each
direction, and take the pointwise maximum. Each pass enforces one of the two
constraints, and taking the larger value at each index satisfies both while
staying minimal, because the value at each index is the smallest number that
clears whichever neighbour demanded more

```python
def candy(ratings: list[int]) -> int:
    n = len(ratings)
    give = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            give[i] = give[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            give[i] = max(give[i], give[i + 1] + 1)
    return sum(give)


assert candy([1, 0, 2]) == 5
assert candy([1, 2, 2]) == 4
assert candy([1]) == 1
assert candy([]) == 0
```

```text
ratings          1    0    2
after left pass  1    1    2      total 4, and index 0 violates its right neighbour
after right pass 2    1    2      total 5
```

The `max` in the second loop is the line people drop. Writing
`give[i] = give[i + 1] + 1` overwrites work the first pass did, so a child sitting
at the peak of a long rise followed by a short fall gets demoted and the left
constraint breaks. The second pass may only ever raise a value

## Worked Example: [Task Scheduler](https://leetcode.com/problems/task-scheduler/)

A CPU runs one task per unit of time. Two runs of the **same** task must be
separated by at least `n` units, and the CPU may sit idle. Find the shortest
total time to run every task in the list

**Input**:

- `tasks`, a `list[str]` where each element is a single uppercase letter naming a
  task type, and repeated letters mean repeated runs of that same task
- `n`, an `int` cooldown, the minimum number of units that must pass between two
  runs of the same task type, where `n` may be `0`, meaning no cooldown at all

**Output**: an `int`, the minimum number of time units the CPU is busy or idle
before the last task finishes. It counts *every* unit on the clock, including the
idle ones, so it is a wall-clock duration and not a count of tasks

The phrase that identifies the technique is "separated by at least `n`", which
makes this a scheduling problem where one task type is the bottleneck.
Simulating minute by minute, repeatedly choosing whichever task has the most
copies remaining, is the natural greedy and it is correct, but re-picking the
maximum from up to 26 counters at every one of up to `10^4` minutes does far more
work than the answer needs. The counts alone determine the answer

The idea is to build the schedule around the most frequent task. Say it appears
`max_count` times. Those runs create `max_count - 1` gaps between them, and every
gap must be at least `n + 1` units long counting the task itself. That lays out a
skeleton of `(max_count - 1) * (n + 1)` units, plus a final block holding the last
run of every task type that is tied at `max_count`. Every other task is strictly
less frequent, so it always fits into an idle slot inside the skeleton. When
there are enough different tasks to fill all the idle slots, the skeleton stops
being the constraint and the answer is simply `len(tasks)`, since the CPU never
rests

> "The most frequent task fixes the shape of the schedule. It needs `max_count - 1`
> gaps of `n + 1` units, plus one final block for the tasks tied at that count.
> Everything else slots into the idle time, so the answer is that frame — unless
> there are so many task types that nothing is ever idle, in which case it is just
> the number of tasks."

1. Count how many times each task type appears, which is all the structure the
   problem has, because the identity of a task never matters, only how often it
   recurs
2. Take `max_count`, the largest of those counts. That task type is the bottleneck,
   since it is the one whose copies are hardest to keep `n` apart
3. Count `kinds_at_max`, how many task types are tied at `max_count`. Those tie-ing
   types all need a slot in the final block, because each of them has one last run
   that cannot be pushed any earlier
4. Lay out the frame as `(max_count - 1) * (n + 1)` units. Read it as
   `max_count - 1` complete blocks, each holding one run of the bottleneck task
   followed by `n` units of cooldown, whether that cooldown is filled with other
   work or spent idle
5. Add `kinds_at_max` to the frame for the final block, which needs no trailing
   cooldown because nothing runs after it
6. Return `max(frame, len(tasks))`. The frame counts idle time that assumes there
   is nothing else to run, so when the task list is long and varied enough to fill
   every gap, the true answer is the number of tasks and the frame undercounts

```python
from collections import Counter


def least_interval(tasks: list[str], n: int) -> int:
    counts = Counter(tasks)
    max_count = max(counts.values())
    kinds_at_max = sum(1 for c in counts.values() if c == max_count)
    frame = (max_count - 1) * (n + 1) + kinds_at_max
    return max(frame, len(tasks))


assert least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8
assert least_interval(["A", "C", "A", "B", "D", "B"], 1) == 6
assert least_interval(["A", "A", "A", "B", "B", "B"], 3) == 10
assert least_interval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2) == 16
assert least_interval(["A"], 0) == 1
```

The first and second asserts are the two branches of that final `max`, so they are
the pair to check by hand

```text
tasks = AAABBB, n = 2
  max_count = 3, kinds_at_max = 2 (both A and B hit 3)
  frame = (3 - 1) * (2 + 1) + 2 = 8
  len(tasks) = 6, so the frame wins
  schedule:  A B idle | A B idle | A B          8 units, 2 idle

tasks = ACABDB, n = 1
  max_count = 2, kinds_at_max = 2 (A and B)
  frame = (2 - 1) * (1 + 1) + 2 = 4
  len(tasks) = 6, so the frame is REJECTED as an undercount
  schedule:  A B C A D B                        6 units, 0 idle
```

The second block is the discarded case. The frame of 4 is not merely
non-optimal, it is impossible, since six tasks cannot run in four minutes. That is
exactly what the `max` guards against, and forgetting it is the standard wrong
answer on this problem

- **Time Complexity:** `O(t)` where `t` is `len(tasks)`, because building the
  counter is one pass over the list and both `max` and the tie count scan at most
  26 entries, which is a constant
- **Space Complexity:** `O(1)`, because the counter holds one entry per distinct
  uppercase letter and there are at most 26 of them, so it does not grow with the
  input

## Time and Space Complexity

Throughout, `n` is the number of intervals or elements in the input, `d` is the
number of distinct values, and `g` is the required group size

**Choosing the most non-overlapping intervals**

| Approach                              | Time                                                                                                                                      | Space                                                                                                                                                                                        |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sort by end, one sweep                | `O(n log n)`: the sort dominates, since the sweep itself does `O(1)` work per interval for one comparison and one assignment              | `O(n)`: `sorted` allocates a new list of `n` intervals, and even an in-place `list.sort` needs `O(n)` scratch for its merge step, while the sweep itself keeps only `last_end` and a counter |
| DP over intervals sorted by end       | `O(n²)`: each interval scans every earlier interval to find the latest compatible one, which is what the weighted version genuinely needs | `O(n)`: one `dp` entry per interval, which the greedy version does not have to store at all                                                                                                  |
| Enumerating every subset of intervals | `O(2^n * n)`: there are `2^n` subsets and checking one for pairwise compatibility is `O(n)` once the intervals are sorted                 | `O(n)`: one subset held at a time, plus recursion depth of `n`                                                                                                                               |

**Sweeps that build their own boundary instead of sorting**

| Problem                                 | Time                                                                                                                                                             | Space                                                                                                                               |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Partition Labels                        | `O(n)`: one pass over the `n` characters to record last occurrences and a second to sweep, with no sort anywhere because the string is already in position order | `O(1)`: the last-occurrence map holds at most 26 lowercase letters, a fixed bound that does not grow with `n`                       |
| Partition Array into Disjoint Intervals | `O(n)`: a single pass maintaining two running maxima, each updated in `O(1)`                                                                                     | `O(1)`: two integers and the boundary index, since nothing about the prefix needs storing                                           |
| Candy                                   | `O(n)`: two passes over the line, one in each direction, each doing `O(1)` work per child                                                                        | `O(n)`: the `give` array holds one count per child and cannot be collapsed, because the second pass reads what the first pass wrote |

**Sort-then-commit variants**

| Problem                                   | Time                                                                                                                                                             | Space                                                                                          |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Boats to Save People                      | `O(n log n)`: the sort dominates the two-pointer pass, which advances `right` on every iteration and so runs at most `n` times                                   | `O(n)`: `sorted` copies the weights, and the pointers and boat count are `O(1)` on top of that |
| Advantage Shuffle                         | `O(n log n)`: two sorts, one over your cards and one over the opponent's indices, then a single linear assignment pass                                           | `O(n)`: the sorted copy, the index ordering, and the result array are each `O(n)`              |
| Hand of Straights                         | `O(n + d log d + d * g)`: counting is `O(n)`, sorting the `d` distinct values is `O(d log d)`, and each distinct value can start a run that touches `g` counters | `O(d)`: the counter holds one entry per distinct card value                                    |
| Split Array into Consecutive Subsequences | `O(n)`: one pass over the already-sorted input, with `O(1)` counter lookups per value and no sort of its own                                                     | `O(d)`: two counters, each with at most one entry per distinct value                           |
| Queue Reconstruction by Height            | `O(n²)`: the sort is `O(n log n)` but each `list.insert` shifts up to `n` elements, and there are `n` of them, so insertion dominates                            | `O(n)`: the output queue, which is also the working structure                                  |
| Task Scheduler                            | `O(t)` for `t` tasks: one counting pass, then constant work over at most 26 counts                                                                               | `O(1)`: at most 26 counter entries, independent of `t`                                         |

The `O(n²)` on Queue Reconstruction is worth volunteering rather than hiding. It
is accepted for that problem's input size, and the interviewer asking "can you do
better?" is fishing for a balanced tree or Fenwick structure that finds the `k`-th
empty slot in `O(log n)`, which is a
[range structure](../../17_advanced/notes/04_range_structures.md) follow-up rather
than a greedy one

## Summary

- An **interval** is a pair `[start, end]` claiming a stretch of a line, and two
  intervals **overlap** when they share at least one point. Unlike a sliding
  window, an interval is given data rather than a range you move, so the only
  lever you control is the order in which you read the input
- **Interval greedy** means sorting on one field and then sweeping once, carrying a
  single number that is usually `last_end`, the end of the most recently committed
  item, and accepting or discarding each item on the spot with no undo
  - Almost all the difficulty is in choosing the sort key. Everything after the
    sort is five lines
- For "keep the most non-overlapping intervals", **sort by end time**, not start
  time. Sorting by start lets one long interval such as `[0, 10]` be accepted
  early and consume the rest of the line, giving 1 where the answer is 2
  - The justifying **exchange argument** is that any optimal schedule's first
    interval can be swapped for the earliest-ending one, which finishes no later,
    so everything else in that schedule still fits and the count is unchanged
  - "Remove the fewest" is the same algorithm, since `erased = n - kept`, and there
    is never a reason to write a second sweep for it
- The comparison against `last_end` encodes the **overlap boundary**, and the
  problem's own physics decides whether it admits equality
  - Meetings `[1, 2]` and `[2, 3]` do not conflict, because one room is vacated at
    2 and the next occupied at 2, so the keep test is `start >= last_end`
  - Balloons `[1, 2]` and `[2, 3]` do share the point `x = 2` and one arrow pops
    both, so a new arrow is only needed when `start > last_end`
  - Update `last_end` only on an accepted item. Advancing it on a rejection
    silently refuses intervals that were bookable, and small tests will not catch it
- Some problems supply no intervals and expect you to derive them, then sweep the
  same way. Partition Labels turns each letter's first and last occurrence into an
  interval and carries a running `end` that only moves right, cutting when the scan
  index catches it
  - Partition Array into Disjoint Intervals is the same running boundary with two
    maxima, `left_max` for the committed prefix and `running_max` for everything
    seen, which are genuinely different numbers
- Several problems in this family sort by something that is not an endpoint, and
  the reasoning is unchanged: settle the **most constrained item** first, because
  its choice is forced, then recurse on what is left
  - Boats to Save People pairs the heaviest remaining person with the lightest,
    from both ends of a sorted array, launching one boat per loop pass
  - Hand of Straights starts a run at the smallest remaining card, since nothing
    smaller can sit below it
  - Queue Reconstruction by Height places the tallest people first, sorted
    `(-height, k)`, because a later, shorter insertion is invisible to everyone
    already placed and cannot disturb their `k`
- **Greedy is only safe when every item is worth the same.** Attach a value to each
  interval and earliest-end greedy takes `[0, 1]` and `[2, 3]` worth 1 each over
  `[0, 10]` worth 100. That version is weighted interval scheduling and needs DP
  - When a single left-to-right sweep cannot see a constraint on the other side, as
    in Candy, run the greedy twice in opposite directions and take the pointwise
    maximum. The second pass must use `max` and may only raise a value
- Cost is dominated by the sort at `O(n log n)` time whenever one is needed, and
  `O(1)` auxiliary space for the sweep itself on top of whatever the sort allocates
  - The exceptions in this topic are the derived-boundary sweeps such as Partition
    Labels, which are `O(n)` because the input is already in position order, and
    Queue Reconstruction, which is `O(n²)` because each `list.insert` shifts the
    tail of the queue

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
What is my sort key, and can I state the resource the greedy sweep is spending?
Why does sorting by end beat sorting by start for this problem specifically?
Can I give the exchange argument in one sentence: swap the optimal's first pick for mine, and nothing later breaks?
Do touching endpoints count as overlapping here, so is the test `start > last_end` or `start >= last_end`?
Is `last_end` seeded at -inf rather than 0, in case coordinates can be negative?
Am I updating `last_end` only when I actually commit to an item?
Am I counting the items I keep, the items I remove, or the number of groups I was forced to open?
Does the problem hand me intervals, or do I have to derive them from last occurrences or running maxima?
Do the intervals carry values? If so, greedy is wrong and this is a DP.
Does my answer have to line up with the input's original ordering, so must I sort indices instead of values?
Can one pass see every constraint, or does a right-side rule force a second pass with a `max`?
Am I mutating the caller's list with `.sort()` when `sorted()` would leave it alone?
```
