# Intervals Problem Set

## Goal

Build interval intuition from the ground up, then use that foundation to solve the
medium and hard scheduling and overlap problems that show up in LeetCode-style
interviews.

## How To Use

Work the file in order. The early sections are the fundamentals. The later sections
are the medium and hard extensions.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Fundamentals

These are the interval basics you should be able to do without thinking too hard.

### 1. [Summary Ranges](https://leetcode.com/problems/summary-ranges/)

- Pattern: group consecutive numbers into ranges.

### 2. [Minimum Number Of Arrows To Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

- Pattern: sort by end, count non-overlapping groups.

### 3. [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)

- Pattern: two pointers walking two sorted interval lists.

### 4. [Determine if Two Events Have Conflict](https://leetcode.com/problems/determine-if-two-events-have-conflict/)

- Pattern: two intervals overlap iff each start is not after the other's end.

### 5. [Partition Labels](https://leetcode.com/problems/partition-labels/)

- Pattern: build last-index intervals per char, then merge greedily while scanning.

### 6. [Maximum Population Year](https://leetcode.com/problems/maximum-population-year/)

- Pattern: delta array, +1 at birth and -1 at death, prefix sum for the peak.

### 7. [Points That Intersect With Cars](https://leetcode.com/problems/points-that-intersect-with-cars/)

- Pattern: difference array over the coordinate range, count covered points.

## Merge And Insert

These build and maintain a clean, non-overlapping set of intervals.

### 8. [Merge Intervals](https://leetcode.com/problems/merge-intervals/)

- Pattern: sort by start, extend or start a new merged interval.

### 9. [Insert Interval](https://leetcode.com/problems/insert-interval/)

- Pattern: split into before, overlapping, and after the new interval.

### 10. [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

- Pattern: sort by end, greedily keep the interval that ends earliest.

### 11. [Data Stream As Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)

- Pattern: maintain a running merged interval set as values stream in.

### 12. [Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/)

- Pattern: sort by start asc and end desc, drop intervals covered by the last kept end.

## Meeting Rooms And Scheduling

These track how many intervals are active at once or gate new bookings against
existing ones.

### 13. [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)

- Pattern: sort by start, check adjacent pairs for overlap.

### 14. [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

- Pattern: sorted starts/ends two pointers or a min heap of end times.

### 15. [Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/)

- Pattern: two heaps tracking free rooms and occupied rooms with end times.

### 16. [My Calendar I](https://leetcode.com/problems/my-calendar-i/)

- Pattern: reject a booking that overlaps any existing booking.

### 17. [My Calendar II](https://leetcode.com/problems/my-calendar-ii/)

- Pattern: track single bookings and double-booked overlaps, reject triple.

### 18. [My Calendar III](https://leetcode.com/problems/my-calendar-iii/)

- Pattern: sweep-line delta counting to track maximum k-booking.

### 19. [Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/)

- Pattern: sweep days, min heap of end days, greedily attend the soonest-ending event.

### 20. [Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/)

- Pattern: max concurrent overlap equals the group count, sweep starts and ends.

## Sweep Line

These convert interval starts and ends into events and scan in sorted order.

### 21. [Employee Free Time](https://leetcode.com/problems/employee-free-time/)

- Pattern: flatten and merge all schedules, then read the gaps.

### 22. [Range Module](https://leetcode.com/problems/range-module/)

- Pattern: maintain a sorted disjoint interval set with add/remove/query.

### 23. [Car Pooling](https://leetcode.com/problems/car-pooling/)

- Pattern: delta array of passenger changes at pickup and dropoff points.

### 24. [Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/)

- Pattern: difference array of seat deltas, prefix sum for per-flight totals.

### 25. [Describe the Painting](https://leetcode.com/problems/describe-the-painting/)

- Pattern: color-sum deltas at segment endpoints, sweep and emit non-zero runs.

## Hards And Extensions

These stack sweep line with heaps, sorted structures, or BIT/segment trees.

### 26. [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

- Pattern: sweep x events with a max heap of active heights, emit height changes.

### 27. [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/)

- Pattern: sort queries and intervals, min heap of sizes for intervals covering each query.

### 28. [Number of Flowers in Full Bloom](https://leetcode.com/problems/number-of-flowers-in-full-bloom/)

- Pattern: binary search sorted starts and ends per person, or sweep with events.

### 29. [Maximum Number of Events That Can Be Attended II](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/)

- Pattern: sort by end, DP with binary search over the next non-conflicting event.

### 30. [Set Intersection Size At Least Two](https://leetcode.com/problems/set-intersection-size-at-least-two/)

- Pattern: sort by end, greedily add the two largest points each interval needs.

### 31. [Falling Squares](https://leetcode.com/problems/falling-squares/)

- Pattern: coordinate-compressed segment tree of range max heights.

### 32. [Amount of New Area Painted Each Day](https://leetcode.com/problems/amount-of-new-area-painted-each-day/)

- Pattern: track painted coordinates with a sorted set or union-find skip pointers.

## Recommended Order

If you want the shortest path to interval fluency, do them in this order:

```text
1. [Summary Ranges](https://leetcode.com/problems/summary-ranges/)
2. [Merge Intervals](https://leetcode.com/problems/merge-intervals/)
3. [Insert Interval](https://leetcode.com/problems/insert-interval/)
4. [Partition Labels](https://leetcode.com/problems/partition-labels/)
5. [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
6. [Minimum Number Of Arrows To Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)
7. [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)
8. [Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/)
9. [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
10. [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
11. [My Calendar I](https://leetcode.com/problems/my-calendar-i/)
12. [My Calendar II](https://leetcode.com/problems/my-calendar-ii/)
13. [Car Pooling](https://leetcode.com/problems/car-pooling/)
14. [Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/)
15. [My Calendar III](https://leetcode.com/problems/my-calendar-iii/)
16. [Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/)
17. [Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/)
18. [Data Stream As Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)
19. [Employee Free Time](https://leetcode.com/problems/employee-free-time/)
20. [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/)
```
