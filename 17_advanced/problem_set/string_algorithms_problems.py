def build_failure_table(pattern: str) -> list[int]:
    # Shared KMP failure/prefix table: longest proper prefix that is also a suffix.

    raise NotImplementedError


def str_str(haystack: str, needle: str) -> int:
    # Problem 15: Find The Index Of The First Occurrence In A String
    # Key idea: KMP failure table lets the pattern pointer fall back without rewinding the text.
    # Time:
    # Space:

    raise NotImplementedError


def repeated_string_match(a: str, b: str) -> int:
    # Problem 16: Repeated String Match
    # Key idea: repeat `a` until it is at least as long as `b`, then KMP search for `b`.
    # Time:
    # Space:

    raise NotImplementedError


def shortest_palindrome(s: str) -> str:
    # Problem 17: Shortest Palindrome
    # Key idea: failure table of s + separator + reverse(s) gives the longest palindromic prefix.
    # Time:
    # Space:

    raise NotImplementedError


def longest_prefix(s: str) -> str:
    # Problem 18: Longest Happy Prefix
    # Key idea: the last value of the KMP failure table is the longest prefix that is also a suffix.
    # Time:
    # Space:

    raise NotImplementedError
