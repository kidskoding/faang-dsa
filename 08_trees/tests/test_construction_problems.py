from problem_set.construction_problems import (
    construct_from_inorder_postorder,
    construct_from_preorder_inorder,
    deserialize_binary_tree,
    serialize_binary_tree,
)


def test_construction_problem_functions_are_importable():
    assert callable(construct_from_preorder_inorder)
    assert callable(construct_from_inorder_postorder)
    assert callable(serialize_binary_tree)
    assert callable(deserialize_binary_tree)
