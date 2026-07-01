def hamming_weight(n: int) -> int:
    # Problem 1: Number of 1 Bits
    # Key idea: repeatedly clear the lowest set bit with n & (n - 1) and count steps.
    # Time:
    # Space:

    pass


def count_bits(n: int) -> list[int]:
    # Problem 2: Counting Bits
    # Key idea: build a DP table where ans[i] = ans[i >> 1] + (i & 1).
    # Time:
    # Space:

    pass


def reverse_bits(n: int) -> int:
    # Problem 3: Reverse Bits
    # Key idea: shift bits out of n while shifting them into the result.
    # Time:
    # Space:

    pass


def is_power_of_two(n: int) -> bool:
    # Problem 4: Power of Two
    # Key idea: a positive power of two has exactly one set bit, so n & (n - 1) == 0.
    # Time:
    # Space:

    pass


def is_power_of_four(n: int) -> bool:
    # Problem 5: Power of Four
    # Key idea: one set bit plus that bit sitting at an even position.
    # Time:
    # Space:

    pass
