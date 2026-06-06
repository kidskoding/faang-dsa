from tree_node import TreeNode


def preorder(root: TreeNode | None) -> list[int]:
    # Time: O(n), because we visit every node exactly once.
    #
    # Space: O(n) for the output list, plus O(h) for the recursion stack.
    # If the interviewer only asks for auxiliary space, it is O(h).
    # Worst case h = n for a skewed tree; balanced case h = log n.

    if root is None:
        return []

    res = []

    res.append(root.val)
    res.extend(preorder(root.left))
    res.extend(preorder(root.right))

    return res


def inorder(root: TreeNode | None) -> list[int]:
    # Time: O(n), because we visit every node exactly once.
    #
    # Space: O(n) for the output list, plus O(h) for the recursion stack.
    # If the interviewer only asks for auxiliary space, it is O(h).
    # Worst case h = n for a skewed tree; balanced case h = log n.

    if root is None:
        return []

    res = []

    res.extend(inorder(root.left))
    res.append(root.val)
    res.extend(inorder(root.right))

    return res


def postorder(root: TreeNode | None) -> list[int]:
    # Time: O(n), because we visit every node exactly once.
    #
    # Space: O(n) for the output list, plus O(h) for the recursion stack.
    # If the interviewer only asks for auxiliary space, it is O(h).
    # Worst case h = n for a skewed tree; balanced case h = log n.

    if root is None:
        return []

    res = []

    res.extend(postorder(root.left))
    res.extend(postorder(root.right))
    res.append(root.val)

    return res
