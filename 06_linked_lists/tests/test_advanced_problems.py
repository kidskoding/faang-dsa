from list_node import ListNode
from problem_set.advanced_problems import (
    MultilevelNode,
    RandomNode,
    copy_random_list,
    delete_duplicates_ii,
    flatten,
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


def test_delete_duplicates_ii_removes_all_dupes():
    head = build_list([1, 2, 3, 3, 4, 4, 5])
    assert to_list(delete_duplicates_ii(head)) == [1, 2, 5]


def test_delete_duplicates_ii_leading_dupes():
    head = build_list([1, 1, 1, 2, 3])
    assert to_list(delete_duplicates_ii(head)) == [2, 3]


def test_delete_duplicates_ii_empty():
    assert delete_duplicates_ii(None) is None


def build_random_list(values: list[int], randoms: list[int | None]) -> RandomNode | None:
    if not values:
        return None
    nodes = [RandomNode(value) for value in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, target in enumerate(randoms):
        nodes[i].random = nodes[target] if target is not None else None
    return nodes[0]


def test_copy_random_list_is_deep_copy():
    original = build_random_list([7, 13, 11, 10, 1], [None, 0, 4, 2, 0])
    clone = copy_random_list(original)

    orig_nodes, clone_nodes = [], []
    o, c = original, clone
    while o:
        orig_nodes.append(o)
        clone_nodes.append(c)
        o, c = o.next, c.next

    assert [n.val for n in clone_nodes] == [n.val for n in orig_nodes]
    for oc in clone_nodes:
        assert oc not in orig_nodes
    for i, o in enumerate(orig_nodes):
        if o.random is None:
            assert clone_nodes[i].random is None
        else:
            assert clone_nodes[i].random is clone_nodes[orig_nodes.index(o.random)]


def test_copy_random_list_empty():
    assert copy_random_list(None) is None


def flatten_to_list(head: MultilevelNode | None) -> list[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def test_flatten_multilevel():
    # 1 - 2 - 3 - 4
    #         |
    #         5 - 6
    nodes = [MultilevelNode(i) for i in range(1, 7)]
    nodes[0].next = nodes[1]
    nodes[1].prev = nodes[0]
    nodes[1].next = nodes[2]
    nodes[2].prev = nodes[1]
    nodes[2].next = nodes[3]
    nodes[3].prev = nodes[2]
    nodes[2].child = nodes[4]
    nodes[4].next = nodes[5]
    nodes[5].prev = nodes[4]

    result = flatten(nodes[0])
    assert flatten_to_list(result) == [1, 2, 3, 5, 6, 4]

    # prev links should be consistent and no child pointers remain
    curr = result
    prev = None
    while curr:
        assert curr.prev is prev
        assert curr.child is None
        prev = curr
        curr = curr.next


def test_flatten_empty():
    assert flatten(None) is None
