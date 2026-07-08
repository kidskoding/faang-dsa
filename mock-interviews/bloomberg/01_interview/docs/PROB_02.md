# The Slowest Data Path

**Difficulty:** Medium

Closest LeetCode: [543 - Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

## Description

Bloomberg's market-data distribution fabric is laid out as a binary tree of
relay nodes, given to you as the `root` node. Each relay forwards a price feed
to at most two downstream relays, and every direct link between two relays adds
one hop of latency.

The infrastructure team wants to know the fabric's worst-case internal latency:
the length of the **longest path between any two relay nodes**, measured as the
number of hops (links) on that path. This path does not have to pass through the
`root` relay.

Return the length (the number of hops, i.e. edges, on the longest path between
any two relay nodes).

## Reference

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
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
Explanation: The longest path runs 4 -> 2 -> 1 -> 3 (or 5 -> 2 -> 1 -> 3),
             which is 3 hops.
```

### Example 2

```
Input:
            1
           /
          2

Output: 1
Explanation: The only path, 1 -> 2, is 1 hop.
```

### Example 3

```
Input:  A single relay with no downstream links.

Output: 0
```
