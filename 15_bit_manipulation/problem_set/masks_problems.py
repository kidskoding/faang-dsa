def get_sum(a: int, b: int) -> int:
    # Problem 9: Sum of Two Integers
    # Key idea: XOR gives the sum without carry, AND-and-shift gives the carry, repeat until no carry.
    # Time:
    # Space:

    raise NotImplementedError


def range_bitwise_and(left: int, right: int) -> int:
    # Problem 10: Bitwise AND of Numbers Range
    # Key idea: shift both bounds right together until they match, then shift the shared prefix back.
    # Time:
    # Space:

    raise NotImplementedError


def min_flips(a: int, b: int, c: int) -> int:
    # Problem 11: Minimum Flips to Make a OR b Equal to c
    # Key idea: compare a, b, and c bit by bit and count the flips needed to fix each mismatch.
    # Time:
    # Space:

    raise NotImplementedError


def gray_code(n: int) -> list[int]:
    # Problem 12: Gray Code
    # Key idea: generate the sequence with i ^ (i >> 1) so consecutive codes differ by one bit.
    # Time:
    # Space:

    raise NotImplementedError


def valid_utf8(data: list[int]) -> bool:
    # Problem 13: UTF-8 Validation
    # Key idea: mask the leading bits of each byte to decode and verify continuation counts.
    # Time:
    # Space:

    raise NotImplementedError
