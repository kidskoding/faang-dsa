# Common Operation Costs

A correct algorithm can still time out because one innocent-looking Python
operation repeats expensive hidden work. Choosing a container means choosing
which operations should be cheap.

In the tables below, `n` is the current number of elements and `k` is the number
of elements copied, added, or removed by the operation. The costs describe
CPython's documented operation model, which is the normal model used in Python
interviews.

## Lists Reward Work at the End

A Python **list** stores references in an array. Indexing is constant time
because an index identifies a direct position. Inserting or deleting near the
front is linear because every later reference must shift.

| List operation                                 | Time              | Why it matters                                                 |
| ---------------------------------------------- | ----------------- | -------------------------------------------------------------- |
| `values[i]`, assignment, or `len(values)`      | `O(1)`            | An index goes directly to one slot, and the length is stored   |
| `values.append(x)`                             | `O(1)` amortized  | Most appends use spare capacity; a rare resize copies the list |
| `values.pop()`                                 | `O(1)`            | Removing the last item shifts nothing                          |
| `values.insert(i, x)` or `values.pop(i)`       | `O(n)` worst case | Items after `i` shift; the front is the worst position         |
| `x in values`, `min(values)`, or `max(values)` | `O(n)`            | The answer may require checking every item                     |
| `values[a:b]` or `values.copy()`               | `O(k)` or `O(n)`  | A new list receives copied references                          |
| `values.extend(items)`                         | `O(k)` amortized  | Each of the `k` incoming items is appended                     |
| `values.sort()` or `sorted(values)`            | `O(n log n)`      | General comparison sorting performs logarithmic levels of work |

These costs make a list a good array and stack. They make `pop(0)` a poor queue
operation: one removal is `O(n)`, so repeatedly draining `n` items from the
front costs `O(n²)`.

Slicing is also real work. `nums[:]` is a convenient copy, not an `O(1)` view.
Inside a loop, a slice of growing length can quietly turn linear code into
quadratic code.

## Dictionaries and Sets Buy Fast Membership with Space

Dictionaries and sets are hash tables. A **hash** turns a key into a location to
search. With ordinary well-distributed keys, lookup, insertion, and deletion are
`O(1)` average case. Many collisions can force `O(n)` worst-case work, so call
the constant bound average case rather than guaranteed.

| Dictionary or set operation       | Average time                                              | Worst-case time                                       |
| --------------------------------- | --------------------------------------------------------- | ----------------------------------------------------- |
| `key in table` or `table[key]`    | `O(1)`: hash the key and inspect its expected slot        | `O(n)`: many keys may collide                         |
| Insert, update, or delete one key | `O(1)`: the expected number of examined slots is constant | `O(n)`: collisions or a resize can touch many entries |
| Iterate or copy                   | `O(n)`: every stored entry is visited                     | `O(n)`: every stored entry still must be visited      |

The tradeoff is `O(n)` space for up to `n` stored keys. Spend that space when it
replaces repeated scans. For example, checking every earlier list item for a
duplicate can take `O(n²)` total time, while keeping a set makes the scan `O(n)`
average time and `O(n)` auxiliary space.

```python
def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()
    for value in nums:
        if value in seen:
            return True
        seen.add(value)
    return False


assert contains_duplicate([4, 1, 4]) is True
assert contains_duplicate([4, 1, 7]) is False
```

## A Deque Makes Both Ends Cheap

`collections.deque` is a **double-ended queue**. It stores values in blocks so
neither end needs the all-element shift that a list front requires.

| Deque operation                             | Time   | Consequence                                                  |
| ------------------------------------------- | ------ | ------------------------------------------------------------ |
| `append`, `appendleft`, `pop`, or `popleft` | `O(1)` | A deque is the normal queue and also supports both ends      |
| `d[0]` or `d[-1]`                           | `O(1)` | The ends are directly accessible                             |
| `d[i]` near the middle                      | `O(n)` | A deque is not a replacement for random-access list indexing |
| `x in d` or `d.remove(x)`                   | `O(n)` | Finding an arbitrary value may scan the deque                |
| `len(d)`                                    | `O(1)` | The size is stored                                           |

