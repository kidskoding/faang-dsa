def subsets(nums: list[int]) -> list[list[int]]:
    # Problem 4: Subsets
    # Key idea: save the path at every node, advance start by one each recursion.
    # Time:
    # Space:

    raise NotImplementedError


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    # Problem 5: Subsets II
    # Key idea: sort first, skip repeated values at the same recursion depth.
    # Time:
    # Space:

    raise NotImplementedError


def combine(n: int, k: int) -> list[list[int]]:
    # Problem 6: Combinations
    # Key idea: save the path only when it reaches size k.
    # Time:
    # Space:

    raise NotImplementedError


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    # Problem 7: Combination Sum
    # Key idea: reuse the same index to allow repeated picks, prune when the running sum exceeds the target.
    # Time:
    # Space:

    raise NotImplementedError


def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    # Problem 8: Combination Sum II
    # Key idea: sort first, advance past duplicates at the same depth, no reuse of the same index.
    # Time:
    # Space:

    raise NotImplementedError


def combination_sum3(k: int, n: int) -> list[list[int]]:
    # Problem 9: Combination Sum III
    # Key idea: fixed count and target sum both bound the recursion.
    # Time:
    # Space:

    raise NotImplementedError
