class MedianFinder:
    # Problem 14: Find Median From Data Stream
    # Key idea: max heap for the lower half, min heap for the upper half.

    def __init__(self) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def add_num(self, num: int) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def find_median(self) -> float:
        # Time:
        # Space:

        raise NotImplementedError


def find_maximized_capital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    # Problem 15: IPO
    # Key idea: min heap gates projects by capital, max heap picks the best profit.
    # Time:
    # Space:

    raise NotImplementedError


def median_sliding_window(nums: list[int], k: int) -> list[float]:
    # Problem 16: Sliding Window Median
    # Key idea: two heaps with lazy deletion as the window slides.
    # Time:
    # Space:

    raise NotImplementedError


def get_order(tasks: list[list[int]]) -> list[int]:
    # Problem 17: Single-Threaded CPU
    # Key idea: min heap by availability feeds a min heap by processing time and index.
    # Time:
    # Space:

    raise NotImplementedError


def assign_tasks(servers: list[int], tasks: list[int]) -> list[int]:
    # Problem 18: Process Tasks Using Servers
    # Key idea: one heap of free servers by weight, one heap of busy servers by free time.
    # Time:
    # Space:

    raise NotImplementedError
