import statistics
from collections import deque

from tree_node import TreeNode


def level_order(root: TreeNode | None) -> list[list[int]]:
    # Problem 8: Binary Tree Level Order Traversal
    # Key idea: BFS by level using a queue.
    # Time:
    # Space:

    if not root:
        return []

    res = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        curr_level = []

        for _ in range(level_size):
            node = queue.popleft()

            if node:
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        res.append(curr_level)

    return res


def right_side_view(root: TreeNode | None) -> list[int]:
    # Problem 9: Right Side View
    # Key idea: take the last node at each BFS level.
    # Time:
    # Space:

    if not root:
        return []

    res = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        curr_level = []

        for _ in range(level_size):
            node = queue.popleft()

            if node:
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        res.append(curr_level[-1])

    return res


def minimum_depth(root: TreeNode | None) -> int:
    # Problem 10: Minimum Depth
    # Key idea: BFS until the first leaf.
    # Time:
    # Space:

    if not root:
        return 0

    min_depth = 1

    queue = deque([root])
    while queue:
        level_size = len(queue)
        curr_level = []

        for _ in range(level_size):
            node = queue.popleft()

            if not node.left and not node.right:
                return min_depth

            if node:
                curr_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        min_depth += 1

    return min_depth


def average_of_levels(root: TreeNode | None) -> list[float]:
    # Problem 11: Average Of Levels
    # Key idea: sum each BFS level and divide by its size.
    # Time:
    # Space:

    if root is None:
        return []

    res = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        curr_level = []

        for _ in range(level_size):
            node = queue.popleft()

            if node:
                curr_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        res.append(statistics.mean(curr_level))

    return res


def zigzag_level_order(root: TreeNode | None) -> list[list[int]]:
    # Problem 12: Zigzag Level Order
    # Key idea: BFS by level with alternating output direction.
    # Time:
    # Space:

    if root is None:
        return []

    res = []
    queue = deque([root])
    zigzag = False
    while queue:
        level_size = len(queue)
        curr_level = []

        for _ in range(level_size):
            node = queue.popleft()

            if node:
                curr_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        if zigzag:
            res.append(list(reversed(curr_level)))
        else:
            res.append(curr_level)

        zigzag = not zigzag

    return res


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
