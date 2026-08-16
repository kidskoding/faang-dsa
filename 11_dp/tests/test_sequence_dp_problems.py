from problem_set.sequence_dp_problems import (
    cherry_pickup,
    count_substrings,
    is_interleave,
    is_match_regex,
    is_match_wildcard,
    length_of_lis,
    longest_common_subsequence,
    longest_palindrome,
    longest_palindrome_subseq,
    longest_valid_parentheses,
    max_coins,
    max_profit_iv,
    max_profit_with_cooldown,
    max_profit_with_fee,
    maximal_rectangle,
    merge_stones,
    min_cut,
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


def test_longest_palindrome_subseq_normal():
    assert longest_palindrome_subseq("bbbab") == 4


def test_longest_palindrome_subseq_no_repeat():
    assert longest_palindrome_subseq("cbbd") == 2


def test_longest_palindrome_subseq_single():
    assert longest_palindrome_subseq("a") == 1


def test_longest_palindrome_subseq_full_palindrome():
    assert longest_palindrome_subseq("racecar") == 7


def test_min_cut_one_cut():
    assert min_cut("aab") == 1


def test_min_cut_already_palindrome():
    assert min_cut("a") == 0


def test_min_cut_no_shared_letters():
    assert min_cut("ab") == 1


def test_max_profit_iv_one_trade_fits():
    assert max_profit_iv(2, [2, 4, 1]) == 2


def test_max_profit_iv_two_trades():
    assert max_profit_iv(2, [3, 2, 6, 5, 0, 3]) == 7


def test_max_profit_iv_no_trades_allowed():
    assert max_profit_iv(0, [1, 3]) == 0


def test_longest_valid_parentheses_partial():
    assert longest_valid_parentheses("(()") == 2


def test_longest_valid_parentheses_normal():
    assert longest_valid_parentheses(")()())") == 4


def test_maximal_rectangle_normal():
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    assert maximal_rectangle(matrix) == 6


def test_maximal_rectangle_all_zero():
    assert maximal_rectangle([["0"]]) == 0


def test_merge_stones_pairs():
    assert merge_stones([3, 2, 4, 1], 2) == 20


def test_merge_stones_impossible():
    assert merge_stones([3, 2, 4, 1], 3) == -1


def test_merge_stones_triples():
    assert merge_stones([3, 5, 1, 2, 6], 3) == 25


def test_cherry_pickup_normal():
    assert cherry_pickup([[0, 1, -1], [1, 0, -1], [1, 1, 1]]) == 5


def test_cherry_pickup_blocked():
    assert cherry_pickup([[1, 1, -1], [1, -1, 1], [-1, 1, 1]]) == 0


def test_cherry_pickup_open_grid():
    assert cherry_pickup([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 8
