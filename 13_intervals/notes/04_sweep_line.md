# Sweep Line

A **sweep line** is an imaginary vertical line that slides left to right across the
coordinate axis while you keep track of what it is currently touching. The
intervals stop being objects you compare against each other and become instructions
that fire as the line passes them: this one turns something on here, that one turns
it off there

The whole technique rests on one observation about that line. Between two
consecutive endpoints, **nothing changes**. If the line is at position 12 and the
nearest endpoint in either direction is at 9 and 20, then the set of intervals
covering the line is identical at 10, at 11, at 12, and at 19. So the line does not
need to visit every position, only the positions where something happens, and those
are exactly the interval endpoints. Each one is an **event**

An event is a pair: a position, and the **delta**, meaning the amount the running
value changes there. An interval `[s, e)` that contributes `v` becomes `+v` at `s`
and `-v` at `e`, because that pair of deltas is true at every point on the line —
before `s` the interval contributes nothing, from `s` onward it contributes `v`, and
from `e` onward it contributes nothing again. Add up the deltas at or before any
position and you get the value there, which is a
[prefix sum](../../01_arrays_and_hashing/notes/03_prefix_suffix_sums.md) over the
event list

```text
        0    1    2    3    4    5    6    7    8    9
   a         [===================)                       a = [1, 5), value +1
   b                   [=============================)   b = [3, 9), value +1

delta       +1        +1        -1                  -1
position     1         3         5                   9
running 0    1    1    2    2    1    1    1    1    0
```

The `running` row is the answer to "how many intervals cover this point" at every
point at once, built from four writes instead of from scanning the intervals at each
of the ten positions. [Meeting rooms](03_meeting_rooms.md) already used a
`+1`/`-1` running count to find its peak. This topic is what that turns into when
the delta is an arbitrary number rather than one, when the coordinates are dense
enough to index directly, and when the thing you read off the running value is not a
peak but a whole profile

## Range Updates Instead Of Questions About A Pair

The signal is that every interval carries an **additive contribution over its whole
range**, and the question is about the accumulated total somewhere. It arrives
dressed as:

- Passengers boarding and leaving a car, seats booked across a run of flights, or
  paint applied over a stretch, which are *Car Pooling*, *Corporate Flight
  Bookings*, and *Describe the Painting*
- People alive in a given year, or points on a line covered by at least one car,
  which are *Maximum Population Year* and *Points That Intersect With Cars*
- Many range updates followed by one read of the whole array, which is the shape
  that makes the difference array below worth its extra slot
- The gaps rather than the coverage, as in *Employee Free Time*, since a gap is
  precisely a stretch where the running count sits at zero

What it is **not** for is a question about the shape of the union, which
[merging](02_merge_insert.md) answers directly and more simply, or a question about
one specific pair of intervals, which the
[overlap test](01_interval_basics.md) settles in a line. It is also the wrong tool
when the contribution is not additive, which is the last section of this topic

## Why Writing Into Every Position Of A Range Dies

*Corporate Flight Bookings* gives `n` flights numbered `1` through `n` and a list of
bookings, each `[first, last, seats]`, meaning `seats` seats were reserved on every
flight from `first` to `last` inclusive. Return how many seats are booked on each
flight

The direct reading of that sentence is also a direct program. For each booking, loop
over its flights and add the seats

```python
def stamp_bookings(bookings: list[list[int]], n: int) -> list[int]:
    seats = [0] * n
    for first, last, booked in bookings:
        for flight in range(first, last + 1):
            seats[flight - 1] += booked
    return seats


assert stamp_bookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5) == [10, 55, 45, 25, 25]
assert stamp_bookings([], 3) == [0, 0, 0]
```

It is correct and it is `O(b * n)` for `b` bookings over `n` flights, because a
single booking spanning the whole schedule touches every one of the `n` slots. This
problem allows `2 * 10^4` bookings over `2 * 10^4` flights, so the worst case is
`4 * 10^8` additions and a timeout

The waste is worth naming precisely, because naming it is the algorithm. Look at
what the inner loop writes into `seats` for the booking `[2, 5, 25]`: it adds 25,
then 25, then 25, then 25. Three of those four writes record that **nothing
changed** relative to the slot before. The only two positions where this booking
makes any difference to its neighbour are its two ends, where the contribution goes
from nothing to 25 and from 25 back to nothing

So stop storing the value and start storing the **change** in the value. A booking
becomes two writes rather than a whole range of them, and the values are recovered
at the end by adding the changes up

## Two Writes Per Range And One Prefix Sum

