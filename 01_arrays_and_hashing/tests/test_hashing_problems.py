from problem_set.hashing_problems import (
    Codec,
    MyHashMap,
    TinyURLCodec,
    contains_duplicate,
    custom_sort_string,
    four_sum_count,
    group_anagrams,
    intersect,
    is_anagram,
    is_valid_sudoku,
    least_bricks,
    longest_consecutive,
    majority_element,
    majority_element_ii,
    top_k_frequent,
    two_sum,
)


def test_two_sum_normal():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_middle_pair():
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_two_sum_duplicate_values():
    assert two_sum([3, 3], 6) == [0, 1]


def test_two_sum_all_negative():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]


def test_two_sum_mixed_signs():
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]


def test_two_sum_no_pair():
    assert two_sum([1, 2, 3], 100) == []


def test_contains_duplicate_true():
    assert contains_duplicate([1, 2, 3, 1]) is True


def test_contains_duplicate_false():
    assert contains_duplicate([1, 2, 3, 4]) is False


def test_contains_duplicate_empty():
    assert contains_duplicate([]) is False


def test_contains_duplicate_single_element():
    assert contains_duplicate([1]) is False


def test_is_anagram_true():
    assert is_anagram("anagram", "nagaram") is True


def test_is_anagram_false_different_lengths():
    assert is_anagram("rat", "car") is False


def test_is_anagram_empty_strings():
    assert is_anagram("", "") is True


def test_is_anagram_t_longer_with_repeat():
    assert is_anagram("ab", "aab") is False


def test_is_anagram_same_length_different_counts():
    assert is_anagram("aabb", "abbb") is False


def test_is_anagram_same_letters_wrong_multiplicity():
    assert is_anagram("aacc", "ccac") is False


