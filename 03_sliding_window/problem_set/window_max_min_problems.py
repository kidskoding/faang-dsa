def max_sliding_window(nums: list[int], k: int) -> list[int]:
    # Problem 10: Sliding Window Maximum
    # Key idea: monotonic decreasing deque of indices gives the max of each window in O(1).
    # Time:
    # Space:

    raise NotImplementedError


def min_sliding_window(nums: list[int], k: int) -> list[int]:
    # Problem 11: Sliding Window Minimum
    # Key idea: mirror of the maximum; a monotonic increasing deque of indices gives each window min.
    # Time:
    # Space:

    raise NotImplementedError


def longest_subarray(nums: list[int], limit: int) -> int:
    # Problem 12: Longest Continuous Subarray With Absolute Diff <= Limit
    # Key idea: keep two deques (max and min) over the window; shrink left while max - min > limit.
    # Time:
    # Space:

    raise NotImplementedError


def shortest_subarray(nums: list[int], k: int) -> int:
    # Problem 14: Shortest Subarray with Sum at Least K
    # Key idea: monotonic deque over prefix sums to find the shortest qualifying window with negatives allowed.
    # Time:
    # Space:

    raise NotImplementedError


def count_subarrays(nums: list[int], min_k: int, max_k: int) -> int:
    # Problem 15: Count Subarrays With Fixed Bounds
    # Key idea: track last positions of minK, maxK, and out-of-range values to count valid windows per right edge.
    # Time:
    # Space:

    raise NotImplementedError
