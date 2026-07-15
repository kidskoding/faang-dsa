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


def next_larger_nodes(head: ListNode | None) -> list[int]:
    # Problem 27: Next Greater Node In Linked List
    # Key idea: monotonic stack over the values in one pass.
    # Time:
    # Space:

    pass


def reverse_even_length_groups(head: ListNode | None) -> ListNode | None:
    # Problem 28: Reverse Nodes In Even Length Groups
    # Key idea: walk growing groups, reverse only the even-length ones.
    # Time:
    # Space:

    pass
