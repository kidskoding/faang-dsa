from problem_set.fixed_window_problems import (
    contains_nearby_duplicate,
    count_good_substrings,
    find_max_average,
    max_satisfied,
    max_score,
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


def test_contains_nearby_duplicate_within_k():
    assert contains_nearby_duplicate([1, 2, 3, 1], 3) is True


def test_contains_nearby_duplicate_outside_k():
    assert contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2) is False


def test_contains_nearby_duplicate_adjacent():
    assert contains_nearby_duplicate([1, 0, 1, 1], 1) is True


def test_count_good_substrings_one():
    assert count_good_substrings("xyzzaz") == 1


def test_count_good_substrings_several():
    assert count_good_substrings("aababcabc") == 4


def test_max_satisfied_uses_window():
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]

    assert max_satisfied(customers, grumpy, 3) == 16


def test_max_satisfied_single_minute():
    assert max_satisfied([1], [0], 1) == 1


def test_max_score_takes_from_both_ends():
    assert max_score([1, 2, 3, 4, 5, 6, 1], 3) == 12


def test_max_score_takes_all():
    assert max_score([2, 2, 2], 2) == 4


def test_max_score_whole_array():
    assert max_score([9, 7, 7, 9, 7, 7, 9], 7) == 55
