from redo_problems import (
    group_anagrams,
    is_anagram,
    longest_consecutive,
    top_k_frequent,
)


def test_is_anagram_true():
    assert is_anagram("anagram", "nagaram") is True


def test_is_anagram_false_different_lengths():
    assert is_anagram("rat", "car") is False


def test_is_anagram_t_longer_with_repeat():
    assert is_anagram("ab", "aab") is False


def test_is_anagram_same_length_different_counts():
    assert is_anagram("aabb", "abbb") is False


def test_is_anagram_empty_strings():
    assert is_anagram("", "") is True


def test_group_anagrams_normal():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    normalized = sorted(sorted(group) for group in result)
    expected = sorted(sorted(g) for g in [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])

    assert normalized == expected


def test_group_anagrams_empty_string():
    assert group_anagrams([""]) == [[""]]


def test_group_anagrams_empty():
    assert group_anagrams([]) == []


def test_top_k_frequent_normal():
    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}


def test_top_k_frequent_k_equals_distinct_count():
    assert sorted(top_k_frequent([1, 2, 3], 3)) == [1, 2, 3]


def test_top_k_frequent_with_negatives():
    assert set(top_k_frequent([-1, -1, -1, -2, -2, 5], 2)) == {-1, -2}


def test_longest_consecutive_normal():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4


def test_longest_consecutive_empty():
    assert longest_consecutive([]) == 0


def test_longest_consecutive_with_duplicates():
    assert longest_consecutive([1, 2, 0, 1]) == 3


def test_longest_consecutive_with_negatives():
    assert longest_consecutive([-3, -2, -1, 5, 7]) == 3
