class NumArray:
    # Problem 29: Range Sum Query - Immutable
    # Key idea: precompute a prefix sum array for O(1) range queries.

    def __init__(self, nums: list[int]) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def sum_range(self, left: int, right: int) -> int:
        # Time:
        # Space:
        raise NotImplementedError


def subarray_sum(nums: list[int], k: int) -> int:
    # Problem 30: Subarray Sum Equals K
    # Key idea: running prefix sum plus a count hash map.
    # Time:
    # Space:

    raise NotImplementedError


def check_subarray_sum(nums: list[int], k: int) -> bool:
    # Problem 31: Continuous Subarray Sum
    # Key idea: running prefix sum modulo k, hash map of first-seen remainder index.
    # Time:
    # Space:

    raise NotImplementedError


class NumMatrix:
    # Problem 33: Range Sum Query 2D - Immutable
    # Key idea: 2D prefix sum with inclusion-exclusion.

    def __init__(self, matrix: list[list[int]]) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Time:
        # Space:
        raise NotImplementedError


def subarrays_div_by_k(nums: list[int], k: int) -> int:
    # Problem 32: Subarrays Divisible By K
    # Key idea: running prefix sum modulo k, count matching remainders.
    # Time:
    # Space:

    raise NotImplementedError


def max_sub_array_len(nums: list[int], k: int) -> int:
    # Problem 34: Maximum Size Subarray Sum Equals k
    # Key idea: prefix sum with first-seen index in a hash map to get longest subarray.
    # Time:
    # Space:

    raise NotImplementedError


def pivot_index(nums: list[int]) -> int:
    # Problem 37: Find Pivot Index
    # Key idea: the pivot is where the left prefix sum equals the right suffix sum.
    # Time:
    # Space:

    raise NotImplementedError


def left_right_difference(nums: list[int]) -> list[int]:
    # Problem 38: Left and Right Sum Differences
    # Key idea: build a left prefix-sum array and a right suffix-sum array, take the absolute difference per index.
    # Time:
    # Space:

    raise NotImplementedError


def max_score(s: str) -> int:
    # Problem 39: Maximum Score After Splitting a String
    # Key idea: prefix zeros on the left plus suffix ones on the right, maximized over every split.
    # Time:
    # Space:

    raise NotImplementedError


def ways_to_split_array(nums: list[int]) -> int:
    # Problem 40: Number of Ways to Split Array
    # Key idea: sweep the split point comparing the left prefix sum against the remaining suffix sum.
    # Time:
    # Space:

    raise NotImplementedError


def find_max_length(nums: list[int]) -> int:
    # Problem 35: Contiguous Array
    # Key idea: map 0 to -1, track first index of each running prefix sum.
    # Time:
    # Space:

    raise NotImplementedError


def product_except_self(nums: list[int]) -> list[int]:
    # Problem 36: Product of Array Except Self
    # Key idea: one prefix pass and one suffix pass, never dividing.
    # Time:
    # Space:

    raise NotImplementedError


def matrix_block_sum(mat: list[list[int]], k: int) -> list[list[int]]:
    # Problem 41: Matrix Block Sum
    # Key idea: 2D prefix sums with inclusion-exclusion over a clamped window.
    # Time:
    # Space:

    raise NotImplementedError


def max_sum_two_no_overlap(nums: list[int], first_len: int, second_len: int) -> int:
    # Problem 42: Maximum Sum of Two Non-Overlapping Subarrays
    # Key idea: prefix sums plus a sweep tracking the best earlier window, both orderings.
    # Time:
    # Space:

    raise NotImplementedError
