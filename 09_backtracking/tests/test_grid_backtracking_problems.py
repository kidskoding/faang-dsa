from problem_set.grid_backtracking_problems import (
    exist,
    makesquare,
    solve_n_queens,
    solve_sudoku,
    total_n_queens,
)


def test_exist_single_cell_match():
    assert exist([["A"]], "A") is True


def test_exist_normal_found():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert exist(board, "ABCCED") is True


def test_exist_not_found():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert exist(board, "ABCB") is False


def test_solve_n_queens_n_equals_one():
    assert solve_n_queens(1) == [["Q"]]


def test_solve_n_queens_n_equals_two_no_solution():
    assert solve_n_queens(2) == []


def test_solve_n_queens_n_equals_four_count():
    assert len(solve_n_queens(4)) == 2


def test_total_n_queens_n_equals_four():
    assert total_n_queens(4) == 2


def test_total_n_queens_n_equals_one():
    assert total_n_queens(1) == 1


def test_solve_sudoku_solves_in_place():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    solve_sudoku(board)
    assert all("." not in row for row in board)


def test_makesquare_normal_true():
    assert makesquare([1, 1, 2, 2, 2]) is True


def test_makesquare_cannot_split():
    assert makesquare([3, 3, 3, 3, 4]) is False


def test_makesquare_too_few_sticks():
    assert makesquare([1, 1, 1]) is False
