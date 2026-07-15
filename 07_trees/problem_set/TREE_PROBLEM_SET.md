# Trees Problem Set

## Goal

Build tree intuition across the core traversal patterns — recursive
subtree DFS, level-order BFS, root-to-leaf paths, BST navigation, and
tree construction — then use each pattern to solve the medium and hard
binary-tree problems that show up in LeetCode-style interviews.

## How To Use

Each section maps to one solution file in this folder and to one tree
pattern. Work a section top to bottom: problems are ordered roughly easy
to hard, and the implemented ones come first. `solves:` names the
function in that section's file; `solves: (todo)` means the solution is
not written yet.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Recursive Shape

`recursive_shape_problems.py` — recursive DFS that returns information
from the left and right subtrees to answer a question about the tree's
shape or structure.

### 1. [Maximum Depth Of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

- solves: `max_depth`
- Pattern: return information from subtrees.

### 2. [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

- solves: `invert_tree`
- Pattern: swap each node's left and right children recursively.

### 3. [Same Tree](https://leetcode.com/problems/same-tree/)

- solves: `same_tree`
- Pattern: compare two trees node by node.

### 4. [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

- solves: `symmetric_tree`
- Pattern: compare the left and right subtrees as mirrors.

### 5. [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

- solves: `balanced_binary_tree`
- Pattern: return height while detecting imbalance.

### 6. [Diameter Of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

- solves: `diameter_of_binary_tree`
- Pattern: combine left height and right height at each node.

### 7. [Subtree Of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

- solves: `subtree_of_another_tree`
- Pattern: search candidate roots and use `same_tree`.

### 8. [Lowest Common Ancestor Of A Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

- solves: `lowest_common_ancestor`
- Pattern: recurse on left and right subtrees and combine the results.

### 9. [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)

- solves: `count_nodes`
- Pattern: compare left and right heights to count in less than O(n).

### 10. [Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/)

- solves: `prune_tree`
- Pattern: remove subtrees that do not contain a `1`.

### 11. [Flatten Binary Tree To Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

- solves: `flatten`
- Pattern: mutate the tree in place using preorder logic.

### 12. [Lowest Common Ancestor Of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/)

- solves: `lca_deepest_leaves`
- Pattern: compare subtree heights and propagate the deeper side.

### 13. [House Robber III](https://leetcode.com/problems/house-robber-iii/)

- solves: `rob`
- Pattern: return a rob/skip pair from each subtree.

### 14. [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

- solves: `max_path_sum`
- Pattern: choose whether to continue a path through a node.

### 15. [Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/)

- solves: `min_camera_cover`
- Pattern: return a covered/needs-camera state from each subtree.

## BFS Levels

`bfs_level_problems.py` — level-order BFS with a queue that processes one
full level per iteration.

### 16. [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

- solves: `level_order`
- Pattern: BFS by level using a queue.

### 17. [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

- solves: `right_side_view`
- Pattern: take the last node from each BFS level.

### 18. [Minimum Depth Of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

- solves: `minimum_depth`
- Pattern: BFS until the first leaf.

### 19. [Average Of Levels In Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/)

- solves: `average_of_levels`
- Pattern: sum each BFS level and divide by its size.

### 20. [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

- solves: `zigzag_level_order`
- Pattern: BFS by level with alternating output direction.

### 21. [Populating Next Right Pointers In Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

- solves: `connect`
- Pattern: link nodes level by level using existing next pointers.

### 22. [Vertical Order Traversal Of A Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)

- solves: `vertical_traversal`
- Pattern: track column indices during traversal.

### 23. [All Nodes Distance K In Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

- solves: `distance_k`
- Pattern: combine parent links with BFS from the target.

## Root-To-Leaf Paths

`path_problems.py` — DFS that carries state (a running sum, number, or
path) down from the root toward each leaf.

### 24. [Path Sum](https://leetcode.com/problems/path-sum/)

- solves: `path_sum`
- Pattern: carry the remaining sum from root to leaf.

### 25. [Path Sum II](https://leetcode.com/problems/path-sum-ii/)

- solves: `path_sum_ii`
- Pattern: backtrack with a current root-to-leaf path.

### 26. [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

- solves: `binary_tree_paths`
- Pattern: build every root-to-leaf path string.

### 27. [Sum Root To Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)

- solves: `sum_root_to_leaf_numbers`
- Pattern: carry the current number down the tree.

### 28. [Count Good Nodes In Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

- solves: `good_nodes`
- Pattern: carry the maximum value seen so far down each path.

### 29. [Path Sum III](https://leetcode.com/problems/path-sum-iii/)

- solves: `path_sum_iii`
- Pattern: count paths that can start anywhere using prefix sums.

## Binary Search Trees

`bst_problems.py` — exploit the BST ordering property to navigate,
validate, and modify the tree.

### 30. [Search In A Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)

- solves: `search_in_bst`
- Pattern: use the BST ordering to move left or right.

### 31. [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

- solves: `validate_bst`
- Pattern: carry lower and upper bounds.

### 32. [Kth Smallest Element In A BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

- solves: `kth_smallest`
- Pattern: inorder traversal visits BST values in sorted order.

### 33. [Lowest Common Ancestor Of A BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

- solves: `lowest_common_ancestor_bst`
- Pattern: use value ranges to move left, move right, or stop.

### 34. [Range Sum Of BST](https://leetcode.com/problems/range-sum-of-bst/)

- solves: `search_range_bst`
- Pattern: prune branches using BST ordering.

### 35. [Convert Sorted Array To BST](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

- solves: `convert_sorted_array_to_bst`
- Pattern: choose the middle element as the root recursively.

### 36. [Insert Into A BST](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

- solves: `insert_into_bst`
- Pattern: walk down to the insertion point using BST ordering.

### 37. [Delete Node In A BST](https://leetcode.com/problems/delete-node-in-a-bst/)

- solves: `delete_node_bst`
- Pattern: handle leaf, one-child, and two-child deletion cases.

### 38. [Trim A Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/)

- solves: `trim_bst`
- Pattern: remove nodes outside the target value range.

### 39. [Inorder Successor In BST](https://leetcode.com/problems/inorder-successor-in-bst/)

- solves: `inorder_successor`
- Pattern: BST navigation tracking the deepest ancestor greater than the target.

### 40. [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)

- solves: `recover_tree`
- Pattern: fix two swapped nodes found by inorder traversal.

## Construction

`construction_problems.py` — rebuild or serialize a tree from traversal
orderings.

### 41. [Construct Binary Tree From Preorder And Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

- solves: `construct_from_preorder_inorder`
- Pattern: preorder gives the root; inorder splits left and right subtrees.

### 42. [Construct Binary Tree From Inorder And Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

- solves: `construct_from_inorder_postorder`
- Pattern: postorder gives the root; inorder splits left and right subtrees.

### 43. [Serialize And Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

- solves: `serialize_binary_tree`, `deserialize_binary_tree`
- Pattern: turn the tree into a sequence that preserves shape, then rebuild it.

### 44. [Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/)

- solves: `construct_maximum_binary_tree`
- Pattern: the array maximum is the root; recurse on the left and right slices.

### 45. [Construct Binary Search Tree From Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)

- solves: `bst_from_preorder`
- Pattern: preorder gives each root; BST bounds split values into subtrees.

### 46. [Construct Binary Tree From Preorder And Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)

- solves: `construct_from_preorder_postorder`
- Pattern: the second preorder value is the left child root; find it in postorder to split.

### 47. [Construct String From Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/)

- solves: `tree_to_string`
- Pattern: preorder emit with parentheses around children, dropping empty pairs.