def test_group_anagrams_normal():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    normalized = sorted(sorted(group) for group in result)
    expected = sorted(sorted(group) for group in [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    assert normalized == expected


def test_group_anagrams_empty():
    assert group_anagrams([]) == []


def test_group_anagrams_single_word():
    assert group_anagrams(["abc"]) == [["abc"]]


def test_group_anagrams_empty_string():
    assert group_anagrams([""]) == [[""]]


def test_group_anagrams_identical_words_group_together():
    assert group_anagrams(["a", "a"]) == [["a", "a"]]


def test_group_anagrams_same_letters_different_lengths_do_not_group():
    result = group_anagrams(["ab", "aab"])
    normalized = sorted(sorted(group) for group in result)

    assert normalized == [["aab"], ["ab"]]


def test_top_k_frequent_normal():
    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}


def test_top_k_frequent_single_element():
    assert top_k_frequent([1], 1) == [1]


def test_top_k_frequent_k_equals_distinct_count():
    assert sorted(top_k_frequent([1, 2, 3], 3)) == [1, 2, 3]


def test_top_k_frequent_breaks_a_tie():
    assert set(top_k_frequent([1, 1, 2, 2, 3], 2)) == {1, 2}


def test_top_k_frequent_with_negatives():
    assert set(top_k_frequent([-1, -1, -1, -2, -2, 5], 2)) == {-1, -2}


def test_longest_consecutive_normal():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4


def test_longest_consecutive_empty():
    assert longest_consecutive([]) == 0


def test_longest_consecutive_with_duplicates():
    assert longest_consecutive([1, 2, 0, 1]) == 3


def test_longest_consecutive_single_element():
    assert longest_consecutive([7]) == 1


def test_longest_consecutive_with_negatives():
    assert longest_consecutive([-3, -2, -1, 5, 7]) == 3


def test_longest_consecutive_no_run_longer_than_one():
    assert longest_consecutive([10, 30, 20]) == 1


def _valid_board() -> list[list[str]]:
    return [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]


def _invalid_board() -> list[list[str]]:
    board = _valid_board()
    board[0][0] = "8"
    return board


def test_is_valid_sudoku_true():
    assert is_valid_sudoku(_valid_board()) is True


def test_is_valid_sudoku_false_duplicate_in_column():
    assert is_valid_sudoku(_invalid_board()) is False


def _sparse_board() -> list[list[str]]:
    return [["." for _ in range(9)] for _ in range(9)]


def test_is_valid_sudoku_false_duplicate_only_in_box():
    """Rows and columns are clean; only the top-left 3x3 box repeats.

    A solution that checks rows and columns but forgets the boxes passes every
    other test in this file, so this is the one that catches it.
    """
    board = _sparse_board()
    board[0][0] = "5"
    board[1][1] = "5"

    assert is_valid_sudoku(board) is False


def test_is_valid_sudoku_false_duplicate_only_in_row():
    board = _sparse_board()
    board[3][0] = "7"
    board[3][8] = "7"

    assert is_valid_sudoku(board) is False


def test_is_valid_sudoku_same_value_in_different_boxes_is_fine():
    board = _sparse_board()
    board[0][0] = "5"
    board[4][4] = "5"
    board[8][8] = "5"

    assert is_valid_sudoku(board) is True


def test_is_valid_sudoku_empty_board():
    assert is_valid_sudoku(_sparse_board()) is True


def test_codec_roundtrip_normal():
    codec = Codec()
    strs = ["neet", "code", "love", "you"]
    assert codec.decode(codec.encode(strs)) == strs


def test_codec_roundtrip_empty():
    codec = Codec()
    assert codec.decode(codec.encode([])) == []


def test_codec_roundtrip_empty_strings():
    codec = Codec()
    strs = ["", "a", ""]
    assert codec.decode(codec.encode(strs)) == strs


def test_intersect_with_repeats():
    assert sorted(intersect([1, 2, 2, 1], [2, 2])) == [2, 2]


def test_intersect_keeps_multiplicity():
    assert sorted(intersect([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]


def test_intersect_no_overlap():
    assert intersect([1, 2], [3, 4]) == []


def test_intersect_first_array_limits_the_count():
    assert intersect([2], [2, 2, 2]) == [2]


def test_intersect_second_array_limits_the_count():
    assert intersect([2, 2, 2], [2]) == [2]


def test_intersect_empty_first():
    assert intersect([], [1, 2]) == []


def test_intersect_empty_second():
    assert intersect([1, 2], []) == []


def test_majority_element_normal():
    assert majority_element([3, 2, 3]) == 3


def test_majority_element_longer():
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2


def test_majority_element_single():
    assert majority_element([1]) == 1


def test_majority_element_ii_one_winner():
    assert sorted(majority_element_ii([3, 2, 3])) == [3]


def test_majority_element_ii_single():
    assert sorted(majority_element_ii([1])) == [1]


def test_majority_element_ii_two_winners():
    assert sorted(majority_element_ii([1, 2])) == [1, 2]


def test_majority_element_ii_excludes_below_threshold():
    assert sorted(majority_element_ii([1, 1, 1, 3, 3, 2, 2, 2])) == [1, 2]


def test_my_hash_map_put_and_get():
    hash_map = MyHashMap()
    hash_map.put(1, 1)
    hash_map.put(2, 2)

    assert hash_map.get(1) == 1
    assert hash_map.get(3) == -1


def test_my_hash_map_overwrites_existing_key():
    hash_map = MyHashMap()
    hash_map.put(2, 2)
    hash_map.put(2, 1)

    assert hash_map.get(2) == 1


def test_my_hash_map_remove():
    hash_map = MyHashMap()
    hash_map.put(2, 1)
    hash_map.remove(2)

    assert hash_map.get(2) == -1


def test_four_sum_count_two_tuples():
    assert four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2


def test_four_sum_count_all_zeros():
    assert four_sum_count([0], [0], [0], [0]) == 1


def test_four_sum_count_no_match():
    assert four_sum_count([1], [1], [1], [1]) == 0


def test_four_sum_count_counts_every_index_combination():
    """Duplicates must multiply, not collapse.

    Every one of the 2*2*2*2 index choices sums to zero. A solution that stores
    pair sums in a set rather than a counter returns 4 here and still passes
    every other test in this file.
    """
    assert four_sum_count([0, 0], [0, 0], [0, 0], [0, 0]) == 16


def test_four_sum_count_duplicates_across_arrays():
    assert four_sum_count([1, 1], [-1, -1], [0, 0], [0, 0]) == 16


def test_four_sum_count_mixed_signs():
    assert four_sum_count([-1, -1], [-1, 1], [-1, 1], [1, -1]) == 6


def test_least_bricks_normal():
    wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
    assert least_bricks(wall) == 2


def test_least_bricks_no_shared_edges():
    assert least_bricks([[1], [1], [1]]) == 3


def test_least_bricks_two_rows():
    assert least_bricks([[1, 1], [2]]) == 1


def test_least_bricks_every_row_aligned():
    """A seam every row shares, so the line crosses nothing."""
    assert least_bricks([[1, 1], [1, 1], [1, 1]]) == 0


def test_least_bricks_single_row():
    assert least_bricks([[1, 2, 3]]) == 0


def test_least_bricks_mirrored_rows():
    assert least_bricks([[2, 1], [1, 2]]) == 1


def test_custom_sort_string_all_ordered():
    assert custom_sort_string("cba", "abcd") == "cbad"


def test_custom_sort_string_order_has_extra_letters():
    assert custom_sort_string("bcafg", "abcd") == "bcad"


def test_custom_sort_string_with_repeats():
    assert custom_sort_string("kqep", "pekeq") == "kqeep"


def test_tiny_url_codec_round_trips():
    codec = TinyURLCodec()
    url = "https://leetcode.com/problems/design-tinyurl"

    assert codec.decode(codec.encode(url)) == url


def test_tiny_url_codec_is_stable_for_the_same_url():
    codec = TinyURLCodec()
    url = "http://example.com"

    assert codec.encode(url) == codec.encode(url)


def test_tiny_url_codec_gives_distinct_codes():
    codec = TinyURLCodec()
    first = codec.encode("http://a.com")
    second = codec.encode("http://b.com")

    assert first != second
    assert codec.decode(first) == "http://a.com"
    assert codec.decode(second) == "http://b.com"
