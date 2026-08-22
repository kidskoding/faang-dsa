from problem_set.queue_deque_problems import (
    FrontMiddleBackQueue,
    MovingAverage,
    MyCircularDeque,
    MyCircularQueue,
    MyQueue,
    MyStack,
    RecentCounter,
)


def test_my_queue_fifo_order():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.empty() is False


def test_my_queue_single_element():
    queue = MyQueue()
    queue.push(5)
    assert queue.peek() == 5
    assert queue.pop() == 5
    assert queue.empty() is True


def test_my_queue_empty_after_construction():
    queue = MyQueue()
    assert queue.empty() is True


def test_my_queue_multiple_push_pop_cycles():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    assert queue.pop() == 1
    queue.push(4)
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.empty() is True


def test_my_stack_lifo_order():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.pop() == 2
    assert stack.empty() is False


def test_my_stack_single_element():
    stack = MyStack()
    stack.push(9)
    assert stack.top() == 9
    assert stack.pop() == 9
    assert stack.empty() is True


def test_my_stack_empty_after_construction():
    stack = MyStack()
    assert stack.empty() is True


def test_my_stack_multiple_push_pop_cycles():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    stack.push(4)
    assert stack.pop() == 4
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.empty() is True


def test_my_circular_deque_insert_and_get_front_rear():
    deque_ = MyCircularDeque(3)
    assert deque_.insert_last(1) is True
    assert deque_.insert_last(2) is True
    assert deque_.insert_front(3) is True
    assert deque_.insert_front(4) is False
    assert deque_.get_rear() == 2
    assert deque_.get_front() == 3


def test_my_circular_deque_single_capacity():
    deque_ = MyCircularDeque(1)
    assert deque_.insert_front(1) is True
    assert deque_.is_full() is True
    assert deque_.get_front() == 1
    assert deque_.get_rear() == 1
    assert deque_.delete_front() is True
    assert deque_.is_empty() is True


def test_my_circular_deque_empty_deletes_fail():
    deque_ = MyCircularDeque(2)
    assert deque_.is_empty() is True
    assert deque_.delete_front() is False
    assert deque_.delete_last() is False


def test_my_circular_deque_full_after_wraparound():
    deque_ = MyCircularDeque(2)
    assert deque_.insert_last(1) is True
    assert deque_.insert_last(2) is True
    assert deque_.is_full() is True
    assert deque_.delete_front() is True
    assert deque_.insert_last(3) is True
    assert deque_.get_front() == 2
    assert deque_.get_rear() == 3


def test_recent_counter_window():
    counter = RecentCounter()

    assert counter.ping(1) == 1
    assert counter.ping(100) == 2
    assert counter.ping(3001) == 3
    assert counter.ping(3002) == 3


def test_my_circular_queue_fills_and_wraps():
    queue = MyCircularQueue(3)

    assert queue.en_queue(1) is True
    assert queue.en_queue(2) is True
    assert queue.en_queue(3) is True
    assert queue.en_queue(4) is False
    assert queue.rear() == 3
    assert queue.is_full() is True
    assert queue.de_queue() is True
    assert queue.en_queue(4) is True
    assert queue.rear() == 4


def test_my_circular_queue_empty_reads():
    queue = MyCircularQueue(2)

    assert queue.is_empty() is True
    assert queue.front() == -1
    assert queue.rear() == -1
    assert queue.de_queue() is False


def test_moving_average_window_slides():
    average = MovingAverage(3)

    assert average.next(1) == 1.0
    assert average.next(10) == 5.5
    assert average.next(3) == 14 / 3
    assert average.next(5) == 6.0


def test_front_middle_back_queue_operations():
    queue = FrontMiddleBackQueue()
    queue.push_front(1)
    queue.push_back(2)
    queue.push_middle(3)
    queue.push_middle(4)

    assert queue.pop_front() == 1
    assert queue.pop_middle() == 3
    assert queue.pop_middle() == 4
    assert queue.pop_back() == 2
    assert queue.pop_front() == -1


def test_recent_counter_all_within_window():
    counter = RecentCounter()

    assert counter.ping(1) == 1
    assert counter.ping(2) == 2
    assert counter.ping(3) == 3


def test_recent_counter_drops_everything_old():
    counter = RecentCounter()
    counter.ping(1)

    assert counter.ping(10000) == 1


def test_moving_average_window_of_one():
    average = MovingAverage(1)

    assert average.next(5) == 5.0
    assert average.next(10) == 10.0


def test_moving_average_before_window_fills():
    average = MovingAverage(5)

    assert average.next(4) == 4.0
    assert average.next(6) == 5.0


def test_front_middle_back_queue_empty_pops():
    queue = FrontMiddleBackQueue()

    assert queue.pop_front() == -1
    assert queue.pop_middle() == -1
    assert queue.pop_back() == -1


def test_front_middle_back_queue_single_element():
    queue = FrontMiddleBackQueue()
    queue.push_back(1)

    assert queue.pop_middle() == 1
    assert queue.pop_back() == -1
