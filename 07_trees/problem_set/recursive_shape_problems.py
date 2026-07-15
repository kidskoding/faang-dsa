from tree_node import TreeNode


def max_depth(root: TreeNode | None) -> int:
    # Problem 1: Maximum Depth Of Binary Tree
    #
    # Key idea: return information from left and right subtrees.
    # Time: O(n) because you have to visit all nodes to find the depth
    # Space: O(h) because the recursion stack runs down through tree's height of h

    if root is None:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    # Problem 2: Invert Binary Tree
    #
    # Key idea: swap each node's left and right children.
    # Time: O(n) because you have to visit all nodes to find the depth
    # Space: O(h) because the recursion stack runs down through the tree's height of h

    if root is None:
        return None

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root


def same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    # Problem 3: Same Tree
    # Key idea: compare two trees node-by-node.
    # Time:
    # Space:

    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False

    left_match = same_tree(p.left, q.left)
    right_match = same_tree(p.right, q.right)

    return left_match and right_match


def symmetric_tree(root: TreeNode | None) -> bool:
    # Problem 4: Symmetric Tree
    # Key idea: compare left and right subtrees as mirrors.
    # Time:
    # Space:

    if root is None:
        return True

    def symmetric_tree_helper(left: TreeNode | None, right: TreeNode | None) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        l_mirrored = symmetric_tree_helper(left.left, right.right)
        r_mirrored = symmetric_tree_helper(right.left, left.right)

        return l_mirrored and r_mirrored

    return symmetric_tree_helper(root.left, root.right)


def balanced_binary_tree(root: TreeNode | None) -> bool:
    # Problem 5: Balanced Binary Tree
    # Key idea: compute height while detecting imbalance.
    # Time:
    # Space:

    def balanced_binary_tree_helper(node: TreeNode | None) -> int:
        if node is None:
            return 0

        left = balanced_binary_tree_helper(node.left)
        right = balanced_binary_tree_helper(node.right)

        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return balanced_binary_tree_helper(root) != -1


def diameter_of_binary_tree(root: TreeNode | None) -> int:
    # Problem 6: Diameter Of Binary Tree
    # Key idea: combine left height and right height at each node.
    # Time:
    # Space:

    best_diameter = 0

    def height(node: TreeNode | None):
        nonlocal best_diameter
        if node is None:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        best_diameter = max(best_diameter, left_height + right_height)

        return 1 + max(left_height, right_height)

    height(root)
    return best_diameter


def subtree_of_another_tree(
    root: TreeNode | None,
    subroot: TreeNode | None,
) -> bool:
    # Problem 7: Subtree Of Another Tree
    # Key idea: search each node and use same_tree when values might match.
    # Time:
    # Space:

    def same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        left_match = same_tree(p.left, q.left)
        right_match = same_tree(p.right, q.right)

        return left_match and right_match

    if subroot is None:
        return True
    if not root and subroot:
        return False

    if same_tree(root, subroot):
        return True

    return subtree_of_another_tree(root.left, subroot) or subtree_of_another_tree(root.right, subroot)


def lowest_common_ancestor(
    root: TreeNode | None,
    p: TreeNode | None,
    q: TreeNode | None,
) -> TreeNode | None:
    # Problem 8: Lowest Common Ancestor Of A Binary Tree
    # Key idea: recurse on left and right subtrees and combine the results.
    # Time:
    # Space:

    pass


def count_nodes(root: TreeNode | None) -> int:
    # Problem 9: Count Complete Tree Nodes
    # Key idea: compare left and right heights to count in less than O(n).
    # Time:
    # Space:

    pass


def prune_tree(root: TreeNode | None) -> TreeNode | None:
    # Problem 10: Binary Tree Pruning
    # Key idea: remove subtrees that do not contain a `1`.
    # Time:
    # Space:

    pass


def flatten(root: TreeNode | None) -> None:
    # Problem 11: Flatten Binary Tree To Linked List
    # Key idea: mutate the tree in place using preorder logic.
    # Time:
    # Space:

    pass


def lca_deepest_leaves(root: TreeNode | None) -> TreeNode | None:
    # Problem 12: Lowest Common Ancestor Of Deepest Leaves
    # Key idea: compare subtree heights and propagate the deeper side.
    # Time:
    # Space:

    pass


def rob(root: TreeNode | None) -> int:
    # Problem 13: House Robber III
    # Key idea: return a rob/skip pair from each subtree.
    # Time:
    # Space:

    pass


def max_path_sum(root: TreeNode | None) -> int:
    # Problem 14: Binary Tree Maximum Path Sum
    # Key idea: choose whether to continue a path through a node.
    # Time:
    # Space:

    pass


def min_camera_cover(root: TreeNode | None) -> int:
    # Problem 15: Binary Tree Cameras
    # Key idea: return a covered/needs-camera state from each subtree.
    # Time:
    # Space:

    pass
