from problem_set.union_find_problems import (
    UnionFind,
    calc_equation,
    equations_possible,
    find_redundant_connection,
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


def test_union_find_merges_and_counts():
    union_find = UnionFind(5)

    assert union_find.union(0, 1) is True
    assert union_find.union(0, 1) is False
    assert union_find.find(0) == union_find.find(1)


def test_union_find_keeps_disjoint_sets_apart():
    union_find = UnionFind(4)
    union_find.union(0, 1)
    union_find.union(2, 3)

    assert union_find.find(0) != union_find.find(2)


def test_find_redundant_connection_triangle():
    assert find_redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]


def test_find_redundant_connection_later_edge():
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    assert find_redundant_connection(edges) == [1, 4]


def test_calc_equation_normal():
    equations = [["a", "b"], ["b", "c"]]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    assert calc_equation(equations, [2.0, 3.0], queries) == [6.0, 0.5, -1.0, 1.0, -1.0]


def test_calc_equation_single_pair():
    result = calc_equation([["a", "b"]], [2.0], [["a", "b"], ["b", "a"]])

    assert result == [2.0, 0.5]


def test_calc_equation_unknown_variable():
    assert calc_equation([["a", "b"]], [2.0], [["a", "c"]]) == [-1.0]
