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
Why build one trie of all target words instead of running DFS per word?
How does the trie prune board paths that no word could possibly match?
How do I mark a cell visited and correctly unmark it on backtrack?
How do I avoid adding the same found word to the result twice?
What optimization removes a leaf node from the trie once its word is found?
Why is runtime bounded by valid trie prefixes rather than by board size alone?
```
