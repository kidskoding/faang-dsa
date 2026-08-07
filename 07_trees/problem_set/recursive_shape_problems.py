from tree_node import TreeNode


def max_depth(root: TreeNode | None) -> int:
    # Problem 1: Maximum Depth Of Binary Tree
    #
    # Key idea: return information from left and right subtrees.
    # Time:
    # Space:

    raise NotImplementedError


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    # Problem 2: Invert Binary Tree
    #
    # Key idea: swap each node's left and right children.
    # Time:
    # Space:

    raise NotImplementedError


def same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    # Problem 3: Same Tree
    # Key idea: compare two trees node-by-node.
    # Time:
    # Space:

    raise NotImplementedError


def symmetric_tree(root: TreeNode | None) -> bool:
    # Problem 4: Symmetric Tree
    # Key idea: compare left and right subtrees as mirrors.
    # Time:
    # Space:

    raise NotImplementedError


def balanced_binary_tree(root: TreeNode | None) -> bool:
    # Problem 5: Balanced Binary Tree
    # Key idea: compute height while detecting imbalance.
    # Time:
    # Space:

    raise NotImplementedError


def diameter_of_binary_tree(root: TreeNode | None) -> int:
    # Problem 6: Diameter Of Binary Tree
    # Key idea: combine left height and right height at each node.
    # Time:
    # Space:

    raise NotImplementedError


def subtree_of_another_tree(
    root: TreeNode | None,
    subroot: TreeNode | None,
) -> bool:
    # Problem 7: Subtree Of Another Tree
    # Key idea: search each node and use same_tree when values might match.
    # Time:
    # Space:

    raise NotImplementedError


def lowest_common_ancestor(
    root: TreeNode | None,
    p: TreeNode | None,
    q: TreeNode | None,
) -> TreeNode | None:
    # Problem 8: Lowest Common Ancestor Of A Binary Tree
    # Key idea: recurse on left and right subtrees and combine the results.
    # Time:
    # Space:

    raise NotImplementedError


def count_nodes(root: TreeNode | None) -> int:
    # Problem 9: Count Complete Tree Nodes
    # Key idea: compare left and right heights to count in less than O(n).
    # Time:
    # Space:

    raise NotImplementedError


def prune_tree(root: TreeNode | None) -> TreeNode | None:
    # Problem 10: Binary Tree Pruning
    # Key idea: remove subtrees that do not contain a `1`.
    # Time:
    # Space:

    raise NotImplementedError


def flatten(root: TreeNode | None) -> None:
    # Problem 11: Flatten Binary Tree To Linked List
    # Key idea: mutate the tree in place using preorder logic.
    # Time:
    # Space:

    raise NotImplementedError


def lca_deepest_leaves(root: TreeNode | None) -> TreeNode | None:
    # Problem 12: Lowest Common Ancestor Of Deepest Leaves
    # Key idea: compare subtree heights and propagate the deeper side.
    # Time:
    # Space:

    raise NotImplementedError


def max_path_sum(root: TreeNode | None) -> int:
    # Problem 14: Binary Tree Maximum Path Sum
    # Key idea: choose whether to continue a path through a node.
    # Time:
    # Space:

    raise NotImplementedError
