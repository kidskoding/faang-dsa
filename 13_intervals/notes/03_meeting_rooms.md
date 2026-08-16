# Meeting Rooms

Pick any single moment in time and count how many intervals contain it. That
count is the **concurrency** at that moment, also called the **overlap depth**.
It changes as you move along the time axis, going up whenever an interval opens
and down whenever one closes, and the largest value it ever reaches is the
**maximum concurrency**.

That one number is the answer to a whole family of interview problems. If every
interval is a meeting that needs a room, and two meetings happening at the same
time cannot share a room, then the number of rooms you must book is exactly the
maximum concurrency. Book that many and you are never short; book one fewer and
the moment of peak overlap has a meeting with nowhere to go.

This is a different question from the one [merging](02_merge_insert.md) answers.
Merging collapses a pile of overlapping intervals into a single interval and
deliberately throws away how deep the pile was. Five meetings stacked on top of
each other and five meetings chained end to end both merge to one block, and the
first needs five rooms while the second needs one.

```text
        0         1         2         3         4
        0....5....0....5....0....5....0....5....0
   A    [=============================)
   B         [====)
   C                [============)
   D                   [====)
   E                                  [=========)
active  11111222221122233333222221111111111111110
```

Merging those five meetings gives `[0, 40)`, one block, which says nothing
useful. The `active` row is the real shape: it climbs to 3 during `[15, 20)`
where A, C and D are all running, and never goes higher. Three rooms.

## Booking Rooms Versus Merging A Calendar

The signal is a question about **how many things are happening at once**, or
about whether a new thing can be squeezed in beside what is already there. It
shows up dressed as:

- Rooms, servers, or workers that must be allocated so nothing collides, which is
  *Meeting Rooms II* and *Divide Intervals Into Minimum Number of Groups* wearing
  different words
- A booking system that accepts or rejects a request depending on what overlaps
  it, which is the *My Calendar* family
- A count taken at one instant, as in "how many flowers are blooming when this
  person walks past"
- A yes-or-no question about whether **any** two things collide, which is the
  degenerate case where you only need to know whether the peak reaches 2

That last one is *Meeting Rooms*, the easy warmup, and it does not need any of
the machinery below. Sort by start and compare each meeting against the one
before it, since after sorting the only meeting that can conflict with a given
one is the meeting immediately preceding it in start order.

```python
def can_attend_meetings(intervals: list[list[int]]) -> bool:
    ordered = sorted(intervals)
    for i in range(1, len(ordered)):
        if ordered[i][0] < ordered[i - 1][1]:
            return False
    return True


assert can_attend_meetings([[0, 30], [5, 10], [15, 20]]) is False
assert can_attend_meetings([[7, 10], [2, 4]]) is True
assert can_attend_meetings([[1, 5], [5, 9]]) is True
assert can_attend_meetings([]) is True
```

The `<` rather than `<=` is the endpoint convention doing real work. A meeting
`[1, 5)` and a meeting `[5, 9)` are back to back, and the first has vacated the
room before the second walks in, so they do not conflict. Every problem in this
topic has this decision buried in it, and it is the first thing to ask about out
loud.

> "Are the intervals half-open, so a meeting ending at 5 and one starting at 5
> can share a room? I will assume yes unless the examples say otherwise, and I
> will point out the single comparison that flips if I am wrong."

What this topic is **not** for is any question about total covered time or about
the shape of the union, since those are merge problems, and any question that only
asks whether a specific pair overlaps, which the
[overlap test](01_interval_basics.md) already settles in one line.

## Why Counting Overlaps One Meeting At A Time Dies

The obvious way to find the peak is to compute the concurrency at each meeting's
start, since the count only ever rises at a start and so the peak must be
attained at one. For each meeting, walk the whole list and count how many
meetings contain that start time, then take the largest count.

```python
def min_rooms_pairwise(intervals: list[list[int]]) -> int:
    best = 0
    for start, _ in intervals:
        active = sum(1 for s, e in intervals if s <= start < e)
        best = max(best, active)
    return best


assert min_rooms_pairwise([[0, 30], [5, 10], [15, 20]]) == 2
assert min_rooms_pairwise([[7, 10], [2, 4]]) == 1
assert min_rooms_pairwise([]) == 0
```

