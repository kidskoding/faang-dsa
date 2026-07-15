class Robot:
    # Interface provided by the problem; the robot's absolute position is hidden.

    def move(self) -> bool:
        raise NotImplementedError

    def turn_left(self) -> None:
        raise NotImplementedError

    def turn_right(self) -> None:
        raise NotImplementedError

    def clean(self) -> None:
        raise NotImplementedError


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


def unique_paths_iii(grid: list[list[int]]) -> int:
    # Problem 19: Unique Paths III
    # Key idea: DFS every path that covers all empty cells, marking and unmarking cells as visited.
    # Time:
    # Space:

    raise NotImplementedError


def clean_room(robot: Robot) -> None:
    # Problem 20: Robot Room Cleaner
    # Key idea: DFS with a relative-coordinate visited set, turning the robot back to its prior heading on backtrack.
    # Time:
    # Space:

    raise NotImplementedError


def can_partition_k_subsets(nums: list[int], k: int) -> bool:
    # Problem 22: Partition to K Equal Sum Subsets
    # Key idea: fill one bucket at a time to the target sum, sort descending and skip duplicate starts to prune.
    # Time:
    # Space:

    raise NotImplementedError


def add_operators(num: str, target: int) -> list[str]:
    # Problem 23: Expression Add Operators
    # Key idea: choose "+", "-", "*", or concatenation between digits, carrying the
    # last operand to undo multiplication precedence.
    # Time:
    # Space:

    raise NotImplementedError


def word_break(s: str, word_dict: list[str]) -> list[str]:
    # Problem 24: Word Break II
    # Key idea: choose each next dictionary-word prefix, memoizing suffixes to avoid re-exploring dead ends.
    # Time:
    # Space:

    raise NotImplementedError


def remove_invalid_parentheses(s: str) -> list[str]:
    # Problem 25: Remove Invalid Parentheses
    # Key idea: compute the minimum removals, then backtrack over which parentheses to drop, deduping at each depth.
    # Time:
    # Space:

    raise NotImplementedError


def judge_point24(cards: list[int]) -> bool:
    # Problem 26: 24 Game
    # Key idea: pick two numbers and an operator, recurse on the reduced multiset until one value reaches 24.
    # Time:
    # Space:

    raise NotImplementedError
