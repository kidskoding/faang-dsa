# Problem 2: ACH Settlement Capacity

Robinhood settles customer bank deposits through an ACH pipeline. Each
pending deposit has a dollar amount, and regulations require deposits to be
settled **in the exact order they were initiated** — the queue cannot be
reordered or split: a single deposit must settle entirely within one
business day.

The settlement pipeline has a fixed daily processing limit. Each day, the
pipeline takes deposits from the front of the queue, in order, until adding
the next deposit would push the day's total over the limit; the rest wait
for the next day.

Ops wants to provision the cheapest pipeline that still clears the backlog
on time. Given the queue of deposit amounts `deposits` and an integer
`days`, return the minimum daily processing limit that settles every
deposit within `days` business days.

## Examples

### Example 1

```python
Input:
deposits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
days = 5

Output: 1500
```

With a daily limit of 1500 the schedule is:

```text
Day 1: 100, 200, 300, 400, 500
Day 2: 600, 700
Day 3: 800
Day 4: 900
Day 5: 1000
```

A limit of 1400 would need a 6th day.

### Example 2

```python
Input:
deposits = [300, 200, 200, 400, 100, 400]
days = 3

Output: 600
```

```text
Day 1: 300, 200
Day 2: 200, 400
Day 3: 100, 400
```

### Example 3

```python
Input:
deposits = [50, 20, 50, 70, 60]
days = 5

Output: 70
```

One deposit per day; the limit only needs to cover the largest deposit.

## Constraints

```text
1 <= len(deposits) <= 5 * 10^4
1 <= deposits[i] <= 500
1 <= days <= len(deposits)
```

## Source

[LeetCode 1011](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
