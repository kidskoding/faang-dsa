from problem_set.topological_sort_problems import (
    all_paths_source_target,
    can_finish,
    check_if_prerequisite,
    eventual_safe_nodes,
    find_itinerary,
    find_min_height_trees,
    find_order,
    get_ancestors,
    largest_path_value,
    longest_increasing_path,
    minimum_time,
    num_of_minutes,
)


def test_can_finish_true():
    assert can_finish(2, [[1, 0]]) is True


def test_can_finish_cycle_false():
    assert can_finish(2, [[1, 0], [0, 1]]) is False


def test_can_finish_no_prerequisites():
    assert can_finish(3, []) is True


def test_find_order_normal_case():
    assert find_order(2, [[1, 0]]) == [0, 1]


def test_find_order_cycle_returns_empty():
    assert find_order(2, [[1, 0], [0, 1]]) == []


def test_find_order_no_prerequisites():
    assert sorted(find_order(3, [])) == [0, 1, 2]


def test_all_paths_source_target_normal_case():
    result = all_paths_source_target([[1, 2], [3], [3], []])

    assert sorted(result) == sorted([[0, 1, 3], [0, 2, 3]])


def test_all_paths_source_target_single_node():
    assert all_paths_source_target([[]]) == [[0]]


def test_eventual_safe_nodes_normal_case():
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]

    assert eventual_safe_nodes(graph) == [2, 4, 5, 6]


def test_eventual_safe_nodes_no_unsafe_nodes():
    graph = [[], [], []]

    assert eventual_safe_nodes(graph) == [0, 1, 2]


def test_find_min_height_trees_normal_case():
    edges = [[1, 0], [1, 2], [1, 3]]

    assert sorted(find_min_height_trees(4, edges)) == [1]


def test_find_min_height_trees_single_node():
    assert find_min_height_trees(1, []) == [0]


def test_num_of_minutes_normal_case():
    assert num_of_minutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]) == 1


def test_num_of_minutes_single_employee():
    assert num_of_minutes(1, 0, [-1], [0]) == 0


def test_check_if_prerequisite_normal_case():
    result = check_if_prerequisite(
        5,
        [[0, 1], [1, 2], [2, 3], [3, 4]],
        [[0, 4], [4, 0], [1, 3], [3, 0]],
    )

    assert result == [True, False, True, False]


def test_find_itinerary_normal_case():
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

    assert find_itinerary(tickets) == ["JFK", "MUC", "LHR", "SFO", "SJC"]


def test_find_itinerary_lexical_ordering():
    tickets = [
        ["JFK", "SFO"],
        ["JFK", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "JFK"],
        ["ATL", "SFO"],
    ]

    assert find_itinerary(tickets) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]


def test_get_ancestors_normal_case():
    edges = [[0, 1], [0, 2], [1, 3], [2, 3]]

    result = get_ancestors(4, edges)

    assert result == [[], [0], [0], [0, 1, 2]]


def test_get_ancestors_no_edges():
    assert get_ancestors(3, []) == [[], [], []]


def test_minimum_time_normal_case():
    assert minimum_time(3, [[1, 3], [2, 3]], [3, 2, 5]) == 8


def test_minimum_time_no_relations():
    assert minimum_time(1, [], [5]) == 5


def test_largest_path_value_normal_case():
    assert largest_path_value("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]) == 3


def test_largest_path_value_cycle_returns_negative_one():
    assert largest_path_value("a", [[0, 0]]) == -1


def test_longest_increasing_path_normal():
    assert longest_increasing_path([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4


def test_longest_increasing_path_diagonal_not_allowed():
    assert longest_increasing_path([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4


def test_longest_increasing_path_single_cell():
    assert longest_increasing_path([[1]]) == 1
