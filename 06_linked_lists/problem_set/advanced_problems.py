from __future__ import annotations

from list_node import ListNode


class RandomNode:
    # Node for Copy List With Random Pointer.
    def __init__(
        self,
        val: int = 0,
        next: RandomNode | None = None,
        random: RandomNode | None = None,
    ) -> None:
        self.val = val
        self.next = next
        self.random = random


class MultilevelNode:
    # Node for Flatten A Multilevel Doubly Linked List.
    def __init__(
        self,
        val: int = 0,
        prev: MultilevelNode | None = None,
        next: MultilevelNode | None = None,
        child: MultilevelNode | None = None,
    ) -> None:
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def delete_duplicates_ii(head: ListNode | None) -> ListNode | None:
    # Problem 23: Remove Duplicates From Sorted List II
    # Key idea: dummy head, skip every node in a duplicate run.
    # Time:
    # Space:

    raise NotImplementedError


def copy_random_list(head: RandomNode | None) -> RandomNode | None:
    # Problem 24: Copy List With Random Pointer
    # Key idea: map old nodes to clones, then wire pointers.
    # Time:
    # Space:

    raise NotImplementedError


def flatten(head: MultilevelNode | None) -> MultilevelNode | None:
    # Problem 25: Flatten A Multilevel Doubly Linked List
    # Key idea: splice each child list inline using a stack.
    # Time:
    # Space:

    raise NotImplementedError


class LRUCache:
    # Problem 26: LRU Cache
    # Key idea: hash map plus a doubly linked list for O(1) eviction.

    def __init__(self, capacity: int) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def get(self, key: int) -> int:
        # Time:
        # Space:
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        # Time:
        # Space:
        raise NotImplementedError
