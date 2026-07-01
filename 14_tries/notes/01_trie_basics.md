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
How do I represent a node's children — dict, array of 26, or defaultdict?
How does the end-of-word marker differ from a node simply existing?
Does insert create nodes for characters that are already present?
How does prefix search (startsWith) differ from full word search (search)?
What happens if the word or prefix is empty?
Why is each operation O(word length) and independent of the number of stored words?
```
