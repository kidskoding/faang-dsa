def find_max_average(nums: list[int], k: int) -> float:
    # Problem 1: Maximum Average Subarray I
    # Key idea: fixed-size window sum, add the incoming value and remove the outgoing one.
    # Time:
    # Space:

    raise NotImplementedError


def max_vowels(s: str, k: int) -> int:
    # Problem 2: Maximum Number of Vowels in a Substring of Given Length
    # Key idea: slide a size-k window, +1 when a vowel enters, -1 when a vowel leaves.
    # Time:
    # Space:

    raise NotImplementedError


def num_of_subarrays(arr: list[int], k: int, threshold: int) -> int:
    # Problem 3: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
    # Key idea: average >= threshold means window sum >= k * threshold; count qualifying windows.
    # Time:
    # Space:

    raise NotImplementedError


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    # Problem 4: Contains Duplicate II
    # Key idea: fixed-size window of at most k indices held in a set; a hit inside the set is a duplicate.
    # Time:
    # Space:

    raise NotImplementedError


def count_good_substrings(s: str) -> int:
    # Problem 5: Substrings of Size Three with Distinct Characters
    # Key idea: fixed-size window of length three, count windows whose characters are all distinct.
    # Time:
    # Space:

    raise NotImplementedError


def max_satisfied(customers: list[int], grumpy: list[int], minutes: int) -> int:
    # Problem 6: Grumpy Bookstore Owner
    # Key idea: fixed-size window over grumpy minutes to maximize the extra customers the technique saves.
    # Time:
    # Space:

    raise NotImplementedError


def max_score(card_points: list[int], k: int) -> int:
    # Problem 7: Maximum Points You Can Obtain from Cards
    # Key idea: minimize the fixed-size middle window so the taken ends (its complement) are maximized.
    # Time:
    # Space:

    raise NotImplementedError


def get_averages(nums: list[int], k: int) -> list[int]:
    # Problem 8: K Radius Subarray Averages
    # Key idea: fixed window of width 2k+1 with a running sum, -1 where it overhangs.
    # Time:
    # Space:

    raise NotImplementedError


def get_subarray_beauty(nums: list[int], k: int, x: int) -> list[int]:
    # Problem 9: Sliding Subarray Beauty
    # Key idea: values are bounded, so count them instead of sorting each window.
    # Time:
    # Space:

    raise NotImplementedError
