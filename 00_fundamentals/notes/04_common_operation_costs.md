# Common Operation Costs

## Python Containers

```text
list append: amortized O(1)
list pop from end: O(1)
list pop from front: O(n)
list insert at front/middle: O(n)
list indexing: O(1)
list slicing: O(k), where k is slice length
```

```text
dict/set lookup: average O(1), worst-case O(n)
dict/set insert/delete: average O(1), worst-case O(n)
```

```text
deque append/pop from either end: O(1)
heapq push/pop: O(log n)
sort / sorted: O(n log n)
len(collection): O(1)
```

## Pattern Costs

Arrays and strings:

```text
single scan: O(n)
two pointers: O(n), if each pointer only moves forward
sliding window: O(n), if each pointer only moves forward
prefix sums: O(n) build, O(1) range query
sorting first: O(n log n)
```

Hashing:

```text
frequency map: O(n) time, O(n) space
seen set: O(n) time, O(n) space
lookup per item: average O(1)
```

Linked lists:

```text
traversal: O(n)
fast/slow pointers: O(n)
reverse list: O(n) time, O(1) space
random access by index: O(n)
```

Stacks and queues:

```text
stack push/pop: O(1)
queue push/pop with deque: O(1)
monotonic stack/queue: O(n), because each item is pushed and popped at most once
```

Trees:

```text
recursive DFS: O(n) time, O(h) auxiliary space
BFS: O(n) time, O(w) auxiliary space
BST search/insert: O(h)
balanced BST height: O(log n)
skewed BST height: O(n)
```

Graphs:

```text
BFS/DFS adjacency list: O(V + E)
visited set: O(V)
queue/stack: O(V)
```

Heaps:

```text
push or pop: O(log n)
build heap: O(n)
top-k with size-k heap: O(n log k)
```

Dynamic programming:

```text
Time: number of states * work per state
Space: number of stored states
1D DP: often O(n)
2D DP: often O(n * m)
```
