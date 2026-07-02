def permute(nums: list[int]) -> list[list[int]]:
    # Problem 10: Permutations
    # Key idea: track used values with a boolean array, build the path position by position.
    # Time:
    # Space:

    raise NotImplementedError


def permute_unique(nums: list[int]) -> list[list[int]]:
    # Problem 11: Permutations II
    # Key idea: sort first, skip a duplicate value at the same depth unless the previous copy was used.
    # Time:
    # Space:

    raise NotImplementedError


def partition(s: str) -> list[list[str]]:
    # Problem 12: Palindrome Partitioning
    # Key idea: choose the next substring cut, only recurse when the prefix is a palindrome.
    # Time:
    # Space:

    raise NotImplementedError


def restore_ip_addresses(s: str) -> list[str]:
    # Problem 13: Restore IP Addresses
    # Key idea: choose 1-3 digit segments, prune on the 0-255 and leading-zero constraints.
    # Time:
    # Space:

    raise NotImplementedError
