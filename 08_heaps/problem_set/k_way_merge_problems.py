from __future__ import annotations


class ListNode:
    # Node for Merge K Sorted Lists.
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    # Problem 13: Merge K Sorted Lists
    # Key idea: heap holds one candidate per list, always advancing the smallest.
    # Time:
    # Space:

    raise NotImplementedError


def smallest_range(nums: list[list[int]]) -> list[int]:
    # Problem 14: Smallest Range Covering Elements From K Lists
    # Key idea: heap tracks the current min across k lists while a running max bounds the range.
    # Time:
    # Space:

    raise NotImplementedError


class Twitter:
    # Problem 15: Design Twitter
    # Key idea: merge each followee's recent tweets with a heap keyed by timestamp.

    def __init__(self) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def get_news_feed(self, user_id: int) -> list[int]:
        # Time:
        # Space:

        raise NotImplementedError

    def follow(self, follower_id: int, followee_id: int) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        # Time:
        # Space:

        raise NotImplementedError


def employee_free_time(schedule: list[list[list[int]]]) -> list[list[int]]:
    # Problem 16: Employee Free Time
    # Key idea: heap merges each employee's sorted intervals to find shared gaps.
    # Time:
    # Space:

    raise NotImplementedError


def k_smallest_pairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    # Problem 17: Find K Pairs With Smallest Sums
    # Key idea: heap expands the frontier of pair sums across two sorted arrays.
    # Time:
    # Space:

    pass


def kth_smallest(matrix: list[list[int]], k: int) -> int:
    # Problem 18: Kth Smallest Element In A Sorted Matrix
    # Key idea: heap merges sorted rows, popping k times to reach the kth smallest.
    # Time:
    # Space:

    pass


def nth_super_ugly_number(n: int, primes: list[int]) -> int:
    # Problem 19: Super Ugly Number
    # Key idea: heap merges the multiples generated from each prime factor.
    # Time:
    # Space:

    pass
