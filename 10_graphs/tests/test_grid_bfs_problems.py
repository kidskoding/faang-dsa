from problem_set.grid_bfs_problems import (
    contains_cycle,
    highest_peak,
    max_distance,
    nearest_exit,
    oranges_rotting,
    shortest_bridge,
    shortest_path_binary_matrix,
    update_matrix,
    walls_and_gates,
)


def test_oranges_rotting_normal_case():
    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4


def test_oranges_rotting_impossible():
    assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1


def test_oranges_rotting_no_fresh_oranges():
    assert oranges_rotting([[0, 2]]) == 0


def test_walls_and_gates_normal_case():
    inf = 2**31 - 1
    rooms = [
        [inf, -1, 0, inf],
        [inf, inf, inf, -1],
        [inf, -1, inf, -1],
        [0, -1, inf, inf],
    ]
    expected = [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]

    walls_and_gates(rooms)

    assert rooms == expected


def test_walls_and_gates_no_gates():
    inf = 2**31 - 1
    rooms = [[inf, inf], [inf, inf]]

    walls_and_gates(rooms)

    assert rooms == [[inf, inf], [inf, inf]]


def test_update_matrix_normal_case():
    assert update_matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]


def test_update_matrix_single_one():
    assert update_matrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [
        [0, 0, 0],
        [0, 1, 0],
        [1, 2, 1],
    ]


def test_shortest_path_binary_matrix_normal_case():
    assert shortest_path_binary_matrix([[0, 1], [1, 0]]) == 2


def test_shortest_path_binary_matrix_blocked():
    assert shortest_path_binary_matrix([[0, 1], [1, 1]]) == -1


def test_shortest_path_binary_matrix_single_cell():
    assert shortest_path_binary_matrix([[0]]) == 1


def test_nearest_exit_normal_case():
    maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]

    assert nearest_exit(maze, [1, 2]) == 1


def test_nearest_exit_no_exit():
    maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]

    assert nearest_exit(maze, [1, 0]) == -1


def test_max_distance_normal_case():
    assert max_distance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]) == 2


def test_max_distance_all_land():
    assert max_distance([[1, 1], [1, 1]]) == -1


def test_highest_peak_normal_case():
    assert highest_peak([[0, 1], [0, 0]]) == [[1, 0], [2, 1]]


def test_highest_peak_all_water():
    assert highest_peak([[0, 0], [0, 0]]) == [[0, 0], [0, 0]]


def test_shortest_bridge_normal_case():
    assert shortest_bridge([[0, 1], [1, 0]]) == 1


def test_shortest_bridge_adjacent_islands_across_gap():
    grid = [[0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 1]]

    assert shortest_bridge(grid) == 2


def test_contains_cycle_true():
    grid = [["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]

    assert contains_cycle(grid) is True


def test_contains_cycle_false():
    grid = [["a", "b"], ["c", "d"]]

    assert contains_cycle(grid) is False
