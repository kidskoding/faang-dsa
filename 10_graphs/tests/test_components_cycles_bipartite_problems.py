from problem_set.components_cycles_bipartite_problems import (
    accounts_merge,
    closest_meeting_node,
    count_components,
    find_redundant_connection,
    find_smallest_set_of_vertices,
    is_bipartite,
    min_reorder,
    possible_bipartition,
    valid_tree,
)


def test_count_components_two_components():
    assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2


def test_count_components_no_edges():
    assert count_components(3, []) == 3


def test_count_components_single_node():
    assert count_components(1, []) == 1


def test_valid_tree_true():
    assert valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True


def test_valid_tree_cycle_false():
    assert valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False


def test_valid_tree_disconnected_false():
    assert valid_tree(4, [[0, 1], [2, 3]]) is False


def test_find_redundant_connection_normal_case():
    assert find_redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]


def test_find_redundant_connection_last_edge_closes_cycle():
    assert find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]


def test_is_bipartite_true():
    assert is_bipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) is True


def test_is_bipartite_false():
    assert is_bipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) is False


def test_is_bipartite_no_edges():
    assert is_bipartite([[], []]) is True


def test_possible_bipartition_true():
    assert possible_bipartition(4, [[1, 2], [1, 3], [2, 4]]) is True


def test_possible_bipartition_false():
    assert possible_bipartition(3, [[1, 2], [1, 3], [2, 3]]) is False


def test_accounts_merge_normal_case():
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    expected = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]

    result = accounts_merge(accounts)
    normalized = sorted([acc[0]] + sorted(acc[1:]) for acc in result)
    expected_normalized = sorted([acc[0]] + sorted(acc[1:]) for acc in expected)

    assert normalized == expected_normalized


def test_accounts_merge_no_shared_emails():
    accounts = [["A", "a@mail.com"], ["B", "b@mail.com"]]

    result = accounts_merge(accounts)

    assert sorted(result) == sorted(accounts)


def test_min_reorder_normal_case():
    assert min_reorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3


def test_min_reorder_already_oriented():
    assert min_reorder(3, [[1, 0], [2, 0]]) == 0


def test_find_smallest_set_of_vertices_normal_case():
    edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]

    assert sorted(find_smallest_set_of_vertices(5, edges)) == [0, 2, 3]


def test_find_smallest_set_of_vertices_no_edges():
    assert sorted(find_smallest_set_of_vertices(3, [])) == [0, 1, 2]


def test_closest_meeting_node_normal_case():
    assert closest_meeting_node([2, 2, 3, -1], 0, 1) == 2


def test_closest_meeting_node_no_meeting_node():
    assert closest_meeting_node([1, 2, -1], 0, 2) == -1
