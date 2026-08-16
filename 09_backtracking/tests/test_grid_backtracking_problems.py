from problem_set.grid_backtracking_problems import (
    add_operators,
    can_partition_k_subsets,
    clean_room,
    exist,
    judge_point24,
    makesquare,
    remove_invalid_parentheses,
    solve_n_queens,
    solve_sudoku,
    total_n_queens,
    unique_paths_iii,
    word_break,
)


class _GridRobot:
    """Concrete stand-in for the Robot interface the problem hands you.

    The robot only knows "did the move succeed"; its absolute position stays
    hidden from the solution, exactly as on the real judge.
    """

    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, grid: list[list[int]], row: int, col: int) -> None:
        self.grid = grid
        self.row = row
        self.col = col
        self.facing = 0
        self.cleaned: set[tuple[int, int]] = set()

    def move(self) -> bool:
        row_step, col_step = self.DIRECTIONS[self.facing]
        next_row, next_col = self.row + row_step, self.col + col_step
        in_bounds = 0 <= next_row < len(self.grid) and 0 <= next_col < len(self.grid[0])
        if in_bounds and self.grid[next_row][next_col] == 1:
            self.row, self.col = next_row, next_col
            return True
        return False

    def turn_left(self) -> None:
        self.facing = (self.facing - 1) % 4

    def turn_right(self) -> None:
        self.facing = (self.facing + 1) % 4

    def clean(self) -> None:
        self.cleaned.add((self.row, self.col))


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


def test_unique_paths_iii_with_obstacle():
    assert unique_paths_iii([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2


def test_unique_paths_iii_open_grid():
    assert unique_paths_iii([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4


def test_unique_paths_iii_unreachable():
    assert unique_paths_iii([[0, 1], [2, 0]]) == 0


def test_clean_room_cleans_every_reachable_cell():
    grid = [
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]
    robot = _GridRobot(grid, 1, 3)
    clean_room(robot)

    assert len(robot.cleaned) == 30


def test_clean_room_small_room():
    robot = _GridRobot([[1, 1], [1, 1]], 0, 0)
    clean_room(robot)

    assert robot.cleaned == {(0, 0), (0, 1), (1, 0), (1, 1)}


def test_can_partition_k_subsets_possible():
    assert can_partition_k_subsets([4, 3, 2, 3, 5, 2, 1], 4) is True


def test_can_partition_k_subsets_impossible():
    assert can_partition_k_subsets([1, 2, 3, 4], 3) is False


def test_add_operators_target_six():
    assert sorted(add_operators("123", 6)) == ["1*2*3", "1+2+3"]


def test_add_operators_multiplication_precedence():
    assert sorted(add_operators("232", 8)) == ["2*3+2", "2+3*2"]


def test_add_operators_no_solution():
    assert add_operators("3456237490", 9191) == []


def test_word_break_two_sentences():
    words = ["cat", "cats", "and", "sand", "dog"]
    assert sorted(word_break("catsanddog", words)) == ["cat sand dog", "cats and dog"]


def test_word_break_no_sentence():
    words = ["cats", "dog", "sand", "and", "cat"]
    assert word_break("catsandog", words) == []


def test_remove_invalid_parentheses_normal():
    assert sorted(remove_invalid_parentheses("()())()")) == ["(())()", "()()()"]


def test_remove_invalid_parentheses_removes_everything():
    assert remove_invalid_parentheses(")(") == [""]


def test_judge_point24_reachable():
    assert judge_point24([4, 1, 8, 7]) is True


def test_judge_point24_unreachable():
    assert judge_point24([1, 2, 1, 2]) is False
