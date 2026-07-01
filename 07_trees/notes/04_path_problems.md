# Tree Path Problems

## Pattern

Path problems carry information along a route through the tree.

The route is usually from root to current node, but some problems count paths that can start at any ancestor.

## Intuition

At each node, ask:

```text
What information from the path so far do I need here?
```

Common path state:

```text
running_sum
current_path
current_number
max_value_seen
prefix_sum_counts
```

## Root-To-Leaf Paths

A root-to-leaf path is only complete when the current node is a leaf.

```text
leaf = node.left is None and node.right is None
```

For root-to-leaf problems, the final check usually happens at the leaf.

## Template: Running Sum

```text
function dfs(node, current_sum):
    if node is None:
        return false

    current_sum += node.val

    if node is a leaf:
        return current_sum == target

    return dfs(node.left, current_sum) or dfs(node.right, current_sum)
```

## Template: Backtracking Path List

```text
function dfs(node, path):
    if node is None:
        return

    path.append(node.val)

    if node is a leaf and path is valid:
        result.append(copy of path)

    dfs(node.left, path)
    dfs(node.right, path)

    path.pop()
```

Copy the path when saving it because the same list keeps changing.

## Template: Prefix Sum Paths

Use prefix sums when a path can start anywhere above the current node.

```text
current_sum += node.val
needed = current_sum - target
answer += prefix_count[needed]

prefix_count[current_sum] += 1
recurse children
prefix_count[current_sum] -= 1
```

The decrement is backtracking. It removes the current path sum before returning to a sibling branch.

## Complexity

Simple path checks:

```text
Time: O(n)
Space: O(h)
```

Returning all paths includes output size because copied paths take space.

Prefix-sum path counting:

```text
Time: O(n)
Space: O(h)
```

The prefix map holds sums on the current root-to-node path.

## Pitfalls

- Treating a node with one missing child as a leaf.
- Saving `path` instead of `path.copy()`.
- Forgetting to `pop` after recursion.
- Forgetting to decrement prefix counts during backtracking.
- Applying root-to-leaf logic to paths that can start anywhere.

## Interview Checklist

Before coding, make sure you can answer:

```text
Does the path have to start at the root, or can it start at any ancestor?
Is the "path complete" check only valid at a leaf, or can it fire mid-path?
If I'm saving a path into results, am I copying it (not storing a reference)?
If backtracking, where does the undo (pop, or prefix_count decrement) happen relative to recursion?
What state travels down the recursion (running_sum, current_path, prefix_count) and why is it needed?
```
