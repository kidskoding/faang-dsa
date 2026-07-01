def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    # Problem 8: Non-overlapping Intervals
    # Key idea: sort by end time, keep the earliest-ending interval, count removals for the rest.
    # Time:
    # Space:

    pass


def partition_labels(s: str) -> list[int]:
    # Problem 9: Partition Labels
    # Key idea: extend the current partition boundary to each character's last occurrence.
    # Time:
    # Space:

    pass


def candy(ratings: list[int]) -> int:
    # Problem 10: Candy
    # Key idea: two greedy passes (left-to-right, right-to-left) taking the max at each index.
    # Time:
    # Space:

    pass


def reconstruct_queue(people: list[list[int]]) -> list[list[int]]:
    # Problem 11: Reconstruct Queue by Height
    # Key idea: sort tall-first, then insert each person at their k-index.
    # Time:
    # Space:

    pass


def find_min_arrow_shots(points: list[list[int]]) -> int:
    # Problem 12: Minimum Number of Arrows to Burst Balloons
    # Key idea: sort by end coordinate, reuse one arrow while balloons overlap the current end.
    # Time:
    # Space:

    pass


def num_rescue_boats(people: list[int], limit: int) -> int:
    # Problem 13: Boats to Save People
    # Key idea: sort by weight, greedily pair the lightest with the heaviest that still fits.
    # Time:
    # Space:

    pass


def least_interval(tasks: list[str], n: int) -> int:
    # Problem 14: Task Scheduler
    # Key idea: greedily schedule the most frequent remaining task first to spread out cooldowns.
    # Time:
    # Space:

    pass
