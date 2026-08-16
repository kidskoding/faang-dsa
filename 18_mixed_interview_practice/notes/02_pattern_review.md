# Pattern Review

**Pattern recognition** is the skill of reading a problem you have never seen and
naming the technique it wants, before writing anything. Every module before this
one taught a technique in a folder labelled with its name, so recognition was
free. A real interview hands you an unlabelled problem, and choosing wrong costs
you most of the clock

This topic is not a new technique. It is the reverse index of everything already
learned: given a problem, which module does it belong to, and what in the wording
told you

Two skills sit underneath that, and they fail differently

- **Recognition** is naming the right technique from the wording. It fails by
  producing a plausible wrong answer, such as reaching for dynamic programming on
  a problem that greedy solves in three lines
- **Discrimination** is telling apart two techniques that look alike. It fails
  more quietly, because the wrong one often produces correct output on the small
  examples and dies on the real constraints

## Reading The Constraints First

The problem statement tells you the goal. The **constraints** tell you the
technique, and reading them first is the single highest-value habit in a live
interview. An input size implies a complexity budget, and a complexity budget
narrows the technique list to a handful

```text
n <= 20                 exponential is fine    subsets, bitmask DP, permutations
n <= 500                O(n^3) fits            Floyd-Warshall, interval DP
n <= 5000               O(n^2) fits            two-pointer over pairs, LCS-style DP
n <= 10^5               needs O(n log n)       sorting, heap, binary search on answer
n <= 10^6               needs O(n)             counting, prefix sums, single pass
values <= 10^9          the VALUE is not n     binary search the answer, not the array
```

The last line is the one people miss. A huge value range beside a small array
usually means the search happens over the answer space rather than the input, and
that is [binary search on the answer](../../05_binary_search/notes/04_search_on_answer.md)

> "The array is only 10^4 long but the answers go to 10^9, so I am not searching
> the array. I am binary searching the answer and writing a feasibility check."

## Phrases That Name The Technique

Interview problems reuse a small vocabulary. These phrases are close to
deterministic

| The wording                                                  | What it wants                                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| "contiguous subarray" plus a window condition                | [sliding window](../../04_sliding_window/notes/02_variable_size_window.md)           |
| "sorted array" plus "find a pair"                            | [opposite-end pointers](../../02_two_pointers/notes/01_opposite_end_pointers.md)     |
| "next greater", "previous smaller", "how many days until"    | [monotonic stack](../../03_stacks_and_queues/notes/03_monotonic_stack.md)            |
| "kth largest", "top k", "closest k"                          | [heap](../../08_heaps/notes/02_top_k.md)                                             |
| "all permutations", "all combinations", "all valid ways"     | [backtracking](../../09_backtracking/notes/01_backtracking_basics.md)                |
| "shortest path" on an unweighted graph or grid               | [BFS](../../10_graphs/notes/03_grid_bfs.md)                                          |
| "shortest path" with edge weights                            | [Dijkstra](../../10_graphs/notes/07_weighted_shortest_paths.md)                      |
| "prerequisites", "build order", "depends on"                 | [topological sort](../../10_graphs/notes/05_topological_sort.md)                     |
| "minimum cost to connect all"                                | [minimum spanning tree](../../17_advanced/notes/03_mst.md)                           |
| "number of ways" or "maximum value" with overlapping choices | [dynamic programming](../../11_dp/notes/01_dp_fundamentals.md)                       |
| "minimize the maximum" or "maximum feasible value"           | [binary search on the answer](../../05_binary_search/notes/04_search_on_answer.md)   |
| "starts with", "prefix", a dictionary of words               | [trie](../../14_tries/notes/01_trie_basics.md)                                       |
| "merge overlapping", "how many rooms", "busiest moment"      | [intervals](../../13_intervals/notes/01_interval_basics.md)                          |
| "in place" with `O(1)` extra space                           | [read and write pointers](../../02_two_pointers/notes/02_same_direction_pointers.md) |

The table is a starting point rather than a lookup. The phrase narrows the field,
and the constraints confirm it

## The Pairs That Get Confused

Most recognition failures are not wild misses. They are one of a handful of
lookalike pairs, and knowing the distinguishing question is worth more than
knowing either technique better

**Greedy or dynamic programming.** Ask whether a locally best choice can ever be
regretted. If taking the best option now can block a better total later, greedy is
wrong and you need DP. Jump Game is greedy because reach only ever grows; Coin
Change is DP because the largest coin can strand you

**BFS or DFS on a grid.** Ask whether the answer is a distance. BFS finds fewest
steps because it expands by layer; DFS finds connectivity and shapes. Using DFS
for a shortest path returns a path, just not the short one

**Sliding window or prefix sums.** Ask whether the values can be negative. A
window relies on growing right increasing the total, which negatives break. Prefix
sums do not care

**Sorting or a heap.** Ask whether you need everything ordered or only the
extremes. Sorting is `O(n log n)` for the whole array; a size-k heap is
`O(n log k)` and wins when `k` is much smaller than `n`

