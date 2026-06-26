# Word Dictionary Patterns

## Pattern

Extend trie search to support wildcard choices.

## Intuition

A wildcard means branch into every child at that position.

## How It Works

DFS over trie nodes handles wildcard matching.

## Template

```text
def search(node, i):
    if i == len(word): return node.is_word
    if word[i] == .:
        try all children
    else:
        follow matching child
```

## Example

Pattern `c.t` can match `cat` or `cot`.

## Complexity

```text
Worst-case can branch exponentially with many wildcards
Usually bounded by trie size
```

## Pitfalls

- Forgetting wildcard branches.
- Returning true for prefix when full word is required.
- Not stopping when character path is missing.

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
