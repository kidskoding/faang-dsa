from binary_tree import build_tree_from_level_order, tree_to_level_order
from problem_set.recursive_shape_problems import (
    balanced_binary_tree,
    diameter_of_binary_tree,
    flatten,
    invert_tree,
    lca_deepest_leaves,
    lowest_common_ancestor,
    max_depth,
    max_path_sum,
    prune_tree,
    same_tree,
    subtree_of_another_tree,
    symmetric_tree,
)
from problem_set.tree_traversal_problems import preorder_traversal
from tree_node import TreeNode


def test_max_depth_empty_tree():
    assert max_depth(None) == 0


def test_max_depth_single_node():
    assert max_depth(TreeNode(1)) == 1


def test_max_depth_balanced_tree():
    root = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3),
    )

    assert max_depth(root) == 3


def test_max_depth_skewed_tree():
    root = TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4))))

    assert max_depth(root) == 4


def test_invert_tree_empty_tree():
    assert invert_tree(None) is None


def test_invert_tree_single_node():
    root = TreeNode(1)

    assert invert_tree(root) is root
    assert tree_to_level_order(root) == [1]


def test_invert_tree_complete_tree():
    root = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)),
    )

    assert invert_tree(root) is root
    assert tree_to_level_order(root) == [1, 3, 2, 7, 6, 5, 4]


def test_invert_tree_sparse_tree():
    root = TreeNode(1, left=TreeNode(2, right=TreeNode(3)))

    assert invert_tree(root) is root
    assert tree_to_level_order(root) == [1, None, 2, 3]


def test_same_tree_both_empty():
    assert same_tree(None, None)


def test_same_tree_one_empty():
    assert not same_tree(TreeNode(1), None)
    assert not same_tree(None, TreeNode(1))


def test_same_tree_identical_trees():
    p = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    q = TreeNode(1, left=TreeNode(2), right=TreeNode(3))

    assert same_tree(p, q)


def test_same_tree_different_values():
    p = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    q = TreeNode(1, left=TreeNode(2), right=TreeNode(4))

    assert not same_tree(p, q)


def test_same_tree_different_shapes():
    p = TreeNode(1, left=TreeNode(2))
    q = TreeNode(1, right=TreeNode(2))

    assert not same_tree(p, q)


def test_symmetric_tree_empty_tree():
    assert symmetric_tree(None)


def test_symmetric_tree_single_node():
    assert symmetric_tree(TreeNode(1))


def test_symmetric_tree_mirror_shape():
    root = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
        right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)),
    )

    assert symmetric_tree(root)


def test_symmetric_tree_same_values_wrong_shape():
    root = TreeNode(
        1,
        left=TreeNode(2, right=TreeNode(3)),
        right=TreeNode(2, right=TreeNode(3)),
    )

    assert not symmetric_tree(root)


def test_balanced_binary_tree_empty_tree():
    assert balanced_binary_tree(None)


def test_balanced_binary_tree_balanced_tree():
    root = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3),
    )

    assert balanced_binary_tree(root)


def test_balanced_binary_tree_unbalanced_tree():
    root = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(3, left=TreeNode(4))),
        right=TreeNode(5),
    )

    assert not balanced_binary_tree(root)


def test_diameter_of_binary_tree_empty_tree():
    assert diameter_of_binary_tree(None) == 0


def test_diameter_of_binary_tree_single_node():
    assert diameter_of_binary_tree(TreeNode(1)) == 0


def test_diameter_of_binary_tree_through_root():
    root = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3),
    )

    assert diameter_of_binary_tree(root) == 3


def test_diameter_of_binary_tree_not_through_root():
    root = TreeNode(
        1,
        left=TreeNode(
            2,
            left=TreeNode(4, left=TreeNode(6)),
            right=TreeNode(5, right=TreeNode(7)),
        ),
    )

    assert diameter_of_binary_tree(root) == 4


def test_subtree_of_another_tree_identical_tree():
    root = TreeNode(1, left=TreeNode(2), right=TreeNode(3))

    assert subtree_of_another_tree(root, root)


def test_subtree_of_another_tree_nested_match():
    root = TreeNode(
        3,
        left=TreeNode(4, left=TreeNode(1), right=TreeNode(2)),
        right=TreeNode(5),
    )
    subroot = TreeNode(4, left=TreeNode(1), right=TreeNode(2))

    assert subtree_of_another_tree(root, subroot)


def test_subtree_of_another_tree_same_values_extra_node():
    root = TreeNode(
        3,
        left=TreeNode(4, left=TreeNode(1), right=TreeNode(2, left=TreeNode(0))),
        right=TreeNode(5),
    )
    subroot = TreeNode(4, left=TreeNode(1), right=TreeNode(2))

    assert not subtree_of_another_tree(root, subroot)


def test_subtree_of_another_tree_empty_subroot():
    assert subtree_of_another_tree(TreeNode(1), None)


def test_subtree_of_another_tree_empty_root_nonempty_subroot():
    assert not subtree_of_another_tree(None, TreeNode(1))


def test_lowest_common_ancestor_split():
    root = build_tree_from_level_order([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    assert lowest_common_ancestor(root, root.left, root.right).val == 3


def test_lowest_common_ancestor_node_is_its_own_ancestor():
    root = build_tree_from_level_order([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    assert lowest_common_ancestor(root, root.left, root.left.right.right).val == 5


def test_prune_tree_drops_zero_only_subtrees():
    root = build_tree_from_level_order([1, None, 0, 0, 1])
    assert preorder_traversal(prune_tree(root)) == [1, 0, 1]


def test_prune_tree_removes_everything():
    assert prune_tree(TreeNode(0)) is None


def test_flatten_produces_right_leaning_list():
    root = build_tree_from_level_order([1, 2, 5, 3, 4, None, 6])
    flatten(root)

    assert preorder_traversal(root) == [1, 2, 3, 4, 5, 6]
    assert root.left is None


def test_flatten_empty():
    assert flatten(None) is None


def test_lca_deepest_leaves_normal():
    root = build_tree_from_level_order([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    assert lca_deepest_leaves(root).val == 2


def test_lca_deepest_leaves_single_node():
    assert lca_deepest_leaves(TreeNode(1)).val == 1


def test_max_path_sum_all_positive():
    assert max_path_sum(build_tree_from_level_order([1, 2, 3])) == 6


def test_max_path_sum_skips_negative_root():
    root = build_tree_from_level_order([-10, 9, 20, None, None, 15, 7])
    assert max_path_sum(root) == 42


def test_max_path_sum_single_negative_node():
    assert max_path_sum(TreeNode(-3)) == -3
