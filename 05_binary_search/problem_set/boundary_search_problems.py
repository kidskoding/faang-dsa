from collections.abc import Callable


def first_bad_version(n: int, is_bad_version: Callable[[int], bool]) -> int:
    # Problem 3: First Bad Version
    # Key idea: boundary search over a monotonic false...false, true...true predicate.
    # Time:
    # Space:

    pass


def search_range(nums: list[int], target: int) -> list[int]:
    # Problem 5: Find First and Last Position of Element in Sorted Array
    # Key idea: run two boundary searches, one for the first true and one for the last true.
    # Time:
    # Space:

    pass


def find_peak_element(nums: list[int]) -> int:
    # Problem 7: Find Peak Element
    # Key idea: binary search using the local slope instead of full sortedness.
    # Time:
    # Space:

    pass


def find_closest_elements(arr: list[int], k: int, x: int) -> list[int]:
    # Problem 8: Find K Closest Elements
    # Key idea: boundary search for the left edge of a fixed-size window.
    # Time:
    # Space:

    pass


class TimeMap:
    # Problem 13: Time Based Key-Value Store
    # Key idea: boundary search over stored timestamps to find the latest
    # value at or before a query time.

    def __init__(self) -> None:
        # Time:
        # Space:

        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Time:
        # Space:

        pass

    def get(self, key: str, timestamp: int) -> str:
        # Time:
        # Space:

        pass
