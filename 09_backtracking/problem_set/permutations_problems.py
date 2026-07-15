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


def get_permutation(n: int, k: int) -> str:
    # Problem 14: Permutation Sequence
    # Key idea: pick each digit by factorial block count rather than enumerating every permutation.
    # Time:
    # Space:

    pass


def num_tile_possibilities(tiles: str) -> int:
    # Problem 15: Letter Tile Possibilities
    # Key idea: count sequences from a multiset of tiles, using per-depth counts to skip duplicate letters.
    # Time:
    # Space:

    pass
