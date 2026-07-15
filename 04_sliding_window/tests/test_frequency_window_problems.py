from problem_set.frequency_window_problems import (
    character_replacement,
    check_inclusion,
    find_anagrams,
    length_of_longest_substring_k_distinct,
    min_window,
    number_of_subarrays,
    subarrays_with_k_distinct,
    total_fruit,
)


def test_character_replacement_single():
    assert character_replacement("A", 0) == 1


def test_character_replacement_normal():
    assert character_replacement("ABAB", 2) == 4


def test_character_replacement_normal_two():
    assert character_replacement("AABABBA", 1) == 4


def test_character_replacement_no_budget():
    assert character_replacement("ABBB", 0) == 3


def test_check_inclusion_true():
    assert check_inclusion("ab", "eidbaooo") is True


def test_check_inclusion_false():
    assert check_inclusion("ab", "eidboaoo") is False


def test_check_inclusion_match_at_end():
    assert check_inclusion("adc", "dcda") is True


def test_check_inclusion_s1_longer_than_s2():
    assert check_inclusion("abcd", "ab") is False


def test_find_anagrams_normal():
    assert find_anagrams("cbaebabacd", "abc") == [0, 6]


def test_find_anagrams_no_match():
    assert find_anagrams("abc", "xyz") == []


def test_find_anagrams_p_longer_than_s():
    assert find_anagrams("a", "ab") == []


def test_find_anagrams_full_match():
    assert find_anagrams("ab", "ab") == [0]


def test_total_fruit_single_tree():
    assert total_fruit([1]) == 1


def test_total_fruit_all_same_two_types():
    assert total_fruit([1, 2, 1]) == 3


def test_total_fruit_normal():
    assert total_fruit([0, 1, 2, 2]) == 3


def test_total_fruit_normal_two():
    assert total_fruit([1, 2, 3, 2, 2]) == 4


def test_min_window_normal():
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"


def test_min_window_no_valid_window():
    assert min_window("a", "aa") == ""


def test_min_window_no_matching_characters():
    assert min_window("a", "b") == ""


def test_min_window_exact_match():
    assert min_window("a", "a") == "a"


def test_length_of_longest_substring_k_distinct_single():
    assert length_of_longest_substring_k_distinct("a", 1) == 1


def test_length_of_longest_substring_k_distinct_normal():
    assert length_of_longest_substring_k_distinct("eceba", 2) == 3


def test_length_of_longest_substring_k_distinct_zero_k():
    assert length_of_longest_substring_k_distinct("abc", 0) == 0


def test_length_of_longest_substring_k_distinct_k_exceeds_distinct():
    assert length_of_longest_substring_k_distinct("aa", 5) == 2


def test_subarrays_with_k_distinct_normal():
    assert subarrays_with_k_distinct([1, 2, 1, 2, 3], 2) == 7


def test_subarrays_with_k_distinct_normal_two():
    assert subarrays_with_k_distinct([1, 2, 1, 3, 4], 3) == 3


def test_subarrays_with_k_distinct_single_element():
    assert subarrays_with_k_distinct([1], 1) == 1


def test_subarrays_with_k_distinct_k_exceeds_distinct():
    assert subarrays_with_k_distinct([1, 2], 3) == 0


def test_number_of_subarrays_normal():
    assert number_of_subarrays([1, 1, 2, 1, 1], 3) == 2


def test_number_of_subarrays_no_odds_needed_but_none_present():
    assert number_of_subarrays([2, 4, 6], 1) == 0


def test_number_of_subarrays_normal_two():
    assert number_of_subarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) == 16


def test_number_of_subarrays_single_odd():
    assert number_of_subarrays([1], 1) == 1
