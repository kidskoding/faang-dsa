from collections.abc import Callable


def search(nums: list[int], target: int) -> int:
    # Problem 1: Binary Search
    # Key idea: repeatedly cut the sorted search space in half.
    # Time:
    # Space:

    raise NotImplementedError


def search_insert(nums: list[int], target: int) -> int:
    # Problem 2: Search Insert Position
    # Key idea: find the first index where target could be inserted.
    # Time:
    # Space:

    raise NotImplementedError


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    # Problem 3: Search a 2D Matrix
    # Key idea: treat the row-sorted, column-sorted grid as one flattened sorted array.
    # Time:
    # Space:

    raise NotImplementedError


def search_matrix_ii(matrix: list[list[int]], target: int) -> bool:
    # Problem 4: Search a 2D Matrix II
    # Key idea: start at a sorted corner and eliminate a full row or column each step.
    # Time:
    # Space:

    raise NotImplementedError


def guess_number(n: int, guess: Callable[[int], int]) -> int:
    # Problem 5: Guess Number Higher or Lower
    # Key idea: exact-match search driven by a comparison oracle instead of array reads.
    # Time:
    # Space:

    raise NotImplementedError


def find_peak_grid(mat: list[list[int]]) -> list[int]:
    # Problem 6: Find a Peak Element II
    # Key idea: binary search columns, take the row-max, move toward the larger neighbour.
    # Time:
    # Space:

    raise NotImplementedError


def h_index(citations: list[int]) -> int:
    # Problem 7: H-Index II
    # Key idea: binary search for the first index whose citations cover the papers left.
    # Time:
    # Space:

    raise NotImplementedError


class ArrayReader:
    # Interface provided by the problem; get returns 2^31 - 1 past the end.

    def get(self, index: int) -> int:
        raise NotImplementedError


def search_unknown_size(reader: ArrayReader, target: int) -> int:
    # Problem 8: Search in a Sorted Array of Unknown Size
    # Key idea: double the bound until it overshoots, then binary search that range.
    # Time:
    # Space:

    raise NotImplementedError
