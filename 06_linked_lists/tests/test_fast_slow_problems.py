from list_node import ListNode
from problem_set.fast_slow_problems import (
    delete_middle,
    detect_cycle,
    has_cycle,
    is_palindrome,
    middle_node,
    remove_nth_from_end,
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


def node_at(head: ListNode | None, index: int) -> ListNode | None:
    for _ in range(index):
        head = head.next
    return head


def make_cycle(values: list[int], pos: int) -> ListNode | None:
    head = build_list(values)
    if pos < 0:
        return head
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = node_at(head, pos)
    return head


def test_middle_node_odd():
    assert middle_node(build_list([1, 2, 3, 4, 5])).val == 3


def test_middle_node_even_returns_second():
    assert middle_node(build_list([1, 2, 3, 4, 5, 6])).val == 4


def test_middle_node_single():
    assert middle_node(build_list([1])).val == 1


def test_has_cycle_true():
    assert has_cycle(make_cycle([3, 2, 0, -4], 1))


def test_has_cycle_false():
    assert not has_cycle(build_list([1, 2, 3]))


def test_has_cycle_empty():
    assert not has_cycle(None)


def test_detect_cycle_returns_entry():
    head = make_cycle([3, 2, 0, -4], 1)
    assert detect_cycle(head) is node_at(head, 1)


def test_detect_cycle_none_when_acyclic():
    assert detect_cycle(build_list([1, 2])) is None


def test_is_palindrome_true():
    assert is_palindrome(build_list([1, 2, 2, 1]))


def test_is_palindrome_odd_true():
    assert is_palindrome(build_list([1, 2, 3, 2, 1]))


def test_is_palindrome_false():
    assert not is_palindrome(build_list([1, 2]))


def test_is_palindrome_single():
    assert is_palindrome(build_list([1]))


def test_remove_nth_from_end_middle():
    head = build_list([1, 2, 3, 4, 5])
    assert to_list(remove_nth_from_end(head, 2)) == [1, 2, 3, 5]


def test_remove_nth_from_end_head():
    head = build_list([1, 2])
    assert to_list(remove_nth_from_end(head, 2)) == [2]


def test_remove_nth_from_end_single():
    assert remove_nth_from_end(build_list([1]), 1) is None


def test_delete_middle_odd_length():
    head = build_list([1, 3, 4, 7, 1, 2, 6])
    assert to_list(delete_middle(head)) == [1, 3, 4, 1, 2, 6]


def test_delete_middle_even_length():
    head = build_list([1, 2, 3, 4])
    assert to_list(delete_middle(head)) == [1, 2, 4]


def test_delete_middle_single_node():
    assert delete_middle(build_list([1])) is None


def test_delete_middle_two_nodes():
    assert to_list(delete_middle(build_list([2, 1]))) == [2]
