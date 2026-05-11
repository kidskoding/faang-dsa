from tree_node import TreeNode
from binary_tree import (
    build_tree_from_level_order,
    count_nodes,
    height,
    is_leaf,
    tree_to_level_order,
)


def test_tree_node_defaults_to_no_children():
    node = TreeNode(10)

    assert node.val == 10
    assert node.left is None
    assert node.right is None


def test_tree_node_accepts_children():
    left = TreeNode(5)
    right = TreeNode(15)
    root = TreeNode(10, left=left, right=right)

    assert root.val == 10
    assert root.left is left
    assert root.right is right


def test_is_leaf_returns_true_for_node_without_children():
    assert is_leaf(TreeNode(1))


def test_is_leaf_returns_false_for_left_child_only():
    root = TreeNode(1, left=TreeNode(2))

    assert not is_leaf(root)


def test_is_leaf_returns_false_for_right_child_only():
    root = TreeNode(1, right=TreeNode(2))

    assert not is_leaf(root)


def test_height_of_empty_tree_is_zero():
    assert height(None) == 0


def test_height_of_single_node_tree_is_one():
    assert height(TreeNode(1)) == 1


def test_height_of_balanced_tree():
    root = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3),
    )

    assert height(root) == 3


def test_height_of_left_skewed_tree():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3, left=TreeNode(4))))

    assert height(root) == 4


def test_height_of_right_skewed_tree():
    root = TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4))))

    assert height(root) == 4


def test_count_nodes_empty_tree_is_zero():
    assert count_nodes(None) == 0


def test_count_nodes_single_node_tree_is_one():
    assert count_nodes(TreeNode(1)) == 1


def test_count_nodes_balanced_tree():
    root = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)),
    )

    assert count_nodes(root) == 7


def test_count_nodes_sparse_tree():
    root = TreeNode(
        1,
        left=TreeNode(2, right=TreeNode(4)),
        right=TreeNode(3, left=TreeNode(5)),
    )

    assert count_nodes(root) == 5


def test_basic_tree_helpers():
    root = TreeNode(
        1,
        left=TreeNode(2),
        right=TreeNode(3, left=TreeNode(4)),
    )

    assert height(root) == 3
    assert count_nodes(root) == 4
    assert is_leaf(root.left)
    assert not is_leaf(root)


def test_build_tree_from_empty_level_order_returns_none():
    assert build_tree_from_level_order([]) is None


def test_build_tree_from_none_root_returns_none():
    assert build_tree_from_level_order([None]) is None


def test_build_tree_from_single_value():
    root = build_tree_from_level_order([1])

    assert root is not None
    assert root.val == 1
    assert root.left is None
    assert root.right is None


def test_build_tree_from_complete_level_order():
    root = build_tree_from_level_order([1, 2, 3, 4, 5, 6, 7])

    assert root is not None
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.left.left.val == 4
    assert root.left.right.val == 5
    assert root.right.left.val == 6
    assert root.right.right.val == 7


def test_build_tree_from_level_order_with_missing_left_child():
    root = build_tree_from_level_order([1, None, 2])

    assert root is not None
    assert root.val == 1
    assert root.left is None
    assert root.right.val == 2


def test_build_tree_from_level_order_with_missing_right_child():
    root = build_tree_from_level_order([1, 2, None])

    assert root is not None
    assert root.val == 1
    assert root.left.val == 2
    assert root.right is None


def test_build_tree_from_level_order_with_sparse_middle_level():
    root = build_tree_from_level_order([1, 2, 3, None, 4, 5, None])

    assert root is not None
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.left.left is None
    assert root.left.right.val == 4
    assert root.right.left.val == 5
    assert root.right.right is None


def test_tree_to_level_order_empty_tree():
    assert tree_to_level_order(None) == []


def test_tree_to_level_order_single_node():
    assert tree_to_level_order(TreeNode(1)) == [1]


def test_tree_to_level_order_complete_tree_trims_trailing_nones():
    root = TreeNode(
        1,
        left=TreeNode(2),
        right=TreeNode(3),
    )

    assert tree_to_level_order(root) == [1, 2, 3]


def test_tree_to_level_order_preserves_internal_none_for_right_child():
    root = TreeNode(1, right=TreeNode(2))

    assert tree_to_level_order(root) == [1, None, 2]


def test_tree_to_level_order_preserves_internal_none_for_sparse_tree():
    root = TreeNode(
        1,
        left=TreeNode(2, right=TreeNode(4)),
        right=TreeNode(3, left=TreeNode(5)),
    )

    assert tree_to_level_order(root) == [1, 2, 3, None, 4, 5]


def test_level_order_round_trip_with_missing_nodes():
    root = build_tree_from_level_order([1, 2, 3, None, 4])

    assert tree_to_level_order(root) == [1, 2, 3, None, 4]


def test_level_order_round_trip_complete_tree():
    values = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree_from_level_order(values)

    assert tree_to_level_order(root) == values


def test_level_order_round_trip_right_skewed_shape():
    values = [1, None, 2, None, 3, None, 4]
    root = build_tree_from_level_order(values)

    assert tree_to_level_order(root) == values


def test_level_order_round_trip_left_skewed_shape():
    values = [1, 2, None, 3, None, 4]
    root = build_tree_from_level_order(values)

    assert tree_to_level_order(root) == values


def test_empty_level_order_builds_empty_tree():
    assert build_tree_from_level_order([]) is None
    assert build_tree_from_level_order([None]) is None
    assert tree_to_level_order(None) == []
