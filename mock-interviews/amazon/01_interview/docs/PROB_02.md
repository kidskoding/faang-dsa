# Walls And Gates

Source: [LeetCode 286](https://leetcode.com/problems/walls-and-gates/description/)

You are given an `m x n` grid `rooms` initialized with these three values:

- `-1` — a wall or an obstacle.
- `0` — a gate.
- `INF` (2147483647) — an empty room.

Fill each empty room with the distance to its *nearest* gate. If it is
impossible to reach a gate, leave the room as `INF`.

Distance is measured in the number of steps moving up, down, left, or right.
Modify the grid in place; return nothing.

## Examples

### Example 1

```python
Input:
INF = 2147483647
rooms = [
    [INF,  -1,   0, INF],
    [INF, INF, INF,  -1],
    [INF,  -1, INF,  -1],
    [  0,  -1, INF, INF],
]

Output:
[
    [3, -1, 0, 1],
    [2,  2, 1, -1],
    [1, -1, 2, -1],
    [0, -1, 3,  4],
]
```

### Example 2

```python
Input:
rooms = [[-1]]

Output:
[[-1]]
```

### Example 3

```python
Input:
rooms = [[0]]

Output:
[[0]]
```

## Constraints

```text
m == len(rooms)
n == len(rooms[0])
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 2147483647
```