This is correct, and it is `O(n²)`, because each of the `n` starts rescans all
`n` meetings. At the `10^4` and `10^5` input sizes these problems are given, that
is `10^8` to `10^10` comparisons and a timeout.

The waste is specific, and naming it hands you the algorithm. Between one start
and the next start in time order, the true concurrency changes by a small,
knowable amount: it drops by one for every meeting that ended in between, and
rises by one for the new start. The pairwise version recomputes the entire count
from zero anyway, discarding a number it already had and that was almost right.

So stop recomputing and start carrying. Keep a running count, walk the boundaries
in time order, add one at every start and subtract one at every end. The peak of
that running count is the answer, and every boundary is visited once.

## Racing Sorted Starts Against Sorted Ends

To walk boundaries in time order you need the starts in order and the ends in
order, and here is the move that surprises people the first time: **sort them
independently, breaking the pairing between a meeting's start and its end**.

That looks like it destroys information, and for merging it would. For counting
it does not, because the running count never asks *which* meeting just ended. It
only asks whether some meeting ended, since any freed room is as good as any
other. A meeting is nothing but a `+1` at one time and a `-1` at another, and the
two halves can travel separately.

```python
def min_meeting_rooms(intervals: list[list[int]]) -> int:
    starts = sorted(start for start, _ in intervals)
    ends = sorted(end for _, end in intervals)
    rooms = best = 0
    freed = 0
    for start in starts:
        while freed < len(ends) and ends[freed] <= start:
            freed += 1
            rooms -= 1
        rooms += 1
        best = max(best, rooms)
    return best


assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
assert min_meeting_rooms([[1, 5], [5, 9]]) == 1
assert min_meeting_rooms([[0, 30], [5, 10], [15, 20], [12, 25], [30, 40]]) == 3
assert min_meeting_rooms([]) == 0
```

**The four lines that carry the idea**:

- The outer `for` walks starts, because a new room is only ever needed at a start,
  so those are the only moments worth measuring the peak at
- The inner `while` drains every end that has already passed *before* the new
  meeting is seated, which is what lets a room be reused instead of bought. Drain
  after seating and you would count a room that was about to be freed, giving an
  answer one too large on inputs like `[[1, 5], [5, 9]]`
- `ends[freed] <= start` is the half-open convention again. Change it to `<` and a
  meeting ending exactly when another begins forces a second room
- `freed < len(ends)` guards the index, since a zero-length interval such as
  `[5, 5]` would otherwise let the drain run past the end of the array

`best = max(best, rooms)` sits inside the loop rather than being read off at the
end, because `rooms` finishes at whatever is still running after the last start,
which is usually 1 and never the peak.

**The same function with one comparison changed** solves *Divide Intervals Into
Minimum Number of Groups*, where you must split intervals into groups with no
overlap inside a group. The minimum number of groups is the maximum concurrency,
because intervals that all contain one common moment must go to distinct groups,
so you need at least the peak, and the counting scan shows the peak is always
enough. The one difference is that its intervals are **inclusive** at both ends,
so `[1, 5]` and `[5, 10]` do collide on day 5:

```python
def min_groups(intervals: list[list[int]]) -> int:
    starts = sorted(start for start, _ in intervals)
    ends = sorted(end for _, end in intervals)
    active = best = 0
    freed = 0
    for start in starts:
        while freed < len(ends) and ends[freed] < start:
            freed += 1
            active -= 1
        active += 1
        best = max(best, active)
    return best


assert min_groups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]) == 3
assert min_groups([[1, 3], [5, 6], [8, 10], [11, 13]]) == 1
assert min_groups([[1, 1]]) == 1
```

`ends[freed] < start` instead of `<=` is the entire difference between the two
problems, which is why the endpoint question is worth asking before you write a
line.

## Dry Run: Five Meetings, Three Rooms

The meetings from the figure at the top, `[0, 30)`, `[5, 10)`, `[15, 20)`,
`[12, 25)`, and `[30, 40)`. Their starts and ends sorted independently:

