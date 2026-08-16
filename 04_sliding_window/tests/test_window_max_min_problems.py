from problem_set.window_max_min_problems import (
    longest_subarray_within_limit,
    max_sliding_window,
    min_sliding_window,
    shortest_subarray,
)


def test_max_sliding_window_single_element():
    assert max_sliding_window([1], 1) == [1]


def test_max_sliding_window_normal():
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_max_sliding_window_k_equals_length():
    assert max_sliding_window([9, 11], 2) == [11]


def test_max_sliding_window_decreasing():
    assert max_sliding_window([4, 3, 2, 1], 2) == [4, 3, 2]


def test_min_sliding_window_single_element():
    assert min_sliding_window([5], 1) == [5]


def test_min_sliding_window_normal():
    assert min_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [-1, -3, -3, -3, 3, 3]


def test_min_sliding_window_decreasing():
    assert min_sliding_window([4, 3, 2, 1], 2) == [3, 2, 1]


def test_longest_subarray_small_limit():
    assert longest_subarray_within_limit([8, 2, 4, 7], 4) == 2


def test_longest_subarray_normal():
    assert longest_subarray_within_limit([10, 1, 2, 4, 7, 2], 5) == 4


def test_longest_subarray_zero_limit():
    assert longest_subarray_within_limit([4, 2, 2, 2, 4, 4, 2, 2], 0) == 3


def test_shortest_subarray_single():
    assert shortest_subarray([1], 1) == 1


def test_shortest_subarray_impossible():
    assert shortest_subarray([1, 2], 4) == -1


def test_shortest_subarray_with_negative():
    assert shortest_subarray([2, -1, 2], 3) == 3


def test_shortest_subarray_normal():
    assert shortest_subarray([84, -37, 32, 40, 95], 167) == 3
