def max_sliding_window(nums: list[int], k: int) -> list[int]:
    # Problem 15: Sliding Window Maximum
    # Key idea: monotonic decreasing deque of indices; the front is always the window max.
    # Time:
    # Space:

    raise NotImplementedError


def shortest_subarray(nums: list[int], k: int) -> int:
    # Problem 17: Shortest Subarray with Sum at Least K
    # Key idea: over prefix sums, keep an increasing deque; pop front when prefix[i] - prefix[front] >= k.
    # Time:
    # Space:

    raise NotImplementedError


def continuous_subarrays(nums: list[int]) -> int:
    # Problem 18: Continuous Subarrays
    # Key idea: two deques track window max and min; shrink left while max - min > 2, count windows per right edge.
    # Time:
    # Space:

    pass


def find_max_value_of_equation(points: list[list[int]], k: int) -> int:
    # Problem 19: Max Value of Equation
    # Key idea: monotonic decreasing deque of y - x keeps the best partner within the |xi - xj| <= k window.
    # Time:
    # Space:

    pass


def maximum_robots(charge_times: list[int], running_costs: list[int], budget: int) -> int:
    # Problem 20: Maximum Number of Robots Within Budget
    # Key idea: sliding window with a monotonic deque for the running max charge time against the running sum budget.
    # Time:
    # Space:

    pass
