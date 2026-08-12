# Queues and Deques

A **queue** is a type of data structure where elements/items are added at the **back** and removed from the **front**. While elements/items in a [stack](01_stack.md) are added and removed from the **same end** (the top), elements/items in a queue are added and removed from **different ends**, the front and back respectively.

You can think of a **queue** as like a line. Whoever has been waiting the longest (the person at the front) will be served next, and anyone new will join at the back. This means that the first person who has been in line will be the first person out of the line. This idea refers to a phenomenon known as **first-in, first-out (FIFO)**.

As mentioned previously, a queue has two named ends, and each one allows exactly one operation

- The **front** (also called the head) is where you remove, since that is the
  oldest element
- The **back** (also called the tail or rear) is where you add, since a new
  element is the newest

```text
        front                         back
          |                             |
   out <- [ 10 ][ 20 ][ 30 ][ 40 ] <- in
          oldest                    newest
```

A **deque** (pronounced "deck", and short for **double-ended queue**) is a type of **queue** where you can add or remove elements at *either* end, all in constant time `O(1)`

```text
appendleft ->  [ 10 ][ 20 ][ 30 ][ 40 ]  <- append
   popleft <-                            -> pop
```

Therefore, a deque can behave like a **stack** or a **queue** (or even both!). Use only the right end and it behaves like a stack, use one end for adding and the other for removing and it behaves like a queue

> This topic covers what a queue costs to build, why Python's `list` is the wrong
> container for one, the ring buffer that fixes it, and the two-stack construction
> interviewers may ask you to derive

## When to Use

Typically, the signal to use the queue is a problem that involves
a situation where **the oldest pending item is the one that must be handled
next**. Some ways that may shows up could involve:

- Items arriving over time that are being processed in arrival order, as in a scheduler, a
  print spool, or a request buffer
- You are asked to design a fixed-capacity structure with `enqueue` and `dequeue`,
  which is the whole "Design Circular Queue" family of problems
- You are tracking a **window of recent events** and dropping the ones that have
  aged out, as in "how many calls happened in the last 3000 milliseconds"
- You explore a graph or a tree one layer at a time, which is
  [breadth-first search (BFS)](../../07_trees/notes/03_bfs.md). A queue preserves
  arrival order, so everything one step away is handled before anything two
  steps away

Reach for a **deque** instead when the structure itself is double-ended, as in
"Design Circular Deque", or when you need to add/remove from both ends

If the most recently added item is the one you want back, you want a [stack](01_stack.md). Nested and bracket-shaped problems are almost always stacks (i.e. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/))

## Moving The Boundary Instead Of The Data

A list can `append` at the back and `pop(0)` from the
front, meaning it can behave like a queue. While it does work, it is `O(n)` per removal, since
[every remaining element shifts left](../../00_fundamentals/notes/04_common_operation_costs.md)
to keep the front at index 0. Draining `n` elements that way costs `O(n²)`, which
is a correct solution, but can time out for larger inputs

That shift only happens because the front is *defined* as index 0. Nothing forces
that. Keep an integer `head` that says where the front currently is, and removing an
element becomes `head += 1`, which touches one integer instead of `n`

```text
head = 0     [ 10 ][ 20 ][ 30 ][ 40 ]
                ^ front
head = 1     [ 10 ][ 20 ][ 30 ][ 40 ]
                      ^ front, and slot 0 is now dead space
```

That leaves one problem: `head` only ever grows, so the slots behind it are
abandoned and the buffer creeps rightward forever. The fix is to let the indices
**wrap around** with `% capacity`, so slot 0 gets reused once the front has moved
past it. An array used this way, with the ends joined into a loop, is a **ring
buffer** (also called a circular buffer)

Typically, Python's `collections.deque` can be used, which is built into the language. However, there may sometimes be fixed-capacity design problems that will ask you to build such ring buffers yourself.

## A Ring Buffer From Scratch

The structure needs a fixed array, the index of the front, and a way to know how
many elements are live

```python
class MyCircularQueue:
    def __init__(self, k: int) -> None:
        self.buf: list[int] = [0] * k
        self.cap = k
        self.head = 0
        self.count = 0

    def enqueue(self, value: int) -> bool:
        if self.count == self.cap:
            return False
        tail = (self.head + self.count) % self.cap
        self.buf[tail] = value
        self.count += 1
        return True

    def dequeue(self) -> bool:
        if self.count == 0:
            return False
        self.head = (self.head + 1) % self.cap
        self.count -= 1
        return True

    def front(self) -> int:
        return -1 if self.count == 0 else self.buf[self.head]

    def rear(self) -> int:
        if self.count == 0:
            return -1
        return self.buf[(self.head + self.count - 1) % self.cap]
```

