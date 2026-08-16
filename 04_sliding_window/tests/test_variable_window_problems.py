from problem_set.variable_window_problems import (
    equal_substring,
    length_of_longest_substring,
    longest_nice_subarray,
    longest_ones,
    longest_subarray,
    max_frequency,
    max_profit,
    maximum_unique_subarray,
    min_sub_array_len,
    num_subarray_product_less_than_k,
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


def test_longest_subarray_one_zero():
    assert longest_subarray([1, 1, 0, 1]) == 3


def test_longest_subarray_multiple_zeros():
    assert longest_subarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5


def test_longest_subarray_all_ones_still_deletes_one():
    assert longest_subarray([1, 1, 1]) == 2


def test_num_subarray_product_less_than_k_normal():
    assert num_subarray_product_less_than_k([10, 5, 2, 6], 100) == 8


def test_equal_substring_full_budget():
    assert equal_substring("abcd", "bcdf", 3) == 3


def test_equal_substring_tight_budget():
    assert equal_substring("abcd", "cdef", 3) == 1


def test_equal_substring_zero_budget():
    assert equal_substring("abcd", "acde", 0) == 1


def test_maximum_unique_subarray_normal():
    assert maximum_unique_subarray([4, 2, 4, 5, 6]) == 17


def test_maximum_unique_subarray_repeating():
    assert maximum_unique_subarray([5, 2, 1, 2, 5, 2, 1, 2, 5]) == 8


def test_max_frequency_all_equal():
    assert max_frequency([1, 2, 4], 5) == 3


def test_max_frequency_limited():
    assert max_frequency([1, 4, 8, 13], 5) == 2


def test_max_frequency_no_moves_help():
    assert max_frequency([3, 9, 6], 2) == 1


def test_longest_nice_subarray_normal():
    assert longest_nice_subarray([1, 3, 8, 48, 10]) == 3


def test_longest_nice_subarray_all_overlap():
    assert longest_nice_subarray([3, 1, 5, 11, 13]) == 1