A **difference array** is an array `diff` where `diff[i]` holds how much the answer
changes between position `i - 1` and position `i`, rather than the answer itself.
Adding `v` across the closed range `[l, r]` is then two assignments, `diff[l] += v`
and `diff[r + 1] -= v`, no matter how wide the range is. Running a prefix sum over
`diff` at the end turns the changes back into values

```python
def corp_flight_bookings(bookings: list[list[int]], n: int) -> list[int]:
    diff = [0] * (n + 1)
    for first, last, booked in bookings:
        diff[first - 1] += booked
        diff[last] -= booked
    seats: list[int] = []
    running = 0
    for i in range(n):
        running += diff[i]
        seats.append(running)
    return seats


assert corp_flight_bookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5) == [10, 55, 45, 25, 25]
assert corp_flight_bookings([[1, 2, 10], [2, 2, 15]], 2) == [10, 25]
assert corp_flight_bookings([[1, 5, 4]], 5) == [4, 4, 4, 4, 4]
assert corp_flight_bookings([], 3) == [0, 0, 0]
```

**The four decisions in those eight lines**:

- `[0] * (n + 1)` allocates one slot more than there are flights, and that extra
  slot is the entire reason this code has no special case for a booking that runs to
  the last flight. Its closing `-v` needs somewhere to land, and without the spare
  slot `diff[last]` with `last == n` raises `IndexError`
- The subtraction goes at `last` rather than `last + 1` **only because flights are
  1-indexed and the array is 0-indexed**, so `diff[last]` already means "the slot
  after flight `last`". Written on 0-indexed coordinates the pair is
  `diff[l] += v` and `diff[r + 1] -= v`, and mixing the two conventions is the
  standard off-by-one here
- The deltas from different bookings simply pile up in the same slot, which is why
  `diff[1]` ends up holding `45` from two separate bookings. Nothing has to be
  sorted or grouped, since addition does not care what order it happens in
- `running` is carried across the loop rather than recomputed, which is the prefix
  sum. Every booking is now `O(1)` work and the single recovery pass is `O(n)`,
  giving `O(b + n)` in place of `O(b * n)`

### Dry Run: Three Bookings Over Five Flights

Bookings `[[1, 2, 10], [2, 3, 20], [2, 5, 25]]` with `n = 5`, so `diff` has six
slots for five flights

```text
booking          writes                       diff after
-               -                             [ 0,  0,  0,  0,  0,  0]
[1, 2, 10]      diff[0] += 10, diff[2] -= 10  [10,  0,-10,  0,  0,  0]
[2, 3, 20]      diff[1] += 20, diff[3] -= 20  [10, 20,-10,-20,  0,  0]
[2, 5, 25]      diff[1] += 25, diff[5] -= 25  [10, 45,-10,-20,  0,-25]
```

```text
i    diff[i]   running    flight   seats
0      10        10          1       10
1      45        55          2       55
2     -10        45          3       45
3     -20        25          4       25
4       0        25          5       25
5     -25       DISCARDED    -        -
```

Two rows in that second table carry the idea. Slot 4 holds a delta of zero, and the
running total passes straight through it unchanged, which is exactly the redundancy
the stamping version was paying for three times over on the booking `[2, 5, 25]`

Slot 5 is the discarded one, and it is discarded on purpose. It holds the `-25` that
closes the booking running through flight 5, and the recovery loop stops at `i < n`
so it is never read. It has to be **written** anyway, because if the code guarded
that write with an `if last < n` it would still be correct here and would break the
moment the same array was reused, and because leaving the closing delta out is what
turns a difference array into a silently wrong one when a later range starts where
an earlier one ended

### The Same Two Writes, Three More Problems

*Car Pooling* asks whether a car of a given capacity can serve every trip, where
each trip is `[passengers, from, to]` and passengers occupy the car over `[from, to)`.
Positions are locations along a road bounded at 1000, so the array can be sized once
and the sweep reads the peak rather than the whole profile

```python
def car_pooling(trips: list[list[int]], capacity: int) -> bool:
    diff = [0] * 1001
    for passengers, start, end in trips:
        diff[start] += passengers
        diff[end] -= passengers
    riders = 0
    for delta in diff:
        riders += delta
        if riders > capacity:
            return False
    return True


assert car_pooling([[2, 1, 5], [3, 3, 7]], 4) is False
assert car_pooling([[2, 1, 5], [3, 3, 7]], 5) is True
assert car_pooling([[2, 1, 5], [3, 5, 7]], 3) is True
assert car_pooling([], 1) is True
```