```text
starts  [ 0,  5, 12, 15, 30]
ends    [10, 20, 25, 30, 40]
```

```text
start= 0   no end <= 0            rooms=1  best=1   freed points at 10
start= 5   no end <= 5            rooms=2  best=2   freed points at 10
start=12   end 10 <= 12, reuse    rooms=1
           no further end <= 12   rooms=2  best=2   freed points at 20
start=15   no end <= 15           rooms=3  best=3   freed points at 20
start=30   end 20 <= 30, reuse    rooms=2
           end 25 <= 30, reuse    rooms=1
           end 30 <= 30, reuse    rooms=0
           no further end <= 30   rooms=1  best=3   freed points at 40
```

The step at `start=12` is the one to study, because it is where the algorithm
**declines** to buy a room. Two meetings were running, a third is starting, and
the naive instinct is `rooms = 3`. The drain fires first, sees that the end at
time 10 has already passed, and hands that room back, so the new meeting moves
into it and the count goes 2, then 1, then back to 2. Delete the inner `while`
and this input returns 5 instead of 3.

The end value 30 draining at `start=30` is the second thing to look at. That is
meeting A finishing at exactly the moment meeting E begins, and `<=` lets E take
A's room. Under inclusive endpoints it would not, which is the `min_groups`
difference above.

Notice also that `rooms` ends the run at 1, not 3. The peak happened three steps
earlier and is only preserved because `best` was updated inside the loop.

## The Same Count From A Heap Of End Times

There is a second way to write this that most people find easier to recall under
pressure, and it keeps the meetings intact rather than splitting them into loose
boundaries. Walk the meetings in start order and keep a
[min-heap](../../08_heaps/notes/01_heap_basics.md) holding the end time of every
meeting currently occupying a room. The heap's root is the soonest a room will
come free, which is the only end time worth comparing against.

```python
import heapq


def min_meeting_rooms_heap(intervals: list[list[int]]) -> int:
    in_use: list[int] = []
    for start, end in sorted(intervals):
        if in_use and in_use[0] <= start:
            heapq.heappop(in_use)
        heapq.heappush(in_use, end)
    return len(in_use)


assert min_meeting_rooms_heap([[0, 30], [5, 10], [15, 20]]) == 2
assert min_meeting_rooms_heap([[7, 10], [2, 4]]) == 1
assert min_meeting_rooms_heap([[0, 30], [5, 10], [15, 20], [12, 25], [30, 40]]) == 3
assert min_meeting_rooms_heap([]) == 0
```

The heap's **size** is the number of occupied rooms, so no separate counter is
needed and `len(in_use)` at the end is the peak. That works because the heap never
shrinks below its high-water mark: a pop is always immediately followed by a push,
so the only way the size grows is a start that found no free room, and it never
falls.

One `if` rather than a `while` is enough, and this is the line people question.
Each iteration adds exactly one meeting, so it can consume at most one freed room,
and freeing several rooms at once would not change the size. A `while` here is not
wrong, it is just wasted work.

**Which of the two to write** depends on what the problem wants back:

- The two-pointer scan is slightly faster and uses no heap, so it is the better
  answer when the question is purely "how many"
- The heap holds identity, so it is the only one that extends when the question
  becomes "which room" or "which meeting is still running", which is the next
  section

## When The Answer Names A Room

*Meeting Rooms III* asks which of `n` numbered rooms hosts the most meetings, with
a delay rule: a meeting whose start finds every room busy waits for the earliest
one to free, keeps its original duration, and starts late. Ties go to the
lowest-numbered room.

Counting concurrency is no longer enough, because the answer is a room number.
Two heaps carry it, which is the [facing-heaps](../../08_heaps/notes/03_two_heaps.md)
idea specialised to this shape:

- `free`, a min-heap of **room numbers**, whose root is the lowest-numbered
  available room, which is exactly what the tie-break rule asks for
- `busy`, a min-heap of `(end_time, room_number)`, whose root is the room that
  frees soonest, with the room number second so ties among rooms freeing at the
  same instant still resolve to the lowest number

