from problem_set.monotonic_queue_problems import max_sliding_window


def test_max_sliding_window_normal_case():
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_max_sliding_window_empty():
    assert max_sliding_window([], 0) == []


def test_max_sliding_window_single_element():
    assert max_sliding_window([5], 1) == [5]


def test_max_sliding_window_k_equals_length():
    assert max_sliding_window([4, 2, 8], 3) == [8]


def test_max_sliding_window_decreasing_values():
    assert max_sliding_window([9, 8, 7, 6], 2) == [9, 8, 7]
