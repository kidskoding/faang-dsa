import tree_traversals
from tree_node import TreeNode


def build_sample_tree() -> TreeNode:
    return TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3),
    )


def test_preorder_empty_tree():
    assert tree_traversals.preorder(None) == []


def test_preorder_single_node():
    assert tree_traversals.preorder(TreeNode(1)) == [1]


def test_preorder_visits_node_left_right():
    assert tree_traversals.preorder(build_sample_tree()) == [1, 2, 4, 5, 3]


def test_preorder_left_skewed_tree():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))

    assert tree_traversals.preorder(root) == [1, 2, 3]


def test_preorder_right_skewed_tree():
    root = TreeNode(1, right=TreeNode(2, right=TreeNode(3)))

    assert tree_traversals.preorder(root) == [1, 2, 3]


def test_inorder_empty_tree():
    assert tree_traversals.inorder(None) == []


def test_inorder_single_node():
    assert tree_traversals.inorder(TreeNode(1)) == [1]


def test_inorder_visits_left_node_right():
    assert tree_traversals.inorder(build_sample_tree()) == [4, 2, 5, 1, 3]


def test_inorder_left_skewed_tree():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))

    assert tree_traversals.inorder(root) == [3, 2, 1]


def test_inorder_right_skewed_tree():
    root = TreeNode(1, right=TreeNode(2, right=TreeNode(3)))

    assert tree_traversals.inorder(root) == [1, 2, 3]


def test_postorder_empty_tree():
    assert tree_traversals.postorder(None) == []


def test_postorder_single_node():
    assert tree_traversals.postorder(TreeNode(1)) == [1]


def test_postorder_visits_left_right_node():
    assert tree_traversals.postorder(build_sample_tree()) == [4, 5, 2, 3, 1]


def test_postorder_left_skewed_tree():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))

    assert tree_traversals.postorder(root) == [3, 2, 1]


def test_postorder_right_skewed_tree():
    root = TreeNode(1, right=TreeNode(2, right=TreeNode(3)))

    assert tree_traversals.postorder(root) == [3, 2, 1]
