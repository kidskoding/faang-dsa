# Redo — 2026-08-22
#
# Second attempt at the four hashing problems that needed help on 2026-08-19.
# Write each from scratch. Do not open hashing_problems.py first.


def is_anagram(s: str, t: str) -> bool:
    # Valid Anagram
    # First time: missed the length guard, so "ab" compared equal to "aab".
    # Time:
    # Space:

    raise NotImplementedError


def group_anagrams(strs: list[str]) -> list[list[str]]:
    # Group Anagrams
    # First time: code was right, complexity was wrong — the sort inside the loop.
    # Time:
    # Space:

    raise NotImplementedError


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # Top K Frequent Elements
    # First time: scanned the map k times, O(n*k). Aim for the bucket sort, O(n).
    # Time:
    # Space:

    raise NotImplementedError


def longest_consecutive(nums: list[int]) -> int:
    # Longest Consecutive Sequence
    # First time: needed the whole insight. Which numbers are worth walking from?
    # Time:
    # Space:

    raise NotImplementedError