The subtraction lands on `end` and not `end + 1`, which is the half-open convention
from [interval basics](01_interval_basics.md) written as arithmetic: passengers get
out at the drop-off point, so they are not in the car at `end`. The third assert is
what enforces it, since one group leaving at 5 and another boarding at 5 must not be
counted together, and moving the subtraction to `end + 1` returns `False` there

*Maximum Population Year* is the same array with the coordinate shifted, since the
years run from 1950 to 2050 and an array is indexed from zero. A person alive over
`[birth, death)` is `+1` and `-1`, and the answer is the earliest year achieving the
peak, which falls out of using a strict `>` when updating the best

```python
def maximum_population(logs: list[list[int]]) -> int:
    diff = [0] * 101
    for birth, death in logs:
        diff[birth - 1950] += 1
        diff[death - 1950] -= 1
    best_year = 1950
    best = alive = 0
    for offset, delta in enumerate(diff):
        alive += delta
        if alive > best:
            best = alive
            best_year = 1950 + offset
    return best_year


assert maximum_population([[1993, 1999], [2000, 2010]]) == 1993
assert maximum_population([[1950, 1961], [1960, 1971], [1970, 1981]]) == 1960
assert maximum_population([[2033, 2034]]) == 2033
```

The strict `alive > best` is the tie rule. A later year that merely matches the peak
leaves `best_year` alone, and writing `>=` would return the last such year instead of
the first, which is the wrong answer with no visible symptom on inputs that have a
unique peak

*Points That Intersect With Cars* uses **inclusive** endpoints, so the closing delta
moves one slot right, and the question is a count of positions rather than a peak

```python
def number_of_points(nums: list[list[int]]) -> int:
    diff = [0] * 102
    for start, end in nums:
        diff[start] += 1
        diff[end + 1] -= 1
    covered = running = 0
    for delta in diff:
        running += delta
        if running > 0:
            covered += 1
    return covered


assert number_of_points([[3, 6], [1, 5], [4, 7]]) == 7
assert number_of_points([[1, 3], [5, 8]]) == 7
assert number_of_points([[4, 4]]) == 1
assert number_of_points([]) == 0
```

`running > 0` rather than `running == 1` is the whole difference between counting
covered points and counting singly-covered ones, and the first assert is the case
that separates them, since three cars overlap heavily and the answer 7 counts each
position once

Three problems, one array, and the only things that varied were where the closing
delta lands and what gets read off the running total. That is the shape to keep

## When The Coordinates Are Too Spread Out To Index

The difference array needs one slot per possible coordinate, so it works only when
the coordinate range is small enough to allocate. Flights, road markers, years, and
positions bounded at 100 all qualify. Timestamps up to `10^9` do not, and neither do
the coordinates in *Describe the Painting* or *The Skyline Problem*

Keep the same events and drop the array. Build a list of `(position, delta)` pairs,
sort it, and walk it carrying the running total. The sort costs `O(n log n)` and
buys independence from how far apart the coordinates are, since only the `2n`
positions that actually appear are ever visited

```python
def max_overlap(intervals: list[list[int]]) -> int:
    events: list[tuple[int, int]] = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    events.sort()
    active = best = 0
    for _, delta in events:
        active += delta
        best = max(best, active)
    return best


assert max_overlap([[0, 30], [5, 10], [15, 20]]) == 2
assert max_overlap([[1, 5], [5, 9], [2, 6]]) == 2
assert max_overlap([[1, 5], [5, 9]]) == 1
assert max_overlap([[7, 7]]) == 0
assert max_overlap([]) == 0
```

Compare this against the two-array race in [meeting rooms](03_meeting_rooms.md),
which answers the same question by sorting the starts and the ends into separate
lists. Both are sweeps. The event list is the version that generalises, because an
event can carry any delta rather than an implied `+1`, and because one list can hold
events of several kinds at once, which is what the skyline needs below

**The tie-break is the one real decision here, and `events.sort()` makes it
silently.** Tuples compare element by element, so events at the same position are
ordered by their delta, and `-1` sorts before `+1`. Ends are therefore processed
before starts at a shared coordinate, which is precisely the half-open convention:
an interval ending at 5 has already released its contribution before one starting at
5 claims it

For **inclusive** endpoints, where two intervals sharing the coordinate 5 do overlap
there, the starts must come first instead, which is one key away

