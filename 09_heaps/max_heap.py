class MaxHeap:
    def __init__(self):
        # TODO: initialize internal list to store heap elements
        pass

    def __len__(self) -> int:
        # TODO: return number of elements
        pass

    def __repr__(self) -> str:
        # TODO: return string representation of internal list
        pass

    def push(self, val: int):
        # TODO: append val to end of list, then heapify up
        pass

    def pop(self) -> int:
        # TODO: swap root with last element, pop last, heapify down from root
        # raise IndexError if empty
        pass

    def peek(self) -> int:
        # TODO: return root element without removing it
        # raise IndexError if empty
        pass

    def heapify(self, vals: list[int]):
        # TODO: build heap from arbitrary list in O(n)
        # assign list to internal storage, then heapify down from last non-leaf to root
        pass
    
    def heapify_up(self, i: int):
        # TODO: while i > 0 and element at i is greater than its parent, swap and move up
        pass
    
    def heapify_down(self, i: int):
        # TODO: while i has at least one child, find largest child
        # if largest child is greater than element at i, swap and continue down
        pass

    def parent(self, i: int) -> int:
        return (i - 1) // 2 if i > 0 else -1
    
    def left(self, i: int) -> int:
        return 2 * i + 1
    
    def right(self, i: int) -> int:
        return 2 * i + 2
