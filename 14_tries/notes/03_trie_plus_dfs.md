# Trie Plus DFS

## Pattern

Use a trie to prune DFS over a board or search space.

## Intuition

Instead of checking every word separately, DFS follows only prefixes that exist in the trie.

## How It Works

This is common for word search II.

## Template

```text
dfs(cell, trie_node):
    if char not in trie_node.children: return
    advance trie node
    mark visited
    explore neighbors
    unmark visited
```

## Example

If prefix `qx` is not in the trie, stop that path immediately.

## Complexity

```text
Time depends on board size and valid trie prefixes
Space: trie plus recursion path
```

## Pitfalls

- Not marking board cells visited.
- Not pruning dead prefixes.
- Adding duplicate words to result.

## Interview Checklist

Before coding, make sure you can answer:

```text
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
