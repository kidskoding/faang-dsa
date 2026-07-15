def character_replacement(s: str, k: int) -> int:
    # Problem 6: Longest Repeating Character Replacement
    # Key idea: frequency map tracks the most frequent character; shrink when replacements needed exceed k.
    # Time:
    # Space:

    raise NotImplementedError


def check_inclusion(s1: str, s2: str) -> bool:
    # Problem 7: Permutation in String
    # Key idea: fixed-size frequency-map window compared against the target's character counts.
    # Time:
    # Space:

    raise NotImplementedError


def find_anagrams(s: str, p: str) -> list[int]:
    # Problem 8: Find All Anagrams in a String
    # Key idea: fixed-size frequency-map window, record every index where counts match.
    # Time:
    # Space:

    raise NotImplementedError


def total_fruit(fruits: list[int]) -> int:
    # Problem 9: Fruit Into Baskets
    # Key idea: frequency map window that shrinks while more than two distinct types are present.
    # Time:
    # Space:

    raise NotImplementedError


def min_window(s: str, t: str) -> str:
    # Problem 11: Minimum Window Substring
    # Key idea: frequency map with a matched-count check; shrink while the window still satisfies all required counts.
    # Time:
    # Space:

    raise NotImplementedError


def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    # Problem 12: Longest Substring with At Most K Distinct Characters
    # Key idea: frequency map shrinks while the number of distinct keys exceeds k.
    # Time:
    # Space:

    raise NotImplementedError


def subarrays_with_k_distinct(nums: list[int], k: int) -> int:
    # Problem 13: Subarrays with K Different Integers
    # Key idea: exactly-k count via atMost(k) - atMost(k - 1) using two frequency-map windows.
    # Time:
    # Space:

    raise NotImplementedError


def number_of_subarrays(nums: list[int], k: int) -> int:
    # Problem 14: Count Number of Nice Subarrays
    # Key idea: exactly-k count via atMost(k) - atMost(k - 1) applied to a parity/frequency window.
    # Time:
    # Space:

    raise NotImplementedError


def number_of_substrings(s: str) -> int:
    # Problem 15: Number of Substrings Containing All Three Characters
    # Key idea: shrink left while all three characters are present, add left valid substrings for each right.
    # Time:
    # Space:

    pass


def num_subarrays_with_sum(nums: list[int], goal: int) -> int:
    # Problem 16: Binary Subarrays With Sum
    # Key idea: exact-sum count via atMost(goal) - atMost(goal - 1) over a 0/1 window.
    # Time:
    # Space:

    pass


def balanced_string(s: str) -> int:
    # Problem 17: Replace the Substring for Balanced String
    # Key idea: shrink the smallest window whose removal lets the outside counts be rebalanced to n / 4 each.
    # Time:
    # Space:

    pass


def find_substring(s: str, words: list[str]) -> list[int]:
    # Problem 18: Substring with Concatenation of All Words
    # Key idea: word-length-stepped windows with a word frequency map, one pass per starting offset.
    # Time:
    # Space:

    pass


def min_window_subsequence(s1: str, s2: str) -> str:
    # Problem 19: Minimum Window Subsequence
    # Key idea: forward-scan then backtrack two-pointer window (not a classic monotonic slide).
    # Time:
    # Space:

    pass
