from heapq import heapify

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def __len__(self) -> int:
        # TODO: return number of elements
        pass

    def __repr__(self) -> str:
        # TODO: return string representation of internal list
        pass

    def push(self, val: int):
        self.heap.append(val)
        i = len(self.heap) - 1

        self.heapify_up(i)

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
        while i > 0:
            p = self.parent(i)
            
            if self.heap[i] >= self.heap[p]:
                break
            
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p
            
    def heapify_down(self, i: int):
        while i > 0 and self.heap[i] > self.heap[2 * i + 1]

    def parent(self, i: int) -> int:
        return (i - 1) // 2 if i > 0 else -1
    
    def left(self, i: int) -> int:
        return 2 * i + 1
    
    def right(self, i: int) -> int:
        return 2 * i + 2
