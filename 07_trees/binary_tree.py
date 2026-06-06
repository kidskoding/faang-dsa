from collections import deque

from tree_node import TreeNode


def is_leaf(root: TreeNode) -> bool:
    # Time: O(1), because we only check the two child pointers.
    #
    # Space: O(1), because we use no extra data structures.
    return root.left is None and root.right is None


def height(root: TreeNode | None) -> int:
    # Time: O(n), because we visit every node exactly once.
    #
    # Space: O(h), where h is the height of the tree, due to the recursion stack.
    # Worst case h = n for a skewed tree; balanced case h = log n.
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))


def count_nodes(root: TreeNode | None) -> int:
    # Time: O(n), because we visit and count every node exactly once.
    #
    # Space: O(h), where h is the height of the tree, due to the recursion stack.
    # Worst case h = n for a skewed tree; balanced case h = log n.
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)


def build_tree_from_level_order(values: list[int | None]) -> TreeNode | None:
    # Time: O(n), where n is len(values), because we scan the input list once.
    #
    # Space: O(n), because we create up to n tree nodes and the queue can hold
    # a full level of nodes in the worst case.
    # Auxiliary space excluding the returned tree is O(w), where w is max width.

    if not values or values[0] is None:
        return None

    i = 1
    root = TreeNode(values[0])
    queue = deque([root])

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
        i += 1

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return root


def tree_to_level_order(root: TreeNode | None) -> list[int | None]:
    # Time: O(n), because each real node contributes at most two child entries,
    # and the final trailing-None cleanup is also linear overall.
    #
    # Space: O(n) for the output list, plus O(w) for the BFS queue, where w is
    # the max width of the tree. In the worst case, w can be O(n).
    # If the interviewer only asks for auxiliary space, it is O(w).

    if root is None:
        return []

    res = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node is not None:
            res.append(node.val)

            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)

    while res and res[-1] is None:
        res.pop()

    return res
