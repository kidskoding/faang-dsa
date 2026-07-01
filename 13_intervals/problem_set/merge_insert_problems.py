class SummaryRanges:
    # Problem 7: Data Stream As Disjoint Intervals
    # Key idea: keep a sorted, merged interval set and re-merge around each insert.

    def __init__(self) -> None:
        # Time:
        # Space:

        pass

    def add_num(self, value: int) -> None:
        # Time:
        # Space:

        pass

    def get_intervals(self) -> list[list[int]]:
        # Time:
        # Space:

        pass


def merge(intervals: list[list[int]]) -> list[list[int]]:
    # Problem 4: Merge Intervals
    # Key idea: sort by start, extend the current merged interval or start a new one.
    # Time:
    # Space:

    pass


def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    # Problem 5: Insert Interval
    # Key idea: append intervals fully before, merge overlapping, append fully after.
    # Time:
    # Space:

    pass


def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    # Problem 6: Non-overlapping Intervals
    # Key idea: sort by end, greedily keep the interval that finishes earliest.
    # Time:
    # Space:

    pass
