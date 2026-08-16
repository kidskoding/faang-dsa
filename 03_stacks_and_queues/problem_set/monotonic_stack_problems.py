class StockSpanner:
    # Problem 25: Online Stock Span
    # Key idea: monotonic stack of (price, span) pairs collapsed as new prices arrive.

    def __init__(self) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def next(self, price: int) -> int:
        # Time:
        # Space:
        raise NotImplementedError


def daily_temperatures(temperatures: list[int]) -> list[int]:
    # Problem 23: Daily Temperatures
    # Key idea: monotonic decreasing stack of indices resolved by the next warmer day.
    # Time:
    # Space:

    raise NotImplementedError


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    # Problem 22: Next Greater Element I
    # Key idea: monotonic stack over the full array plus a hash map lookup for the subset query.
    # Time:
    # Space:

    raise NotImplementedError


def next_greater_elements(nums: list[int]) -> list[int]:
    # Problem 24: Next Greater Element II
    # Key idea: monotonic stack over a circular array by iterating twice the length.
    # Time:
    # Space:

    raise NotImplementedError


def asteroid_collision(asteroids: list[int]) -> list[int]:
    # Problem 26: Asteroid Collision
    # Key idea: stack resolves collisions immediately as each new asteroid arrives.
    # Time:
    # Space:

    raise NotImplementedError


def remove_k_digits(num: str, k: int) -> str:
    # Problem 27: Remove K Digits
    # Key idea: monotonic increasing stack removes larger trailing digits while removals remain.
    # Time:
    # Space:

    raise NotImplementedError


def largest_rectangle_area(heights: list[int]) -> int:
    # Problem 28: Largest Rectangle In Histogram
    # Key idea: monotonic increasing stack tracks left/right boundaries for each bar's max rectangle.
    # Time:
    # Space:

    raise NotImplementedError


def trap(height: list[int]) -> int:
    # Problem 29: Trapping Rain Water
    # Key idea: monotonic decreasing stack resolves trapped water between bars as taller bars appear.
    # Time:
    # Space:

    raise NotImplementedError


def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    # Problem 30: Car Fleet
    # Key idea: sort by position and use a stack of arrival times to merge cars into fleets.
    # Time:
    # Space:

    raise NotImplementedError


def remove_duplicate_letters(s: str) -> str:
    # Problem 31: Remove Duplicate Letters
    # Key idea: monotonic increasing stack keeps the lexicographically smallest result using last-occurrence counts.
    # Time:
    # Space:

    raise NotImplementedError


def find132pattern(nums: list[int]) -> bool:
    # Problem 32: 132 Pattern
    # Key idea: right-to-left monotonic stack tracks the largest valid "2" below each candidate "3".
    # Time:
    # Space:

    raise NotImplementedError


def sum_subarray_mins(arr: list[int]) -> int:
    # Problem 33: Sum Of Subarray Minimums
    # Key idea: monotonic stack counts subarrays where each element is the minimum via span boundaries.
    # Time:
    # Space:

    raise NotImplementedError


def sub_array_ranges(nums: list[int]) -> int:
    # Problem 34: Sum Of Subarray Ranges
    # Key idea: monotonic-stack contribution counting for both subarray minimums and maximums.
    # Time:
    # Space:

    raise NotImplementedError


def maximal_rectangle(matrix: list[list[str]]) -> int:
    # Problem 35: Maximal Rectangle
    # Key idea: build per-row histograms and apply the largest-rectangle monotonic stack to each.
    # Time:
    # Space:

    raise NotImplementedError
