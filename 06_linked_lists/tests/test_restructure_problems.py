from list_node import ListNode
from problem_set.restructure_problems import (
    odd_even_list,
    reorder_list,
    rotate_right,
    split_list_to_parts,
)


def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    curr = dummy
    for value in values:
        curr.next = ListNode(value)
        curr = curr.next
    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def test_reorder_list_even():
    head = build_list([1, 2, 3, 4])
    reorder_list(head)
    assert to_list(head) == [1, 4, 2, 3]


def test_reorder_list_odd():
    head = build_list([1, 2, 3, 4, 5])
    reorder_list(head)
    assert to_list(head) == [1, 5, 2, 4, 3]


def test_rotate_right_basic():
    head = build_list([1, 2, 3, 4, 5])
    assert to_list(rotate_right(head, 2)) == [4, 5, 1, 2, 3]


def test_rotate_right_wraps_around():
    head = build_list([0, 1, 2])
    assert to_list(rotate_right(head, 4)) == [2, 0, 1]


def test_rotate_right_empty():
    assert rotate_right(None, 3) is None


def test_odd_even_list_basic():
    head = build_list([1, 2, 3, 4, 5])
    assert to_list(odd_even_list(head)) == [1, 3, 5, 2, 4]


def test_odd_even_list_even_length():
    head = build_list([2, 1, 3, 5, 6, 4, 7])
    assert to_list(odd_even_list(head)) == [2, 3, 6, 7, 1, 5, 4]


def test_split_list_to_parts_uneven():
    parts = split_list_to_parts(build_list([1, 2, 3]), 5)
    assert [to_list(part) for part in parts] == [[1], [2], [3], [], []]


def test_split_list_to_parts_balanced():
    parts = split_list_to_parts(build_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)
    assert [to_list(part) for part in parts] == [
        [1, 2, 3, 4],
        [5, 6, 7],
        [8, 9, 10],
    ]
