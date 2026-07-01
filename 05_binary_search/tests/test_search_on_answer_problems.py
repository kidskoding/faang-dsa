from problem_set.search_on_answer_problems import (
    find_median_sorted_arrays,
    min_eating_speed,
    my_sqrt,
    ship_within_days,
    split_array,
)


def test_my_sqrt_perfect_square():
    assert my_sqrt(4) == 2


def test_my_sqrt_rounds_down():
    assert my_sqrt(8) == 2


def test_my_sqrt_zero():
    assert my_sqrt(0) == 0


def test_my_sqrt_one():
    assert my_sqrt(1) == 1


def test_min_eating_speed_basic():
    assert min_eating_speed([3, 6, 7, 11], 8) == 4


def test_min_eating_speed_exact_pile_count():
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30


def test_min_eating_speed_generous_hours():
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23


def test_min_eating_speed_single_pile():
    assert min_eating_speed([5], 1) == 5


def test_ship_within_days_basic():
    assert ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15


def test_ship_within_days_one_day():
    assert ship_within_days([3, 2, 2, 4, 1, 4], 1) == 16


def test_ship_within_days_one_per_day():
    assert ship_within_days([1, 2, 3, 1, 1], 4) == 3


def test_ship_within_days_single_package():
    assert ship_within_days([7], 1) == 7


def test_split_array_basic():
    assert split_array([7, 2, 5, 10, 8], 2) == 18


def test_split_array_single_group():
    assert split_array([1, 2, 3, 4, 5], 1) == 15


def test_split_array_groups_equal_length():
    assert split_array([1, 4, 4], 3) == 4


def test_split_array_single_element():
    assert split_array([5], 1) == 5


def test_find_median_sorted_arrays_odd_total():
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0


def test_find_median_sorted_arrays_even_total():
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5


def test_find_median_sorted_arrays_one_empty():
    assert find_median_sorted_arrays([], [1]) == 1.0


def test_find_median_sorted_arrays_both_single():
    assert find_median_sorted_arrays([2], [3]) == 2.5
