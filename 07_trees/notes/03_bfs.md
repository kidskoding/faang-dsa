# Tree BFS

## Pattern

BFS processes a tree level by level using a queue.

The queue stores nodes waiting to be processed. The level boundary is controlled by `level_size`.

## Intuition

If a problem asks about depth, levels, nearest leaf, right side view, or level averages, BFS is usually natural.

DFS goes deep first. BFS stays at the current depth before going deeper.

## How It Works

At the start of each outer loop, the queue contains exactly the nodes for the current level.

```text
level_size = len(queue)
```

Then process exactly `level_size` nodes. Any children you append belong to the next level.

## Template

```text
if root is None:
    return empty_answer

queue = deque([root])
result = []

while queue:
    level_size = len(queue)
    level = []

    repeat level_size times:
        node = queue.popleft()
        process node into level

        if node.left exists:
            queue.append(node.left)
        if node.right exists:
            queue.append(node.right)

    add level to result
```

## Dry Run Mental Model

For this tree:

```text
    1
   / \
  2   3
 /     \
4       5
```

The queue evolves by levels:

```text
[1]
[2, 3]
[4, 5]
```

That is why BFS can build `[[1], [2, 3], [4, 5]]` cleanly.

## Minimum Depth Rule

For minimum depth, return as soon as BFS sees the first leaf.

A leaf is:

```text
node.left is None and node.right is None
```

The first leaf found by BFS is guaranteed to be the shallowest leaf.

## Complexity

```text
Time: O(n)
Space: O(w)
```

`w` is the maximum width of the tree. Worst case, `w = O(n)`.

## Pitfalls

- Returning `[[]]` for an empty tree.
- Appending values to the queue instead of nodes.
- Forgetting `level_size`, causing levels to blur together.
- Returning minimum depth when one child is missing instead of when the node is a leaf.
- Accidentally reversing child order unless the problem asks for it.

## Interview Checklist

Before coding, make sure you can answer:

```text
Why does this problem need level boundaries instead of plain DFS?
How do I capture level_size before draining the queue, so levels don't blur together?
Am I enqueuing nodes (not values), and checking children with `if node.left exists`?
For minimum depth, why is the first leaf BFS reaches guaranteed to be shallowest?
What does the queue look like at the start of each outer loop iteration?
```