```python
def max_overlap_closed(intervals: list[list[int]]) -> int:
    events: list[tuple[int, int]] = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    events.sort(key=lambda event: (event[0], -event[1]))
    active = best = 0
    for _, delta in events:
        active += delta
        best = max(best, active)
    return best


assert max_overlap_closed([[1, 5], [5, 9]]) == 2
assert max_overlap_closed([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]) == 3
assert max_overlap_closed([[7, 7]]) == 1
assert max_overlap_closed([]) == 0
```

The zero-width interval `[7, 7]` is the cleanest test of which convention you have
built. Half-open, it covers nothing and the peak is 0; inclusive, it covers the
single point 7 and the peak is 1. Both asserts above are on the same input and
disagree, which is the whole point

> "Events at the same coordinate need an order. I am sorting `(position, delta)`,
> which puts the `-1` first and makes a meeting ending at 5 free the room for one
> starting at 5. If these endpoints are inclusive instead, I flip the tie-break to
> `(position, -delta)` and nothing else changes."

### Dry Run: Three Intervals Sharing One Coordinate

`[[1, 5], [5, 9], [2, 6]]` under the half-open convention, so the six events sort to

```text
[(1, 1), (2, 1), (5, -1), (5, 1), (6, -1), (9, -1)]
```

```text
position   delta   active   best   note
   1        +1        1       1    [1, 5) opens
   2        +1        2       2    [2, 6) opens, two intervals now cover this point
   5        -1        1       2    [1, 5) closes FIRST, because -1 sorts before +1
   5        +1        2       2    [5, 9) opens into the slot just released
   6        -1        1       2    [2, 6) closes
   9        -1        0       2    [5, 9) closes, and the count returns to zero
```

The two rows at position 5 are the whole trace. The `-1` is processed and the `+1`
is made to wait, so `active` never reaches 3, and the peak stays at 2. Reverse those
two rows, which is what `sort(key=lambda e: (e[0], -e[1]))` does, and `active` hits 3
at position 5 and the function reports 3. Both answers are computed correctly by the
same code; only one of them answers the question the problem asked

The last row is worth a glance too. `active` finishes at 0, not at the peak, which is
why `best` is updated inside the loop and never read off the final value

## Reading The Gaps Where The Count Falls To Zero

Everything so far reads a peak or a profile. The third thing to read is the
**absence** of coverage, and it needs no new machinery, because a gap is a maximal
stretch where the running count is zero

*Employee Free Time* hands you a schedule per employee, each already sorted and
disjoint, and asks for the intervals where **every** employee is free. Pooling all
the busy intervals into one event list and sweeping them collapses the "every
employee" part, since the count is zero exactly when nobody is busy

```python
def employee_free_time(schedule: list[list[list[int]]]) -> list[list[int]]:
    events: list[tuple[int, int]] = []
    for person in schedule:
        for start, end in person:
            events.append((start, 1))
            events.append((end, -1))
    events.sort()
    free: list[list[int]] = []
    active = 0
    gap_start: int | None = None
    for position, delta in events:
        if active == 0 and gap_start is not None and position > gap_start:
            free.append([gap_start, position])
        active += delta
        if active == 0:
            gap_start = position
    return free


assert employee_free_time([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]) == [[3, 4]]
assert employee_free_time([[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]) == [[5, 6], [7, 9]]
assert employee_free_time([[[1, 2], [2, 3]]]) == []
assert employee_free_time([[[1, 4]]]) == []
assert employee_free_time([]) == []
```

**Why the check runs before the delta is applied**: `gap_start` is set the moment
the count reaches zero, and the gap closes at the next position where work resumes.
Testing `active == 0` before adding the delta is what catches that reopening event
while the count still reflects the empty stretch behind it

**Why `position > gap_start` is not optional**: back-to-back intervals such as
`[1, 2]` and `[2, 3]` produce a `-1` and a `+1` at position 2, and the `-1` runs
first, so the count momentarily touches zero and `gap_start` becomes 2. The very
next event is at position 2 as well, and without the strict comparison the code
would emit the empty interval `[2, 2]` as free time. The third assert is that case

The trace on the second assert shows the events after the pool and the sort

```text
position   delta   active   gap_start   emitted
   1        +1        1        None        -
   2        +1        2        None        -
   2        +1        3        None        -
   3        -1        2        None        -
   4        -1        1        None        -
   5        -1        0          5         -        count hits zero, a gap opens
   6        +1        1          5      [5, 6]      work resumes, the gap closes
   7        -1        0          7         -        another gap opens
   9        +1        1          7      [7, 9]      and closes
  12        -1        0         12         -        DISCARDED: no event follows
```