**Design decisions**:

- `self.count` is stored instead of a second `tail` index, and this is the design
  decision to defend out loud
  - With `head` and `tail` alone, the state `head == tail` means *both* empty and
    full, because the tail wraps all the way back around to the head in either case
  - Everybody who stores two indices then has to either waste one slot or keep a
    separate flag, and both fixes are fiddly
  - A count is never ambiguous, since `count == 0` is empty and `count == cap` is
    full, and it makes `rear()` free
- `tail = (self.head + self.count) % self.cap` derives the write position rather
  than storing it, because the next free slot is always `count` steps past the
  front, wrapped
- `% self.cap` is what makes the array circular, since without it the index runs
  off the end of a buffer that still has free slots at the start
- `dequeue` never clears `self.buf`, since the old value is unreachable the moment
  `head` moves past it, so overwriting it later is enough
- The `return False` guards are the capacity contract, and a fixed-size structure
  that silently accepts an over-capacity push is corrupt rather than slow

## Dry Run: The Ring Buffer

Capacity 3, so the buffer has exactly three slots to recycle

```text
enqueue(10) -> True    buf=[10,  0,  0]  head=0 count=1   front=10  rear=10
enqueue(20) -> True    buf=[10, 20,  0]  head=0 count=2   front=10  rear=20
enqueue(30) -> True    buf=[10, 20, 30]  head=0 count=3   front=10  rear=30
enqueue(40) -> False   buf=[10, 20, 30]  head=0 count=3   REJECTED, count == cap
dequeue()   -> True    buf=[10, 20, 30]  head=1 count=2   front=20  rear=30
enqueue(40) -> True    buf=[40, 20, 30]  head=1 count=3   front=20  rear=40
dequeue()   -> True    buf=[40, 20, 30]  head=2 count=2   front=30  rear=40
```

The rejected enqueue is the first thing to look at. The buffer was full, so the
call returned `False` and changed nothing. Without that guard, `tail` would have
been `(0 + 3) % 3 = 0`, which overwrites the 10 that had not been served yet and
loses it with no error

The second interesting step is the enqueue that succeeded. `tail` came out as
`(1 + 2) % 3 = 0`, so 40 landed in slot 0, physically *before* the front element
20\. The array is now `[40, 20, 30]`, which looks scrambled, and reading it left to
right would give the wrong answer. The queue order is `head`, then wrap, which is
20, 30, 40

The dequeue on the line above also shows why the values are never cleared. Slot 0
still held a stale 10 for one step, and nothing read it, because `head` had already
moved past

The same `head` and `count` state extends to a **circular deque**. The front lives
at `head`, the rear lives at `(head + count - 1) % capacity`, and the next free
slot after the rear is `(head + count) % capacity`. Adding at the front first
moves `head` backward; deleting at the front moves it forward. Adding or deleting
at the rear changes only `count`, because the rear index is derived from it.

```python
class MyCircularDeque:
    def __init__(self, k: int) -> None:
        self.buf: list[int] = [0] * k
        self.cap = k
        self.head = 0
        self.count = 0

    def insert_front(self, value: int) -> bool:
        if self.count == self.cap:
            return False
        self.head = (self.head - 1) % self.cap
        self.buf[self.head] = value
        self.count += 1
        return True

    def insert_last(self, value: int) -> bool:
        if self.count == self.cap:
            return False
        rear_next = (self.head + self.count) % self.cap
        self.buf[rear_next] = value
        self.count += 1
        return True

    def delete_front(self) -> bool:
        if self.count == 0:
            return False
        self.head = (self.head + 1) % self.cap
        self.count -= 1
        return True

    def delete_last(self) -> bool:
        if self.count == 0:
            return False
        self.count -= 1
        return True

    def get_front(self) -> int:
        return -1 if self.count == 0 else self.buf[self.head]

    def get_rear(self) -> int:
        if self.count == 0:
            return -1
        return self.buf[(self.head + self.count - 1) % self.cap]
```

```text
capacity=3
insert_last(10)   buf=[10, 0, 0]   head=0 count=1   logical=[10]
insert_front(5)   buf=[10, 0, 5]   head=2 count=2   logical=[5,10]
insert_last(20)   buf=[10,20, 5]   head=2 count=3   logical=[5,10,20]
delete_last()     buf=[10,20, 5]   head=2 count=2   logical=[5,10]
delete_front()    buf=[10,20, 5]   head=0 count=1   logical=[10]
```

