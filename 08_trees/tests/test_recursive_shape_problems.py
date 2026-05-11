from binary_tree import tree_to_level_order
from problem_set.recursive_shape_problems import (
    balanced_binary_tree,
    diameter_of_binary_tree,
    invert_tree,
    max_depth,
    same_tree,
    subtree_of_another_tree,
    symmetric_tree,
)
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
