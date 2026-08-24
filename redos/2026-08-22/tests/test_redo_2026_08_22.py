from redo_2026_08_22 import top_k_frequent


def test_top_k_frequent_normal():
    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}

def test_top_k_frequent_k_equals_distinct_count():
    assert sorted(top_k_frequent([1, 2, 3], 3)) == [1, 2, 3]

def test_top_k_frequent_with_negatives():
    assert set(top_k_frequent([-1, -1, -1, -2, -2, 5], 2)) == {-1, -2}
