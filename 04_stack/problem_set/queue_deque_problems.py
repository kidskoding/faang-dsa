class MyQueue:
    # Problem 3: Implement Queue Using Stacks
    # Key idea: two stacks simulate FIFO order.

    def __init__(self) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def push(self, x: int) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def pop(self) -> int:
        # Time:
        # Space:
        raise NotImplementedError

    def peek(self) -> int:
        # Time:
        # Space:
        raise NotImplementedError

    def empty(self) -> bool:
        # Time:
        # Space:
        raise NotImplementedError


class MyStack:
    # Problem 4: Implement Stack Using Queues
    # Key idea: rotate a queue after each push to simulate LIFO order.

    def __init__(self) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def push(self, x: int) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def pop(self) -> int:
        # Time:
        # Space:
        raise NotImplementedError

    def top(self) -> int:
        # Time:
        # Space:
        raise NotImplementedError

    def empty(self) -> bool:
        # Time:
        # Space:
        raise NotImplementedError


class MyCircularDeque:
    # Problem 5: Design Circular Deque
    # Key idea: fixed-size buffer with head and tail indices for O(1) operations at both ends.

    def __init__(self, k: int) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def insert_front(self, value: int) -> bool:
        # Time:
        # Space:
        raise NotImplementedError

    def insert_last(self, value: int) -> bool:
        # Time:
        # Space:
        raise NotImplementedError

    def delete_front(self) -> bool:
        # Time:
        # Space:
        raise NotImplementedError

    def delete_last(self) -> bool:
        # Time:
        # Space:
        raise NotImplementedError

    def get_front(self) -> int:
        # Time:
        # Space:
        raise NotImplementedError

    def get_rear(self) -> int:
        # Time:
        # Space:
        raise NotImplementedError

    def is_empty(self) -> bool:
        # Time:
        # Space:
        raise NotImplementedError

    def is_full(self) -> bool:
        # Time:
        # Space:
        raise NotImplementedError
