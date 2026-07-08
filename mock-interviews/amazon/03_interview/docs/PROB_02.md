# The Critical Delivery Route

**Difficulty:** Medium

Closest LeetCode: [543 - Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

## Description

Amazon's regional sortation network is laid out as a binary tree of scan
stations, given to you as the `root` station. Each station forwards packages to
at most two downstream stations, and each direct link between two stations is a
single conveyor segment.

Operations wants to know the network's worst-case internal span: the length of
the **longest route between any two stations**, measured as the number of
conveyor segments on that route. This route does not have to pass through the
`root` station.

Write a function `critical_delivery_route()` that returns that length (the
number of segments, i.e. edges, on the longest path between any two stations).

Evaluate the time and space complexity of your solution. Define your variables
and provide a rationale for why you believe your solution has the stated time
and space complexity.

## Function Signature

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def critical_delivery_route(root):
    pass
```

## Examples

### Example 1

```
Input:
            1
           / \
          2   3
         / \
        4   5

Output: 3
Explanation: The longest route runs 4 -> 2 -> 1 -> 3 (or 5 -> 2 -> 1 -> 3),
             which is 3 conveyor segments.
```

### Example 2

```
Input:
            1
           /
          2

Output: 1
Explanation: The only route, 1 -> 2, is 1 conveyor segment.
```

### Example 3

```
Input:  A single station with no downstream links.

Output: 0
```