The final row is the discarded one, and it is discarded correctly. The count drops
to zero at 12 and `gap_start` is set, but the event list is exhausted and no later
event ever closes that gap. Free time after everybody's last meeting stretches to
infinity and is not an interval, so the loop structure drops it for free rather than
needing a guard

## When The Running Value Cannot Be Undone

Every sweep above kept a running **sum**, and sums are what make the two-write trick
work: `+v` at the start and `-v` at the end cancel exactly, so a delta can undo
itself with no memory of what else is going on

*The Skyline Problem* breaks that. Buildings arrive as `[left, right, height]`, and
the outline you must emit is governed by the **tallest** active building at each
position, not the total. A maximum cannot be undone by a delta, because subtracting
the height of a building that just ended tells you nothing about what the new
maximum is. You would have to know the second-tallest, and the third, in case they
ended too

So the running value becomes an actual collection of the active heights rather than a
single number, and a max-heap keeps its largest at the root. Two details make it
work. Entries are pushed as `(-height, right)` so Python's min-heap behaves as a
max-heap and each entry remembers when it expires, and expired entries are cleared by
**lazy deletion**, the same delayed-cleanup idea used by
[two heaps](../../08_heaps/notes/03_two_heaps.md) and by
[Dijkstra](../../10_graphs/notes/07_weighted_shortest_paths.md): a buried stale entry
is left alone and only discarded once it surfaces at the root

```python
import heapq


def get_skyline(buildings: list[list[int]]) -> list[list[int]]:
    events: list[tuple[int, int, int]] = []
    for left, right, height in buildings:
        events.append((left, -height, right))
        events.append((right, 0, 0))
    events.sort()
    active: list[tuple[int, float]] = [(0, float("inf"))]
    skyline: list[list[int]] = []
    for position, negative_height, right in events:
        while active[0][1] <= position:
            heapq.heappop(active)
        if negative_height:
            heapq.heappush(active, (negative_height, right))
        tallest = -active[0][0]
        if not skyline or skyline[-1][1] != tallest:
            skyline.append([position, tallest])
    return skyline


assert get_skyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]) == [
    [2, 10],
    [3, 15],
    [7, 12],
    [12, 0],
    [15, 10],
    [20, 8],
    [24, 0],
]
assert get_skyline([[0, 2, 3], [2, 5, 3]]) == [[0, 3], [5, 0]]
assert get_skyline([[1, 2, 1]]) == [[1, 1], [2, 0]]
assert get_skyline([]) == []
```

**The sentinel `(0, float("inf"))` seeded into the heap** is why there is no
empty-heap branch. Ground level is a building of height 0 that never ends, so the
root is always readable and the drop back to 0 between separate buildings is emitted
by the same line as every other height change

**The `if negative_height` test distinguishes the two event kinds** in one list. A
left edge carries a real negative height and is pushed; a right edge carries 0, which
is falsy, and only exists so the sweep stops at that coordinate to re-read the root

**The `skyline[-1][1] != tallest` guard is the output contract**, since the answer is
a list of the positions where the height *changes*. A building that opens entirely
underneath a taller one changes nothing visible and must emit nothing

Tracing three buildings, `[[2, 9, 10], [3, 7, 15], [5, 12, 12]]`

```text
position   event         heap after (height, expiry)          tallest   emitted
   2       open h=10     [(10, 9), (0, inf)]                     10      [2, 10]
   3       open h=15     [(15, 7), (10, 9), (0, inf)]            15      [3, 15]
   5       open h=12     [(15, 7), (12, 12), (10, 9), (0, inf)]  15      REJECTED
   7       close         [(12, 12), (10, 9), (0, inf)]           12      [7, 12]
   9       close         [(12, 12), (10, 9), (0, inf)]           12      REJECTED
  12       close         [(0, inf)]                               0      [12, 0]
```

Row three is the rejected emission and the reason the guard exists. A building of
height 12 opens at position 5 and is completely hidden behind the 15, so the tallest
is unchanged and nothing is written to the output

Row five is the rejected **pop**, and it is lazy deletion made visible. The building
`[2, 9, 10]` expires at position 9, but its heap entry `(10, 9)` is sitting behind
`(12, 12)` rather than at the root, so the `while` loop does not reach it and it
stays in the heap as garbage. That is harmless, because it can only be wrong if it
surfaces, and the moment it surfaces at row six it is popped before the root is read.
Hunting it down when it expires would cost a linear scan of the heap for no gain

Not every sweep-shaped problem in the ladder reduces to a running total, and knowing
which tool the deviation needs is the recognition step:

- *Falling Squares* sweeps squares in order and needs the **maximum** height over an
  arbitrary sub-range rather than at a point, which is a
  [range structure](../../17_advanced/notes/04_range_structures.md) question once the
  coordinates are compressed onto the endpoints that actually occur
- *Amount of New Area Painted Each Day* asks for newly covered length, so it must
  remember which coordinates are already painted and skip over them, which is a
  disjoint set of painted stretches rather than a counter
- *Range Module* is the disjoint interval set from [merging](02_merge_insert.md)
  turned into a design problem with add, remove, and query
- *Set Intersection Size At Least Two* sorts by end and greedily takes the two
  largest points each interval can spare, which is
  [interval greedy](../../12_greedy_algorithms/notes/03_interval_greedy.md) rather
  than a sweep at all

## Worked Example: [Describe the Painting](https://leetcode.com/problems/describe-the-painting/)

A long wall is painted by a sequence of segments, each covering a stretch of the wall
in one color. Colors mix by adding their numeric labels together, so a stretch
painted by colors 5 and 9 has color sum 14. Return the painting as a list of maximal
pieces that each have a single color sum, skipping stretches nobody painted

**Input**: `segments`, a `list[list[int]]` where each entry is
`[start, end, color]`. The segment covers the half-open stretch `[start, end)` of the
wall with `start < end`, and `color` is a positive integer label. No two segments
share both endpoints with the same color, but any number of segments may overlap each
other, and the list may be empty

**Output**: a `list[list[int]]` of entries `[start, end, mixed_color]`, where
`mixed_color` is the **sum** of the labels of every segment covering that stretch.
The pieces must be non-overlapping, must cover exactly the painted parts of the wall,
and adjacent pieces must have different color sums — except that two pieces are still
separate when equal sums come from genuinely different segments, since the problem
compares the mixtures and not only their totals. Unpainted stretches produce no entry
at all, so the output can have gaps

The identifying phrase is "colors mix by adding", which makes the contribution
additive and hands the problem to a sweep. The naive version walks the wall
coordinate by coordinate summing the colors covering each one, and it dies for the
reason the flight bookings did, except worse: coordinates here reach `10^5` and there
are up to `2 * 10^4` segments, so stamping every coordinate of every segment is
`2 * 10^9` additions

Each segment becomes `+color` at its start and `-color` at its end. Sorting the
distinct positions gives the boundaries of every piece, since between two consecutive
boundaries no segment starts or ends and the color sum is therefore constant. Walk
those positions carrying the running sum, and each adjacent pair of positions is one
candidate piece

> "Colors add, so each segment is `+color` at its start and `-color` at its end. The
> sorted distinct positions are the only places the mixture can change, so between
> consecutive positions the sum is constant and each adjacent pair is one output
> piece. I emit a piece only when the running sum is non-zero, because a zero sum
> means nobody painted that stretch."

1. Accumulate the deltas into a dictionary keyed by position, adding `color` at
   `start` and subtracting it at `end`. A dictionary rather than an array, because
   the coordinates are too spread out to allocate a slot each, and a
   `defaultdict(int)` so that several segments sharing a boundary accumulate there
   instead of overwriting one another
2. Sort the dictionary's keys. These are every position where the mixture can change,
   and there are at most `2n` of them for `n` segments, which is far fewer than the
   width of the wall
3. Walk the sorted positions with an index, stopping one short of the last. Each step
   considers the stretch from the current position to the next one, and the final
   position closes the last stretch rather than opening a new one, so it has no
   partner to its right
4. At each position add its delta to the running sum **before** emitting, because the
   delta at a position describes the stretch beginning there. Adding afterwards
   shifts every piece one boundary to the left
5. Emit `[positions[i], positions[i + 1], running]` when `running` is non-zero. A
   zero sum means every segment that opened here has already closed, so this stretch
   of wall is bare and produces no entry, which is how the gaps appear in the output
6. Return the collected pieces, which are already sorted and non-overlapping because
   the positions were walked in increasing order and each piece spans exactly one
   consecutive pair

```python
from collections import defaultdict


def split_painting(segments: list[list[int]]) -> list[list[int]]:
    delta: defaultdict[int, int] = defaultdict(int)
    for start, end, color in segments:
        delta[start] += color
        delta[end] -= color
    positions = sorted(delta)
    painted: list[list[int]] = []
    running = 0
    for i in range(len(positions) - 1):
        running += delta[positions[i]]
        if running:
            painted.append([positions[i], positions[i + 1], running])
    return painted


assert split_painting([[1, 4, 5], [4, 7, 7], [1, 7, 9]]) == [[1, 4, 14], [4, 7, 16]]
assert split_painting([[1, 7, 9], [6, 8, 15], [8, 10, 7]]) == [
    [1, 6, 9],
    [6, 7, 24],
    [7, 8, 15],
    [8, 10, 7],
]
assert split_painting([[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]]) == [[1, 4, 12], [4, 7, 12]]
assert split_painting([[1, 4, 5], [6, 8, 7]]) == [[1, 4, 5], [6, 8, 7]]
assert split_painting([]) == []
```