```python
import heapq


def most_booked_room(n: int, meetings: list[list[int]]) -> int:
    free = list(range(n))
    heapq.heapify(free)
    busy: list[tuple[int, int]] = []
    count = [0] * n
    for start, end in sorted(meetings):
        while busy and busy[0][0] <= start:
            _, room = heapq.heappop(busy)
            heapq.heappush(free, room)
        if free:
            room = heapq.heappop(free)
            heapq.heappush(busy, (end, room))
        else:
            free_at, room = heapq.heappop(busy)
            heapq.heappush(busy, (free_at + (end - start), room))
        count[room] += 1
    return count.index(max(count))


assert most_booked_room(2, [[0, 10], [1, 5], [2, 7], [3, 4]]) == 0
assert most_booked_room(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) == 1
assert most_booked_room(1, [[0, 10]]) == 0
```

Here the drain really is a `while`, unlike the counting version, because every
room that has freed must be back in `free` before the tie-break picks the lowest
number. Return one room too few and a meeting takes room 3 when room 1 was
available.

The `else` branch is where the delay rule lives. No room is free, so the meeting
takes the one that frees first and runs for `end - start` from that moment, which
is why the new end is `free_at + (end - start)` and not `end`. Writing `end` there
silently shortens delayed meetings and is the bug this problem is built around.

`count.index(max(count))` returns the first index holding the maximum, which is
the lowest-numbered room among ties, matching the tie rule one more time.

## Accepting Or Rejecting A Booking

The *My Calendar* problems flip the direction. Instead of being handed all the
intervals at once, they arrive one at a time and each one must be answered
immediately, which means every booking is checked against the accumulated state
rather than against a sorted array you get to build first.

**My Calendar I** accepts a booking only if it overlaps nothing already accepted.
Because accepted bookings never overlap each other, they stay sorted and disjoint,
so [binary search](../../05_binary_search/notes/02_boundary_search.md) finds the
only two neighbours that could possibly collide.

```python
from bisect import bisect_left


class MyCalendar:
    def __init__(self) -> None:
        self.bookings: list[tuple[int, int]] = []

    def book(self, start: int, end: int) -> bool:
        i = bisect_left(self.bookings, (start, end))
        if i > 0 and self.bookings[i - 1][1] > start:
            return False
        if i < len(self.bookings) and self.bookings[i][0] < end:
            return False
        self.bookings.insert(i, (start, end))
        return True


calendar = MyCalendar()
assert [calendar.book(10, 20), calendar.book(15, 25), calendar.book(20, 30)] == [
    True,
    False,
    True,
]
assert MyCalendar().book(0, 1) is True
```

Only two neighbours need checking, because the list is sorted and disjoint: any
booking further left ends before the predecessor does, and any booking further
right starts after the successor does. The two `if` guards are the two halves of
the standard overlap test, split apart because each side is checked against a
different neighbour. The empty-calendar case needs no special handling, since
`i` is `0` and `len(self.bookings)` is `0`, so both guards are skipped.

**My Calendar II** allows double booking and rejects only a triple. The trick is
to keep a second list of the regions that are **already double booked**, computed
as the intersections produced by each accepted booking:

```python
class MyCalendarTwo:
    def __init__(self) -> None:
        self.single: list[tuple[int, int]] = []
        self.double: list[tuple[int, int]] = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.double:
            if start < e and s < end:
                return False
        for s, e in self.single:
            if start < e and s < end:
                self.double.append((max(start, s), min(end, e)))
        self.single.append((start, end))
        return True


calendar = MyCalendarTwo()
assert [
    calendar.book(10, 20),
    calendar.book(50, 60),
    calendar.book(10, 40),
    calendar.book(5, 15),
    calendar.book(5, 10),
    calendar.book(25, 55),
] == [True, True, True, False, True, True]
assert MyCalendarTwo().book(0, 1) is True
```

The two loops must run in this order and the rejection must complete before any
mutation, because a booking that gets rejected has to leave `single` and `double`
exactly as it found them. Overlapping a doubled region means three bookings would
cover that region, so it is refused; overlapping a single region only creates a
new doubled region, which is `(max(start, s), min(end, e))`, the intersection.

