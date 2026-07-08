# Diameter Of N-Ary Tree

Source: [AlgoMonster 1522](https://algo.monster/liteproblems/1522)

Given the root of an N-ary tree, return the diameter of the tree.

The diameter is the length of the longest path between any two nodes. The path
does not need to pass through the root, and its length is measured by the number
of edges rather than the number of nodes.

Each node is represented by a `Node` object:

```python
class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []
```

## Examples

### Example 1

```python
Input:
root = [1,null,3,2,4,null,5,6]

Output:
3

Explanation:
One longest path is 5 -> 3 -> 1 -> 2, which contains 3 edges.
```

### Example 2

```python
Input:
root = [1,null,2,null,3,null,4]

Output:
3

Explanation:
The tree is a chain from node 1 to node 4.
```

### Example 3

```python
Input:
root = [1]

Output:
0

Explanation:
A single-node tree has no edges.
```

## Constraints

```text
Each node contains an integer value and a list of zero or more children
The input forms a valid N-ary tree
The diameter is measured in edges
```
