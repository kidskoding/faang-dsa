from problem_set.fixed_window_problems import find_max_average


def test_find_max_average_single_element():
    assert find_max_average([5], 1) == 5.0


def test_find_max_average_normal():
    assert find_max_average([1, 12, -5, -6, 50, 3], 4) == 12.75


def test_find_max_average_k_equals_one():
    assert find_max_average([0, 4, 0, 3, 2], 1) == 4.0
