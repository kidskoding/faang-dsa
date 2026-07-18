# Problem 1: Options Desk Scheduling

Robinhood's derivatives desk hedges its options exposure by renting time on
an external execution venue. The venue offers a list of upcoming execution
windows. Each window has a start time, an end time, and the expected profit
(in dollars) from hedging during that window.

The desk operates a single execution pipeline, so it can only work one
window at a time: two booked windows may not overlap. Back-to-back is fine —
a window that ends at time `t` and another that starts at time `t` can both
be booked.

Given three arrays `start`, `end`, and `profit`, where window `i` runs from
`start[i]` to `end[i]` and yields `profit[i]`, return the maximum total
profit the desk can earn by booking a subset of non-overlapping windows.

## Examples

### Example 1

```python
Input:
start  = [1, 2, 3, 3]
end    = [3, 4, 5, 6]
profit = [50, 10, 40, 70]

Output: 120
```

Book window 0 (time 1–3, $50) and window 3 (time 3–6, $70).

### Example 2

```python
Input:
start  = [1, 2, 3, 4, 6]
end    = [3, 5, 10, 6, 9]
profit = [20, 20, 100, 70, 60]

Output: 150
```

Book window 0 (time 1–3, $20), window 3 (time 4–6, $70), and window 4
(time 6–9, $60) for $150. Taking the single $100 window instead caps the
desk at $120.

### Example 3

```python
Input:
start  = [1, 1, 1]
end    = [2, 3, 4]
profit = [5, 6, 4]

Output: 6
```

All three windows overlap; only one can be booked.

## Constraints

```text
1 <= len(start) == len(end) == len(profit) <= 5 * 10^4
1 <= start[i] < end[i] <= 10^9
1 <= profit[i] <= 10^4
```

## Source

[LeetCode 1235](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)
