# Interview Python

Interview Python is a small, practical subset of the language. You need to
represent the input, move through it, store useful state, and return an answer
that another person can read while you write it. You do not need clever syntax.

Python names refer to objects. A name such as `nums` may refer to a list, while
`nums[0]` selects one object inside it. Lists, dictionaries, and sets are
**mutable**, which means their contents can change. Strings and tuples are
**immutable**, which means an operation creates a new value instead of changing
the old one.

## Functions Carry the Contract

A function signature tells the interviewer what comes in and what goes out.
**Type hints** document that contract, but Python does not enforce them while the
program runs.

```python
def first_negative(nums: list[int]) -> int | None:
    for value in nums:
        if value < 0:
            return value
    return None


assert first_negative([4, -2, 7]) == -2
assert first_negative([4, 2, 7]) is None
```

An early return handles a finished case immediately. Here, the loop returns as
soon as it finds an answer; the final `return None` covers the case where no
answer exists. Use `is None` to test the absence marker, since `0`, `False`, and
an empty container may all be valid values.

Names created inside a function are local to that call. A helper function is
useful when it gives a repeated piece of logic a clear contract. Do not split a
five-line scan into helpers merely to look organized.

## Move Through Values and Indices Deliberately

Use `for value in nums` when you need values, and `enumerate(nums)` when you also
need indices. Use `range(len(nums))` only when the index itself drives the logic.

```python
nums = [8, 3, 5]

visited: list[tuple[int, int]] = []
for index, value in enumerate(nums):
    visited.append((index, value))

assert visited == [(0, 8), (1, 3), (2, 5)]

for left in range(len(nums) // 2):
    right = len(nums) - 1 - left
    nums[left], nums[right] = nums[right], nums[left]

assert nums == [5, 3, 8]
```

Tuple assignment performs the swap without a temporary variable. `zip(a, b)`
pairs values from two sequences and stops when the shorter one ends, so clarify
whether unequal lengths are allowed before relying on it.

Python ranges exclude the stop value. `range(start, stop)` includes `start` but
not `stop`, and `range(stop - 1, -1, -1)` walks backward through index `0`.

## Lists Are Arrays, Stacks, and Answer Builders

A Python **list** is the default indexed sequence. It preserves order, allows
duplicates, and can change size.

```python
stack: list[int] = []
stack.append(10)
stack.append(20)

assert stack[-1] == 20
assert stack.pop() == 20
assert stack == [10]

values = [2, 4, 6, 8]
assert values[1:3] == [4, 6]
assert values[::-1] == [8, 6, 4, 2]
```

`append` and `pop()` at the end make a list a natural stack. Negative index
`-1` means the last element. A **slice** such as `values[1:3]` creates a new list
containing indices `1` and `2`; the stop index is excluded.

Assignment does not copy a list. Both names below refer to the same mutable
object, so a change through one name is visible through the other:

```python
original = [1, 2]
alias = original
copy = original[:]

alias.append(3)

assert original == [1, 2, 3]
assert alias is original
assert copy == [1, 2]
```

This matters when a problem says not to mutate the input or when it stores a
path, changes that path, and later needs the earlier version. Store `path.copy()`
when you need the current snapshot; storing `path` stores another reference to
the object that will keep changing.

## Dictionaries and Sets Make Lookup Explicit

A **dictionary** maps each unique key to a value. A **set** stores unique values
without an associated value. Keys and set members must be **hashable**, which
means Python can derive a stable lookup code from the value while it is stored.
Integers, strings, and tuples containing only hashable values work, while lists
do not.

```python
def frequencies(nums: list[int]) -> dict[int, int]:
    counts: dict[int, int] = {}
    for value in nums:
        counts[value] = counts.get(value, 0) + 1
    return counts


assert frequencies([4, 1, 4, 4]) == {4: 3, 1: 1}

seen: set[int] = set()
for value in [3, 1, 3]:
    if value in seen:
        duplicate = value
        break
    seen.add(value)

assert duplicate == 3
```

