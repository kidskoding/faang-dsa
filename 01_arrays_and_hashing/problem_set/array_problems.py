def rotate(nums: list[int], k: int) -> None:
    # Problem 4: Rotate Array
    # Key idea: reverse the whole array, then reverse each part in place.
    # Time:
    # Space:

    raise NotImplementedError


def product_except_self(nums: list[int]) -> list[int]:
    # Problem 10: Product Of Array Except Self
    # Key idea: prefix products times suffix products.
    # Time:
    # Space:

    raise NotImplementedError


def set_zeroes(matrix: list[list[int]]) -> None:
    # Problem 16: Set Matrix Zeroes
    # Key idea: use the first row and column as marker storage.
    # Time:
    # Space:

    raise NotImplementedError


def find_duplicates(nums: list[int]) -> list[int]:
    # Problem 17: Find All Duplicates In An Array
    # Key idea: mark visited values in place using index sign flips.
    # Time:
    # Space:

    raise NotImplementedError


def first_missing_positive(nums: list[int]) -> int:
    # Problem 19: First Missing Positive
    # Key idea: place each value at its index in place, then scan for the first mismatch.
    # Time:
    # Space:

    raise NotImplementedError


class RandomizedSet:
    # Problem 24: Insert Delete GetRandom O(1)
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
    # Problem 25: Sort Colors
    # Key idea: Dutch national flag three-way partition in one pass.
    # Time:
    # Space:

    raise NotImplementedError


def find_duplicate(nums: list[int]) -> int:
    # Problem 26: Find The Duplicate Number
    # Key idea: treat values as pointers, Floyd cycle detection to find the repeat.
    # Time:
    # Space:

    raise NotImplementedError


def spiral_order(matrix: list[list[int]]) -> list[int]:
    # Problem 27: Spiral Matrix
    # Key idea: shrink top/bottom/left/right bounds while walking the layers.
    # Time:
    # Space:

    raise NotImplementedError


def rotate_image(matrix: list[list[int]]) -> None:
    # Problem 28: Rotate Image
    # Key idea: transpose in place, then reverse each row.
    # Time:
    # Space:

    raise NotImplementedError
