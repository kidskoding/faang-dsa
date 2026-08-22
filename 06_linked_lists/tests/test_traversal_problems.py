from list_node import ListNode
from problem_set.traversal_problems import (
    MyLinkedList,
    delete_duplicates,
    delete_node,
    get_decimal_value,
    get_intersection_node,
    merge_two_lists,
    remove_elements,
    reverse_list,
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


def test_reverse_list_empty():
    assert reverse_list(None) is None


def test_reverse_list_single():
    assert to_list(reverse_list(build_list([1]))) == [1]


def test_reverse_list_multiple():
    assert to_list(reverse_list(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]


def test_merge_two_lists_both_empty():
    assert merge_two_lists(None, None) is None


def test_merge_two_lists_one_empty():
    assert to_list(merge_two_lists(build_list([1, 3, 5]), None)) == [1, 3, 5]


def test_merge_two_lists_interleaved():
    merged = merge_two_lists(build_list([1, 2, 4]), build_list([1, 3, 4]))
    assert to_list(merged) == [1, 1, 2, 3, 4, 4]


def test_delete_duplicates_empty():
    assert delete_duplicates(None) is None


def test_delete_duplicates_no_dupes():
    assert to_list(delete_duplicates(build_list([1, 2, 3]))) == [1, 2, 3]


def test_delete_duplicates_with_dupes():
    assert to_list(delete_duplicates(build_list([1, 1, 2, 3, 3]))) == [1, 2, 3]


def test_delete_node_middle():
    head = build_list([4, 5, 1, 9])
    delete_node(node_at(head, 1))
    assert to_list(head) == [4, 1, 9]


def test_remove_elements_removes_matches():
    head = build_list([1, 2, 6, 3, 4, 5, 6])
    assert to_list(remove_elements(head, 6)) == [1, 2, 3, 4, 5]


def test_remove_elements_all_match():
    assert remove_elements(build_list([7, 7, 7]), 7) is None


def test_get_intersection_node_overlap():
    shared = build_list([8, 4, 5])
    head_a = build_list([4, 1])
    node_at(head_a, 1).next = shared
    head_b = build_list([5, 6, 1])
    node_at(head_b, 2).next = shared

    assert get_intersection_node(head_a, head_b) is shared


def test_get_intersection_node_no_overlap():
    head_a = build_list([2, 6, 4])
    head_b = build_list([1, 5])

    assert get_intersection_node(head_a, head_b) is None


def test_get_decimal_value_normal():
    assert get_decimal_value(build_list([1, 0, 1])) == 5


def test_get_decimal_value_zero():
    assert get_decimal_value(build_list([0])) == 0


def test_get_decimal_value_all_ones():
    assert get_decimal_value(build_list([1, 1, 1, 1])) == 15


def test_my_linked_list_add_and_get():
    linked_list = MyLinkedList()
    linked_list.add_at_head(1)
    linked_list.add_at_tail(3)
    linked_list.add_at_index(1, 2)

    assert linked_list.get(1) == 2


def test_my_linked_list_delete_shifts_indices():
    linked_list = MyLinkedList()
    linked_list.add_at_head(1)
    linked_list.add_at_tail(3)
    linked_list.add_at_index(1, 2)
    linked_list.delete_at_index(1)

    assert linked_list.get(1) == 3


def test_my_linked_list_get_out_of_range():
    linked_list = MyLinkedList()
    linked_list.add_at_head(1)

    assert linked_list.get(5) == -1


def test_delete_node_deeper_in_the_list():
    head = build_list([1, 2, 3, 4, 5])
    delete_node(node_at(head, 2))

    assert to_list(head) == [1, 2, 4, 5]


def test_delete_node_second_to_last():
    head = build_list([1, 2])
    delete_node(head)

    assert to_list(head) == [2]
