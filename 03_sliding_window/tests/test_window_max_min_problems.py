from problem_set.window_max_min_problems import max_sliding_window


def test_max_sliding_window_single_element():
    assert max_sliding_window([1], 1) == [1]


def test_max_sliding_window_normal():
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_max_sliding_window_k_equals_length():
    assert max_sliding_window([9, 11], 2) == [11]


def test_max_sliding_window_decreasing():
    assert max_sliding_window([4, 3, 2, 1], 2) == [4, 3, 2]
