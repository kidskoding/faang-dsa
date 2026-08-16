from problem_set.implicit_state_bfs_problems import (
    has_path,
    ladder_length,
    min_mutation,
    minimum_moves,
    num_buses_to_destination,
    open_lock,
    shortest_path_all_keys,
    shortest_path_length,
    snakes_and_ladders,
)


def test_min_mutation_normal_case():
    assert min_mutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) == 1


def test_min_mutation_multi_step():
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

    assert min_mutation("AACCGGTT", "AAACGGTA", bank) == 2


def test_min_mutation_no_valid_path():
    assert min_mutation("AACCGGTT", "AACCGGTA", []) == -1


def test_open_lock_normal_case():
    deadends = ["0201", "0101", "0102", "1212", "2002"]

    assert open_lock(deadends, "0202") == 6


def test_open_lock_start_is_deadend():
    assert open_lock(["8888"], "0009") == -1


def test_open_lock_target_is_start():
    assert open_lock([], "0000") == 0


def test_ladder_length_normal_case():
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5


def test_ladder_length_no_path():
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0


def test_snakes_and_ladders_normal_case():
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]

    assert snakes_and_ladders(board) == 4


def test_snakes_and_ladders_single_cell():
    assert snakes_and_ladders([[-1]]) == 0


def test_shortest_path_all_keys_normal_case():
    assert shortest_path_all_keys(["@.a.#", "###.#", "b.A.B"]) == 8


def test_shortest_path_all_keys_no_keys():
    assert shortest_path_all_keys(["@..", "...", "..."]) == 0


def test_num_buses_to_destination_normal_case():
    routes = [[1, 2, 7], [3, 6, 7]]

    assert num_buses_to_destination(routes, 1, 6) == 2


def test_num_buses_to_destination_same_start_and_target():
    assert num_buses_to_destination([[1, 2, 7]], 1, 1) == 0


def test_shortest_path_length_normal_case():
    assert shortest_path_length([[1, 2, 3], [0], [0], [0]]) == 4


def test_shortest_path_length_two_nodes():
    assert shortest_path_length([[1], [0]]) == 1


def test_minimum_moves_normal_case():
    grid = [
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
    ]

    assert minimum_moves(grid) == 11


def test_minimum_moves_smallest_grid():
    assert minimum_moves([[0, 0], [0, 0]]) == 1


def test_has_path_true():
    maze = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
    ]

    assert has_path(maze, [0, 4], [4, 4]) is True


def test_has_path_false():
    maze = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
    ]

    assert has_path(maze, [0, 4], [3, 2]) is False
