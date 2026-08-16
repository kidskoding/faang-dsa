from list_node import ListNode
from problem_set.merge_split_problems import (
    add_two_numbers,
    add_two_numbers_ii,
    merge_in_between,
    merge_k_lists,
    partition,
    sort_list,
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


def test_add_two_numbers_basic():
    result = add_two_numbers(build_list([2, 4, 3]), build_list([5, 6, 4]))
    assert to_list(result) == [7, 0, 8]


def test_add_two_numbers_carry_out():
    result = add_two_numbers(build_list([9, 9]), build_list([1]))
    assert to_list(result) == [0, 0, 1]


def test_add_two_numbers_zeros():
    result = add_two_numbers(build_list([0]), build_list([0]))
    assert to_list(result) == [0]


def test_partition_splits_around_x():
    head = build_list([1, 4, 3, 2, 5, 2])
    result = to_list(partition(head, 3))
    assert result == [1, 2, 2, 4, 3, 5]


def test_partition_all_less():
    head = build_list([1, 2])
    assert to_list(partition(head, 3)) == [1, 2]


def test_sort_list_unsorted():
    assert to_list(sort_list(build_list([4, 2, 1, 3]))) == [1, 2, 3, 4]


def test_sort_list_with_negatives():
    assert to_list(sort_list(build_list([-1, 5, 3, 4, 0]))) == [-1, 0, 3, 4, 5]


def test_sort_list_empty():
    assert sort_list(None) is None


def test_merge_k_lists_basic():
    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    assert to_list(merge_k_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_merge_k_lists_empty():
    assert merge_k_lists([]) is None


def test_merge_k_lists_with_empty_lists():
    assert to_list(merge_k_lists([None, build_list([1]), None])) == [1]


def test_add_two_numbers_ii_normal():
    total = add_two_numbers_ii(build_list([7, 2, 4, 3]), build_list([5, 6, 4]))
    assert to_list(total) == [7, 8, 0, 7]


def test_add_two_numbers_ii_carry_out():
    total = add_two_numbers_ii(build_list([2, 4, 3]), build_list([5, 6, 4]))
    assert to_list(total) == [8, 0, 7]


def test_add_two_numbers_ii_zeros():
    assert to_list(add_two_numbers_ii(build_list([0]), build_list([0]))) == [0]


def test_merge_in_between_normal():
    list1 = build_list([0, 1, 2, 3, 4, 5])
    list2 = build_list([1000000, 1000001, 1000002])

    merged = merge_in_between(list1, 3, 4, list2)
    assert to_list(merged) == [0, 1, 2, 1000000, 1000001, 1000002, 5]


def test_merge_in_between_wider_cut():
    list1 = build_list([0, 1, 2, 3, 4, 5, 6])
    list2 = build_list([1000000, 1000001, 1000002, 1000003, 1000004])

    merged = merge_in_between(list1, 2, 5, list2)
    assert to_list(merged) == [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]
