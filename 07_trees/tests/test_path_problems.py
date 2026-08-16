from binary_tree import build_tree_from_level_order
from problem_set.path_problems import (
    binary_tree_paths,
    good_nodes,
    path_sum,
    path_sum_ii,
    path_sum_iii,
    sum_root_to_leaf_numbers,
)
from tree_node import TreeNode


def build_sample_tree() -> TreeNode:
    return TreeNode(
        5,
        left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))),
        right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, right=TreeNode(1))),
    )


def build_small_path_tree() -> TreeNode:
    return TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)),
    )


def build_path_sum_ii_tree() -> TreeNode:
    return TreeNode(
        5,
        left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))),
        right=TreeNode(
            8,
            left=TreeNode(13),
            right=TreeNode(4, left=TreeNode(5), right=TreeNode(1)),
        ),
    )


def test_path_sum_empty_tree():
    assert not path_sum(None, 0)


def test_path_sum_single_node_true():
    assert path_sum(TreeNode(5), 5)


def test_path_sum_single_node_false():
    assert not path_sum(TreeNode(5), 7)


def test_path_sum_sample_tree_true():
    assert path_sum(build_sample_tree(), 22)


def test_path_sum_sample_tree_false():
    assert not path_sum(build_sample_tree(), 24)


def test_path_sum_partial_path_does_not_count():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))

    assert not path_sum(root, 3)


def test_path_sum_with_negative_values():
    root = TreeNode(-2, right=TreeNode(-3))

    assert path_sum(root, -5)


def test_path_sum_ii_empty_tree():
    assert path_sum_ii(None, 0) == []


def test_path_sum_ii_single_valid_path():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))

    assert path_sum_ii(root, 6) == [[1, 2, 3]]


def test_path_sum_ii_multiple_paths():
    root = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4)),
        right=TreeNode(3, right=TreeNode(3)),
    )

    assert sorted(path_sum_ii(root, 7)) == [[1, 2, 4], [1, 3, 3]]


def test_path_sum_ii_no_valid_path():
    root = build_small_path_tree()

    assert path_sum_ii(root, 100) == []


def test_path_sum_ii_leetcode_sample_tree():
    assert sorted(path_sum_ii(build_path_sum_ii_tree(), 22)) == [
        [5, 4, 11, 2],
        [5, 8, 4, 5],
    ]


def test_path_sum_ii_partial_path_does_not_count():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))

    assert path_sum_ii(root, 3) == []


def test_path_sum_ii_handles_negative_values():
    root = TreeNode(1, left=TreeNode(-2, left=TreeNode(1)), right=TreeNode(-3))

    assert path_sum_ii(root, 0) == [[1, -2, 1]]


def test_binary_tree_paths_empty_tree():
    assert binary_tree_paths(None) == []


def test_binary_tree_paths_single_node():
    assert binary_tree_paths(TreeNode(1)) == ["1"]


def test_binary_tree_paths_sample_tree():
    root = TreeNode(1, left=TreeNode(2, right=TreeNode(5)), right=TreeNode(3))

    assert binary_tree_paths(root) == ["1->2->5", "1->3"]


def test_binary_tree_paths_left_skewed_tree():
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))

    assert binary_tree_paths(root) == ["1->2->3"]


def test_binary_tree_paths_multiple_leaves():
    assert binary_tree_paths(build_small_path_tree()) == [
        "1->2->4",
        "1->2->5",
        "1->3->6",
        "1->3->7",
    ]


def test_sum_root_to_leaf_numbers_empty_tree():
    assert sum_root_to_leaf_numbers(None) == 0


def test_sum_root_to_leaf_numbers_single_node():
    assert sum_root_to_leaf_numbers(TreeNode(7)) == 7


def test_sum_root_to_leaf_numbers_two_paths():
    root = TreeNode(1, left=TreeNode(2), right=TreeNode(3))

    assert sum_root_to_leaf_numbers(root) == 25


def test_sum_root_to_leaf_numbers_multi_digit_paths():
    root = TreeNode(
        4,
        left=TreeNode(9, left=TreeNode(5), right=TreeNode(1)),
        right=TreeNode(0),
    )

    assert sum_root_to_leaf_numbers(root) == 1026


def test_sum_root_to_leaf_numbers_skewed_tree():
    root = TreeNode(1, right=TreeNode(0, right=TreeNode(5)))

    assert sum_root_to_leaf_numbers(root) == 105


def test_good_nodes_normal():
    assert good_nodes(build_tree_from_level_order([3, 1, 4, 3, None, 1, 5])) == 4


def test_good_nodes_left_child_equal():
    assert good_nodes(build_tree_from_level_order([3, 3, None, 4, 2])) == 3


def test_good_nodes_single_node():
    assert good_nodes(build_tree_from_level_order([1])) == 1


def test_path_sum_iii_normal():
    root = build_tree_from_level_order([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    assert path_sum_iii(root, 8) == 3


def test_path_sum_iii_deeper_tree():
    root = build_tree_from_level_order([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    assert path_sum_iii(root, 22) == 3
