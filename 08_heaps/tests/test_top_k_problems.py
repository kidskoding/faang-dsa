from problem_set.top_k_problems import (
    least_interval,
    reorganize_string,
    top_k_frequent,
    top_k_frequent_words,
)


def test_top_k_frequent_normal():
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]


def test_top_k_frequent_all_unique():
    assert sorted(top_k_frequent([1, 2, 3], 3)) == [1, 2, 3]


def test_top_k_frequent_single():
    assert top_k_frequent([1], 1) == [1]


def test_top_k_frequent_words_normal():
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    assert top_k_frequent_words(words, 2) == ["i", "love"]


def test_top_k_frequent_words_tie_break_alphabetical():
    words = ["the", "day", "is", "sunny", "the", "the", "sunny", "is", "is"]
    assert top_k_frequent_words(words, 4) == ["the", "is", "sunny", "day"]


def test_top_k_frequent_words_single():
    assert top_k_frequent_words(["a"], 1) == ["a"]


def test_least_interval_normal():
    assert least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8


def test_least_interval_no_cooldown():
    assert least_interval(["A", "A", "A", "B", "B", "B"], 0) == 6


def test_least_interval_single_task_type():
    assert least_interval(["A", "A", "A"], 2) == 7


def test_reorganize_string_possible():
    result = reorganize_string("aab")
    assert result in {"aba"}


def test_reorganize_string_impossible():
    assert reorganize_string("aaab") == ""


def test_reorganize_string_single_char():
    assert reorganize_string("a") == "a"
