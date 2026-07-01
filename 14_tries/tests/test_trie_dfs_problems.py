from problem_set.trie_dfs_problems import (
    find_all_concatenated_words,
    find_words,
    palindrome_pairs,
)


def test_find_words_normal_board():
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    assert set(find_words(board, words)) == {"oath", "eat"}


def test_find_words_no_matches():
    board = [["a", "b"], ["c", "d"]]
    words = ["xyz"]
    assert find_words(board, words) == []


def test_find_words_single_cell_board():
    board = [["a"]]
    words = ["a", "b"]
    assert find_words(board, words) == ["a"]


def test_palindrome_pairs_normal():
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = palindrome_pairs(words)
    expected_pairs = {(0, 1), (1, 0), (2, 4), (3, 2)}
    assert {tuple(pair) for pair in result} == expected_pairs


def test_palindrome_pairs_no_matches():
    assert palindrome_pairs(["abc", "def"]) == []


def test_palindrome_pairs_empty_string_pairs_with_palindromes():
    words = ["bat", "tab", "cat", ""]
    result = palindrome_pairs(words)
    expected_pairs = {(0, 1), (1, 0)}
    assert {tuple(pair) for pair in result} == expected_pairs


def test_find_all_concatenated_words_normal():
    words = [
        "cat", "cats", "catsdogcats", "dog", "dogcatsdog",
        "hippopotamuses", "rat", "ratcatdogcat",
    ]
    result = find_all_concatenated_words(words)
    assert set(result) == {"catsdogcats", "dogcatsdog", "ratcatdogcat"}


def test_find_all_concatenated_words_no_matches():
    assert find_all_concatenated_words(["cat", "dog", "bird"]) == []


def test_find_all_concatenated_words_empty_input():
    assert find_all_concatenated_words([]) == []
