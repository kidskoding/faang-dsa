from __future__ import annotations


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next: ListNode | None = None,
    ) -> None:
        self.val = val
        self.next = next
