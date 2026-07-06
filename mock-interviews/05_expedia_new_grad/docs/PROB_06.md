# Cheapest Flights Within K Stops

Source: [LeetCode 787](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

There are `n` cities connected by some number of flights. You are given
`flights`, where `flights[i] = [from_i, to_i, price_i]` is a directed flight
from `from_i` to `to_i` costing `price_i`.

Given `src`, `dst`, and an integer `k`, return the cheapest price from `src` to
`dst` using **at most `k` stops**. If there is no such route, return `-1`.

## Examples

### Example 1

```python
Input:  n = 4
        flights = [[0,1,100], [1,2,100], [2,0,100], [1,3,600], [2,3,200]]
        src = 0, dst = 3, k = 1
Output: 700
Explanation: 0 -> 1 -> 3 costs 700 (2 stops route 0->1->2->3 is cheaper at 500
but uses 2 stops, exceeding k = 1).
```

### Example 2

```python
Input:  n = 3
        flights = [[0,1,100], [1,2,100], [0,2,500]]
        src = 0, dst = 2, k = 1
Output: 200
```

### Example 3

```python
Input:  n = 3
        flights = [[0,1,100], [1,2,100], [0,2,500]]
        src = 0, dst = 2, k = 0
Output: 500
```

## Constraints

```text
1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= from_i, to_i < n
from_i != to_i
1 <= price_i <= 10^4
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
```
