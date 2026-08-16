from list_node import ListNode
from problem_set.reversal_problems import (
    reverse_between,
    reverse_k_group,
    swap_nodes,
    swap_pairs,
    twin_sum,
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


def test_reverse_between_middle():
    head = build_list([1, 2, 3, 4, 5])
    assert to_list(reverse_between(head, 2, 4)) == [1, 4, 3, 2, 5]


def test_reverse_between_from_head():
    head = build_list([1, 2, 3])
    assert to_list(reverse_between(head, 1, 3)) == [3, 2, 1]


def test_reverse_between_single_span():
    head = build_list([1, 2, 3])
    assert to_list(reverse_between(head, 2, 2)) == [1, 2, 3]


def test_swap_pairs_even():
    assert to_list(swap_pairs(build_list([1, 2, 3, 4]))) == [2, 1, 4, 3]


def test_swap_pairs_odd_leaves_last():
    assert to_list(swap_pairs(build_list([1, 2, 3]))) == [2, 1, 3]


def test_swap_pairs_empty():
    assert swap_pairs(None) is None


def test_reverse_k_group_exact():
    head = build_list([1, 2, 3, 4, 5])
    assert to_list(reverse_k_group(head, 2)) == [2, 1, 4, 3, 5]


def test_reverse_k_group_full_group():
    head = build_list([1, 2, 3, 4, 5])
    assert to_list(reverse_k_group(head, 3)) == [3, 2, 1, 4, 5]


def test_reverse_k_group_k_one():
    head = build_list([1, 2, 3])
    assert to_list(reverse_k_group(head, 1)) == [1, 2, 3]


def test_twin_sum_normal():
    assert twin_sum(build_list([5, 4, 2, 1])) == 6


def test_twin_sum_middle_pair_wins():
    assert twin_sum(build_list([4, 2, 2, 3])) == 7


def test_twin_sum_two_nodes():
    assert twin_sum(build_list([1, 100000])) == 100001


def test_swap_nodes_normal():
    assert to_list(swap_nodes(build_list([1, 2, 3, 4, 5]), 2)) == [1, 4, 3, 2, 5]


def test_swap_nodes_longer_list():
    head = build_list([7, 9, 6, 6, 7, 8, 3, 0, 9, 5])
    assert to_list(swap_nodes(head, 5)) == [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]


def test_swap_nodes_single_node():
    assert to_list(swap_nodes(build_list([1]), 1)) == [1]
