
from tree_node import TreeNode


def level_order(root: TreeNode | None) -> list[list[int]]:
    # Problem 8: Binary Tree Level Order Traversal
    # Key idea: BFS by level using a queue.
    # Time:
    # Space:

    raise NotImplementedError


def right_side_view(root: TreeNode | None) -> list[int]:
    # Problem 9: Right Side View
    # Key idea: take the last node at each BFS level.
    # Time:
    # Space:

    raise NotImplementedError


def minimum_depth(root: TreeNode | None) -> int:
    # Problem 10: Minimum Depth
    # Key idea: BFS until the first leaf.
    # Time:
    # Space:

    raise NotImplementedError


def average_of_levels(root: TreeNode | None) -> list[float]:
    # Problem 11: Average Of Levels
    # Key idea: sum each BFS level and divide by its size.
    # Time:
    # Space:

    raise NotImplementedError


def zigzag_level_order(root: TreeNode | None) -> list[list[int]]:
    # Problem 12: Zigzag Level Order
    # Key idea: BFS by level with alternating output direction.
    # Time:
    # Space:

    raise NotImplementedError


def connect(root: TreeNode | None) -> TreeNode | None:
    # Problem 13: Populating Next Right Pointers In Each Node
    # Key idea: link nodes level by level using existing next pointers.
    # Time:
    # Space:

    raise NotImplementedError


def vertical_traversal(root: TreeNode | None) -> list[list[int]]:
    # Problem 14: Vertical Order Traversal Of A Binary Tree
    # Key idea: track column indices during traversal.
    # Time:
    # Space:

    raise NotImplementedError


def distance_k(
    root: TreeNode | None,
    target: TreeNode | None,
    k: int,
) -> list[int]:
    # Problem 15: All Nodes Distance K In Binary Tree
    # Key idea: combine parent links with BFS from the target.
    # Time:
    # Space:

    raise NotImplementedError


def width_of_binary_tree(root: TreeNode | None) -> int:
    # Problem 16: Maximum Width Of Binary Tree
    # Key idea: BFS carrying heap-style position indices; width is last minus first index per level.
    # Time:
    # Space:

    raise NotImplementedError


def find_bottom_left_value(root: TreeNode | None) -> int:
    # Problem 17: Find Bottom Left Tree Value
    # Key idea: BFS level by level, remembering the first value of each level; the last remembered wins.
    # Time:
    # Space:

    raise NotImplementedError


def is_cousins(root: TreeNode | None, x: int, y: int) -> bool:
    # Problem 18: Cousins In Binary Tree
    # Key idea: BFS tracking each target's depth and parent; cousins share depth but not parent.
    # Time:
    # Space:

    raise NotImplementedError
