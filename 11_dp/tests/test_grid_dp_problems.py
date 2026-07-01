from problem_set.grid_dp_problems import (
    maximal_square,
    min_path_sum,
    minimum_total,
    unique_paths,
    unique_paths_with_obstacles,
)


def test_unique_paths_single_cell():
    assert unique_paths(1, 1) == 1


def test_unique_paths_single_row():
    assert unique_paths(1, 5) == 1


def test_unique_paths_normal():
    assert unique_paths(3, 7) == 28


def test_unique_paths_with_obstacles_no_obstacle():
    assert unique_paths_with_obstacles([[0, 0], [0, 0]]) == 2


def test_unique_paths_with_obstacles_normal():
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert unique_paths_with_obstacles(grid) == 2


def test_unique_paths_with_obstacles_start_blocked():
    assert unique_paths_with_obstacles([[1, 0]]) == 0


def test_min_path_sum_single_cell():
    assert min_path_sum([[5]]) == 5


def test_min_path_sum_normal():
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    assert min_path_sum(grid) == 7


def test_min_path_sum_single_row():
    assert min_path_sum([[1, 2, 3]]) == 6


def test_minimum_total_single_row():
    assert minimum_total([[1]]) == 1


def test_minimum_total_normal():
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    assert minimum_total(triangle) == 11


def test_maximal_square_empty():
    assert maximal_square([]) == 0


def test_maximal_square_no_square():
    assert maximal_square([["0", "0"], ["0", "0"]]) == 0


def test_maximal_square_normal():
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    assert maximal_square(matrix) == 4


def test_maximal_square_single_cell():
    assert maximal_square([["1"]]) == 1
