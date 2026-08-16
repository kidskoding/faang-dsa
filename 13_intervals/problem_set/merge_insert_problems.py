class SummaryRanges:
    # Problem 9: Data Stream As Disjoint Intervals
    # Key idea: keep a sorted, merged interval set and re-merge around each insert.

    def __init__(self) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def add_num(self, value: int) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def get_intervals(self) -> list[list[int]]:
        # Time:
        # Space:

        raise NotImplementedError


def merge(intervals: list[list[int]]) -> list[list[int]]:
    # Problem 6: Merge Intervals
    # Key idea: sort by start, extend the current merged interval or start a new one.
    # Time:
    # Space:

    raise NotImplementedError


def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    # Problem 7: Insert Interval
    # Key idea: append intervals fully before, merge overlapping, append fully after.
    # Time:
    # Space:

    raise NotImplementedError


def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    # Problem 8: Non-overlapping Intervals
    # Key idea: sort by end, greedily keep the interval that finishes earliest.
    # Time:
    # Space:

    raise NotImplementedError


def remove_covered_intervals(intervals: list[list[int]]) -> int:
    # Problem 10: Remove Covered Intervals
    # Key idea: sort by start asc and end desc, drop intervals covered by the last kept end.
    # Time:
    # Space:

    raise NotImplementedError
