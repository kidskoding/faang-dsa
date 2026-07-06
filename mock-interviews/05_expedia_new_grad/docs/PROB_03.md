# Trapping Rain Water

Source: [LeetCode 42](https://leetcode.com/problems/trapping-rain-water/)

Given `n` non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it can trap after raining.

## Examples

### Example 1

```python
Input:  height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
```

### Example 2

```python
Input:  height = [4, 2, 0, 3, 2, 5]
Output: 9
```

## Constraints

```text
n == len(height)
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
```

## Follow-up

Can you do it in O(n) time using O(1) extra space?
