from problem_set.queue_deque_problems import MyCircularDeque, MyQueue, MyStack


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
