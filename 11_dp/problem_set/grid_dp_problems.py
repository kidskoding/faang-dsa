def unique_paths(m: int, n: int) -> int:
    # Problem 6: Unique Paths
    # Key idea: dp[r][c] = dp[r - 1][c] + dp[r][c - 1].
    # Time:
    # Space:

    raise NotImplementedError


def unique_paths_with_obstacles(obstacle_grid: list[list[int]]) -> int:
    # Problem 7: Unique Paths II
    # Key idea: same recurrence as Unique Paths, but an obstacle cell is forced to 0.
    # Time:
    # Space:

    raise NotImplementedError


def min_path_sum(grid: list[list[int]]) -> int:
    # Problem 8: Minimum Path Sum
    # Key idea: dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1]).
    # Time:
    # Space:

    raise NotImplementedError


def minimum_total(triangle: list[list[int]]) -> int:
    # Problem 9: Triangle
    # Key idea: min path sum from the bottom row upward on a triangular grid.
    # Time:
    # Space:

    raise NotImplementedError


def maximal_square(matrix: list[list[str]]) -> int:
    # Problem 10: Maximal Square
    # Key idea: dp[r][c] is the largest square side ending at that cell.
    # Time:
    # Space:

    raise NotImplementedError
