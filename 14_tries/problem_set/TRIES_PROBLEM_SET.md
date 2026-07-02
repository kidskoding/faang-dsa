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

### 2. [Implement Trie II (Prefix Tree)](https://leetcode.com/problems/implement-trie-ii-prefix-tree/)

- Pattern: nodes track word counts and prefix counts to support insert, count, and erase.

### 3. [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/)

- Pattern: trie nodes carry a running value sum for every prefix.

### 4. [Longest Word In Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/)

- Pattern: a word is only reachable if every prefix of it is itself a complete word.

### 5. [Replace Words](https://leetcode.com/problems/replace-words/)

- Pattern: walk the trie from each word's start and stop at the first end-of-word marker.

### 6. [Short Encoding Of Words](https://leetcode.com/problems/short-encoding-of-words/)

- Pattern: insert reversed words into a suffix trie; only leaf words contribute to the encoding.

## Word Dictionary And Wildcard Search

These extend trie search to support wildcards and near-miss matching.

### 7. [Design Add And Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

- Pattern: DFS branches into every child when the pattern character is a wildcard.

### 8. [Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/)

- Pattern: DFS search that must change exactly one character to reach a stored word.

### 9. [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/)

- Pattern: walk the trie one character at a time, collecting the smallest matches at each prefix.

### 10. [Stream Of Characters](https://leetcode.com/problems/stream-of-characters/)

- Pattern: build the trie on reversed words, then check backward from the newest character.

### 11. [Prefix And Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/)

- Pattern: index each word by combined suffix#prefix keys so a single trie answers both filters.

### 12. [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/)

- Pattern: trie nodes store historical query frequencies, ranked as the user types each character.

### 13. [Camelcase Matching](https://leetcode.com/problems/camelcase-matching/)

- Pattern: match each query against the pattern trie, allowing extra lowercase but never extra uppercase.

## Trie Plus DFS

These combine a trie with DFS or backtracking over a larger search space.

### 14. [Word Search II](https://leetcode.com/problems/word-search-ii/)

- Pattern: build one trie of all target words, then DFS the board while pruning on dead prefixes.

### 15. [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)

- Pattern: trie of reversed words plus palindrome checks on the remaining substring.

### 16. [Concatenated Words](https://leetcode.com/problems/concatenated-words/)

- Pattern: trie or hash set of words plus DFS/DP to check if a word splits into other words.

### 17. [Word Squares](https://leetcode.com/problems/word-squares/)

- Pattern: prefix trie feeds backtracking that builds the grid row by row under column constraints.

### 18. [Maximum XOR Of Two Numbers In An Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

- Pattern: binary trie of bits, greedily choosing the opposite bit at each level to maximize XOR.

### 19. [Maximum XOR With an Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)

- Pattern: bit-trie with offline sorted queries, inserting values under an upper-bound limit.

### 20. [Longest Common Suffix Queries](https://leetcode.com/problems/longest-common-suffix-queries/)

- Pattern: suffix trie of reversed words where each node caches the best (shortest, smallest-index) word.

## Recommended Order

If you want the shortest path to trie fluency, do them in this order:

```text
1. [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
2. [Implement Trie II (Prefix Tree)](https://leetcode.com/problems/implement-trie-ii-prefix-tree/)
3. [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/)
4. [Replace Words](https://leetcode.com/problems/replace-words/)
5. [Longest Word In Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/)
6. [Short Encoding Of Words](https://leetcode.com/problems/short-encoding-of-words/)
7. [Design Add And Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
8. [Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/)
9. [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/)
10. [Camelcase Matching](https://leetcode.com/problems/camelcase-matching/)
11. [Word Search II](https://leetcode.com/problems/word-search-ii/)
12. [Stream Of Characters](https://leetcode.com/problems/stream-of-characters/)
13. [Prefix And Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/)
14. [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/)
15. [Maximum XOR Of Two Numbers In An Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)
16. [Maximum XOR With an Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)
17. [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)
18. [Concatenated Words](https://leetcode.com/problems/concatenated-words/)
19. [Word Squares](https://leetcode.com/problems/word-squares/)
20. [Longest Common Suffix Queries](https://leetcode.com/problems/longest-common-suffix-queries/)
```