The deletion steps deliberately leave stale values in `buf`. Changing the
boundary and count makes those slots unreachable, so clearing them would add work
without changing the deque.

## collections.deque: Python's built-in queue/deque

As mentioned previously, Python ships a queue/deque built from a linked chain of
fixed-size blocks, which gives `O(1)` at both ends without shifting a list

You can import it from Python's collections (shown below):

```python
from collections import deque
```

For FIFO use, append new arrivals at the back and remove the oldest arrival from
the front. The additional methods are for arbitrary double-ended use:

```python
from collections import deque

fifo: deque[int] = deque([10, 20])
fifo.append(30)
oldest = fifo.popleft()  # 10 was first in, so it is first out

double_ended: deque[int] = deque([10, 20])
double_ended.appendleft(5)
double_ended.append(30)
leftmost = double_ended.popleft()  # 5
rightmost = double_ended.pop()  # 30
```

[Operation Costs](../../00_fundamentals/notes/04_common_operation_costs.md):

```text
deque.append / appendleft / pop / popleft    O(1)   no element ever moves
deque[0] and deque[-1]                       O(1)   both ends are tracked
deque[i] for a middle index                  O(n)   it walks block by block
len(deque)                                   O(1)   the count is stored
```

Deques are inefficient when it comes to random access because there is no contiguous
array underneath, `q[len(q) // 2]` walks. If a problem needs indexing into the
middle, a deque is the wrong container

One constructor detail saves real code. `deque(maxlen=k)` makes a fixed-size
window that evicts from the opposite end automatically when it overflows. That
is enough when you only need the recent values. A moving average also needs a
running sum, so explicitly subtract the value that is about to leave before
appending the new one

When a problem needs the **middle** as a third access point, as in a front-middle-back
queue, the usual move is to hold **two deques split at the midpoint** and rebalance
after every operation so the front half stays the right size. Both ends of both
halves are `O(1)`, so the middle becomes an end

## A Queue From Two Stacks

Interviewers may ask you to build a queue when the only structure you are given
is a stack. Since stacks hand back the newest element and a queue needs the oldest, the
order needs to somehow be reversed

The solution is to drain one stack into another. The oldest value was pushed into
`in` first, so it is popped from `in` last and pushed into `out` last. That leaves
the oldest value on top of `out`, ready to be popped first

```text
in  = [1, 2, 3]        top is 3, the newest
drain it into out
out = [3, 2, 1]        top is 1, the oldest, which is what a queue wants
```

The naive version reverses on every single operation, which costs `O(n)` per
`pop`. The fix is to keep both stacks alive and **only refill `out` when it is
empty**

```python
class MyQueue:
    def __init__(self) -> None:
        self.in_stack: list[int] = []
        self.out_stack: list[int] = []

    def _shift(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._shift()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._shift()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
```

**Why this is amortized O(1)**:

- `if not self.out_stack` is the whole algorithm, and transferring while `out` is
  non-empty is the bug that breaks correctness rather than speed
  - Elements already in `out` are older than everything in `in`
  - Dumping newer elements on top of them means the newer ones come out first, so
    you have built a structure that is neither FIFO nor LIFO
- `push` never touches `out`, which is what lets a push happen mid-drain without
  disturbing the elements already waiting
- `empty` has to check **both** stacks, since elements can be sitting in either one
- Each element is pushed to `in`, popped from `in`, pushed to `out`, and popped
  from `out`, so it is touched exactly four times across its whole life
  - That is `O(1)` **amortized** per operation, even though one individual `pop`
    can cost `O(n)`
  - Say "amortized" out loud, because a single expensive call is the follow-up the
    interviewer is waiting to ask about

## Dry Run: Two Stacks

```text
push(1)      no transfer   in=[1]     out=[]
push(2)      no transfer   in=[1, 2]  out=[]
peek() -> 1  TRANSFER      in=[]      out=[2, 1]
pop()  -> 1  no transfer   in=[]      out=[2]
push(3)      no transfer   in=[3]     out=[2]
pop()  -> 2  no transfer   in=[3]     out=[]
pop()  -> 3  TRANSFER      in=[]      out=[]
```

Values come out as 1, 2, 3, which is the order they went in

The skipped transfers are the load-bearing part. Look at the `push(3)` step and the
`pop()` right after it. When 3 arrived, `out` still held 2, and 2 is older, so the
transfer was correctly declined and 2 came out next. Had `_shift` run there, `out`
would have become `[2, 3]` with 3 on top, and the next pop would have returned 3
ahead of 2

