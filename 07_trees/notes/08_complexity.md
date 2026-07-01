# Tree Complexity

## Pattern

Tree complexity usually depends on:

```text
n = number of nodes
h = height of tree
w = maximum width of tree
output = size of returned data
```

## DFS Complexity

Recursive DFS uses stack space based on height:

```text
Time: O(n)
Space: O(h)
```

Balanced tree:

```text
h = O(log n)
```

Skewed tree:

```text
h = O(n)
```

Interview phrasing:

```text
Space is O(h), which is O(log n) for a balanced tree and O(n) worst case.
```

## BFS Complexity

BFS uses queue space based on width:

```text
Time: O(n)
Space: O(w)
```

Worst case:

```text
w = O(n)
```

## Output Space

Some problems return data proportional to the tree.

Examples:

```text
level order result: O(n)
serialized tree: O(n)
all root-to-leaf paths: depends on number and length of paths
```

It is often useful to separate auxiliary space from output space.

## Repeated Work

Some tree solutions look correct but are too slow because they recompute subtree information.

Example:

```text
for every node:
    compute height(left subtree)
    compute height(right subtree)
```

On a skewed tree, this can become `O(n^2)`.

The fix is to return multiple pieces of information from one DFS pass.

## Interview Templates

DFS explanation:

```text
n is the number of nodes and h is the height.
Time is O(n) because each node is visited once.
Space is O(h) from the recursion stack.
```

BFS explanation:

```text
n is the number of nodes and w is the maximum width.
Time is O(n) because each node is processed once.
Space is O(w) for the queue.
```

## Pitfalls

- Saying BFS space is always `O(h)`.
- Saying DFS space is always `O(n)` without mentioning height.
- Ignoring output space for path/list-returning problems.
- Missing repeated-work `O(n^2)` cases.
- Confusing height in nodes with diameter in edges.

## Interview Checklist

Before coding, make sure you can answer:

```text
Is this DFS (space O(h)) or BFS (space O(w)), and can I justify why each bound is correct?
What does h collapse to for a balanced tree vs. a skewed tree, and same for w?
Am I recomputing subtree information (e.g. height) inside a loop over every node, causing O(n^2)?
Does the output itself (level-order list, serialized string, all paths) add space beyond auxiliary recursion/queue space?
Can I state both time and space in the "n is ... because ..." interview phrasing?
```
