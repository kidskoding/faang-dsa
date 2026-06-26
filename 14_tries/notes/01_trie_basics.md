# Trie Basics

## Pattern

A trie stores strings one character at a time in a tree.

## Intuition

Shared prefixes are stored once, which makes prefix queries efficient.

## How It Works

Each node maps character to child node and marks whether a word ends there.

## Template

```text
node = root
for char in word:
    if char not in node.children:
        node.children[char] = TrieNode()
    node = node.children[char]
node.is_word = True
```

## Example

Words `car` and `cat` share the `ca` path.

## Complexity

```text
insert/search/prefix: O(length of word)
space: O(total characters stored)
```

## Pitfalls

- Forgetting end-of-word marker.
- Treating prefix as full word.
- Using trie when hash set is enough.

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