Only two of the four reads triggered a transfer, and that ratio is the amortized
argument made visible. Element 3 was moved between stacks exactly once, on the
final pop, no matter how many operations happened in between

The inverse interview problem, implementing a stack with one queue, rotates the
older items behind each new item after a push. That makes the newest item sit at
the queue's front, so `pop` is `O(1)` while each `push` costs `O(n)`

## Counting Events In A Time Window

One queue pattern that shows up often is **counting how many events happened in
the last N units of time**. When entries expire by age, keep them in a deque in
arrival order and **pop from the front while the front is too old**

```python
from collections import deque


class RecentCounter:
    def __init__(self) -> None:
        self.calls: deque[int] = deque()

    def ping(self, t: int) -> int:
        self.calls.append(t)
        while self.calls[0] < t - 3000:
            self.calls.popleft()
        return len(self.calls)
```

Calls arrive with increasing timestamps, so the deque is automatically sorted and
the oldest entry is always at the front. That means one `while` loop at the front
removes everything expired, because as soon as the front is fresh enough,
everything behind it is too

The loop looks like it could be `O(n)`, and per call it can be. Across the whole
run it is `O(1)` amortized, because each timestamp is appended once and popped at
most once, so the total work is bounded by the number of pings. This is the same
counting argument as the two-stack queue, and it is the standard way to justify a
loop nested inside another loop

## Worked Example: [Design Front Middle Back Queue](https://leetcode.com/problems/design-front-middle-back-queue/)

Design a queue that can push and pop at three positions rather than the usual two:
the **front**, the **middle**, and the **back**. When the queue has an even length
there are two candidates for the middle, and every operation uses the frontmost of
the two

Since this is a **design problem**, the input is a sequence of method calls rather
than one array. The three push methods insert an integer at the front, middle, or
back and return `None`. The three pop methods remove and return from the matching
position, or return `-1` when the queue is empty. If the length is even, “middle”
means the frontmost of the two middle positions

A deque makes its ends `O(1)`, but its middle is still `O(n)` to reach. Therefore,
one deque cannot make all six operations constant time. Split the queue into two
deques instead, so the middle becomes an end of one half

> “I will store the logical queue as `front` followed by `back`. I will maintain
> `len(front) <= len(back) <= len(front) + 1`, so the halves are equal or `back`
> has one extra element. That keeps the middle at the boundary, where a deque can
> reach it in `O(1)`.”

The invariant makes the even and odd cases precise

```text
even:  front=[1, 2]  back=[3, 4]     pop_middle removes front[-1] -> 2
odd:   front=[1, 2]  back=[3, 4, 5]  pop_middle removes back[0]   -> 3
```

After each operation, `_balance` moves at most one boundary element, because one
method call can change the size difference by at most one. The invariant also
keeps every lone element in `back`, so `not back` means the whole queue is empty

Therefore,

1. Store the queue as two deques whose logical order is `front + back`
2. Push or pop at an outer end for front/back operations. For a front pop, use
   `back` only when `front` is empty
3. For a middle push, append to `front` when it is shorter; otherwise prepend to
   `back`. For a middle pop, remove from `front` when the halves are equal;
   otherwise remove from `back`
4. Return `-1` before any empty pop. After every successful change, call
   `_balance` to restore the invariant

```python
from collections import deque


class FrontMiddleBackQueue:
    def __init__(self) -> None:
        self.front: deque[int] = deque()
        self.back: deque[int] = deque()

    def _balance(self) -> None:
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        elif len(self.back) > len(self.front) + 1:
            self.front.append(self.back.popleft())

    def push_front(self, val: int) -> None:
        self.front.appendleft(val)
        self._balance()

    def push_middle(self, val: int) -> None:
        if len(self.front) < len(self.back):
            self.front.append(val)
        else:
            self.back.appendleft(val)
        self._balance()

    def push_back(self, val: int) -> None:
        self.back.append(val)
        self._balance()

    def pop_front(self) -> int:
        if not self.back:
            return -1
        val = self.front.popleft() if self.front else self.back.popleft()
        self._balance()
        return val

    def pop_middle(self) -> int:
        if not self.back:
            return -1
        if len(self.front) == len(self.back):
            val = self.front.pop()
        else:
            val = self.back.popleft()
        self._balance()
        return val

    def pop_back(self) -> int:
        if not self.back:
            return -1
        val = self.back.pop()
        self._balance()
        return val
```

- **Time Complexity:** `O(1)` per method, because each method touches deque ends and
  `_balance` moves at most one element
- **Space Complexity:** `O(n)` for `n` live elements, because the two deques partition the
  values rather than duplicate them

