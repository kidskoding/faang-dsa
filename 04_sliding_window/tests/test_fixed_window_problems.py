from problem_set.fixed_window_problems import (
    find_max_average,
    max_vowels,
    num_of_subarrays,
)


def test_find_max_average_single_element():
    assert find_max_average([5], 1) == 5.0


def test_find_max_average_normal():
    assert find_max_average([1, 12, -5, -6, 50, 3], 4) == 12.75


def test_find_max_average_k_equals_one():
    assert find_max_average([0, 4, 0, 3, 2], 1) == 4.0


def test_max_vowels_normal():
    assert max_vowels("abciiidef", 3) == 3


def test_max_vowels_all_vowels():
    assert max_vowels("aeiou", 2) == 2


def test_max_vowels_spread_out():
    assert max_vowels("leetcode", 3) == 2


def test_max_vowels_no_vowels():
    assert max_vowels("bcdfg", 2) == 0


def test_num_of_subarrays_normal():
    assert num_of_subarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4) == 3


def test_num_of_subarrays_mostly_qualifying():
    assert num_of_subarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5) == 6


def test_num_of_subarrays_none_qualify():
    assert num_of_subarrays([1, 1, 1, 1], 2, 5) == 0
