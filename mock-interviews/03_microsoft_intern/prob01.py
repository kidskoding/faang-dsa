# Input: Two LinkedLists, l1 and l2
# Output: Another LinkedList that is the reversed sum of l1 and l2

# Time: O(max(m, n)) -> m = len(l1), n = len(l2)
# Space: O(1)

from list_node import ListNode

def prob01(l1, l2):
    dummy = ListNode(0)
    temp = dummy
    carry = 0

    curr_l1 = l1
    curr_l2 = l2
    while curr_l1 or curr_l2 or carry:
        digit1 = curr_l1.val if curr_l1 else 0
        digit2 = curr_l2.val if curr_l2 else 0

        total = digit1 + digit2 + carry
        res = total % 10
        carry = total // 10

        temp.next = ListNode(res)
        temp = temp.next

        if curr_l1:
            curr_l1 = curr_l1.next
        if curr_l2:
            curr_l2 = curr_l2.next

    return dummy.next

# 7 -> 0 -> 8
