def letter_combinations(digits: str) -> list[str]:
    # Problem 1: Letter Combinations of a Phone Number
    # Key idea: choose one letter per digit position, recurse to the next digit.
    # Time:
    # Space:

    raise NotImplementedError


def generate_parentheses(n: int) -> list[str]:
    # Problem 2: Generate Parentheses
    # Key idea: choose "(" or ")" while tracking open/close counts as a pruning constraint.
    # Time:
    # Space:

    raise NotImplementedError


def count_arrangement(n: int) -> int:
    # Problem 3: Beautiful Arrangement
    # Key idea: place numbers one position at a time, pruning on the divisibility constraint.
    # Time:
    # Space:

    raise NotImplementedError


def letter_case_permutation(s: str) -> list[str]:
    # Problem 4: Letter Case Permutation
    # Key idea: at each letter branch on lower/upper case, pass digits straight through.
    # Time:
    # Space:

    raise NotImplementedError


def max_unique_split(s: str) -> int:
    # Problem 5: Split A String Into The Max Number Of Unique Substrings
    # Key idea: try every cut, add the piece to a seen set on the way down and remove it on the way back up.
    # Time:
    # Space:

    raise NotImplementedError
