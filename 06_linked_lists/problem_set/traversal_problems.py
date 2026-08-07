from list_node import ListNode


def reverse_list(head: ListNode | None) -> ListNode | None:
    # Problem 1: Reverse Linked List
    # Key idea: walk the list flipping each next pointer.
    # Time:
    # Space:

    raise NotImplementedError


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    # Problem 2: Merge Two Sorted Lists
    # Key idea: weave two lists with a dummy head.
    # Time:
    # Space:

    raise NotImplementedError


def delete_duplicates(head: ListNode | None) -> ListNode | None:
    # Problem 3: Remove Duplicates From Sorted List
    # Key idea: skip a node whose value equals the next.
    # Time:
    # Space:

    raise NotImplementedError


def delete_node(node: ListNode) -> None:
    # Problem 4: Delete Node In A Linked List
    # Key idea: copy the next node's value, then unlink it.
    # Time:
    # Space:

    raise NotImplementedError


def remove_elements(head: ListNode | None, val: int) -> ListNode | None:
    # Problem 5: Remove Linked List Elements
    # Key idea: dummy head plus a previous pointer to unlink matches.
    # Time:
    # Space:

    raise NotImplementedError


def get_intersection_node(head_a: ListNode | None, head_b: ListNode | None) -> ListNode | None:
    # Problem 6: Intersection Of Two Linked Lists
    # Key idea: two pointers that switch lists to align lengths.
    # Time:
    # Space:

    raise NotImplementedError


class MyLinkedList:
    # Problem 7: Design Linked List
    # Key idea: implement get, insert, and delete on a from-scratch list.

    def __init__(self) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def get(self, index: int) -> int:
        # Time:
        # Space:

        raise NotImplementedError

    def add_at_head(self, val: int) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def add_at_tail(self, val: int) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def add_at_index(self, index: int, val: int) -> None:
        # Time:
        # Space:

        raise NotImplementedError

    def delete_at_index(self, index: int) -> None:
        # Time:
        # Space:

        raise NotImplementedError


def get_decimal_value(head: ListNode | None) -> int:
    # Problem 8: Convert Binary Number In A Linked List To Integer
    # Key idea: single pass building the value with shift-and-add.
    # Time:
    # Space:

    raise NotImplementedError
