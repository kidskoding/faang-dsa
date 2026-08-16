from problem_set.construction_problems import (
    bst_from_preorder,
    construct_from_inorder_postorder,
    construct_from_preorder_inorder,
    construct_from_preorder_postorder,
    construct_maximum_binary_tree,
    deserialize_binary_tree,
    serialize_binary_tree,
    tree_to_string,
)
from problem_set.tree_traversal_problems import inorder_traversal, preorder_traversal
from tree_node import TreeNode


def build_sample_tree() -> TreeNode:
    return TreeNode(
        1,
        left=TreeNode(2),
        right=TreeNode(3, left=TreeNode(4), right=TreeNode(5)),
    )


def test_construct_from_preorder_inorder_shape():
    root = construct_from_preorder_inorder([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert preorder_traversal(root) == [3, 9, 20, 15, 7]
    assert inorder_traversal(root) == [9, 3, 15, 20, 7]


def test_construct_from_preorder_inorder_empty():
    assert construct_from_preorder_inorder([], []) is None


def test_construct_from_inorder_postorder_shape():
    root = construct_from_inorder_postorder([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    assert preorder_traversal(root) == [3, 9, 20, 15, 7]


def test_construct_from_inorder_postorder_empty():
    assert construct_from_inorder_postorder([], []) is None


def test_construct_from_preorder_postorder_shape():
    root = construct_from_preorder_postorder([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])
    assert inorder_traversal(root) == [4, 2, 5, 1, 6, 3, 7]


def test_construct_from_preorder_postorder_single():
    assert preorder_traversal(construct_from_preorder_postorder([1], [1])) == [1]


def test_serialize_round_trips():
    root = build_sample_tree()
    restored = deserialize_binary_tree(serialize_binary_tree(root))

    assert preorder_traversal(restored) == preorder_traversal(root)
    assert inorder_traversal(restored) == inorder_traversal(root)


def test_serialize_round_trips_empty_tree():
    assert deserialize_binary_tree(serialize_binary_tree(None)) is None


def test_construct_maximum_binary_tree_normal():
    assert preorder_traversal(construct_maximum_binary_tree([3, 2, 1, 6, 0, 5])) == [
        6,
        3,
        2,
        1,
        5,
        0,
    ]


def test_construct_maximum_binary_tree_single():
    assert preorder_traversal(construct_maximum_binary_tree([1])) == [1]


def test_bst_from_preorder_keeps_preorder():
    assert preorder_traversal(bst_from_preorder([8, 5, 1, 7, 10, 12])) == [8, 5, 1, 7, 10, 12]


def test_bst_from_preorder_is_sorted_in_order():
    assert inorder_traversal(bst_from_preorder([8, 5, 1, 7, 10, 12])) == [1, 5, 7, 8, 10, 12]


def test_tree_to_string_omits_empty_right():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3))
    assert tree_to_string(root) == "1(2(4))(3)"


def test_tree_to_string_keeps_placeholder_for_empty_left():
    root = TreeNode(1, left=TreeNode(2, right=TreeNode(4)), right=TreeNode(3))
    assert tree_to_string(root) == "1(2()(4))(3)"


def test_tree_to_string_empty():
    assert tree_to_string(None) == ""
