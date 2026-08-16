from binary_tree import build_tree_from_level_order
from problem_set.tree_traversal_problems import (
    BSTIterator,
    NaryNode,
    inorder_traversal,
    max_depth_nary,
    nary_level_order,
    nary_postorder,
    nary_preorder,
    postorder_traversal,
    preorder_traversal,
)
from tree_node import TreeNode


def build_sample_tree() -> TreeNode:
    return TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3, right=TreeNode(6)),
    )


def build_sample_nary_tree() -> NaryNode:
    return NaryNode(1, [NaryNode(3, [NaryNode(5), NaryNode(6)]), NaryNode(2), NaryNode(4)])


def test_inorder_traversal_sample_tree():
    assert inorder_traversal(build_sample_tree()) == [4, 2, 5, 1, 3, 6]


def test_inorder_traversal_empty():
    assert inorder_traversal(None) == []


def test_inorder_traversal_single_node():
    assert inorder_traversal(TreeNode(1)) == [1]


def test_preorder_traversal_sample_tree():
    assert preorder_traversal(build_sample_tree()) == [1, 2, 4, 5, 3, 6]


def test_preorder_traversal_empty():
    assert preorder_traversal(None) == []


def test_postorder_traversal_sample_tree():
    assert postorder_traversal(build_sample_tree()) == [4, 5, 2, 6, 3, 1]


def test_postorder_traversal_empty():
    assert postorder_traversal(None) == []


def test_bst_iterator_walks_in_order():
    root = build_tree_from_level_order([7, 3, 15, None, None, 9, 20])
    iterator = BSTIterator(root)

    assert iterator.next() == 3
    assert iterator.next() == 7
    assert iterator.has_next() is True
    assert iterator.next() == 9
    assert iterator.next() == 15
    assert iterator.has_next() is True


def test_bst_iterator_exhausts():
    iterator = BSTIterator(TreeNode(1))

    assert iterator.next() == 1
    assert iterator.has_next() is False


def test_nary_preorder_sample_tree():
    assert nary_preorder(build_sample_nary_tree()) == [1, 3, 5, 6, 2, 4]


def test_nary_preorder_empty():
    assert nary_preorder(None) == []


def test_nary_postorder_sample_tree():
    assert nary_postorder(build_sample_nary_tree()) == [5, 6, 3, 2, 4, 1]


def test_nary_postorder_empty():
    assert nary_postorder(None) == []


def test_nary_level_order_sample_tree():
    assert nary_level_order(build_sample_nary_tree()) == [[1], [3, 2, 4], [5, 6]]


def test_nary_level_order_empty():
    assert nary_level_order(None) == []


def test_max_depth_nary_sample_tree():
    assert max_depth_nary(build_sample_nary_tree()) == 3


def test_max_depth_nary_empty():
    assert max_depth_nary(None) == 0


def test_max_depth_nary_single_node():
    assert max_depth_nary(NaryNode(1)) == 1
