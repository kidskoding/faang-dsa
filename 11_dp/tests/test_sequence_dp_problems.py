from problem_set.sequence_dp_problems import (
    count_substrings,
    is_interleave,
    is_match_regex,
    is_match_wildcard,
    length_of_lis,
    longest_common_subsequence,
    longest_palindrome,
    max_coins,
    max_profit_with_cooldown,
    max_profit_with_fee,
    min_distance,
    num_distinct,
    word_break,
)


def test_length_of_lis_empty():
    assert length_of_lis([]) == 0


def test_length_of_lis_normal():
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_length_of_lis_strictly_decreasing():
    assert length_of_lis([5, 4, 3, 2, 1]) == 1


def test_longest_common_subsequence_no_match():
    assert longest_common_subsequence("abc", "def") == 0


def test_longest_common_subsequence_normal():
    assert longest_common_subsequence("abcde", "ace") == 3


def test_longest_common_subsequence_empty():
    assert longest_common_subsequence("", "abc") == 0


def test_min_distance_normal():
    assert min_distance("horse", "ros") == 3


def test_min_distance_same_word():
    assert min_distance("abc", "abc") == 0


def test_min_distance_empty_source():
    assert min_distance("", "abc") == 3


def test_word_break_true():
    assert word_break("leetcode", ["leet", "code"]) is True


def test_word_break_false():
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False


def test_word_break_empty():
    assert word_break("", ["a"]) is True


def test_longest_palindrome_normal():
    assert longest_palindrome("babad") in ("bab", "aba")


def test_longest_palindrome_single_char():
    assert longest_palindrome("a") == "a"


def test_longest_palindrome_all_same():
    assert longest_palindrome("bb") == "bb"


def test_count_substrings_normal():
    assert count_substrings("abc") == 3


def test_count_substrings_all_same():
    assert count_substrings("aaa") == 6


def test_count_substrings_empty():
    assert count_substrings("") == 0


def test_max_profit_with_cooldown_normal():
    assert max_profit_with_cooldown([1, 2, 3, 0, 2]) == 3


def test_max_profit_with_cooldown_empty():
    assert max_profit_with_cooldown([]) == 0


def test_max_profit_with_cooldown_no_profit():
    assert max_profit_with_cooldown([5, 4, 3, 2, 1]) == 0


def test_max_profit_with_fee_normal():
    assert max_profit_with_fee([1, 3, 2, 8, 4, 9], 2) == 8


def test_max_profit_with_fee_empty():
    assert max_profit_with_fee([], 1) == 0


def test_is_interleave_true():
    assert is_interleave("aabcc", "dbbca", "aadbbcbcac") is True


def test_is_interleave_false():
    assert is_interleave("aabcc", "dbbca", "aadbbbaccc") is False


def test_is_interleave_empty_all():
    assert is_interleave("", "", "") is True


def test_num_distinct_normal():
    assert num_distinct("rabbbit", "rabbit") == 3


def test_num_distinct_no_match():
    assert num_distinct("abc", "d") == 0


def test_num_distinct_empty_target():
    assert num_distinct("abc", "") == 1


def test_is_match_regex_star():
    assert is_match_regex("aa", "a*") is True


def test_is_match_regex_dot():
    assert is_match_regex("ab", ".*") is True


def test_is_match_regex_false():
    assert is_match_regex("mississippi", "mis*is*p*.") is False


def test_is_match_wildcard_star():
    assert is_match_wildcard("adceb", "*a*b") is True


def test_is_match_wildcard_question_mark():
    assert is_match_wildcard("cb", "?a") is False


def test_is_match_wildcard_empty_pattern():
    assert is_match_wildcard("", "") is True


def test_max_coins_normal():
    assert max_coins([3, 1, 5, 8]) == 167


def test_max_coins_single_balloon():
    assert max_coins([5]) == 5


def test_max_coins_empty():
    assert max_coins([]) == 0
