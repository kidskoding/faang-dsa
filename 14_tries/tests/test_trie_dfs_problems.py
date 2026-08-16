from problem_set.trie_dfs_problems import (
    find_all_concatenated_words,
    find_maximum_xor,
    find_words,
    maximize_xor,
    palindrome_pairs,
    string_indices,
    word_squares,
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
        "cat",
        "cats",
        "catsdogcats",
        "dog",
        "dogcatsdog",
        "hippopotamuses",
        "rat",
        "ratcatdogcat",
    ]
    result = find_all_concatenated_words(words)
    assert set(result) == {"catsdogcats", "dogcatsdog", "ratcatdogcat"}


def test_find_all_concatenated_words_no_matches():
    assert find_all_concatenated_words(["cat", "dog", "bird"]) == []


def test_find_all_concatenated_words_empty_input():
    assert find_all_concatenated_words([]) == []


def test_word_squares_two_solutions():
    result = word_squares(["area", "lead", "wall", "lady", "ball"])

    assert sorted(sorted(square) for square in result) == [
        sorted(["ball", "area", "lead", "lady"]),
        sorted(["wall", "area", "lead", "lady"]),
    ]


def test_word_squares_repeated_words():
    result = word_squares(["abat", "baba", "atan", "atal"])

    assert sorted(sorted(square) for square in result) == [
        sorted(["baba", "abat", "baba", "atal"]),
        sorted(["baba", "abat", "baba", "atan"]),
    ]


def test_find_maximum_xor_normal():
    assert find_maximum_xor([3, 10, 5, 25, 2, 8]) == 28


def test_find_maximum_xor_larger():
    nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
    assert find_maximum_xor(nums) == 127


def test_maximize_xor_normal():
    assert maximize_xor([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]]) == [3, 3, 7]


def test_maximize_xor_with_impossible_query():
    assert maximize_xor([5, 2, 4, 6, 6, 3], [[12, 4], [8, 1], [6, 3]]) == [15, -1, 5]


def test_string_indices_shortest_wins_on_tie():
    assert string_indices(["abcd", "bcd", "xbcd"], ["cd", "bcd", "xyz"]) == [1, 1, 1]


def test_string_indices_longest_common_suffix():
    container = ["abcdefgh", "poiuygh", "ghghgh"]
    assert string_indices(container, ["gh", "acbfgh", "acbfegh"]) == [2, 0, 2]
