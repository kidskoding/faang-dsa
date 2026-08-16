from problem_set.string_algorithms_problems import (
    build_failure_table,
    longest_prefix,
    repeated_string_match,
    repeated_substring_pattern,
    shortest_palindrome,
    str_str,
)


def test_str_str_found():
    assert str_str("sadbutsad", "sad") == 0


def test_str_str_not_found():
    assert str_str("leetcode", "leeto") == -1


def test_str_str_empty_needle():
    assert str_str("abc", "") == 0


def test_repeated_string_match_normal():
    assert repeated_string_match("abcd", "cdabcdab") == 3


def test_repeated_string_match_impossible():
    assert repeated_string_match("a", "b") == -1


def test_repeated_string_match_already_contains():
    assert repeated_string_match("abc", "b") == 1


def test_shortest_palindrome_normal():
    assert shortest_palindrome("aacecaaa") == "aaacecaaa"


def test_shortest_palindrome_already_palindrome():
    assert shortest_palindrome("aba") == "aba"


def test_shortest_palindrome_empty():
    assert shortest_palindrome("") == ""


def test_longest_prefix_normal():
    assert longest_prefix("level") == "l"


def test_longest_prefix_full_repeat():
    assert longest_prefix("ababab") == "abab"


def test_longest_prefix_none():
    assert longest_prefix("leetcode") == ""


def test_build_failure_table_with_repeats():
    assert build_failure_table("aabaaab") == [0, 1, 0, 1, 2, 2, 3]


def test_build_failure_table_no_repeats():
    assert build_failure_table("abc") == [0, 0, 0]


def test_repeated_substring_pattern_true():
    assert repeated_substring_pattern("abab") is True


def test_repeated_substring_pattern_false():
    assert repeated_substring_pattern("aba") is False


def test_repeated_substring_pattern_longer():
    assert repeated_substring_pattern("abcabcabcabc") is True
