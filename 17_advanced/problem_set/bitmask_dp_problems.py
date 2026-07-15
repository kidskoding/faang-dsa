def can_partition_k_subsets(nums: list[int], k: int) -> bool:
    # Problem 26: Partition to K Equal Sum Subsets
    # Key idea: dp[mask] tracks which numbers are already placed into a completed bucket.
    # Time:
    # Space:

    raise NotImplementedError


def smallest_sufficient_team(req_skills: list[str], people: list[list[str]]) -> list[int]:
    # Problem 27: Smallest Sufficient Team
    # Key idea: dp[skill_mask] stores the smallest team (as a set of people) covering that skill mask.
    # Time:
    # Space:

    raise NotImplementedError


def min_number_of_semesters(n: int, relations: list[list[int]], k: int) -> int:
    # Problem 28: Parallel Courses II
    # Key idea: dp[mask] stores the minimum semesters to complete exactly the courses in
    # mask, transitioning by taking any valid subset of newly-available courses each round.
    # Time:
    # Space:

    raise NotImplementedError


def max_students(seats: list[list[str]]) -> int:
    # Problem 29: Maximum Students Taking Exam
    # Key idea: dp[row][mask] over seat layouts, checking mask validity against
    # broken seats and diagonal neighbors in the prior row.
    # Time:
    # Space:

    raise NotImplementedError


def number_ways(hats: list[list[int]]) -> int:
    # Problem 30: Number Of Ways To Wear Different Hats To Each Other
    # Key idea: assign hats (not people) one at a time; dp[hat][mask] counts ways to cover the people bitmask.
    # Time:
    # Space:

    raise NotImplementedError