```python
from collections import deque

queue: deque[str] = deque()
queue.append("first")
queue.append("second")

assert queue.popleft() == "first"
assert queue.popleft() == "second"
```

Use a list when you need arbitrary indices. Use a deque when you need to remove
from the front or work at both ends.

## Heaps Make the Smallest Item Cheap

Python's `heapq` treats a list as a min-heap. The smallest element is always at
index `0`, but the remaining elements are only partially ordered.

| Heap operation            | Time       | Why                                                                        |
| ------------------------- | ---------- | -------------------------------------------------------------------------- |
| `heap[0]`                 | `O(1)`     | The heap rule keeps the smallest item at the root                          |
| `heapq.heappush(heap, x)` | `O(log n)` | The new item may move through the heap's height                            |
| `heapq.heappop(heap)`     | `O(log n)` | Restoring the heap rule follows one root-to-leaf path                      |
| `heapq.heapify(values)`   | `O(n)`     | Bottom-up construction is linear, which is better than `n` separate pushes |

Use a heap when you repeatedly need the current smallest item or a small group
of best items. If you need every value in order once, sorting is usually simpler.

```python
import heapq

jobs = [(3, "low"), (1, "urgent"), (2, "normal")]
heapq.heapify(jobs)

assert heapq.heappop(jobs) == (1, "urgent")
assert jobs[0] == (2, "normal")
```

Tuple entries compare left to right, so the numeric priority above decides which
job leaves first. If first fields tie, Python compares the next fields too; make
sure those values are mutually comparable or add a numeric tie-breaker.

## Strings and Sorting Also Allocate Work

Strings are immutable. Indexing one character is `O(1)`, but slicing `k`
characters costs `O(k)` because it creates a new string. Building many pieces in
a list and joining once makes the total copied characters explicit.

```python
pieces: list[str] = []
for value in [4, 1, 7]:
    pieces.append(str(value))

assert ",".join(pieces) == "4,1,7"
```

Both `sorted(values)` and `values.sort()` cost `O(n log n)`. The first allocates
a new `O(n)` list, while the second changes the existing list. A key function is
evaluated once per element and does not change the overall bound when each key is
constant-time to compute.

## Choose by the Repeated Operation

| If the algorithm repeatedly needs...       | Reach for...            | Avoid...                                           |
| ------------------------------------------ | ----------------------- | -------------------------------------------------- |
| Arbitrary indexing or stack operations     | `list`                  | A deque for middle indexing                        |
| Removal from the front or both ends        | `collections.deque`     | `list.pop(0)`                                      |
| Membership, counts, or key-to-value lookup | `set` or `dict`         | Repeated linear list scans                         |
| The current smallest item                  | `heapq`                 | Re-sorting the whole collection after every change |
| All values ordered once                    | `sorted` or `list.sort` | A heap unless values arrive over time              |

The right question is not "which container is fastest?" Each container makes a
different operation cheap. Choose the one that matches the operation inside the
algorithm's repeated loop.

## Summary

- Lists provide `O(1)` indexing and amortized `O(1)` append, but inserting or
  deleting near the front costs `O(n)` because later elements shift.
- Dictionary and set lookup are `O(1)` average case and `O(n)` worst case; they
  trade extra space for avoiding repeated scans.
- Deques provide `O(1)` operations at both ends, while indexing near the middle
  remains `O(n)`.
- A heap exposes its smallest item in `O(1)`, changes the heap in `O(log n)`, and
  can be built from a whole list in `O(n)`.
- Slices and copies allocate new objects, so their cost depends on how much data
  they copy even when the syntax is short.

## Interview Checklist

```text
Which operation happens inside the main loop?
Is the bound worst case, average case, or amortized?
Am I removing from the front of a list?
Am I copying a slice on every iteration?
Would a set or dictionary replace repeated scans?
Do I need arbitrary indices, both ends, or the current minimum?
Am I sorting once, or repeatedly maintaining a changing best item?
Can I explain the extra space bought by the faster operation?
```
