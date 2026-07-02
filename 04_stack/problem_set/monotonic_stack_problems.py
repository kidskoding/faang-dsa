class StockSpanner:
    # Problem 12: Online Stock Span
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
    # Problem 9: Daily Temperatures
    # Key idea: monotonic decreasing stack of indices resolved by the next warmer day.
    # Time:
    # Space:

    raise NotImplementedError


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    # Problem 10: Next Greater Element I
    # Key idea: monotonic stack over the full array plus a hash map lookup for the subset query.
    # Time:
    # Space:

    raise NotImplementedError


def next_greater_elements(nums: list[int]) -> list[int]:
    # Problem 11: Next Greater Element II
    # Key idea: monotonic stack over a circular array by iterating twice the length.
    # Time:
    # Space:

    raise NotImplementedError


def asteroid_collision(asteroids: list[int]) -> list[int]:
    # Problem 13: Asteroid Collision
    # Key idea: stack resolves collisions immediately as each new asteroid arrives.
    # Time:
    # Space:

    raise NotImplementedError


def remove_k_digits(num: str, k: int) -> str:
    # Problem 14: Remove K Digits
    # Key idea: monotonic increasing stack removes larger trailing digits while removals remain.
    # Time:
    # Space:

    raise NotImplementedError


def largest_rectangle_area(heights: list[int]) -> int:
    # Problem 16: Largest Rectangle In Histogram
    # Key idea: monotonic increasing stack tracks left/right boundaries for each bar's max rectangle.
    # Time:
    # Space:

    raise NotImplementedError


def trap(height: list[int]) -> int:
    # Problem 17: Trapping Rain Water
    # Key idea: monotonic decreasing stack resolves trapped water between bars as taller bars appear.
    # Time:
    # Space:

    raise NotImplementedError