**My Calendar III** drops the rejection entirely and asks for the largest `k` such
that some moment is covered by `k` bookings, which is the maximum concurrency
again, now reported after every insertion. Store the boundaries as `+1` and `-1`
counts keyed by time, then walk the keys in order and carry the running total:

```python
from collections import defaultdict


class MyCalendarThree:
    def __init__(self) -> None:
        self.delta: defaultdict[int, int] = defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.delta[start] += 1
        self.delta[end] -= 1
        active = best = 0
        for time in sorted(self.delta):
            active += self.delta[time]
            best = max(best, active)
        return best


calendar = MyCalendarThree()
assert [
    calendar.book(10, 20),
    calendar.book(50, 60),
    calendar.book(10, 40),
    calendar.book(5, 15),
    calendar.book(5, 10),
    calendar.book(25, 55),
] == [1, 1, 2, 3, 3, 3]
assert MyCalendarThree().book(0, 1) == 1
```

`defaultdict(int)` matters because two bookings can share a boundary, and
`self.delta[10] += 1` twice must accumulate to `2` rather than overwrite. Ends are
subtracted at the end coordinate itself, so a booking ending at 10 and one
starting at 10 cancel at that key and never register as concurrent, which is the
half-open convention expressed as arithmetic. This delta encoding generalises well
past calendars, and the [sweep line](04_sweep_line.md) topic takes it further.

## Answering Questions About One Moment In Time

The last shape hands you a pile of intervals and a pile of separate query points,
and asks something about the intervals covering each point.

*Number of Flowers in Full Bloom* wants the count. The concurrency at a time `t`
is the number of intervals that have started minus the number that have finished,
and both of those are counts in a sorted array, so two binary searches answer each
query with no scan at all:

```python
from bisect import bisect_left, bisect_right


def full_bloom_flowers(flowers: list[list[int]], people: list[int]) -> list[int]:
    starts = sorted(start for start, _ in flowers)
    ends = sorted(end for _, end in flowers)
    return [bisect_right(starts, when) - bisect_left(ends, when) for when in people]


assert full_bloom_flowers([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]) == [1, 2, 2, 2]
assert full_bloom_flowers([[1, 10], [3, 3]], [3, 3, 2]) == [2, 2, 1]
assert full_bloom_flowers([[1, 2]], []) == []
```

This is the independent sort from the two-pointer version reused, and the choice
of `bisect_right` against `bisect_left` is the whole correctness argument.
Flowers here bloom on **inclusive** ranges, so a flower starting exactly at `when`
counts as open, which needs `bisect_right` to place the query past its equals, and
a flower ending exactly at `when` is still blooming and must not be subtracted,
which needs `bisect_left` to stop before its equals. Swap the two and every query
landing on a boundary is off by one.

*Minimum Interval to Include Each Query* wants the shortest covering interval
instead of the count, and the queries arrive unsorted. Sorting the queries and
answering them in time order turns them into a single left-to-right sweep, as long
as you remember which slot each answer belongs in:

```python
import heapq


def min_interval(intervals: list[list[int]], queries: list[int]) -> list[int]:
    ordered = sorted(intervals)
    answer = [-1] * len(queries)
    covering: list[tuple[int, int]] = []
    i = 0
    for position in sorted(range(len(queries)), key=lambda k: queries[k]):
        query = queries[position]
        while i < len(ordered) and ordered[i][0] <= query:
            left, right = ordered[i]
            heapq.heappush(covering, (right - left + 1, right))
            i += 1
        while covering and covering[0][1] < query:
            heapq.heappop(covering)
        if covering:
            answer[position] = covering[0][0]
    return answer


assert min_interval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]) == [3, 3, 1, 4]
assert min_interval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]) == [2, -1, 4, 6]
assert min_interval([], [1, 2]) == [-1, -1]
```

`sorted(range(len(queries)), key=...)` sorts the query **indices** rather than the
values, so `answer[position]` writes into the caller's original ordering. Sorting
the values directly loses that mapping and is the standard way to fail this
problem.

