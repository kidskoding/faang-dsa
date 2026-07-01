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
Why does a wildcard require recursing into every child instead of following one path?
What is the base case that distinguishes "reached end of word" from "still matching"?
Why must the base case check node.is_word rather than just i == len(word)?
How do I short-circuit as soon as one branch returns a match?
What is the worst-case complexity when the pattern is all wildcards?
```
