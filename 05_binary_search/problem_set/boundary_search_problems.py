from collections.abc import Callable


def first_bad_version(n: int, is_bad_version: Callable[[int], bool]) -> int:
    # Problem 3: First Bad Version
    # Key idea: boundary search over a monotonic false...false, true...true predicate.
    # Time:
    # Space:

    raise NotImplementedError


def search_range(nums: list[int], target: int) -> list[int]:
    # Problem 5: Find First and Last Position of Element in Sorted Array
    # Key idea: run two boundary searches, one for the first true and one for the last true.
    # Time:
    # Space:

    raise NotImplementedError


def find_peak_element(nums: list[int]) -> int:
    # Problem 7: Find Peak Element
    # Key idea: binary search using the local slope instead of full sortedness.
    # Time:
    # Space:

    raise NotImplementedError


def find_closest_elements(arr: list[int], k: int, x: int) -> list[int]:
    # Problem 8: Find K Closest Elements
    # Key idea: boundary search for the left edge of a fixed-size window.
    # Time:
    # Space:

    raise NotImplementedError


class TimeMap:
    # Problem 13: Time Based Key-Value Store
    # Key idea: boundary search over stored timestamps to find the latest
    # value at or before a query time.

    def __init__(self) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def get(self, key: str, timestamp: int) -> str:
        # Time:
        # Space:

        raise NotImplementedError


def next_greatest_letter(letters: list[str], target: str) -> str:
    # Problem 14: Find Smallest Letter Greater Than Target
    # Key idea: boundary search for the first element strictly greater than the target, with wraparound.
    # Time:
    # Space:

    pass


def find_kth_positive(arr: list[int], k: int) -> int:
    # Problem 15: Kth Missing Positive Number
    # Key idea: boundary search on the count of missing values before each index.
    # Time:
    # Space:

    pass


def single_non_duplicate(nums: list[int]) -> int:
    # Problem 16: Single Element in a Sorted Array
    # Key idea: binary search on pair-index parity to locate where the pairing breaks.
    # Time:
    # Space:

    pass


def successful_pairs(spells: list[int], potions: list[int], success: int) -> list[int]:
    # Problem 17: Successful Pairs of Spells and Potions
    # Key idea: boundary search per spell over sorted potions for the first passing product.
    # Time:
    # Space:

    pass


class MountainArray:
    # Interface provided by the problem; get and length are the only reads allowed.

    def get(self, index: int) -> int:
        pass

    def length(self) -> int:
        pass


def find_in_mountain_array(target: int, mountain_arr: MountainArray) -> int:
    # Problem 18: Find in Mountain Array
    # Key idea: locate the peak, then run separate ascending and descending searches with a limited API.
    # Time:
    # Space:

    pass
