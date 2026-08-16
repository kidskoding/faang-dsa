# Trees Problem Set

## Goal

Build tree intuition across the core traversal patterns — iterative and
N-ary traversal, recursive subtree DFS, level-order BFS, root-to-leaf
paths, BST navigation, and tree construction — then use each pattern to solve the medium and hard
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

## Traversals

`traversal_problems.py` — walk a tree without recursion: explicit-stack
DFS in all three orders, an on-demand iterator, and the N-ary variants.

### 1. [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

- solves: `inorder_traversal`
- Pattern: iterative with an explicit stack — run left pushing nodes, pop to visit, then go right.

### 2. [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

- solves: `preorder_traversal`
- Pattern: iterative with a stack — visit on push, pushing the right child before the left.

### 3. [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

- solves: `postorder_traversal`
- Pattern: modified preorder (node, right, left) reversed, or a stack with a last-visited pointer.

### 4. [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)

- solves: `BSTIterator`
- Pattern: a stack of the current node's left spine makes `next()` amortized O(1).

### 5. [N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)

- solves: `nary_preorder`
- Pattern: stack-based preorder pushing children right-to-left so the leftmost pops first.

### 6. [N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)

- solves: `nary_postorder`
- Pattern: preorder with children left-to-right, then reverse the visit order.

### 7. [N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)

- solves: `nary_level_order`
- Pattern: BFS a queue level by level, extending with each node's children list.

### 8. [Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)

- solves: `max_depth_nary`
- Pattern: one plus the max depth over all children, zero for an empty tree.

## Recursive Shape

`recursive_shape_problems.py` — recursive DFS that returns information
from the left and right subtrees to answer a question about the tree's
shape or structure.

### 9. [Maximum Depth Of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

- solves: `max_depth`
- Pattern: return information from subtrees.

### 10. [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

- solves: `invert_tree`
- Pattern: swap each node's left and right children recursively.

### 11. [Same Tree](https://leetcode.com/problems/same-tree/)

- solves: `same_tree`
- Pattern: compare two trees node by node.

### 12. [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

- solves: `symmetric_tree`
- Pattern: compare the left and right subtrees as mirrors.

### 13. [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

- solves: `balanced_binary_tree`
- Pattern: return height while detecting imbalance.

### 14. [Diameter Of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

- solves: `diameter_of_binary_tree`
- Pattern: combine left height and right height at each node.

### 15. [Subtree Of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

- solves: `subtree_of_another_tree`
- Pattern: search candidate roots and use `same_tree`.

### 16. [Lowest Common Ancestor Of A Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

- solves: `lowest_common_ancestor`
- Pattern: recurse on left and right subtrees and combine the results.

### 17. [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)

- solves: `count_nodes`
- Pattern: compare left and right heights to count in less than O(n).

### 18. [Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/)

- solves: `prune_tree`
- Pattern: remove subtrees that do not contain a `1`.

### 19. [Flatten Binary Tree To Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

- solves: `flatten`
- Pattern: mutate the tree in place using preorder logic.

### 20. [Lowest Common Ancestor Of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/)

- solves: `lca_deepest_leaves`
- Pattern: compare subtree heights and propagate the deeper side.

### 21. [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

- solves: `max_path_sum`
- Pattern: choose whether to continue a path through a node.

## BFS Levels

`bfs_level_problems.py` — level-order BFS with a queue that processes one
full level per iteration.

### 22. [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

- solves: `level_order`
- Pattern: BFS by level using a queue.

### 23. [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

- solves: `right_side_view`
- Pattern: take the last node from each BFS level.

### 24. [Minimum Depth Of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

- solves: `minimum_depth`
- Pattern: BFS until the first leaf.

### 25. [Average Of Levels In Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/)

- solves: `average_of_levels`
- Pattern: sum each BFS level and divide by its size.

### 26. [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

- solves: `zigzag_level_order`
- Pattern: BFS by level with alternating output direction.

### 27. [Populating Next Right Pointers In Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

- solves: `connect`
- Pattern: link nodes level by level using existing next pointers.

### 28. [Vertical Order Traversal Of A Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)

- solves: `vertical_traversal`
- Pattern: track column indices during traversal.

### 29. [All Nodes Distance K In Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

- solves: `distance_k`
- Pattern: combine parent links with BFS from the target.

### 30. [Maximum Width Of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/)

- solves: `width_of_binary_tree`
- Pattern: BFS carrying heap-style position indices; width is last minus first index per level.

