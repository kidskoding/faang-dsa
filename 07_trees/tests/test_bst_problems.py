from binary_tree import build_tree_from_level_order
from problem_set.bst_problems import (
    convert_bst,
    convert_sorted_array_to_bst,
    delete_node_bst,
    inorder_successor,
    insert_into_bst,
    kth_smallest,
    lowest_common_ancestor_bst,
    range_sum_bst,
    recover_tree,
    search_in_bst,
    trim_bst,
    validate_bst,
)
from problem_set.tree_traversal_problems import inorder_traversal, preorder_traversal
from tree_node import TreeNode


def test_search_in_bst_found():
    root = build_tree_from_level_order([4, 2, 7, 1, 3])
    assert preorder_traversal(search_in_bst(root, 2)) == [2, 1, 3]


def test_search_in_bst_missing():
    root = build_tree_from_level_order([4, 2, 7, 1, 3])
    assert search_in_bst(root, 5) is None


def test_validate_bst_valid():
    assert validate_bst(build_tree_from_level_order([2, 1, 3])) is True


def test_validate_bst_invalid_grandchild():
    assert validate_bst(build_tree_from_level_order([5, 1, 4, None, None, 3, 6])) is False


def test_validate_bst_left_child_too_large():
    assert validate_bst(build_tree_from_level_order([5, 4, 6, None, None, 3, 7])) is False


def test_validate_bst_empty():
    assert validate_bst(None) is True


def test_kth_smallest_first():
    assert kth_smallest(build_tree_from_level_order([3, 1, 4, None, 2]), 1) == 1


def test_kth_smallest_middle():
    root = build_tree_from_level_order([5, 3, 6, 2, 4, None, None, 1])
    assert kth_smallest(root, 3) == 3


def test_lowest_common_ancestor_bst_split():
    root = build_tree_from_level_order([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert lowest_common_ancestor_bst(root, root.left, root.right).val == 6


def test_lowest_common_ancestor_bst_ancestor_is_node():
    root = build_tree_from_level_order([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert lowest_common_ancestor_bst(root, root.left, root.left.right).val == 2


def test_range_sum_bst_normal():
    root = build_tree_from_level_order([10, 5, 15, 3, 7, None, 18])
    assert range_sum_bst(root, 7, 15) == 32


def test_range_sum_bst_deeper_tree():
    root = build_tree_from_level_order([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
    assert range_sum_bst(root, 6, 10) == 23


def test_convert_sorted_array_to_bst_is_a_bst():
    assert inorder_traversal(convert_sorted_array_to_bst([-10, -3, 0, 5, 9])) == [
        -10,
        -3,
        0,
        5,
        9,
    ]


def test_convert_sorted_array_to_bst_empty():
    assert convert_sorted_array_to_bst([]) is None


def test_insert_into_bst_normal():
    root = build_tree_from_level_order([4, 2, 7, 1, 3])
    assert inorder_traversal(insert_into_bst(root, 5)) == [1, 2, 3, 4, 5, 7]


def test_insert_into_bst_empty():
    assert inorder_traversal(insert_into_bst(None, 5)) == [5]


def test_delete_node_bst_node_with_two_children():
    root = build_tree_from_level_order([5, 3, 6, 2, 4, None, 7])
    assert inorder_traversal(delete_node_bst(root, 3)) == [2, 4, 5, 6, 7]


def test_delete_node_bst_missing_key():
    root = build_tree_from_level_order([5, 3, 6, 2, 4, None, 7])
    assert inorder_traversal(delete_node_bst(root, 0)) == [2, 3, 4, 5, 6, 7]


def test_trim_bst_drops_low_value():
    assert inorder_traversal(trim_bst(build_tree_from_level_order([1, 0, 2]), 1, 2)) == [1, 2]


def test_trim_bst_keeps_nested_survivor():
    root = build_tree_from_level_order([3, 0, 4, None, 2, None, None, 1])
    assert inorder_traversal(trim_bst(root, 1, 3)) == [1, 2, 3]


def test_inorder_successor_exists():
    root = build_tree_from_level_order([2, 1, 3])
    assert inorder_successor(root, root.left).val == 2


def test_inorder_successor_of_largest_is_none():
    root = build_tree_from_level_order([2, 1, 3])
    assert inorder_successor(root, root.right) is None


def test_recover_tree_swapped_neighbours():
    root = build_tree_from_level_order([1, 3, None, None, 2])
    recover_tree(root)
    assert inorder_traversal(root) == [1, 2, 3]


def test_recover_tree_swapped_non_neighbours():
    root = build_tree_from_level_order([3, 1, 4, None, None, 2])
    recover_tree(root)
    assert inorder_traversal(root) == [1, 2, 3, 4]


def test_convert_bst_accumulates_greater_values():
    root = build_tree_from_level_order([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
    assert inorder_traversal(convert_bst(root)) == [36, 36, 35, 33, 30, 26, 21, 15, 8]


def test_convert_bst_single_node():
    assert inorder_traversal(convert_bst(TreeNode(5))) == [5]