`counts.get(value, 0)` returns the stored count or `0` when the key is absent.
Use `key in mapping` for membership; it checks dictionary keys, not values.
Iterating over a dictionary also yields keys. Use `.items()` when you need both
the key and value.

An empty set is `set()`, because `{}` creates an empty dictionary.

## Tuples Keep Related State Together

A **tuple** is an immutable ordered group. Interview code often uses one to keep
a coordinate, a `(priority, value)` heap entry, or several pieces of queue state
together.

```python
point = (2, 5)
row, column = point
states = {(0, 0), (0, 1), (1, 0)}

assert row == 2 and column == 5
assert (0, 1) in states
```

Python compares tuples from left to right. That becomes important with heaps:
`(2, "a")` comes before `(3, "z")` because the first fields decide the result.

## Use the Built-ins That Match the Job

`collections.deque` supports adding and removing at both ends, so it is the
normal queue. `heapq` maintains a **min-heap**, a container whose smallest value
is available at index `0`.

```python
from collections import deque
import heapq

queue: deque[int] = deque([10, 20])
queue.append(30)
assert queue.popleft() == 10

heap = [7, 2, 5]
heapq.heapify(heap)
heapq.heappush(heap, 1)
assert heapq.heappop(heap) == 1
assert heap[0] == 2
```

The list holding a heap is not globally sorted. Only the heap rule is
guaranteed, which is enough to read or remove the smallest value efficiently.
Later modules derive queues and heaps in depth; for now, know their Python names
and basic operations.

Sorting returns values in ascending order unless you supply `reverse=True` or a
`key` function. The key is the value Python compares:

```python
words = ["pear", "fig", "banana"]

assert sorted(words) == ["banana", "fig", "pear"]
assert sorted(words, key=len) == ["fig", "pear", "banana"]
assert words == ["pear", "fig", "banana"]

words.sort(key=len, reverse=True)
assert words == ["banana", "pear", "fig"]
```

`sorted(...)` creates a new list. `list.sort()` changes the existing list and
returns `None`, so do not write `words = words.sort()`.

## Comprehensions Are Useful Until They Hide the Idea

A **comprehension** builds a container while looping over existing values. Use
it when the expression remains easy to say in one sentence.

```python
nums = [-2, -1, 0, 1, 2]
squares = [value * value for value in nums if value > 0]
positions = {value: index for index, value in enumerate(nums)}

assert squares == [1, 4]
assert positions[2] == 4
```

If a comprehension needs nested conditions, mutation, or a comment, write a
normal loop. Readability matters because the interviewer must understand the
code while you are still producing it.

## Small Python Traps

- `==` compares values, while `is` compares object identity. Use `is None`, but
  use `==` for numbers, strings, lists, and other values.
- `and` and `or` short-circuit from left to right, so put the safety check first:
  `index < len(nums) and nums[index] == target`.
- Empty strings and containers are false in a condition. `if not nums` is a
  clear empty-list check when emptiness is what you mean.
- Strings cannot be changed by index. Build pieces in a list and use
  `"".join(pieces)` when constructing a result from many pieces.
- Do not remove from a list while iterating over that same list unless you have
  deliberately designed the index movement; skipped elements are a common
  result.

The next two notes explain why choosing the right container changes the runtime.

## Summary

- Interview Python needs clear functions, loops, conditionals, and a small set of
  containers; clever language features are optional.
- A list is the default indexed sequence and stack, a dictionary maps keys to
  values, and a set stores unique values for membership checks.
- A deque is the normal queue, while `heapq` maintains a min-heap whose smallest
  value is at index `0`.
- Mutable objects can change through any alias that refers to them, so copy a
  path or input when the algorithm needs an independent snapshot.
- `enumerate`, tuple unpacking, `.get`, and simple comprehensions remove
  bookkeeping without hiding the algorithm.

## Interview Checklist

```text
Does the function signature make the input and return value clear?
Do I need values, indices, or both?
Is a list, dictionary, set, deque, or heap the closest match for the job?
Am I accidentally aliasing a mutable object that needs to be copied?
Does an empty container or None have a distinct meaning here?
Is a compact Python expression still easy to explain out loud?
```
