from problem_set.variable_window_problems import (
    length_of_longest_substring,
    longest_ones,
    max_profit,
    min_sub_array_len,
)


def test_max_profit_empty():
    assert max_profit([]) == 0


def test_max_profit_single_price():
    assert max_profit([5]) == 0


def test_max_profit_normal():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5


def test_max_profit_no_profit():
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_length_of_longest_substring_empty():
    assert length_of_longest_substring("") == 0


def test_length_of_longest_substring_single():
    assert length_of_longest_substring("a") == 1


def test_length_of_longest_substring_normal():
    assert length_of_longest_substring("abcabcbb") == 3


def test_length_of_longest_substring_all_repeats():
    assert length_of_longest_substring("bbbbb") == 1


def test_min_sub_array_len_empty():
    assert min_sub_array_len(7, []) == 0


def test_min_sub_array_len_single_meets_target():
    assert min_sub_array_len(4, [4]) == 1


def test_min_sub_array_len_normal():
    assert min_sub_array_len(7, [2, 3, 1, 2, 4, 3]) == 2


def test_min_sub_array_len_no_valid_subarray():
    assert min_sub_array_len(100, [1, 2, 3]) == 0


def test_longest_ones_single_element():
    assert longest_ones([1], 0) == 1


def test_longest_ones_normal():
    assert longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6


def test_longest_ones_no_flips_allowed():
    assert longest_ones([1, 0, 1, 1, 0], 0) == 2


def test_longest_ones_all_ones():
    assert longest_ones([1, 1, 1], 2) == 3
