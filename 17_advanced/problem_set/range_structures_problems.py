class FenwickTree:
    # Shared 1-indexed binary indexed tree supporting point update and prefix sum query.

    def __init__(self, n: int) -> None:
        raise NotImplementedError

    def update(self, index: int, delta: int) -> None:
        raise NotImplementedError

    def prefix_sum(self, index: int) -> int:
        raise NotImplementedError

    def range_sum(self, left: int, right: int) -> int:
        raise NotImplementedError


class NumArray:
    # Problem 11: Range Sum Query - Mutable

    def __init__(self, nums: list[int]) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def update(self, index: int, val: int) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def sum_range(self, left: int, right: int) -> int:
        # Time:
        # Space:

        raise NotImplementedError


class NumMatrix:
    # Problem 12: Range Sum Query 2D - Mutable

    def __init__(self, matrix: list[list[int]]) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def update(self, row: int, col: int, val: int) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def sum_region(
        self, row1: int, col1: int, row2: int, col2: int
    ) -> int:
        # Time:
        # Space:

        raise NotImplementedError


def count_smaller(nums: list[int]) -> list[int]:
    # Problem 13: Count Of Smaller Numbers After Self
    # Key idea: Fenwick tree over coordinate-compressed values, scanned right to left.
    # Time:
    # Space:

    raise NotImplementedError


def count_range_sum(nums: list[int], lower: int, upper: int) -> int:
    # Problem 14: Count Of Range Sum
    # Key idea: Fenwick tree over compressed prefix sums counts sums in [lower, upper].
    # Time:
    # Space:

    raise NotImplementedError