The heap is keyed by `(length, right)` with length first, because the root must be
the shortest interval, and `right` rides along only so the eviction loop can test
it. That eviction loop is the interesting half: intervals enter the heap when their
start is reached and are only removed when their end has been passed, and since
queries are processed in increasing order an interval discarded as too-far-left can
never be needed again. Anything popped is gone for good, so each interval is pushed
once and popped at most once.

## Worked Example: [Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/)

You are given events, each available over a range of days, and you may attend at
most one event per day and each event at most once. Attending an event takes any
single day within its range. Return the largest number of distinct events you can
attend.

**Input**: `events`, a `list[list[int]]` where `events[i]` is `[start_i, end_i]`,
two day numbers with `start_i <= end_i`, meaning event `i` can be attended on any
one day `d` with `start_i <= d <= end_i`. Both endpoints are **inclusive**, days
are positive integers, and the list may contain duplicate events.

**Output**: an `int`, the maximum number of events attendable under the rule of at
most one event per day. It is a count of events, not of days, and it is at most
`len(events)`

**The approach.** "At most one per day, and each event has a window" is a
[greedy scheduling](../../12_greedy_algorithms/notes/03_interval_greedy.md)
question, but not the usual sort-by-end one. Sorting by end and attending each
event on its start day fails immediately: on `[[1, 2], [1, 2]]` both events want
day 1, the second finds it taken and is lost, giving 1 when the true answer is 2,
since the second could have been attended on day 2. An event is not pinned to any
one day, so the decision is not "which day does this event take" but "which event
does this day take".

Turning it around gives the right question, and the right question has an obvious
answer. Walk forward day by day. On each day, among the events currently available,
attend the one whose deadline is **soonest**, because every other available event
survives to at least that day and can still be attended later, while the
soonest-ending one may not. That is an
[exchange argument](../../12_greedy_algorithms/notes/01_greedy_fundamentals.md):
any schedule that picks a later-ending event today can swap it for the
soonest-ending one without attending fewer events.

> "I will sweep days in increasing order and keep a min-heap of the end days of
> every event that has already opened and is not yet attended. Each day I attend
> the event at the root, because it is the one with the least remaining slack, and
> I drop anything whose end day is now in the past."

**Step by step**:

1. Sort the events by start day, so they can be released into the heap in the
   order the sweep reaches them, using one moving index rather than a rescan
2. Keep a min-heap holding only the **end days** of open, unattended events. The
   start day has done its job the moment the event is released, so it does not need
   to be stored, and the end day is the only thing the greedy choice compares
3. When the heap is empty there is nothing to do until the next event opens, so
   jump the current day straight to the next start rather than stepping through
   empty days one at a time, which is what keeps the loop bounded by the number of
   events instead of by the length of the calendar
4. Release every event whose start day has arrived by pushing its end day, using a
   `while` because many events can open on the same day
5. Attend the root of the heap, which is the soonest-ending open event, and count
   it. The heap is never empty at this point, because either it already held
   something or step 3 and step 4 just filled it
6. Move to the next day, then discard from the root every event whose end day is
   now in the past, since it can never be attended again. Doing this after the
   advance rather than before is what makes the check a simple `end < day`
7. Stop when both the event list is exhausted and the heap is empty, because no
   event remains either unopened or open

```python
import heapq


def max_events(events: list[list[int]]) -> int:
    ordered = sorted(events)
    ending: list[int] = []
    i = attended = 0
    day = 0
    while i < len(ordered) or ending:
        if not ending:
            day = ordered[i][0]
        while i < len(ordered) and ordered[i][0] <= day:
            heapq.heappush(ending, ordered[i][1])
            i += 1
        heapq.heappop(ending)
        attended += 1
        day += 1
        while ending and ending[0] < day:
            heapq.heappop(ending)
    return attended


assert max_events([[1, 2], [2, 3], [3, 4]]) == 3
assert max_events([[1, 2], [2, 3], [3, 4], [1, 2]]) == 4
assert max_events([[1, 5], [1, 5], [1, 5], [2, 3], [2, 3]]) == 5
assert max_events([]) == 0
```

A trace on `[[1, 2], [1, 2], [1, 2], [2, 3]]`, where three events crowd into days
1 and 2 and one of them cannot be saved:

