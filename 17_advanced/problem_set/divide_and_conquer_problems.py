def diff_ways_to_compute(expression: str) -> list[int]:
    # Problem 22: Different Ways To Add Parentheses
    # Key idea: split on each operator, recursively solve both sides, combine every result pair.
    # Time:
    # Space:

    raise NotImplementedError


def get_skyline(buildings: list[list[int]]) -> list[list[int]]:
    # Problem 23: The Skyline Problem
    # Key idea: divide buildings in half, recursively get each skyline, merge with a line sweep.
    # Time:
    # Space:

    raise NotImplementedError


def closest_pair(points: list[list[int]]) -> float:
    # Problem 24: Closest Pair Of Points
    # Key idea: divide by x-coordinate, recurse on each half, combine by checking a narrow strip.
    # Time:
    # Space:

    raise NotImplementedError


def beautiful_array(n: int) -> list[int]:
    # Problem 25: Beautiful Array
    # Key idea: recursively build odd/even-biased halves whose combination avoids arithmetic triples.
    # Time:
    # Space:

    raise NotImplementedError


def max_sub_array(nums: list[int]) -> int:
    # Problem 26: Maximum Subarray
    # Key idea: divide in half; the best subarray is in the left, the right, or crosses the midpoint.
    # Time:
    # Space:

    pass


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    # Problem 27: Median Of Two Sorted Arrays
    # Key idea: binary-search the partition point in the shorter array so both halves balance.
    # Time:
    # Space:

    pass
