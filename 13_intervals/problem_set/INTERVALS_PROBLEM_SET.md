# Intervals Problem Set

## Goal

Build interval intuition across the four interval techniques — sorting and
scanning basics, merging into disjoint sets, room/booking counting, and
sweep-line difference arrays — then use each technique to solve the medium
and hard scheduling and overlap problems that show up in LeetCode-style
interviews.

## How To Use

Each section maps to one solution file in this folder and to one interval
technique. Work a section top to bottom: problems are ordered roughly easy
to hard, and the implemented ones come first. `solves:` names the function
or class in that section's file; `solves: (todo)` means the solution is not
written yet.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Interval Basics

`interval_basics_problems.py` — sort intervals or numbers, then scan once
to group runs, count non-overlapping groups, or walk two lists together.

### 1. [Summary Ranges](https://leetcode.com/problems/summary-ranges/)

- solves: `summary_ranges`
- Pattern: walk the sorted array, extend a run while numbers stay consecutive.

### 2. [Minimum Number Of Arrows To Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

- solves: `find_min_arrow_shots`
- Pattern: sort by end, shoot at the earliest end, skip balloons it pops.

### 3. [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)

- solves: `interval_intersection`
- Pattern: two pointers, take the overlap, advance the pointer that ends first.

### 4. [Determine if Two Events Have Conflict](https://leetcode.com/problems/determine-if-two-events-have-conflict/)

- solves: `have_conflict`
- Pattern: two intervals overlap iff each start is not after the other's end.

### 5. [Partition Labels](https://leetcode.com/problems/partition-labels/)

- solves: `partition_labels`
- Pattern: build last-index intervals per char, then merge greedily while scanning.

## Merge And Insert

`merge_insert_problems.py` — build and maintain a clean, non-overlapping
set of intervals as you merge, insert, or stream values in.

### 6. [Merge Intervals](https://leetcode.com/problems/merge-intervals/)

- solves: `merge`
- Pattern: sort by start, extend the current merged interval or start a new one.

### 7. [Insert Interval](https://leetcode.com/problems/insert-interval/)

- solves: `insert`
- Pattern: append intervals fully before, merge overlapping, append fully after.

### 8. [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

- solves: `erase_overlap_intervals`
- Pattern: sort by end, greedily keep the interval that finishes earliest.

### 9. [Data Stream As Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)

- solves: `SummaryRanges`
- Pattern: keep a sorted, merged interval set and re-merge around each insert.

### 10. [Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/)

- solves: `remove_covered_intervals`
- Pattern: sort by start asc and end desc, drop intervals covered by the last kept end.

## Meeting Rooms And Scheduling

`meeting_rooms_problems.py` — count how many intervals are active at once
or gate new bookings against the existing ones, using two pointers or heaps.

### 11. [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)

- solves: `can_attend_meetings`
- Pattern: sort by start, check every adjacent pair for overlap.

### 12. [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

- solves: `min_meeting_rooms`
- Pattern: sorted start/end two pointers or a min heap of end times.

### 13. [My Calendar I](https://leetcode.com/problems/my-calendar-i/)

- solves: `MyCalendar`
- Pattern: reject a booking that overlaps any existing booking.

### 14. [My Calendar II](https://leetcode.com/problems/my-calendar-ii/)

- solves: `MyCalendarTwo`
- Pattern: track single bookings and double-booked overlaps, reject a triple.

### 15. [My Calendar III](https://leetcode.com/problems/my-calendar-iii/)

- solves: `MyCalendarThree`
- Pattern: sweep-line delta counting to track the maximum k-booking.

### 16. [Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/)

- solves: `most_booked_room`
- Pattern: two heaps track free rooms and occupied rooms with end times.

### 17. [Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/)

- solves: `max_events`
- Pattern: sweep days, min heap of end days, greedily attend the soonest-ending event.

### 18. [Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/)

- solves: `min_groups`
- Pattern: max concurrent overlap equals the group count, sweep starts and ends.

### 19. [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/)

- solves: `min_interval`
- Pattern: sort queries and intervals, min heap of sizes for intervals covering each query.

### 20. [Number of Flowers in Full Bloom](https://leetcode.com/problems/number-of-flowers-in-full-bloom/)

- solves: `full_bloom_flowers`
- Pattern: binary search sorted starts and ends per person, or sweep with events.

## Sweep Line

`sweep_line_problems.py` — convert interval starts and ends into events or
difference-array deltas, then scan in sorted order to read gaps, coverage,
or peaks.

### 21. [Employee Free Time](https://leetcode.com/problems/employee-free-time/)

- solves: `employee_free_time`
- Pattern: flatten every employee's intervals, merge, then read the gaps.

### 22. [Range Module](https://leetcode.com/problems/range-module/)

- solves: `RangeModule`
- Pattern: maintain a sorted disjoint interval set with add/remove/query.

### 23. [Car Pooling](https://leetcode.com/problems/car-pooling/)

- solves: `car_pooling`
- Pattern: delta array of passenger changes at pickup and dropoff points.

### 24. [Maximum Population Year](https://leetcode.com/problems/maximum-population-year/)

- solves: `maximum_population`
- Pattern: delta array, +1 at birth and -1 at death, prefix sum for the peak.

### 25. [Points That Intersect With Cars](https://leetcode.com/problems/points-that-intersect-with-cars/)

- solves: `number_of_points`
- Pattern: difference array over the coordinate range, count covered points.

### 26. [Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/)

- solves: `corp_flight_bookings`
- Pattern: difference array of seat deltas, prefix sum for per-flight totals.

### 27. [Describe the Painting](https://leetcode.com/problems/describe-the-painting/)

- solves: `split_painting`
- Pattern: color-sum deltas at segment endpoints, sweep and emit non-zero runs.

### 28. [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

- solves: `get_skyline`
- Pattern: sweep x events with a max heap of active heights, emit height changes.

### 29. [Set Intersection Size At Least Two](https://leetcode.com/problems/set-intersection-size-at-least-two/)

- solves: `intersection_size_two`
- Pattern: sort by end, greedily add the two largest points each interval needs.

### 30. [Falling Squares](https://leetcode.com/problems/falling-squares/)

- solves: `falling_squares`
- Pattern: coordinate-compressed segment tree of range max heights.

### 31. [Amount of New Area Painted Each Day](https://leetcode.com/problems/amount-of-new-area-painted-each-day/)

- solves: `amount_painted`
- Pattern: track painted coordinates with a sorted set or union-find skip pointers.
  </content>
  </invoke>
