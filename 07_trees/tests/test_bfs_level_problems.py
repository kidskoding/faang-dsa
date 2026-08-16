from binary_tree import build_tree_from_level_order
from problem_set.bfs_level_problems import (
    average_of_levels,
    connect,
    distance_k,
    find_bottom_left_value,
    is_cousins,
    level_order,
    minimum_depth,
    right_side_view,
    vertical_traversal,
    width_of_binary_tree,
    zigzag_level_order,
)
from tree_node import TreeNode


def build_sample_tree() -> TreeNode:
    return TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3, right=TreeNode(6)),
    )


def test_level_order_empty_tree():
    assert level_order(None) == []


def test_level_order_single_node():
    assert level_order(TreeNode(1)) == [[1]]


def test_level_order_sample_tree():
    assert level_order(build_sample_tree()) == [[1], [2, 3], [4, 5, 6]]


def test_level_order_left_skewed_tree():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))

    assert level_order(root) == [[1], [2], [3]]


def test_right_side_view_empty_tree():
    assert right_side_view(None) == []


def test_right_side_view_sample_tree():
    assert right_side_view(build_sample_tree()) == [1, 3, 6]


def test_right_side_view_left_skewed_tree():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))

    assert right_side_view(root) == [1, 2, 3]


def test_minimum_depth_empty_tree():
    assert minimum_depth(None) == 0


def test_minimum_depth_single_node():
    assert minimum_depth(TreeNode(1)) == 1


def test_minimum_depth_sample_tree():
    assert minimum_depth(build_sample_tree()) == 3


def test_minimum_depth_left_skewed_tree():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))

    assert minimum_depth(root) == 3


def test_average_of_levels_empty_tree():
    assert average_of_levels(None) == []


def test_average_of_levels_sample_tree():
    assert average_of_levels(build_sample_tree()) == [1.0, 2.5, 5.0]


def test_average_of_levels_left_skewed_tree():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))

    assert average_of_levels(root) == [1.0, 2.0, 3.0]


def test_zigzag_level_order_empty_tree():
    assert zigzag_level_order(None) == []


def test_zigzag_level_order_single_node():
    assert zigzag_level_order(TreeNode(1)) == [[1]]


def test_zigzag_level_order_sample_tree():
    assert zigzag_level_order(build_sample_tree()) == [[1], [3, 2], [4, 5, 6]]


def test_zigzag_level_order_left_skewed_tree():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))

    assert zigzag_level_order(root) == [[1], [2], [3]]


def test_connect_links_each_level():
    root = connect(build_tree_from_level_order([1, 2, 3, 4, 5, 6, 7]))

    assert root.next is None
    assert root.left.next.val == 3
    assert root.right.next is None
    assert root.left.left.next.val == 5


def test_connect_empty_tree():
    assert connect(None) is None


def test_vertical_traversal_normal():
    root = build_tree_from_level_order([3, 9, 20, None, None, 15, 7])
    assert vertical_traversal(root) == [[9], [3, 15], [20], [7]]


def test_vertical_traversal_sorts_ties_by_value():
    root = build_tree_from_level_order([1, 2, 3, 4, 5, 6, 7])
    assert vertical_traversal(root) == [[4], [2], [1, 5, 6], [3], [7]]


def test_distance_k_normal():
    root = build_tree_from_level_order([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    assert sorted(distance_k(root, root.left, 2)) == [1, 4, 7]


def test_distance_k_zero_is_the_target():
    root = build_tree_from_level_order([1])
    assert distance_k(root, root, 0) == [1]


def test_distance_k_beyond_tree():
    root = build_tree_from_level_order([1])
    assert distance_k(root, root, 3) == []


def test_width_of_binary_tree_with_gaps():
    root = build_tree_from_level_order([1, 3, 2, 5, 3, None, 9])
    assert width_of_binary_tree(root) == 4


def test_width_of_binary_tree_left_heavy():
    assert width_of_binary_tree(build_tree_from_level_order([1, 3, 2, 5])) == 2


def test_width_of_binary_tree_single_node():
    assert width_of_binary_tree(build_tree_from_level_order([1])) == 1


def test_find_bottom_left_value_simple():
    assert find_bottom_left_value(build_tree_from_level_order([2, 1, 3])) == 1


def test_find_bottom_left_value_deeper():
    root = build_tree_from_level_order([1, 2, 3, 4, None, 5, 6, None, None, 7])
    assert find_bottom_left_value(root) == 7


def test_is_cousins_same_parent():
    assert is_cousins(build_tree_from_level_order([1, 2, 3, 4]), 4, 3) is False


def test_is_cousins_true():
    root = build_tree_from_level_order([1, 2, 3, None, 4, None, 5])
    assert is_cousins(root, 5, 4) is True


def test_is_cousins_siblings():
    assert is_cousins(build_tree_from_level_order([1, 2, 3, None, 4]), 2, 3) is False
