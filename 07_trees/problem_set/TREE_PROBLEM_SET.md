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

### 1. [Maximum Depth Of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

- Pattern: return information from subtrees.

### 2. [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

- Pattern: mutate tree shape recursively.

### 3. [Same Tree](https://leetcode.com/problems/same-tree/)

- Pattern: compare two trees node by node.

### 4. [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

- Pattern: compare mirror subtrees.

### 5. [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

- Pattern: return height while checking balance.

### 6. [Diameter Of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

- Pattern: combine left height and right height at each node.

### 7. [Subtree Of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

- Pattern: search candidate roots and use `same_tree`.

### 8. [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

- Pattern: BFS by level.

### 9. [Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

- Pattern: take the last node from each BFS level.

### 10. [Minimum Depth](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

- Pattern: BFS until the first leaf.

### 11. [Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

- Pattern: BFS by level with alternating direction.

## Mediums

These are the tree mediums you should drill for FAANG-style interviews.

### 12. [Path Sum](https://leetcode.com/problems/path-sum/)

- Pattern: root-to-leaf sum check.

### 13. [Path Sum II](https://leetcode.com/problems/path-sum-ii/)

- Pattern: backtracking over root-to-leaf paths.

### 14. [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

- Pattern: collect all root-to-leaf path strings.

### 15. [Sum Root To Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)

- Pattern: carry a running number down the tree.

### 16. [Path Sum III](https://leetcode.com/problems/path-sum-iii/)

- Pattern: count paths that can start anywhere.

### 17. [Lowest Common Ancestor Of A Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

- Pattern: recurse on left and right subtrees.

### 18. [Search In BST](https://leetcode.com/problems/search-in-a-binary-search-tree/)

- Pattern: use BST ordering to move left or right.

### 19. [Validate BST](https://leetcode.com/problems/validate-binary-search-tree/)

- Pattern: carry lower and upper bounds.

### 20. [Kth Smallest Element In A BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

- Pattern: inorder traversal gives sorted order.

### 21. [Lowest Common Ancestor Of A BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

- Pattern: use BST value ranges to stop early.

### 22. [Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)

- Pattern: prune BST subtrees outside the value range.

### 23. [Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/)

- Pattern: BST navigation tracking the deepest ancestor greater than the target.

### 24. [Convert Sorted Array To BST](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

- Pattern: choose the middle element as root.

### 25. [Insert Into A BST](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

- Pattern: walk down to the insertion point.

### 26. [Delete Node In A BST](https://leetcode.com/problems/delete-node-in-a-bst/)

- Pattern: handle leaf, one-child, and two-child cases.

### 27. [Construct Binary Tree From Preorder And Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

- Pattern: preorder gives root, inorder splits left and right.

### 28. [Construct Binary Tree From Inorder And Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

- Pattern: postorder gives root, inorder splits left and right.

### 29. [Serialize And Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

- Pattern: turn the tree into a sequence and rebuild it.

### 30. [Populating Next Right Pointers In Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

- Pattern: link nodes level by level using existing next pointers.

### 31. [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)

- Pattern: compare left and right heights to count in less than O(n).

## Hards And Extensions

These are the tree follow-ups that push beyond the standard medium set.

### 32. [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

- Pattern: choose whether to continue a path through a node.

### 33. [Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/)

- Pattern: dynamic state on each node.

### 34. [House Robber III](https://leetcode.com/problems/house-robber-iii/)

- Pattern: choose between robbing a node or skipping it.

### 35. [Count Good Nodes In Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

- Pattern: carry the maximum value seen so far.

### 36. [Vertical Order Traversal Of A Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)

- Pattern: track column indices during traversal.

### 37. [All Nodes Distance K In Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

- Pattern: combine parent links with BFS or DFS.

### 38. [Flatten Binary Tree To Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

- Pattern: mutate the tree in place using preorder logic.

### 39. [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)

- Pattern: fix two swapped nodes found by inorder traversal.

### 40. [Lowest Common Ancestor Of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/)

- Pattern: compare subtree heights and propagate the deeper side.

### 41. [Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/)

- Pattern: remove subtrees that do not contain a `1`.

## Recommended Order

If you want the shortest path to tree fluency, do them in this order:

```text
1. [Maximum Depth](https://leetcode.com/problems/maximum-depth/)
2. [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
3. [Same Tree](https://leetcode.com/problems/same-tree/)
4. [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
5. [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
6. [Diameter Of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
7. [Subtree Of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
8. [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
9. [Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)
10. [Minimum Depth](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
11. [Average Of Levels](https://leetcode.com/problems/average-of-levels-in-binary-tree/)
12. [Zigzag Level Order](https://leetcode.com/problems/zigzag-level-order/)
13. [Path Sum](https://leetcode.com/problems/path-sum/)
14. [Path Sum II](https://leetcode.com/problems/path-sum-ii/)
15. [Lowest Common Ancestor Of A Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
16. [Validate BST](https://leetcode.com/problems/validate-binary-search-tree/)
17. [Kth Smallest Element In A BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
18. [Serialize And Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
19. [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
20. [All Nodes Distance K In Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)
```
