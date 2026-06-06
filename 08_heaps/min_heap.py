class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val: int):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")

        min_val = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.heapify_down(0)

        return min_val

    def peek(self):
        if not self.heap:
            raise IndexError("peek from empty heap")

        return self.heap[0]

    def build_heap(self, vals: list[int]):
        self.heap = vals
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def heapify_up(self, i: int):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heapify_down(self, i: int):
        size = len(self.heap)
        smallest = i

        while True:
            left = self.left(i)
            right = self.right(i)

            if left < size and self.heap[smallest] > self.heap[left]:
                smallest = left
            if right < size and self.heap[smallest] > self.heap[right]:
                smallest = right
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break

    def parent(self, i: int):
        return (i - 1) // 2

    def left(self, i: int):
        return 2 * i + 1

    def right(self, i: int):
        return 2 * i + 2
