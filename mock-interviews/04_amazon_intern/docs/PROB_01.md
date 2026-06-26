# Container With Most Water

Source: [LeetCode 11](https://leetcode.com/problems/container-with-most-water/description/)

You are given an integer array `height` of length `n`. There are `n` vertical
lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and
`(i, height[i])`.

Find two lines that, together with the x-axis, form a container that holds the
most water. Return the maximum amount of water the container can store.

You may not slant the container.

## Examples

### Example 1

```python
Input:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

Output:
49

Explanation:
The lines at index 1 (height 8) and index 8 (height 7) form the container.
The area is min(8, 7) * (8 - 1) = 7 * 7 = 49.
```

### Example 2

```python
Input:
height = [1, 1]

Output:
1
```

## Constraints

```text
n == len(height)
2 <= n <= 10^5
0 <= height[i] <= 10^4
```
