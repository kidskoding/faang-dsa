# Problem 1: Diagonal Traverse 

Source: [LeetCode 498](https://leetcode.com/problems/diagonal-traverse/description/)

Given an `m x n` matrix, return all of its elements in diagonal order.

Begin at the top-left element. Traverse each diagonal while alternating
directions:

- Move up and to the right for one diagonal.
- Move down and to the left for the next diagonal.
- Continue alternating until every matrix element has been visited.

## Examples

### Example 1

```python
Input:
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

Output:
[1, 2, 4, 7, 5, 3, 6, 8, 9]
```

### Example 2

```python
Input:
mat = [
    [1, 2],
    [3, 4],
]

Output:
[1, 2, 3, 4]
```

### Example 3

```python
Input:
mat = [[1, 2, 3, 4]]

Output:
[1, 2, 3, 4]
```

### Example 4

```python
Input:
mat = [
    [1],
    [2],
    [3],
    [4],
]

Output:
[1, 2, 3, 4]
```

## Constraints

```text
m == len(mat)
n == len(mat[0])
1 <= m, n <= 10^4
1 <= m * n <= 10^4
-10^5 <= mat[r][c] <= 10^5
```
