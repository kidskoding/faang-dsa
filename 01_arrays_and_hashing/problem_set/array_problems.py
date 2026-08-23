def rotate(nums: list[int], k: int) -> None:
    # Problem 17: Rotate Array
    # Key idea: reverse the whole array, then reverse each part in place.
    # Time:
    # Space:

    raise NotImplementedError


def set_zeroes(matrix: list[list[int]]) -> None:
    # Problem 19: Set Matrix Zeroes
    # Key idea: use the first row and column as marker storage.
    # Time:
    # Space:

    raise NotImplementedError


def find_duplicates(nums: list[int]) -> list[int]:
    # Problem 18: Find All Duplicates In An Array
    # Key idea: mark visited values in place using index sign flips.
    # Time:
    # Space:

    raise NotImplementedError


def first_missing_positive(nums: list[int]) -> int:
    # Problem 21: First Missing Positive
    # Key idea: place each value at its index in place, then scan for the first mismatch.
    # Time:
    # Space:

    raise NotImplementedError


class RandomizedSet:
    # Problem 20: Insert Delete GetRandom O(1)
    # Key idea: hash map of value to index paired with a dense array for O(1) random pick.

    def __init__(self) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def insert(self, val: int) -> bool:
        # Time:
        # Space:
        raise NotImplementedError

    def remove(self, val: int) -> bool:
        # Time:
        # Space:
        raise NotImplementedError

    def get_random(self) -> int:
        # Time:
        # Space:
        raise NotImplementedError


def sort_colors(nums: list[int]) -> None:
    # Problem 22: Sort Colors
    # Key idea: Dutch national flag three-way partition in one pass.
    # Time:
    # Space:

    raise NotImplementedError


def find_duplicate(nums: list[int]) -> int:
    # Problem 23: Find The Duplicate Number
    # Key idea: treat values as pointers, Floyd cycle detection to find the repeat.
    # Time:
    # Space:

    raise NotImplementedError


def spiral_order(matrix: list[list[int]]) -> list[int]:
    # Problem 24: Spiral Matrix
    # Key idea: shrink top/bottom/left/right bounds while walking the layers.
    # Time:
    # Space:

    raise NotImplementedError


def rotate_image(matrix: list[list[int]]) -> None:
    # Problem 25: Rotate Image
    # Key idea: transpose in place, then reverse each row.
    # Time:
    # Space:

    raise NotImplementedError


def next_permutation(nums: list[int]) -> None:
    # Problem 26: Next Permutation
    # Key idea: find the rightmost descent, swap with its next-larger successor, reverse the suffix.
    # Time:
    # Space:

    raise NotImplementedError


def increasing_triplet(nums: list[int]) -> bool:
    # Problem 27: Increasing Triplet Subsequence
    # Key idea: track the smallest value and the smallest pair-second seen so far.
    # Time:
    # Space:

    raise NotImplementedError


def maximum_swap(num: int) -> int:
    # Problem 28: Maximum Swap
    # Key idea: last index of each digit, then swap the first digit a bigger one follows.
    # Time:
    # Space:

    raise NotImplementedError
