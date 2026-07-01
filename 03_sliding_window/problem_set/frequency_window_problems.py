def character_replacement(s: str, k: int) -> int:
    # Problem 6: Longest Repeating Character Replacement
    # Key idea: frequency map tracks the most frequent character; shrink when replacements needed exceed k.
    # Time:
    # Space:

    pass


def check_inclusion(s1: str, s2: str) -> bool:
    # Problem 7: Permutation in String
    # Key idea: fixed-size frequency-map window compared against the target's character counts.
    # Time:
    # Space:

    pass


def find_anagrams(s: str, p: str) -> list[int]:
    # Problem 8: Find All Anagrams in a String
    # Key idea: fixed-size frequency-map window, record every index where counts match.
    # Time:
    # Space:

    pass


def total_fruit(fruits: list[int]) -> int:
    # Problem 9: Fruit Into Baskets
    # Key idea: frequency map window that shrinks while more than two distinct types are present.
    # Time:
    # Space:

    pass


def min_window(s: str, t: str) -> str:
    # Problem 11: Minimum Window Substring
    # Key idea: frequency map with a matched-count check; shrink while the window still satisfies all required counts.
    # Time:
    # Space:

    pass


def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    # Problem 12: Longest Substring with At Most K Distinct Characters
    # Key idea: frequency map shrinks while the number of distinct keys exceeds k.
    # Time:
    # Space:

    pass


def subarrays_with_k_distinct(nums: list[int], k: int) -> int:
    # Problem 13: Subarrays with K Different Integers
    # Key idea: exactly-k count via atMost(k) - atMost(k - 1) using two frequency-map windows.
    # Time:
    # Space:

    pass


def number_of_subarrays(nums: list[int], k: int) -> int:
    # Problem 14: Count Number of Nice Subarrays
    # Key idea: exactly-k count via atMost(k) - atMost(k - 1) applied to a parity/frequency window.
    # Time:
    # Space:

    pass
