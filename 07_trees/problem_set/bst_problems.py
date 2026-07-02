from tree_node import TreeNode


def search_in_bst(root: TreeNode | None, val: int) -> TreeNode | None:
    # Problem 17: Search In BST
    # Key idea: use the BST ordering property to move left or right.
    # Time:
    # Space:

    raise NotImplementedError


def validate_bst(root: TreeNode | None) -> bool:
    # Problem 18: Validate BST
    # Key idea: carry lower and upper bounds.
    # Time:
    # Space:

    raise NotImplementedError


def kth_smallest(root: TreeNode | None, k: int) -> int:
    # Problem 19: Kth Smallest In BST
    # Key idea: inorder traversal visits BST values in sorted order.
    # Time:
    # Space:

    raise NotImplementedError


def lowest_common_ancestor_bst(
    root: TreeNode | None,
    p: TreeNode,
    q: TreeNode,
) -> TreeNode | None:
    # Problem 20: Lowest Common Ancestor Of BST
    # Key idea: use value ranges to move left, move right, or stop.
    # Time:
    # Space:

    raise NotImplementedError


def convert_sorted_array_to_bst(nums: list[int]) -> TreeNode | None:
    # Problem 21: Convert Sorted Array To BST
    # Key idea: choose the middle element as the root recursively.
    # Time:
    # Space:

    raise NotImplementedError


def insert_into_bst(root: TreeNode | None, val: int) -> TreeNode:
    # Problem 22: Insert Into A BST
    # Key idea: walk down to the insertion point using BST ordering.
    # Time:
    # Space:

    raise NotImplementedError


def delete_node_bst(root: TreeNode | None, key: int) -> TreeNode | None:
    # Problem 23: Delete Node In A BST
    # Key idea: handle leaf, one-child, and two-child deletion cases.
    # Time:
    # Space:

    raise NotImplementedError


def search_range_bst(root: TreeNode | None, low: int, high: int) -> list[int]:
    # Problem 24: Range Sum / Search Range In BST
    # Key idea: prune branches using BST ordering.
    # Time:
    # Space:

    raise NotImplementedError


def trim_bst(root: TreeNode | None, low: int, high: int) -> TreeNode | None:
    # Problem 25: Trim A Binary Search Tree
    # Key idea: remove nodes outside the target value range.
    # Time:
    # Space:

    raise NotImplementedError
