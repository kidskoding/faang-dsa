from problem_set.graph_basics_problems import (
    Employee,
    Node,
    can_visit_all_rooms,
    clone_graph,
    find_center,
    get_importance,
    valid_path,
)


def test_find_center_of_star_graph_triangle_edges():
    assert find_center([[1, 2], [2, 3], [4, 2]]) == 2


def test_find_center_of_star_graph_minimal():
    assert find_center([[1, 2]]) == 1


def test_valid_path_direct_edge():
    assert valid_path(3, [[0, 1], [1, 2], [2, 0]], 0, 2) is True


def test_valid_path_no_path_disconnected():
    assert valid_path(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) is False


def test_valid_path_single_node_source_equals_destination():
    assert valid_path(1, [], 0, 0) is True


def test_get_importance_with_subordinates():
    employees = [
        Employee(1, 5, [2, 3]),
        Employee(2, 3, []),
        Employee(3, 3, []),
    ]

    assert get_importance(employees, 1) == 11


def test_get_importance_leaf_employee():
    employees = [Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])]

    assert get_importance(employees, 2) == 3


def test_can_visit_all_rooms_true():
    assert can_visit_all_rooms([[1], [2], [3], []]) is True


def test_can_visit_all_rooms_false():
    assert can_visit_all_rooms([[1, 3], [3, 0, 1], [2], [0]]) is False


def test_can_visit_all_rooms_single_room():
    assert can_visit_all_rooms([[]]) is True


def build_two_node_graph() -> Node:
    node1 = Node(1)
    node2 = Node(2)
    node1.neighbors = [node2]
    node2.neighbors = [node1]
    return node1


def test_clone_graph_empty():
    assert clone_graph(None) is None


def test_clone_graph_single_node_no_neighbors():
    original = Node(1)
    cloned = clone_graph(original)

    assert cloned is not original
    assert cloned.val == 1
    assert cloned.neighbors == []


def test_clone_graph_two_connected_nodes():
    original = build_two_node_graph()
    cloned = clone_graph(original)

    assert cloned is not original
    assert cloned.val == 1
    assert len(cloned.neighbors) == 1
    assert cloned.neighbors[0].val == 2
    assert cloned.neighbors[0] is not original.neighbors[0]
