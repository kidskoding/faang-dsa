import bst
from tree_node import TreeNode


def build_bst() -> TreeNode:
    return TreeNode(
        5,
        left=TreeNode(3, left=TreeNode(2), right=TreeNode(4)),
        right=TreeNode(8, left=TreeNode(7), right=TreeNode(9)),
    )


def build_invalid_bst_with_bad_descendant() -> TreeNode:
    return TreeNode(
        5,
        left=TreeNode(3, left=TreeNode(2), right=TreeNode(6)),
        right=TreeNode(8),
    )


def test_search_empty_tree_returns_none():
    assert bst.search(None, 10) is None


def test_search_finds_root():
    root = build_bst()

    assert bst.search(root, 5) is root


def test_search_finds_leaf():
    root = build_bst()

    found = bst.search(root, 7)

    assert found is not None
    assert found.val == 7


def test_search_missing_value_returns_none():
    assert bst.search(build_bst(), 6) is None


def test_contains_empty_tree_returns_false():
    assert not bst.contains(None, 1)


def test_contains_existing_value_returns_true():
    assert bst.contains(build_bst(), 4)


def test_contains_missing_value_returns_false():
    assert not bst.contains(build_bst(), 10)


def test_insert_into_empty_tree_creates_root():
    root = bst.insert(None, 5)

    assert root.val == 5
    assert root.left is None
    assert root.right is None


def test_insert_smaller_value_goes_left():
    root = TreeNode(5)

    result = bst.insert(root, 3)

    assert result is root
    assert root.left is not None
    assert root.left.val == 3


def test_insert_larger_value_goes_right():
    root = TreeNode(5)

    result = bst.insert(root, 8)

    assert result is root
    assert root.right is not None
    assert root.right.val == 8


def test_insert_preserves_inorder_sorted_order():
    root = None
    for value in [5, 3, 8, 2, 4, 7, 9]:
        root = bst.insert(root, value)

    assert bst.inorder_values(root) == [2, 3, 4, 5, 7, 8, 9]


def test_min_value_node_empty_tree_returns_none():
    assert bst.min_value_node(None) is None


def test_min_value_node_returns_leftmost_node():
    found = bst.min_value_node(build_bst())

    assert found is not None
    assert found.val == 2


def test_max_value_node_empty_tree_returns_none():
    assert bst.max_value_node(None) is None


def test_max_value_node_returns_rightmost_node():
    found = bst.max_value_node(build_bst())

    assert found is not None
    assert found.val == 9


def test_inorder_values_empty_tree_returns_empty_list():
    assert bst.inorder_values(None) == []


def test_inorder_values_returns_sorted_values():
    assert bst.inorder_values(build_bst()) == [2, 3, 4, 5, 7, 8, 9]


def test_is_valid_bst_empty_tree_returns_true():
    assert bst.is_valid_bst(None)


def test_is_valid_bst_valid_tree_returns_true():
    assert bst.is_valid_bst(build_bst())


def test_is_valid_bst_rejects_bad_descendant():
    assert not bst.is_valid_bst(build_invalid_bst_with_bad_descendant())


def test_is_valid_bst_rejects_duplicate_value():
    root = TreeNode(5, left=TreeNode(5))

    assert not bst.is_valid_bst(root)


def test_delete_missing_value_leaves_tree_unchanged():
    root = build_bst()

    result = bst.delete(root, 100)

    assert result is root
    assert bst.inorder_values(result) == [2, 3, 4, 5, 7, 8, 9]


def test_delete_leaf_node():
    root = bst.delete(build_bst(), 2)

    assert bst.inorder_values(root) == [3, 4, 5, 7, 8, 9]


def test_delete_node_with_one_child():
    root = TreeNode(5, left=TreeNode(3, left=TreeNode(2)), right=TreeNode(8))

    result = bst.delete(root, 3)

    assert bst.inorder_values(result) == [2, 5, 8]


def test_delete_node_with_two_children():
    root = bst.delete(build_bst(), 3)

    assert bst.inorder_values(root) == [2, 4, 5, 7, 8, 9]
    assert bst.is_valid_bst(root)


def test_delete_root_node_with_two_children():
    root = bst.delete(build_bst(), 5)

    assert bst.inorder_values(root) == [2, 3, 4, 7, 8, 9]
    assert bst.is_valid_bst(root)