```text
heap empty, jump day -> 1
day 1   push end 2                    heap=[2]
day 1   push end 2                    heap=[2, 2]
day 1   push end 2                    heap=[2, 2, 2]
day 1   ATTEND end 2   attended=1     heap=[2, 2]
day 2   push end 3                    heap=[2, 2, 3]
day 2   ATTEND end 2   attended=2     heap=[2, 3]
day 3   DISCARD end 2                 heap=[3]
day 3   ATTEND end 3   attended=3     heap=[]
```

The discard on day 3 is the step that matters. A third event ending on day 2 is
still sitting in the heap when the sweep reaches day 3, and it is thrown away
unattended rather than counted, because its window has closed. Without that loop
it would be attended on day 3, outside its own range, and the function would
return 4. Notice also that on day 2 the heap held `[2, 3]` and the algorithm took
the `2`, deliberately passing over the event ending on day 3 that was already
available, which is the greedy choice earning its keep one line at a time.

- **Time Complexity**: `O(n log n)`, where `n` is the number of events, because
  sorting costs `O(n log n)` and every event is pushed once and popped once from a
  heap of at most `n` entries, at `O(log n)` each
- **Space Complexity**: `O(n)`, because the sorted copy and the heap each hold at
  most one entry per event, and in the worst case every event is open at once

## Time and Space Complexity

`n` is the number of intervals throughout. Sorting dominates almost everything
here, so the interesting comparisons are between the `O(n log n)` methods and the
`O(n²)` ones they replace.

**Maximum concurrency, as in Meeting Rooms II and Divide Intervals Into Groups**

| Approach                             | Time                                                                                                                              | Space                                                                                                    |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Independently sorted starts and ends | `O(n log n)`: two sorts of `n` values, then one pass in which each start and each end is consumed exactly once                    | `O(n)`: the two boundary arrays, since the running count and the freed index are single integers         |
| Min-heap of end times                | `O(n log n)`: sorting by start, then at most `n` pushes and `n` pops at `O(log n)` each                                           | `O(n)`: the heap holds one end time per occupied room, and every meeting is concurrent in the worst case |
| Counting overlaps at each start      | `O(n²)`: each of the `n` starts rescans all `n` intervals, recomputing a count that changes by one between consecutive boundaries | `O(1)`: only the running best is stored, which is why this version looks harmless until it times out     |

**Meeting Rooms III, with `n` meetings and `r` rooms**

| Operation | Time                                                                                                                                                               | Space                                                                                                           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| Whole run | `O(n log n + n log r)`: sorting the meetings, plus each meeting doing a constant number of pushes and pops across two heaps that together hold at most `r` entries | `O(n + r)`: the sorted meeting list plus the two heaps and the per-room counter array, all bounded by `r` rooms |

**My Calendar family, over `q` calls**

