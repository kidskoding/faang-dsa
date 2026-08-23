class MyQueue:
    # Problem 15: Implement Queue Using Stacks
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
    # Problem 16: Implement Stack Using Queues
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
    # Problem 17: Design Circular Deque
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


class RecentCounter:
    # Problem 18: Number Of Recent Calls
    # Key idea: queue of timestamps; pop from the front until inside the sliding time window.

    def __init__(self) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def ping(self, t: int) -> int:
        # Time:
        # Space:
        raise NotImplementedError


class MyCircularQueue:
    # Problem 19: Design Circular Queue
    # Key idea: fixed-size ring buffer with head index and a count for O(1) enqueue/dequeue.

    def __init__(self, k: int) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def en_queue(self, value: int) -> bool:
        # Time:
        # Space:
        raise NotImplementedError

    def de_queue(self) -> bool:
        # Time:
        # Space:
        raise NotImplementedError

    def front(self) -> int:
        # Time:
        # Space:
        raise NotImplementedError

    def rear(self) -> int:
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


class MovingAverage:
    # Problem 20: Moving Average From Data Stream
    # Key idea: fixed-size FIFO window; keep a running sum, evict the front when it overflows.

    def __init__(self, size: int) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def next(self, val: int) -> float:
        # Time:
        # Space:
        raise NotImplementedError


class FrontMiddleBackQueue:
    # Problem 21: Design Front Middle Back Queue
    # Key idea: two deques split at the middle; rebalance after each op to keep the front half sized correctly.

    def __init__(self) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def push_front(self, val: int) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def push_middle(self, val: int) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def push_back(self, val: int) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def pop_front(self) -> int:
        # Time:
        # Space:
        raise NotImplementedError

    def pop_middle(self) -> int:
        # Time:
        # Space:
        raise NotImplementedError

    def pop_back(self) -> int:
        # Time:
        # Space:
        raise NotImplementedError


class HitCounter:
    # Problem 22: Design Hit Counter
    # Key idea: queue of timestamps, evict anything outside the 300 second window.
    # Time:
    # Space:

    def __init__(self) -> None:
        raise NotImplementedError

    def hit(self, timestamp: int) -> None:
        raise NotImplementedError

    def get_hits(self, timestamp: int) -> int:
        raise NotImplementedError


class BrowserHistory:
    # Problem 23: Design Browser History
    # Key idea: one list plus a cursor; visiting truncates everything ahead of it.
    # Time:
    # Space:

    def __init__(self, homepage: str) -> None:
        raise NotImplementedError

    def visit(self, url: str) -> None:
        raise NotImplementedError

    def back(self, steps: int) -> str:
        raise NotImplementedError

    def forward(self, steps: int) -> str:
        raise NotImplementedError


class MRUQueue:
    # Problem 24: Design Most Recently Used Queue
    # Key idea: fetch the kth element and move it to the back.
    # Time:
    # Space:

    def __init__(self, n: int) -> None:
        raise NotImplementedError

    def fetch(self, k: int) -> int:
        raise NotImplementedError
