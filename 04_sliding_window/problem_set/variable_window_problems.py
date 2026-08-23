def max_profit(prices: list[int]) -> int:
    # Problem 10: Best Time to Buy and Sell Stock
    # Key idea: a window that only ever expands right while tracking the minimum seen so far.
    # Time:
    # Space:

    raise NotImplementedError


def length_of_longest_substring(s: str) -> int:
    # Problem 11: Longest Substring Without Repeating Characters
    # Key idea: expand right and shrink left while a duplicate character exists in the window.
    # Time:
    # Space:

    raise NotImplementedError


def min_sub_array_len(target: int, nums: list[int]) -> int:
    # Problem 12: Minimum Size Subarray Sum
    # Key idea: expand right until the sum is valid, then shrink left to find the shortest window.
    # Time:
    # Space:

    raise NotImplementedError


def longest_ones(nums: list[int], k: int) -> int:
    # Problem 13: Max Consecutive Ones III
    # Key idea: shrink left only when the count of zeros in the window exceeds the flip budget.
    # Time:
    # Space:

    raise NotImplementedError


def longest_subarray(nums: list[int]) -> int:
    # Problem 14: Longest Subarray of 1's After Deleting One Element
    # Key idea: window allowing at most one zero; shrink when a second zero enters, answer is length minus one.
    # Time:
    # Space:

    raise NotImplementedError


def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
    # Problem 15: Subarray Product Less Than K
    # Key idea: expand right multiplying in, shrink left while the product is too large, count windows ending at right.
    # Time:
    # Space:

    raise NotImplementedError


def equal_substring(s: str, t: str, max_cost: int) -> int:
    # Problem 16: Get Equal Substrings Within Budget
    # Key idea: expand right accumulating conversion cost, shrink left while the cost exceeds maxCost.
    # Time:
    # Space:

    raise NotImplementedError


def maximum_unique_subarray(nums: list[int]) -> int:
    # Problem 17: Maximum Erasure Value
    # Key idea: variable window of unique elements; shrink left when a duplicate enters, track the max window sum.
    # Time:
    # Space:

    raise NotImplementedError


def max_frequency(nums: list[int], k: int) -> int:
    # Problem 18: Frequency of the Most Frequent Element
    # Key idea: sort, then slide a window where cost to raise all to the right edge stays within k.
    # Time:
    # Space:

    raise NotImplementedError


def longest_nice_subarray(nums: list[int]) -> int:
    # Problem 19: Longest Nice Subarray
    # Key idea: window whose elements are pairwise AND-zero; track a running OR mask and shrink on conflict.
    # Time:
    # Space:

    raise NotImplementedError
