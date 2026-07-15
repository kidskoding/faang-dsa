def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    # Problem 8: Non-overlapping Intervals
    # Key idea: sort by end time, keep the earliest-ending interval, count removals for the rest.
    # Time:
    # Space:

    raise NotImplementedError


def partition_labels(s: str) -> list[int]:
    # Problem 9: Partition Labels
    # Key idea: extend the current partition boundary to each character's last occurrence.
    # Time:
    # Space:

    raise NotImplementedError


def candy(ratings: list[int]) -> int:
    # Problem 10: Candy
    # Key idea: two greedy passes (left-to-right, right-to-left) taking the max at each index.
    # Time:
    # Space:

    raise NotImplementedError


def reconstruct_queue(people: list[list[int]]) -> list[list[int]]:
    # Problem 11: Reconstruct Queue by Height
    # Key idea: sort tall-first, then insert each person at their k-index.
    # Time:
    # Space:

    raise NotImplementedError


def find_min_arrow_shots(points: list[list[int]]) -> int:
    # Problem 12: Minimum Number of Arrows to Burst Balloons
    # Key idea: sort by end coordinate, reuse one arrow while balloons overlap the current end.
    # Time:
    # Space:

    raise NotImplementedError


def num_rescue_boats(people: list[int], limit: int) -> int:
    # Problem 13: Boats to Save People
    # Key idea: sort by weight, greedily pair the lightest with the heaviest that still fits.
    # Time:
    # Space:

    raise NotImplementedError


def least_interval(tasks: list[str], n: int) -> int:
    # Problem 14: Task Scheduler
    # Key idea: greedily schedule the most frequent remaining task first to spread out cooldowns.
    # Time:
    # Space:

    raise NotImplementedError


def is_n_straight_hand(hand: list[int], group_size: int) -> bool:
    # Problem 15: Hand of Straights
    # Key idea: repeatedly start a run from the smallest remaining card and consume consecutive values.
    # Time:
    # Space:

    pass


def advantage_count(nums1: list[int], nums2: list[int]) -> list[int]:
    # Problem 16: Advantage Shuffle
    # Key idea: sort both arrays, beat each opponent with the smallest sufficient card or dump the weakest.
    # Time:
    # Space:

    pass


def eliminate_maximum(dist: list[int], speed: list[int]) -> int:
    # Problem 17: Eliminate Maximum Number of Monsters
    # Key idea: sort by arrival time and shoot the soonest-arriving monster each minute.
    # Time:
    # Space:

    pass


def partition_disjoint(nums: list[int]) -> int:
    # Problem 18: Partition Array into Disjoint Intervals
    # Key idea: prefix-max boundary greedy.
    # Time:
    # Space:

    pass


def is_possible(nums: list[int]) -> bool:
    # Problem 19: Split Array into Consecutive Subsequences
    # Key idea: greedily append each number to an existing run before starting a new length-3 subsequence.
    # Time:
    # Space:

    pass
