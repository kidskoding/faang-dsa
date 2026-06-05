from problem_set.bst_problems import (
    convert_sorted_array_to_bst,
    delete_node_bst,
    insert_into_bst,
    kth_smallest,
    lowest_common_ancestor_bst,
    search_in_bst,
    search_range_bst,
    trim_bst,
    validate_bst,
)


def test_bst_problem_functions_are_importable():
    assert callable(search_in_bst)
    assert callable(validate_bst)
    assert callable(kth_smallest)
    assert callable(lowest_common_ancestor_bst)
    assert callable(convert_sorted_array_to_bst)
    assert callable(insert_into_bst)
    assert callable(delete_node_bst)
    assert callable(search_range_bst)
    assert callable(trim_bst)