### 31. [Find Bottom Left Tree Value](https://leetcode.com/problems/find-bottom-left-tree-value/)

- solves: `find_bottom_left_value`
- Pattern: BFS level by level, remembering the first value of each level; the last remembered wins.

### 32. [Cousins In Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/)

- solves: `is_cousins`
- Pattern: BFS tracking each target's depth and parent; cousins share depth but not parent.

## Root-To-Leaf Paths

`path_problems.py` — DFS that carries state (a running sum, number, or
path) down from the root toward each leaf.

### 33. [Path Sum](https://leetcode.com/problems/path-sum/)

- solves: `path_sum`
- Pattern: carry the remaining sum from root to leaf.

### 34. [Path Sum II](https://leetcode.com/problems/path-sum-ii/)

- solves: `path_sum_ii`
- Pattern: backtrack with a current root-to-leaf path.

### 35. [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

- solves: `binary_tree_paths`
- Pattern: build every root-to-leaf path string.

### 36. [Sum Root To Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)

- solves: `sum_root_to_leaf_numbers`
- Pattern: carry the current number down the tree.

### 37. [Count Good Nodes In Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

- solves: `good_nodes`
- Pattern: carry the maximum value seen so far down each path.

### 38. [Path Sum III](https://leetcode.com/problems/path-sum-iii/)

- solves: `path_sum_iii`
- Pattern: count paths that can start anywhere using prefix sums.

## Binary Search Trees

`bst_problems.py` — exploit the BST ordering property to navigate,
validate, and modify the tree.

### 39. [Search In A Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)

- solves: `search_in_bst`
- Pattern: use the BST ordering to move left or right.

### 40. [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

- solves: `validate_bst`
- Pattern: carry lower and upper bounds.

### 41. [Kth Smallest Element In A BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

- solves: `kth_smallest`
- Pattern: inorder traversal visits BST values in sorted order.

### 42. [Lowest Common Ancestor Of A BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

- solves: `lowest_common_ancestor_bst`
- Pattern: use value ranges to move left, move right, or stop.

### 43. [Range Sum Of BST](https://leetcode.com/problems/range-sum-of-bst/)

- solves: `range_sum_bst`
- Pattern: prune branches using BST ordering.

### 44. [Convert Sorted Array To BST](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

- solves: `convert_sorted_array_to_bst`
- Pattern: choose the middle element as the root recursively.

### 45. [Insert Into A BST](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

- solves: `insert_into_bst`
- Pattern: walk down to the insertion point using BST ordering.

### 46. [Delete Node In A BST](https://leetcode.com/problems/delete-node-in-a-bst/)

- solves: `delete_node_bst`
- Pattern: handle leaf, one-child, and two-child deletion cases.

### 47. [Trim A Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/)

- solves: `trim_bst`
- Pattern: remove nodes outside the target value range.

### 48. [Inorder Successor In BST](https://leetcode.com/problems/inorder-successor-in-bst/)

- solves: `inorder_successor`
- Pattern: BST navigation tracking the deepest ancestor greater than the target.

### 49. [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)

- solves: `recover_tree`
- Pattern: fix two swapped nodes found by inorder traversal.

### 50. [Convert BST To Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/)

- solves: `convert_bst`
- Pattern: reverse inorder (right, node, left) carrying a running sum of all greater values.

## Construction

`construction_problems.py` — rebuild or serialize a tree from traversal
orderings.

### 51. [Construct Binary Tree From Preorder And Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

- solves: `construct_from_preorder_inorder`
- Pattern: preorder gives the root; inorder splits left and right subtrees.

### 52. [Construct Binary Tree From Inorder And Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

- solves: `construct_from_inorder_postorder`
- Pattern: postorder gives the root; inorder splits left and right subtrees.

### 53. [Serialize And Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

- solves: `serialize_binary_tree`, `deserialize_binary_tree`
- Pattern: turn the tree into a sequence that preserves shape, then rebuild it.

### 54. [Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/)

- solves: `construct_maximum_binary_tree`
- Pattern: the array maximum is the root; recurse on the left and right slices.

### 55. [Construct Binary Search Tree From Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)

- solves: `bst_from_preorder`
- Pattern: preorder gives each root; BST bounds split values into subtrees.

### 56. [Construct Binary Tree From Preorder And Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)

- solves: `construct_from_preorder_postorder`
- Pattern: the second preorder value is the left child root; find it in postorder to split.

### 57. [Construct String From Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/)

- solves: `tree_to_string`
- Pattern: preorder emit with parentheses around children, dropping empty pairs.