Tracing the fourth assert, two segments with bare wall between them. The deltas are
`{1: 5, 4: -5, 6: 7, 8: -7}`, so the sorted positions are `1, 4, 6, 8`

```text
i   position   delta   running   stretch    action
0       1        +5       5       [1, 4)    emit [1, 4, 5]
1       4        -5       0       [4, 6)    REJECTED, sum is 0 so the wall is bare
2       6        +7       7       [6, 8)    emit [6, 8, 7]
-       8         -        -         -      no partner to the right, loop has ended
```

Row one is the rejected step and it is the only thing separating this from a solution
that reports a phantom piece `[4, 6, 0]`. The running sum genuinely passes through
that stretch, the boundary at 4 is genuinely an event, and the code still emits
nothing, because a color sum of zero means no segment is active

The last row is why the loop runs to `len(positions) - 1`. Position 8 closes the
final segment and has nothing to its right, so pairing it with a next position would
read past the end of the list

The third assert is worth keeping for a different reason. Both pieces come out with
the sum 12 and are still reported separately, because they are built from different
segments, and any post-processing step that merged adjacent equal sums would fail it

- **Time Complexity**: `O(n log n)` for `n` segments, because building the delta map
  is `O(n)` with `2n` dictionary updates and sorting its at most `2n` keys dominates
  at `O(n log n)`, after which the emitting pass is linear in the number of positions
- **Space Complexity**: `O(n)`, because the map holds at most `2n` keys, one per
  distinct endpoint, and the output holds at most `2n - 1` pieces, one per consecutive
  pair of positions

## Time and Space Complexity

Throughout, `n` is the number of intervals, `C` is the size of the coordinate range
when it is bounded, and `b` is the number of range updates when those are counted
separately from reads

**Applying `b` range updates and then reading the whole array**

| Approach                                          | Time                                                                                                                                            | Space                                                                                                                                             |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Difference array, two writes plus one prefix pass | `O(b + C)`: each update is two constant-time writes regardless of how wide its range is, then one sweep over the `C` slots recovers every value | `O(C)`: one slot per coordinate plus the single spare that catches a closing delta at the far end, allocated whether or not the ranges are sparse |
| Writing into every position of every range        | `O(b * C)`: a single update spanning the whole range touches all `C` slots, and the interior writes all record that nothing changed             | `O(C)`: the same array, which is why this version looks identical in a memory profile and only fails on the clock                                 |

**Finding the peak or the profile when coordinates are unbounded**

| Approach                                                                         | Time                                                                                                                    | Space                                                                             |
| -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Sorted `(position, delta)` event list                                            | `O(n log n)`: building `2n` events is linear and sorting them dominates, after which one pass carries the running total | `O(n)`: the `2n` events, with the running total and the best kept in two integers |
| Difference array over the coordinate range                                       | unusable: with coordinates up to `10^9` the `O(C)` sweep is `10^9` steps regardless of how few intervals there are      | `O(C)`: the allocation alone is what rules it out, since `10^9` slots do not fit  |
| Independently sorted starts and ends, as in [meeting rooms](03_meeting_rooms.md) | `O(n log n)`: two sorts of `n` values, then a single pass consuming each boundary once                                  | `O(n)`: the two boundary arrays, and it cannot carry a delta other than `±1`      |

**The three sweeps in this topic that read something other than a peak**

| Problem                                                            | Time                                                                                                                                             | Space                                                                                                                                         |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Employee Free Time, `n` busy intervals pooled across all employees | `O(n log n)`: sorting the `2n` pooled events dominates the single emitting pass                                                                  | `O(n)`: the event list, plus an output holding at most `n - 1` gaps since a gap needs a busy interval on each side                            |
| Describe the Painting, `n` segments                                | `O(n log n)`: sorting the at most `2n` distinct endpoint keys, with the map built in `O(n)`                                                      | `O(n)`: the delta map keyed by distinct endpoint, plus at most `2n - 1` output pieces                                                         |
| The Skyline Problem, `n` buildings                                 | `O(n log n)`: sorting `2n` events, then each building pushed once and popped at most once from a heap of size at most `n + 1` at `O(log n)` each | `O(n)`: the event list and the heap, which holds every building at once when they all overlap, including stale entries not yet lazily deleted |

