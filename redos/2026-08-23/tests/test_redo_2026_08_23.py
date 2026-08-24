from redo_2026_08_23 import is_valid_sudoku, longest_consecutive


def _valid_board() -> list[list[str]]:
    return [
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


def _sparse_board() -> list[list[str]]:
    return [["." for _ in range(9)] for _ in range(9)]


def test_longest_consecutive_normal():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4


def test_longest_consecutive_empty():
    assert longest_consecutive([]) == 0


def test_longest_consecutive_with_duplicates():
    assert longest_consecutive([1, 2, 0, 1]) == 3


def test_longest_consecutive_with_negatives():
    assert longest_consecutive([-3, -2, -1, 5, 7]) == 3


def test_longest_consecutive_single_element():
    assert longest_consecutive([7]) == 1


def test_is_valid_sudoku_true():
    assert is_valid_sudoku(_valid_board()) is True


def test_is_valid_sudoku_false_duplicate_only_in_box():
    board = _sparse_board()
    board[0][0] = "5"
    board[1][1] = "5"

    assert is_valid_sudoku(board) is False


def test_is_valid_sudoku_false_duplicate_only_in_row():
    board = _sparse_board()
    board[3][0] = "7"
    board[3][8] = "7"

    assert is_valid_sudoku(board) is False


def test_is_valid_sudoku_false_duplicate_in_column():
    board = _sparse_board()
    board[0][4] = "2"
    board[6][4] = "2"

    assert is_valid_sudoku(board) is False


def test_is_valid_sudoku_same_value_in_different_boxes_is_fine():
    board = _sparse_board()
    board[0][0] = "5"
    board[4][4] = "5"
    board[8][8] = "5"

    assert is_valid_sudoku(board) is True


def test_is_valid_sudoku_empty_board():
    assert is_valid_sudoku(_sparse_board()) is True
