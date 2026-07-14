# All Nodes Distance K In Binary Tree

Given the root of a binary tree, a target node, and an integer `k`, return the
values of all nodes that are exactly distance `k` from the target node.

Distance is measured by the number of edges in the shortest path between two
nodes. The path may move from a node to its left child, right child, or parent.

Each node in the tree is represented by a `TreeNode` object:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The answer may be returned in any order.

Example 1:
Input:
root = [3,5,1,6,2,0,8,null,null,7,4]
target = 5
k = 2
Output: [7,4,1]

Example 2:
Input:
root = [1]
target = 1
k = 3
Output: []

Constraints:
1 \<= number of nodes \<= 500
0 \<= Node.val \<= 500
All Node values are unique
target is a node in the tree
0 \<= k \<= 1000
