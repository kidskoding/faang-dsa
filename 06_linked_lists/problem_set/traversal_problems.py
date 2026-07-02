from list_node import ListNode


def reverse_list(head: ListNode | None) -> ListNode | None:
    # Problem 1: Reverse Linked List
    # Key idea: walk the list flipping each next pointer.
    # Time:
    # Space:

    if not head:
        return None

    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    # Problem 2: Merge Two Sorted Lists
    # Key idea: weave two lists with a dummy head.
    # Time:
    # Space:

    dummy = ListNode(0)
    tail = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    tail.next = list1 if list1 else list2
    return dummy.next


def delete_duplicates(head: ListNode | None) -> ListNode | None:
    # Problem 3: Remove Duplicates From Sorted List
    # Key idea: skip a node whose value equals the next.
    # Time:
    # Space:

    if not head:
        return None

    curr = head
    while curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head


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
