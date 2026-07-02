def exist(board: list[list[str]], word: str) -> bool:
    # Problem 14: Word Search
    # Key idea: mark the current cell visited before exploring neighbors, unmark on backtrack.
    # Time:
    # Space:

    raise NotImplementedError


def solve_n_queens(n: int) -> list[list[str]]:
    # Problem 15: N-Queens
    # Key idea: place one queen per row, prune on column and diagonal conflicts.
    # Time:
    # Space:

    raise NotImplementedError


def total_n_queens(n: int) -> int:
    # Problem 16: N-Queens II
    # Key idea: same placement search as N-Queens, count solutions instead of building boards.
    # Time:
    # Space:

    raise NotImplementedError


def solve_sudoku(board: list[list[str]]) -> None:
    # Problem 17: Sudoku Solver
    # Key idea: fill the next empty cell, prune on row/column/box constraints, backtrack on failure.
    # Time:
    # Space:

    raise NotImplementedError


def makesquare(matchsticks: list[int]) -> bool:
    # Problem 18: Matchsticks to Square
    # Key idea: assign each matchstick to one of four sides, prune when a side exceeds the target length.
    # Time:
    # Space:

    raise NotImplementedError
