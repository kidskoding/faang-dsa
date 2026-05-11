# Trees Problem Set

## Goal

Build tree intuition from the ground up, then use that foundation to solve the medium and hard binary-tree problems that show up in LeetCode-style interviews.

## How To Use

Work the file in order. The early sections are the fundamentals. The later sections are the medium and hard extensions.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Fundamentals

These are the tree basics you should be able to do without thinking too hard.

### 1. Maximum Depth Of Binary Tree
- Pattern: return information from subtrees.

### 2. Invert Binary Tree
- Pattern: mutate tree shape recursively.

### 3. Same Tree
- Pattern: compare two trees node by node.

### 4. Symmetric Tree
- Pattern: compare mirror subtrees.

### 5. Balanced Binary Tree
- Pattern: return height while checking balance.

### 6. Diameter Of Binary Tree
- Pattern: combine left height and right height at each node.

### 7. Subtree Of Another Tree
- Pattern: search candidate roots and use `same_tree`.

### 8. Binary Tree Level Order Traversal
- Pattern: BFS by level.

### 9. Right Side View
- Pattern: take the last node from each BFS level.

### 10. Minimum Depth
- Pattern: BFS until the first leaf.

### 11. Average Of Levels
- Pattern: compute one average per BFS level.

### 12. Zigzag Level Order Traversal
- Pattern: BFS by level with alternating direction.

## Mediums

These are the tree mediums you should drill for FAANG-style interviews.

### 13. Path Sum
- Pattern: root-to-leaf sum check.

### 14. Path Sum II
- Pattern: backtracking over root-to-leaf paths.

### 15. Binary Tree Paths
- Pattern: collect all root-to-leaf path strings.

### 16. Sum Root To Leaf Numbers
- Pattern: carry a running number down the tree.

### 17. Path Sum III
- Pattern: count paths that can start anywhere.

### 18. Lowest Common Ancestor Of A Binary Tree
- Pattern: recurse on left and right subtrees.

### 19. Search In BST
- Pattern: use BST ordering to move left or right.

### 20. Validate BST
- Pattern: carry lower and upper bounds.

### 21. Kth Smallest Element In A BST
- Pattern: inorder traversal gives sorted order.

### 22. Lowest Common Ancestor Of A BST
- Pattern: use BST value ranges to stop early.

### 23. Convert Sorted Array To BST
- Pattern: choose the middle element as root.

### 24. Insert Into A BST
- Pattern: walk down to the insertion point.

### 25. Delete Node In A BST
- Pattern: handle leaf, one-child, and two-child cases.

### 26. Construct Binary Tree From Preorder And Inorder Traversal
- Pattern: preorder gives root, inorder splits left and right.

### 27. Construct Binary Tree From Inorder And Postorder Traversal
- Pattern: postorder gives root, inorder splits left and right.

### 28. Serialize And Deserialize Binary Tree
- Pattern: turn the tree into a sequence and rebuild it.

## Hards And Extensions

These are the tree follow-ups that push beyond the standard medium set.

### 29. Binary Tree Maximum Path Sum
- Pattern: choose whether to continue a path through a node.

### 30. Binary Tree Cameras
- Pattern: dynamic state on each node.

### 31. House Robber III
- Pattern: choose between robbing a node or skipping it.

### 32. Count Good Nodes In Binary Tree
- Pattern: carry the maximum value seen so far.

### 33. Vertical Order Traversal Of A Binary Tree
- Pattern: track column indices during traversal.

### 34. All Nodes Distance K In Binary Tree
- Pattern: combine parent links with BFS or DFS.

### 35. Flatten Binary Tree To Linked List
- Pattern: mutate the tree in place using preorder logic.

### 36. Recover Binary Search Tree
- Pattern: fix two swapped nodes found by inorder traversal.

### 37. Lowest Common Ancestor Of Deepest Leaves
- Pattern: compare subtree heights and propagate the deeper side.

### 38. Binary Tree Pruning
- Pattern: remove subtrees that do not contain a `1`.

## Recommended Order

If you want the shortest path to tree fluency, do them in this order:

```text
1. Maximum Depth
2. Invert Binary Tree
3. Same Tree
4. Symmetric Tree
5. Balanced Binary Tree
6. Diameter Of Binary Tree
7. Subtree Of Another Tree
8. Binary Tree Level Order Traversal
9. Right Side View
10. Minimum Depth
11. Average Of Levels
12. Zigzag Level Order
13. Path Sum
14. Path Sum II
15. Lowest Common Ancestor Of A Binary Tree
16. Validate BST
17. Kth Smallest Element In A BST
18. Serialize And Deserialize Binary Tree
19. Binary Tree Maximum Path Sum
20. All Nodes Distance K In Binary Tree
```

## Mastery Rule

A problem is not done until you can:

1. explain the pattern
2. choose the base case
3. write the helper shape
4. pass the tests
5. explain time and space complexity