**Hash map or two pointers.** Ask whether the input is sorted and whether the
original indices are needed. Sorting destroys indices, which is why classic Two
Sum uses a map while Two Sum II uses pointers

**MST or shortest path.** Ask whether the question is about connecting everything
or travelling between two nodes. "All" and "every" point at MST; "from A to B"
points at Dijkstra

## Classifying Three Blind Problems

The exercise is to read a statement stripped of its title and name the technique
before reading on

**"Given an array of integers and an integer k, return the maximum sum of any
contiguous block of exactly k elements."**

Contiguous, fixed width, one aggregate. That is a
[fixed-size window](../../04_sliding_window/notes/01_fixed_size_window.md). The
giveaway is "exactly k", which fixes the width so the window never has to shrink

**"You are given prices for n items and a budget. Return the maximum number of
items you can buy."**

This one is a trap, because "maximum" plus a budget reads like knapsack. Ask the
discrimination question: can taking the cheapest item now ever block a better
total later? It cannot, because items are interchangeable once bought and buying
cheap always leaves more budget. Sort and take greedily. Knapsack only becomes
necessary when items have **both** a cost and a distinct value, so the cheap item
is not automatically the best one

**"Return the length of the longest substring containing at most two distinct
characters."**

"Longest", "substring", and a condition that breaks when you extend. That is a
[variable-size window](../../04_sliding_window/notes/02_variable_size_window.md)
with a [frequency map](../../04_sliding_window/notes/03_frequency_map_windows.md)
as its state. The phrase "at most" is the strongest single signal in the sentence,
because it makes the condition monotonic, which is exactly what a window needs

## Logging A Miss So It Does Not Repeat

Recognition improves by reviewing the misses, not by adding volume. A miss is
worth recording only if the entry is specific enough to act on later

```text
problem      Word Ladder
reached for  DFS, because the state space looked like a tree of words
correct      BFS, because the question asks for the SHORTEST transformation
giveaway     the word "shortest" on an unweighted state graph
retry        in 5 days, cold, no notes
```

The `giveaway` line is the one that transfers. "I got it wrong" teaches nothing;
"the word shortest on an unweighted graph means BFS" is a rule you can apply to a
different problem next week

Re-solve the miss cold on the retry date. Reading the fix creates recognition of
the solution, not the problem, and those are different skills

## Worked Example: [LRU Cache](https://leetcode.com/problems/lru-cache/)

Design a cache with a fixed capacity that supports lookup and insertion. When it
is full and a new key arrives, evict whichever key was used least recently

**Input**: `capacity`, an `int` above zero, then a sequence of calls.
`get(key: int) -> int` looks up a key, and `put(key: int, value: int) -> None`
inserts or overwrites one. Keys and values are non-negative integers

**Output**: `get` returns the stored `int`, or `-1` when the key is absent. `put`
returns nothing and evicts the least recently used key when the cache is already
at capacity. Both operations must run in average `O(1)`, which is part of the
problem statement rather than a hint

This is a **recognition** problem rather than an algorithm problem. Nothing here
is hard once you name the structures, and naming them comes entirely from the
constraint that both operations are `O(1)`

Work backwards from that constraint. `O(1)` lookup by key means a
[hash map](../../01_arrays_and_hashing/notes/02_hashing.md), and nothing else
qualifies. `O(1)` eviction of the least recently used item means you must know
which item that is without searching, so the entries need an order you can update
in constant time. A list cannot do it, because moving an element to the front is
`O(n)`. A [doubly linked list](../../06_linked_lists/notes/01_linked_list_basics.md)
can, because unlinking a node you already hold a pointer to is `O(1)`

> "Both operations have to be `O(1)`, so I need a hash map for lookup and a doubly
> linked list for recency order. The map stores keys to nodes, so I can jump
> straight to a node and move it without walking the list."

**The step by step**

1. Keep a hash map from key to the node holding that key, so a lookup never walks
   the list. This is what buys `O(1)` on `get`
2. Keep a doubly linked list ordered by recency, most recent at the front and least
   recent at the back. Eviction then reads the back directly instead of searching
3. Use permanent `head` and `tail` sentinel nodes that hold no data. Every real
   node then has both a `prev` and a `next`, so unlinking never needs a null check
   and the empty case needs no special branch
4. On `get`, return `-1` when the key is absent. Otherwise unlink the node from its
   current position and push it to the front, because reading a key counts as using
   it, then return its value
5. On `put` with a key already present, overwrite the value and move that node to
   the front. This is an update rather than an insertion, so nothing is evicted
6. On `put` with a new key, first check whether the cache is full. If it is, unlink
   the node at the back and **delete its key from the map**. Forgetting that
   deletion is the classic bug, because the map then holds a node that is no longer
   in the list
7. Create the new node, store it in the map, and push it to the front