| Design                             | Time                                                                                                                                                                                                                         | Space                                                                                                                                                          |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MyCalendar` with `bisect`         | `O(log q)` search and `O(q)` insertion per call, so `O(q²)` overall: the binary search is cheap but `list.insert` shifts the tail, which is the [dynamic array](../../01_arrays_and_hashing/notes/01_dynamic_arrays.md) cost | `O(q)`: one tuple per accepted booking, and rejected bookings store nothing                                                                                    |
| `MyCalendarTwo` with two lists     | `O(q)` per call and `O(q²)` overall: each call scans both lists linearly, and the doubled list can hold one entry per overlapping pair                                                                                       | `O(q)`: the accepted bookings plus their pairwise intersections, which stays linear in practice because a triple booking is rejected before it can be recorded |
| `MyCalendarThree` with a delta map | `O(q log q)` per call and `O(q² log q)` overall: the map has up to `2q` keys and is re-sorted on every call                                                                                                                  | `O(q)`: two delta keys per booking, and repeated boundaries collapse onto the same key                                                                         |

Re-sorting the whole delta map on every call is what makes `MyCalendarThree`
quadratic, and it is accepted only because the call limit is small. The follow-up
to volunteer is a balanced sorted map or a segment tree keyed by time, which turns
each call into `O(log q)`.

**Point queries, with `n` intervals and `m` query points**

| Problem                                | Time                                                                                                                                                                                         | Space                                                                                     |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Number of Flowers in Full Bloom        | `O(n log n + m log n)`: two sorts of the `n` boundaries, then two binary searches per query over arrays of length `n`                                                                        | `O(n)`: the sorted starts and sorted ends, not counting the `m`-length output             |
| Minimum Interval to Include Each Query | `O(n log n + m log m + (n + m) log n)`: sorting intervals and query indices, then each interval pushed and popped at most once from a heap of size at most `n`, with one root read per query | `O(n + m)`: the heap holds at most `n` intervals and the query ordering holds `m` indices |

## Summary

- The **concurrency** at a moment is the number of intervals covering it, and the
  **maximum concurrency** over all moments is the answer to the whole meeting-room
  family. Rooms needed, groups needed, and the largest `k`-booking are all the same
  number wearing different words
  - This is the opposite of merging, which deliberately forgets how deep a pile
    was. Five stacked meetings and five chained meetings merge identically and need
    five rooms and one room respectively
- The count only changes at a boundary, so walk the boundaries in time order and
  carry a running total, adding one at every start and subtracting one at every
  end. Recomputing the count from scratch at each start is `O(n²)` and discards a
  number that was already almost right
- Sorting starts and ends into two **separate** arrays looks like it destroys the
  pairing, and for merging it would, but the running count never asks which meeting
  ended, only that one did, so any freed room is interchangeable with any other
  - Drain the expired ends *before* seating the new meeting, or a room that was
    about to free gets counted as occupied and the answer comes out one too high
  - `best` must be updated inside the loop, because the running count finishes at
    whatever is still active after the final start rather than at the peak
- The min-heap of end times is the same algorithm with the meetings kept intact.
  Its size is the number of occupied rooms, so `len(heap)` is the answer, and one
  `if` suffices instead of a `while` because a single new meeting can reuse at most
  one freed room
  - Choose the heap whenever the answer names something, since the two-pointer
    scan has thrown the identities away. *Meeting Rooms III* needs a min-heap of
    free room numbers beside a min-heap of `(end_time, room)`, and a delayed meeting
    keeps its duration, so its new end is `free_at + (end - start)`
- Whether back-to-back intervals collide is a decision the problem makes, not you,
  and it is exactly one comparison. Half-open intervals such as meetings use
  `end <= start` to free a room; inclusive intervals such as the groups and flower
  problems use `end < start`, and getting it backwards is off by one on every
  boundary case
  - Ask about it out loud before writing code, and say which single line changes if
    the answer is the other way
- Bookings that arrive one at a time are checked against accumulated state rather
  than a pre-sorted array. *My Calendar I* keeps a sorted disjoint list and only has
  to test the two `bisect` neighbours, *My Calendar II* keeps a second list of
  already-doubled regions and rejects anything overlapping it, and *My Calendar III*
  keeps `+1`/`-1` deltas keyed by time and re-reads the peak
  - A rejected booking must leave every structure untouched, so run all the
    rejection checks before any mutation
- Queries about a single moment sort the queries and sweep them in time order.
  Counting the covering intervals is two binary searches against sorted starts and
  sorted ends, and finding the shortest covering interval is a heap keyed by
  `(length, right)` that admits intervals as their start is passed and evicts them
  once their end falls behind the query
  - Sort the query **indices**, not the query values, or the answers cannot be
    written back into the caller's ordering

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
Is the question "does anything collide" (boolean), "how many at once" (peak), or
  "which one" (identity)?
Are endpoints half-open or inclusive, and therefore is my comparison <= or <?
Am I counting maximum overlap, or merging into a union? Those are different answers.
Am I draining expired ends before seating the new interval, not after?
Is the peak recorded inside the loop rather than read off the final count?
If I sort starts and ends separately, can I justify out loud why breaking the
  pairing is safe here?
Does the answer need a name (room number, interval, event), which rules out the
  two-pointer scan and forces a heap?
For a delayed booking, does the new end preserve the original duration?
For an arriving-booking design, do all rejection checks run before any mutation?
For point queries, did I sort query indices so answers land in the caller's order?
Can I state why each interval enters and leaves the heap at most once?
```
