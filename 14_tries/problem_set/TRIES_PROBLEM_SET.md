# Tries Problem Set

## Goal

Build trie intuition from the ground up, then use that foundation to solve the medium
and hard prefix-matching problems that show up in LeetCode-style interviews.

## How To Use

Work the file in order. The early sections are the fundamentals. The later sections are
the medium and hard extensions.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Trie Basics

These build the core trie node structure and the insert/search/prefix operations.

### 1. [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

- Pattern: children map plus an end-of-word marker.

### 2. [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/)

- Pattern: trie nodes carry a running value sum for every prefix.

### 3. [Longest Word In Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/)

- Pattern: a word is only reachable if every prefix of it is itself a complete word.

### 4. [Replace Words](https://leetcode.com/problems/replace-words/)

- Pattern: walk the trie from each word's start and stop at the first end-of-word marker.

## Word Dictionary And Wildcard Search

These extend trie search to support wildcards and near-miss matching.

### 5. [Design Add And Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

- Pattern: DFS branches into every child when the pattern character is a wildcard.

### 6. [Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/)

- Pattern: DFS search that must change exactly one character to reach a stored word.

### 7. [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/)

- Pattern: walk the trie one character at a time, collecting the smallest matches at each prefix.

### 8. [Stream Of Characters](https://leetcode.com/problems/stream-of-characters/)

- Pattern: build the trie on reversed words, then check backward from the newest character.

## Trie Plus DFS

These combine a trie with DFS or backtracking over a larger search space.

### 9. [Word Search II](https://leetcode.com/problems/word-search-ii/)

- Pattern: build one trie of all target words, then DFS the board while pruning on dead prefixes.

### 10. [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)

- Pattern: trie of reversed words plus palindrome checks on the remaining substring.

### 11. [Concatenated Words](https://leetcode.com/problems/concatenated-words/)

- Pattern: trie or hash set of words plus DFS/DP to check if a word splits into other words.

## Recommended Order

If you want the shortest path to trie fluency, do them in this order:

```text
1. [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
2. [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/)
3. [Replace Words](https://leetcode.com/problems/replace-words/)
4. [Longest Word In Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/)
5. [Design Add And Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
6. [Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/)
7. [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/)
8. [Word Search II](https://leetcode.com/problems/word-search-ii/)
9. [Stream Of Characters](https://leetcode.com/problems/stream-of-characters/)
10. [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)
11. [Concatenated Words](https://leetcode.com/problems/concatenated-words/)
```
