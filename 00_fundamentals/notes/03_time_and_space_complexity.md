# Time And Space Complexity

## Goal

Learn to explain where runtime and memory usage come from. Do not memorize Big-O labels without understanding the work being counted.

## The Five Questions

For every function, ask:

1. What is the input size?
1. How many times can each input item be touched?
1. What data structures grow with the input?
1. What is the worst case?
1. Is output space separate from auxiliary space?

Common variables:

```text
n = number of items
m = number of items in a second input
k = requested subset size, top-k size, or window size
h = height of a tree
w = maximum width of a tree
V = number of graph vertices
E = number of graph edges
```

## Time

Time complexity counts work.

```text
single loop over n items: O(n)
nested loop over pairs: O(n^2)
binary search: O(log n)
sorting: O(n log n)
DFS/BFS over graph adjacency list: O(V + E)
backtracking over subsets: O(2^n)
backtracking over permutations: O(n!)
```

Interview phrasing:

```text
Time is O(n), because each element is visited once and each visit does O(1) work.
```

## Space

Space complexity counts memory that grows with input size.

Common sources:

```text
output list: O(n)
hash map or set: O(n)
recursion stack: O(depth)
BFS queue: O(max width)
heap: O(k) or O(n)
DP table: number of states stored
```

Be precise:

```text
Total space includes the returned output.
Auxiliary space excludes the returned output and counts only extra working memory.
```

Example:

```text
Returning a traversal list uses O(n) output space.
The recursion stack uses O(h) auxiliary space.
Total space is O(n + h), which simplifies to O(n).
Auxiliary space is O(h).
```

## Interview Template

Use this after every solution:

```text
Let n be ______.

Time is O(____), because ______.

Space is O(____), because ______.
If we exclude the output, auxiliary space is O(____).
```

## Common Traps

- Two recursive calls do not automatically mean O(2^n). If the calls split a tree into left and right subtrees, each node may still be visited only once.
- Nested loops are not always O(n^2). Count total pointer movement.
- Output space matters when returning lists, paths, subsets, matrices, or strings.
- Worst-case tree height can be O(n), even if balanced height is O(log n).
