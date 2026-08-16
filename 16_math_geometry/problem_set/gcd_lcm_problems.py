def fraction_to_decimal(numerator: int, denominator: int) -> str:
    # Problem 25: Fraction To Recurring Decimal
    # Key idea: use gcd to reduce the fraction, then track remainders to detect a repeating cycle.
    # Time:
    # Space:

    raise NotImplementedError


def gcd_of_strings(str1: str, str2: str) -> str:
    # Problem 24: Greatest Common Divisor of Strings
    # Key idea: a common divisor exists only if str1 + str2 == str2 + str1; its length is gcd(len1, len2).
    # Time:
    # Space:

    raise NotImplementedError


def common_factors(a: int, b: int) -> int:
    # Problem 23: Number of Common Factors
    # Key idea: the common factors of a and b are exactly the divisors of gcd(a, b).
    # Time:
    # Space:

    raise NotImplementedError


def smallest_even_multiple(n: int) -> int:
    # Problem 26: Smallest Even Multiple
    # Key idea: the smallest number divisible by both n and 2 is lcm(n, 2), which is n if n is even else 2 * n.
    # Time:
    # Space:

    raise NotImplementedError


def find_gcd(nums: list[int]) -> int:
    # Problem 27: Find Greatest Common Divisor of Array
    # Key idea: gcd of the whole array equals gcd of only its min and max elements.
    # Time:
    # Space:

    raise NotImplementedError


def can_measure_water(jug1_capacity: int, jug2_capacity: int, target: int) -> bool:
    # Problem 28: Water and Jug Problem
    # Key idea: by Bezout, target is reachable iff target <= jug1 + jug2 and target is a multiple of gcd(jug1, jug2).
    # Time:
    # Space:

    raise NotImplementedError
