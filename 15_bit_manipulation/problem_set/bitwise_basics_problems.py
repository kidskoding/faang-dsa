def hamming_weight(n: int) -> int:
    # Problem 1: Number of 1 Bits
    # Key idea: repeatedly clear the lowest set bit with n & (n - 1) and count steps.
    # Time:
    # Space:

    raise NotImplementedError


def count_bits(n: int) -> list[int]:
    # Problem 2: Counting Bits
    # Key idea: build a DP table where ans[i] = ans[i >> 1] + (i & 1).
    # Time:
    # Space:

    raise NotImplementedError


def reverse_bits(n: int) -> int:
    # Problem 5: Reverse Bits
    # Key idea: shift bits out of n while shifting them into the result.
    # Time:
    # Space:

    raise NotImplementedError


def is_power_of_two(n: int) -> bool:
    # Problem 3: Power of Two
    # Key idea: a positive power of two has exactly one set bit, so n & (n - 1) == 0.
    # Time:
    # Space:

    raise NotImplementedError


def is_power_of_four(n: int) -> bool:
    # Problem 4: Power of Four
    # Key idea: one set bit plus that bit sitting at an even position.
    # Time:
    # Space:

    raise NotImplementedError


def hamming_distance(x: int, y: int) -> int:
    # Problem 6: Hamming Distance
    # Key idea: popcount of x ^ y counts the differing bit positions.
    # Time:
    # Space:

    raise NotImplementedError


def bitwise_complement(n: int) -> int:
    # Problem 7: Complement of Base 10 Integer
    # Key idea: XOR against an all-ones mask sized to the number's bit length.
    # Time:
    # Space:

    raise NotImplementedError


def divide(dividend: int, divisor: int) -> int:
    # Problem 8: Divide Two Integers
    # Key idea: subtract shifted (doubled) divisors to build the quotient bit by bit.
    # Time:
    # Space:

    raise NotImplementedError
