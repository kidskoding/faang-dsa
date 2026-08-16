from problem_set.opposite_end_problems import (
    four_sum,
    is_palindrome,
    max_area,
    num_rescue_boats,
    reverse_string,
    sorted_squares,
    three_sum,
    three_sum_closest,
    trap,
    two_sum,
)


def test_is_palindrome_empty():
    assert is_palindrome("") is True


def test_is_palindrome_single_char():
    assert is_palindrome("a") is True


def test_is_palindrome_alphanumeric_only():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_is_palindrome_not_palindrome():
    assert is_palindrome("race a car") is False


def test_two_sum_normal():
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]


def test_two_sum_single_pair_at_ends():
    assert two_sum([-1, 0, 3, 5], 4) == [1, 4]


def test_two_sum_negative_numbers():
    assert two_sum([-3, -1, 0, 2, 4], 1) == [2, 4]


def test_reverse_string_empty():
    s: list[str] = []
    reverse_string(s)
    assert s == []


def test_reverse_string_single():
    s = ["a"]
    reverse_string(s)
    assert s == ["a"]


def test_reverse_string_multiple():
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    assert s == ["o", "l", "l", "e", "h"]


def test_max_area_normal():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_max_area_two_elements():
    assert max_area([1, 1]) == 1


def test_max_area_increasing_heights():
    assert max_area([1, 2, 3, 4, 5]) == 6


def test_three_sum_empty():
    assert three_sum([]) == []


def test_three_sum_no_triplet():
    assert three_sum([0, 1, 1]) == []


def test_three_sum_normal():
    result = sorted(sorted(triplet) for triplet in three_sum([-1, 0, 1, 2, -1, -4]))
    expected = sorted(sorted(triplet) for triplet in [[-1, -1, 2], [-1, 0, 1]])
    assert result == expected


def test_three_sum_closest_normal():
    assert three_sum_closest([-1, 2, 1, -4], 1) == 2


def test_three_sum_closest_exact_match():
    assert three_sum_closest([0, 0, 0], 1) == 0


def test_num_rescue_boats_single_person():
    assert num_rescue_boats([3], 3) == 1


def test_num_rescue_boats_pairs_fit():
    assert num_rescue_boats([3, 2, 2, 1], 3) == 3


def test_num_rescue_boats_all_pair():
    assert num_rescue_boats([1, 2], 3) == 1


def test_trap_empty():
    assert trap([]) == 0


def test_trap_no_water():
    assert trap([1, 2, 3, 4]) == 0


def test_trap_normal():
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_four_sum_empty():
    assert four_sum([], 0) == []


def test_four_sum_normal():
    result = sorted(sorted(quad) for quad in four_sum([1, 0, -1, 0, -2, 2], 0))
    expected = sorted(sorted(quad) for quad in [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
    assert result == expected


def test_sorted_squares_empty():
    assert sorted_squares([]) == []


def test_sorted_squares_single():
    assert sorted_squares([3]) == [9]


def test_sorted_squares_negatives_and_positives():
    assert sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]


def test_sorted_squares_all_negative():
    assert sorted_squares([-7, -3, -1]) == [1, 9, 49]
