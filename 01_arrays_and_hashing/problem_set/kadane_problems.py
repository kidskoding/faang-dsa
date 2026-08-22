def max_subarray(nums: list[int]) -> int:
    # Problem 36: Maximum Subarray
    # Key idea: Kadane's algorithm, extend or restart at each index.
    # Time:
    # Space:

    raise NotImplementedError


def max_profit(prices: list[int]) -> int:
    # Problem 35: Best Time To Buy And Sell Stock
    # Key idea: track the running minimum while scanning left to right.
    # Time:
    # Space:

    raise NotImplementedError


def max_product_subarray(nums: list[int]) -> int:
    # Problem 37: Maximum Product Subarray
    # Key idea: Kadane's variant tracking running max and min for sign flips.
    # Time:
    # Space:

    raise NotImplementedError


def max_subarray_sum_circular(nums: list[int]) -> int:
    # Problem 38: Maximum Sum Circular Subarray
    # Key idea: Kadane for both max subarray and total-minus-min subarray.
    # Time:
    # Space:

    raise NotImplementedError


def max_absolute_sum(nums: list[int]) -> int:
    # Problem 39: Maximum Absolute Sum of Any Subarray
    # Key idea: run Kadane for both max and min subarray, answer is max(max_sum, -min_sum).
    # Time:
    # Space:

    raise NotImplementedError


def max_turbulence_size(arr: list[int]) -> int:
    # Problem 40: Longest Turbulent Subarray
    # Key idea: Kadane-style up/down run lengths, extend when the comparison sign alternates.
    # Time:
    # Space:

    raise NotImplementedError


def k_concatenation_max_sum(arr: list[int], k: int) -> int:
    # Problem 41: K-Concatenation Maximum Sum
    # Key idea: Kadane on one/two copies, add (k-2) whole-array sums when the total is positive.
    # Time:
    # Space:

    raise NotImplementedError


def maximum_sum(arr: list[int]) -> int:
    # Problem 50: Maximum Subarray Sum with One Deletion
    # Key idea: two Kadane states — no deletion used, and one already used.
    # Time:
    # Space:

    raise NotImplementedError
