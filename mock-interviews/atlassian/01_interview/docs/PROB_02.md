# Binary Tree Maximum Path Sum

Source: [LeetCode 124](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

A **path** in a binary tree is a sequence of nodes where each adjacent pair is
connected by an edge. A node appears at most once in the path, and the path
does **not** need to pass through the root.

The **path sum** is the sum of the node values on the path. Given the root of a
binary tree, return the maximum path sum of any non-empty path.

Node values may be negative, so the optimal path might exclude a subtree
entirely.

Each node is represented by a `TreeNode`:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Examples

### Example 1

```python
Input:
    1
   / \
  2   3
Output: 6        (2 -> 1 -> 3)
```

### Example 2

```python
Input:
      -10
      /  \
     9    20
         /  \
        15   7
Output: 42       (15 -> 20 -> 7)
```

### Example 3

```python
Input:  root = [-3]
Output: -3       (single node; path must be non-empty)
```

## Constraints

```text
The number of nodes is in the range [1, 3 * 10^4].
-1000 <= Node.val <= 1000
```

## The Trick

For each node, distinguish two quantities:

- What you **return upward** to the parent: the node's value plus the best of
  its two child branches (a path can only extend through the parent via one
  side). Clamp negative child contributions to 0.
- What you use to **update the global answer**: node value + both child
  branches (the path can "peak" at this node and turn back down).

These are different values. Getting them confused is the classic mistake.