```python
class Node:
    def __init__(self, key: int = 0, value: int = 0) -> None:
        self.key = key
        self.value = value
        self.prev: "Node | None" = None
        self.next: "Node | None" = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.cap = capacity
        self.table: dict[int, Node] = {}
        self.head = Node()  # sentinel: most recent side
        self.tail = Node()  # sentinel: least recent side
        self.head.next = self.tail
        self.tail.prev = self.head

    def _unlink(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _push_front(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        node = self.table[key]
        self._unlink(node)
        self._push_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            node = self.table[key]
            node.value = value
            self._unlink(node)
            self._push_front(node)
            return
        if len(self.table) == self.cap:
            oldest = self.tail.prev
            self._unlink(oldest)
            del self.table[oldest.key]
        node = Node(key, value)
        self.table[key] = node
        self._push_front(node)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
cache.put(4, 4)
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4

one = LRUCache(1)
one.put(1, 1)
one.put(2, 2)
assert one.get(1) == -1
assert one.get(2) == 2
```

The trace below is the official example, and the interesting line is the eviction
that removes 2 rather than 1

```text
put(1,1)   table={1}      front -> 1
put(2,2)   table={1,2}    front -> 2, 1
get(1)=1   table={1,2}    front -> 1, 2      reading 1 moved it forward
put(3,3)   EVICT key 2    front -> 3, 1      2 was at the back, not 1
get(2)=-1  table={1,3}                       2 is gone from list AND map
put(4,4)   EVICT key 1    front -> 4, 3
get(1)=-1  table={3,4}
```

Node 1 was inserted **before** node 2 and survived it. Insertion order is not
recency order, and the `get(1)` on line three is what separated them. A solution
that evicts by age rather than by use passes the first three lines of this trace
and fails the fourth, which is why the ordering has to be updated on reads as well
as writes

**Time**: `O(1)` for both `get` and `put`, because the map lookup is average
constant and every list operation touches a fixed number of pointers, with no
traversal anywhere

**Space**: `O(capacity)`, since the map holds one entry per stored key and the list
holds one node per stored key, plus two sentinels that do not grow

## Time and Space Complexity

Recognition itself has no runtime. What follows is the cost of the structures this
topic points at, as a reference for choosing between them under a constraint

| Choice                      | Time                                                                                                    | Space                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Sorting the whole input     | `O(n log n)`: comparison sorting cannot beat this bound in general                                      | `O(n)`: Python's `sorted` allocates a copy, though `list.sort` is in place |
| Size-`k` heap for top-k     | `O(n log k)`: where `k` is how many extremes you keep, so each of `n` pushes costs `log k`              | `O(k)`: only the `k` candidates are retained                               |
| Hash map lookup             | `O(1)` average: constant unless hashing degrades, which is rare on interview inputs                     | `O(n)`: one entry per stored key                                           |
| Binary search on the answer | `O(n log R)`: where `R` is the size of the **value** range, not the array, and each check costs `O(n)`  | `O(1)`: two bounds and a midpoint                                          |
| Backtracking over subsets   | `O(2^n)`: one branch per include-or-exclude decision, which is why `n <= 20` appears in the constraints | `O(n)`: the recursion depth and the current path                           |

## Summary

- **Pattern recognition** is naming the technique a blind problem wants before
  writing code. Every earlier module taught its technique under a label, so the
  skill was never exercised until now
  - It splits into **recognition**, naming the right technique, and
    **discrimination**, telling apart two that look alike. The second fails more
    quietly, because the wrong choice often passes the small examples
- Read the **constraints before the statement**. An input size implies a complexity
  budget, and that budget eliminates most techniques immediately
  - `n <= 20` invites exponential search, `n <= 10^5` demands `O(n log n)`, and a
    huge value range beside a small array usually means you binary search the
    **answer** rather than the input
- A small vocabulary of phrases is close to deterministic. "Next greater" means a
  monotonic stack, "top k" means a heap, "prerequisites" means topological sort,
  and "minimum cost to connect all" means a minimum spanning tree
- Most misses are one of a few lookalike pairs, and each has one distinguishing
  question. Greedy versus DP asks whether a local choice can be regretted; BFS
  versus DFS asks whether the answer is a distance; sliding window versus prefix
  sums asks whether values can go negative
- **LRU Cache** is the archetype of a design problem where the constraint picks the
  structures. Both operations being `O(1)` forces a hash map for lookup and a
  doubly linked list for recency, and neither works alone
- Log a miss with the **giveaway phrase**, not the outcome. "The word shortest on
  an unweighted graph means BFS" transfers to a new problem; "I got it wrong" does
  not
- The most common mistake is practising more problems instead of reviewing the
  misses, which grows the count of problems seen without improving the recognition
  that actually gets tested
  - Re-solve a miss cold on a scheduled date, since reading the fix builds
    recognition of the solution rather than of the problem

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
What are the constraints, and what complexity do they permit?
Is the value range far larger than the array, meaning I search the answer instead?
Which phrase in the statement names the technique?
Which lookalike technique could this be, and what question separates them?
If I am about to reach for DP, can a local greedy choice ever be regretted here?
If the problem says shortest, is the graph weighted or unweighted?
For a design problem, which constraint is forcing which data structure?
Have I stated the technique out loud before writing the first line?
What did I miss last time on a problem that looked like this one?
```
