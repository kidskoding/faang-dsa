def climbing_stairs(n: int) -> int:
    # Problem 1: Climbing Stairs
    # Key idea: dp[i] = dp[i - 1] + dp[i - 2], ways to reach step i.
    # Time:
    # Space:

    raise NotImplementedError


def min_cost_climbing_stairs(cost: list[int]) -> int:
    # Problem 2: Min Cost Climbing Stairs
    # Key idea: dp[i] is the cheapest cost to reach step i from one or two steps back.
    # Time:
    # Space:

    raise NotImplementedError


def rob(nums: list[int]) -> int:
    # Problem 3: House Robber
    # Key idea: dp[i] = max(skip house i, rob house i + dp[i - 2]).
    # Time:
    # Space:

    raise NotImplementedError


def rob_ii(nums: list[int]) -> int:
    # Problem 4: House Robber II
    # Key idea: houses form a circle; run House Robber twice, excluding one end each time.
    # Time:
    # Space:

    raise NotImplementedError


def num_decodings(s: str) -> int:
    # Problem 5: Decode Ways
    # Key idea: dp[i] sums the ways using the last one digit and the last two digits.
    # Time:
    # Space:

    raise NotImplementedError


def max_subarray(nums: list[int]) -> int:
    # Problem 6: Maximum Subarray
    # Key idea: Kadane — best subarray ending at i either extends or restarts.
    # Time:
    # Space:

    raise NotImplementedError


def max_product(nums: list[int]) -> int:
    # Problem 7: Maximum Product Subarray
    # Key idea: track both max and min products ending at i since negatives flip signs.
    # Time:
    # Space:

    raise NotImplementedError


def delete_and_earn(nums: list[int]) -> int:
    # Problem 8: Delete and Earn
    # Key idea: bucket values into points, then it reduces to House Robber over the value line.
    # Time:
    # Space:

    raise NotImplementedError