The skyline's `while` loop looks like it could make one iteration `O(n)`, and it can.
Across the whole run it is `O(n log n)` in total, because every entry is pushed once
and popped at most once, which is the same amortized counting argument as
[draining a stale front](../../03_stacks_and_queues/notes/02_queue_and_deque.md)

## Summary

- A **sweep line** is a line moving along the coordinate axis while you carry a
  running value describing what it currently touches. Nothing changes between two
  consecutive endpoints, so the line only ever has to stop at endpoints, which turns
  a question about a whole coordinate range into a walk over at most `2n` positions
  - Each stop is an **event**, a pair of a position and a **delta**. An interval
    `[s, e)` contributing `v` becomes `+v` at `s` and `-v` at `e`, and the running
    total after adding every delta at or before a position is the value there
- Writing the contribution into every position of a range is `O(b * C)` for `b`
  updates over `C` coordinates, and almost all of those writes record that nothing
  changed relative to the position before. Only the two endpoints of a range are
  places where the value actually moves
- A **difference array** stores the change at each position instead of the value, so
  adding `v` over `[l, r]` is `diff[l] += v` and `diff[r + 1] -= v` however wide the
  range is, and one prefix-sum pass turns the changes back into values
  - Allocate one slot more than there are coordinates, since a range ending at the
    last position needs somewhere to put its closing delta, and that slot is written
    and then never read
  - Deltas from different ranges pile into the same slot with no sorting or grouping,
    because addition does not care about order
  - Use it only when the coordinate range is small enough to allocate. Flights,
    years, and road markers bounded near 1000 qualify; timestamps up to `10^9` do not
- When the coordinates are too spread out, build a list of `(position, delta)` pairs
  and sort it instead, which costs `O(n log n)` and visits only the positions that
  actually occur. This is the version that generalises, since a delta can be any
  number and one list can hold several kinds of event
- Sorting `(position, delta)` puts `-1` before `+1` at a shared coordinate, so ends
  are processed before starts, which is the **half-open** convention where an
  interval ending at 5 releases its contribution before one starting at 5 claims it
  - For **inclusive** endpoints, sort by `(position, -delta)` so starts go first, and
    nothing else in the code changes
  - The zero-width interval `[7, 7]` is the fastest way to tell which one you built,
    since it contributes a peak of 0 half-open and 1 inclusive
- What you read off the running total is what varies between problems, and the sweep
  itself does not change
  - The **peak** answers Car Pooling and Maximum Population Year, and the best must
    be recorded inside the loop because the running total finishes at zero
  - The **whole profile** answers Corporate Flight Bookings, emitted one value per
    coordinate
  - A **count of positions where the total is positive** answers Points That
    Intersect With Cars, and testing `> 0` rather than `== 1` is what counts covered
    points rather than singly-covered ones
  - The **stretches where the total is zero** answer Employee Free Time, where a gap
    opens when the count hits zero and closes at the next event, with a strict
    `position > gap_start` to reject the empty gap that back-to-back intervals create
- The two-write trick works because sums are undoable, since `+v` and `-v` cancel
  with no memory of anything else. A running **maximum** is not undoable, because
  removing the current maximum says nothing about what the next one is
  - The Skyline Problem therefore keeps a max-heap of `(-height, right)` entries
    rather than a number, emits only when the root's height differs from the last
    emitted one, and seeds the heap with a ground-level sentinel `(0, inf)` so there
    is never an empty-heap case
  - Expired entries are cleared by **lazy deletion**, meaning a stale entry buried
    below the root is left alone until it surfaces, which keeps every building to one
    push and at most one pop

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
Is each interval an additive contribution over its range, or a question about a pair?
Is the coordinate range small enough to allocate a slot per position, or must I sort events?
For a difference array, did I allocate one extra slot for a range that ends at the far end?
Is the closing delta at end or at end + 1, and which endpoint convention does that encode?
At a shared coordinate, does the end or the start fire first, and can I name the sort key?
Have I checked a zero-width interval like [7, 7] against the convention I claimed?
Am I reading the peak, the whole profile, the covered count, or the zero-valued gaps?
If I want the peak, is best updated inside the loop rather than read off the final total?
Is my running value a sum, which a delta can undo, or a max, which needs the full multiset?
If it needs a heap, are stale entries lazily deleted at the root rather than hunted down?
Would merging into a disjoint set answer this more simply than a sweep?
```
