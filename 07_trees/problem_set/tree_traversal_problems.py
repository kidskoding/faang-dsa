from tree_node import TreeNode


class NaryNode:
    # Shared node for the N-ary traversal problems in this file.
    def __init__(self, val: int = 0, children: "list[NaryNode] | None" = None) -> None:
        self.val = val
        self.children = children if children is not None else []


def inorder_traversal(root: TreeNode | None) -> list[int]:
    # Problem 1: Binary Tree Inorder Traversal
    # Key idea: iterative with an explicit stack — run left pushing nodes, pop to visit, then go right.
    # Time:
    # Space:

    raise NotImplementedError


def preorder_traversal(root: TreeNode | None) -> list[int]:
    # Problem 2: Binary Tree Preorder Traversal
    # Key idea: iterative with a stack — visit on push, pushing right child before left.
    # Time:
    # Space:

    raise NotImplementedError


def postorder_traversal(root: TreeNode | None) -> list[int]:
    # Problem 3: Binary Tree Postorder Traversal
    # Key idea: modified preorder (node, right, left) reversed, or a stack with a last-visited pointer.
    # Time:
    # Space:

    raise NotImplementedError


class BSTIterator:
    # Problem 4: Binary Search Tree Iterator
    # Key idea: a stack of the current node's left spine makes next() amortized O(1).

    def __init__(self, root: TreeNode | None) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def next(self) -> int:
        # Time:
        # Space:

        raise NotImplementedError

    def has_next(self) -> bool:
        # Time:
        # Space:

        raise NotImplementedError


def nary_preorder(root: NaryNode | None) -> list[int]:
    # Problem 5: N-ary Tree Preorder Traversal
    # Key idea: stack-based preorder pushing children right-to-left so the leftmost pops first.
    # Time:
    # Space:

    raise NotImplementedError


def nary_postorder(root: NaryNode | None) -> list[int]:
    # Problem 6: N-ary Tree Postorder Traversal
    # Key idea: preorder with children left-to-right, then reverse the visit order.
    # Time:
    # Space:

    raise NotImplementedError


def nary_level_order(root: NaryNode | None) -> list[list[int]]:
    # Problem 7: N-ary Tree Level Order Traversal
    # Key idea: BFS a queue level by level, extending with each node's children list.
    # Time:
    # Space:

    raise NotImplementedError


def max_depth_nary(root: NaryNode | None) -> int:
    # Problem 8: Maximum Depth of N-ary Tree
    # Key idea: one plus the max depth over all children, zero for an empty tree.
    # Time:
    # Space:

    raise NotImplementedError
