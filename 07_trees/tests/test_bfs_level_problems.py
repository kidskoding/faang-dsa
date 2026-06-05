from problem_set.bfs_level_problems import (
    average_of_levels,
    level_order,
    minimum_depth,
    right_side_view,
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
