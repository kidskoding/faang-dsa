from problem_set.matrix_problems import (
    game_of_life,
    generate_matrix,
    rotate,
    set_zeroes,
    spiral_order,
)


def test_rotate_single_cell():
    matrix = [[1]]
    rotate(matrix)
    assert matrix == [[1]]


def test_rotate_three_by_three():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


def test_rotate_two_by_two():
    matrix = [[1, 2], [3, 4]]
    rotate(matrix)
    assert matrix == [[3, 1], [4, 2]]


def test_spiral_order_normal():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert spiral_order(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_spiral_order_single_row():
    assert spiral_order([[1, 2, 3, 4]]) == [1, 2, 3, 4]


def test_spiral_order_single_column():
    assert spiral_order([[1], [2], [3]]) == [1, 2, 3]


def test_spiral_order_empty():
    assert spiral_order([]) == []


def test_generate_matrix_normal():
    assert generate_matrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]


def test_generate_matrix_single():
    assert generate_matrix(1) == [[1]]


def test_set_zeroes_normal():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


def test_set_zeroes_no_zero():
    matrix = [[1, 2], [3, 4]]
    set_zeroes(matrix)
    assert matrix == [[1, 2], [3, 4]]


def test_set_zeroes_single_cell_zero():
    matrix = [[0]]
    set_zeroes(matrix)
    assert matrix == [[0]]


def test_game_of_life_still_life():
    board = [[1, 1], [1, 1]]
    game_of_life(board)
    assert board == [[1, 1], [1, 1]]


def test_game_of_life_blinker():
    board = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    game_of_life(board)
    assert board == [[0, 0, 0], [1, 1, 1], [0, 0, 0]]


def test_game_of_life_all_dead():
    board = [[0, 0], [0, 0]]
    game_of_life(board)
    assert board == [[0, 0], [0, 0]]
