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

## Merge And Insert

These build and maintain a clean, non-overlapping set of intervals.

### 4. [Merge Intervals](https://leetcode.com/problems/merge-intervals/)

- Pattern: sort by start, extend or start a new merged interval.

### 5. [Insert Interval](https://leetcode.com/problems/insert-interval/)

- Pattern: split into before, overlapping, and after the new interval.

### 6. [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

- Pattern: sort by end, greedily keep the interval that ends earliest.

### 7. [Data Stream As Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)

- Pattern: maintain a running merged interval set as values stream in.

## Meeting Rooms And Scheduling

These track how many intervals are active at once or gate new bookings against
existing ones.

### 8. [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)

- Pattern: sort by start, check adjacent pairs for overlap.

### 9. [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

- Pattern: sorted starts/ends two pointers or a min heap of end times.

### 10. [Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/)

- Pattern: two heaps tracking free rooms and occupied rooms with end times.

### 11. [My Calendar I](https://leetcode.com/problems/my-calendar-i/)

- Pattern: reject a booking that overlaps any existing booking.

### 12. [My Calendar II](https://leetcode.com/problems/my-calendar-ii/)

- Pattern: track single bookings and double-booked overlaps, reject triple.

### 13. [My Calendar III](https://leetcode.com/problems/my-calendar-iii/)

- Pattern: sweep-line delta counting to track maximum k-booking.

## Sweep Line

These convert interval starts and ends into events and scan in sorted order.

### 14. [Employee Free Time](https://leetcode.com/problems/employee-free-time/)

- Pattern: flatten and merge all schedules, then read the gaps.

### 15. [Range Module](https://leetcode.com/problems/range-module/)

- Pattern: maintain a sorted disjoint interval set with add/remove/query.

### 16. [Car Pooling](https://leetcode.com/problems/car-pooling/)

- Pattern: delta array of passenger changes at pickup and dropoff points.

## Recommended Order

If you want the shortest path to interval fluency, do them in this order:

```text
1. [Summary Ranges](https://leetcode.com/problems/summary-ranges/)
2. [Merge Intervals](https://leetcode.com/problems/merge-intervals/)
3. [Insert Interval](https://leetcode.com/problems/insert-interval/)
4. [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
5. [Minimum Number Of Arrows To Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)
6. [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)
7. [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
8. [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
9. [My Calendar I](https://leetcode.com/problems/my-calendar-i/)
10. [My Calendar II](https://leetcode.com/problems/my-calendar-ii/)
11. [Car Pooling](https://leetcode.com/problems/car-pooling/)
12. [My Calendar III](https://leetcode.com/problems/my-calendar-iii/)
13. [Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/)
14. [Data Stream As Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)
15. [Employee Free Time](https://leetcode.com/problems/employee-free-time/)
16. [Range Module](https://leetcode.com/problems/range-module/)
```
