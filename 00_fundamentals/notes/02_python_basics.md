# Python Basics

## Goal

Know the Python features that make interview code clean, fast, and easy to explain.

## Core Syntax

Use clear function signatures:

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    ...
```

Use early returns for edge cases:

```python
if not nums:
    return []
```

Use tuple assignment when swapping:

```python
nums[left], nums[right] = nums[right], nums[left]
```

## Containers

Use `list` for arrays, stacks, and output:

```python
res = []
res.append(value)
res.pop()
```

Use `dict` for mappings and frequency counts:

```python
counts = {}
counts[x] = counts.get(x, 0) + 1
```

Use `set` for membership:

```python
seen = set()
if x in seen:
    return True
seen.add(x)
```

Use `deque` for queues:

```python
from collections import deque

queue = deque([start])
node = queue.popleft()
```

Use `heapq` for priority queues:

```python
import heapq

heapq.heappush(heap, value)
smallest = heapq.heappop(heap)
```

## Interview Defaults

- Prefer readable code over clever one-liners.
- Use `deque` for BFS.
- Use `dict` or `set` when you need fast lookups.
- Use helper functions when recursion needs repeated logic.
- Avoid mutating inputs unless the problem allows it.