## Assessing Time and Space Complexity

**Ring buffer**

| Operation                                | Time                                                     | Space                                                                                      |
| ---------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `enqueue` / `dequeue` / `front` / `rear` | `O(1)`: index arithmetic only, and no element ever moves | `O(k)`: the array is allocated once up front at the fixed capacity of `k`, and never grows |

**`collections.deque`**

| Operation                                   | Time                                                                                               | Space                                                      |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| `append` / `appendleft` / `pop` / `popleft` | `O(1)`: it is a linked chain of blocks, so nothing shifts to make room                             | `O(n)`: one slot per element, plus a little block overhead |
| indexing a middle position                  | `O(n)`: reaching index `i` walks the block list, which is why a deque is not a random-access array | `O(1)`: a traversal that allocates nothing                 |

**Queue from two stacks**

| Operation      | Time                                                                                                                         | Space                                                                                |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `push`         | `O(1)`: append to the `in` stack                                                                                             | `O(n)`: the elements live across the two stacks combined                             |
| `pop` / `peek` | `O(1)` amortized, `O(n)` worst case: one call can transfer everything, but each element crosses at most once in its lifetime | `O(n)`: the transfer moves elements between the two stacks and allocates nothing new |

**Using a `list` as a `queue`**

| Operation                      | Time                                                                     | Space                                                                            |
| ------------------------------ | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| `list.pop(0)`                  | `O(n)`: every survivor shifts one slot left to keep the front at index 0 | `O(n)`: a single list, no worse than the alternatives                            |
| draining `n` elements that way | `O(n²)`: `n` removals, each costing `O(n)`                               | `O(n)`: the space never reveals the problem, which is exactly why it gets missed |

The `O(n²)` row is the one to keep. It is the difference between a solution that
passes and the same solution that times out, with no visible change to the logic

## Summary

- A **queue** is a type of data structure, where elements are added on one end (back) and they come out from the other end (front). Remove at the front, add at the back
  - Many people typically remember this through a mnemonic known as **FIFO**: **First In First Out**. The first element/item that comes into the queue is the first element/item that comes out of the queue
  - A **deque** (double-ended queue) drops that restriction, so you can add and remove at either end
- Interview problems that hint at a queue, typically involve processing things in arrival order,
  a level-by-level traversal, or a window of recent events that ages out
- `list.pop(0)` is `O(n)` because every survivor shifts left, so
  draining costs `O(n²)` and times out while looking correct. This is why queues are used because insertion and removal
  from both ends costs only a constant time of `O(1)`
- The core idea involves moving the **boundary**, not the data. Advance an index instead
  of shifting elements (like a regular list would)
- **Ring buffers** are fixed arrays plus a `head` and `count`, with `% capacity` to
  wrap. Store `count` rather than a `tail`, since `head == tail` cannot tell empty
  from full
- Queues can be built with **two stacks**, where one stack pops all the elements out and the other
  stack takes those elements and pushes them all in, which is amortized `O(1)` because each element crosses at most once
- Queues are efficient because their insertion and removal happen at an end. The
  three designs in this topic are the **ring buffer**, **`collections.deque`**,
  and the **queue from two stacks**. Ring-buffer and deque end operations are
  `O(1)`, while the two-stack queue is `O(1)` amortized
  - The two-stack queue is `O(1)` **amortized** rather than worst case, since one `pop` can transfer the whole `in` stack, and each element only ever crosses once
  - Space is not the same across the three. The deque and the two stacks are `O(n)`, growing with the number of live elements, while the ring buffer is `O(k)` because it allocates all `k` slots up front and holds them even when empty
- The most common mistake involves using a list, with `list.pop(0)`, and transferring between stacks
  before `out` is empty, which destroys the ordering of the elements
  - Always use a **queue** when you need to insert on one end, typically the back,
    and remove from the other end, typically the front
  - Always use a **deque** when you need to insert and remove from both ends

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
Is the next item to handle the oldest one (queue) or the newest (stack)?
Do I need both ends (a deque) or only one at each end (a queue)?
Am I using collections.deque rather than a list with pop(0)?
For a fixed-capacity design: does a full push get rejected, or evict the oldest?
For a ring buffer: am I storing a count so empty and full are distinguishable?
For a ring buffer: is every index computation wrapped with % capacity?
For two stacks: does the transfer only fire when the out stack is empty?
Can I state the amortized cost and justify it by counting touches per element?
What does one entry hold: a bare value, or a tuple with a timestamp or state?
Do I ever need a middle element, which a deque cannot give me in O(1)?
```
