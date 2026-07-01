from problem_set.union_find_problems import (
    equations_possible,
    number_of_islands_ii,
    number_of_provinces,
    smallest_string_with_swaps,
)


def test_number_of_provinces_all_connected():
    assert number_of_provinces([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2


def test_number_of_provinces_none_connected():
    assert number_of_provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3


def test_number_of_provinces_single_city():
    assert number_of_provinces([[1]]) == 1


def test_number_of_islands_ii_sequence():
    result = number_of_islands_ii(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]])
    assert result == [1, 1, 2, 3]


def test_number_of_islands_ii_no_positions():
    assert number_of_islands_ii(2, 2, []) == []


def test_number_of_islands_ii_merges_component():
    result = number_of_islands_ii(1, 3, [[0, 0], [0, 2], [0, 1]])
    assert result == [1, 2, 1]


def test_equations_possible_satisfiable():
    assert equations_possible(["a==b", "b==c", "a==c"]) is True


def test_equations_possible_contradiction():
    assert equations_possible(["a==b", "b!=a"]) is False


def test_equations_possible_single_equation():
    assert equations_possible(["a==a"]) is True


def test_smallest_string_with_swaps_normal():
    assert smallest_string_with_swaps("dcab", [[0, 3], [1, 2]]) == "bacd"


def test_smallest_string_with_swaps_no_pairs():
    assert smallest_string_with_swaps("zyx", []) == "zyx"


def test_smallest_string_with_swaps_full_chain():
    assert smallest_string_with_swaps("dcab", [[0, 3], [1, 2], [0, 2]]) == "abcd"
