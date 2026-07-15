# Tries Problem Set

## Goal

Build trie intuition from the ground up — the core node structure and
insert/search/prefix operations, then wildcard and near-miss search, then
tries combined with DFS or backtracking — and use each technique to solve the
medium and hard prefix-matching problems that show up in LeetCode-style
interviews.

## How To Use

Each section maps to one solution file in this folder and to one trie
technique. Work a section top to bottom: problems are ordered roughly easy to
hard, and the implemented ones come first. `solves:` names the function or
class in that section's file; `solves: (todo)` means the solution is not
written yet.

For every problem, write:

```text
Input size:
Time:
Space:
Key idea:
```

## Trie Basics

`trie_basics_problems.py` — the core trie node structure plus the
insert/search/prefix operations that everything else builds on.

### 1. [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

- solves: `Trie`
- Pattern: children map plus an end-of-word marker.

### 2. [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/)

- solves: `MapSum`
- Pattern: trie nodes carry a running value sum for every prefix.

### 3. [Longest Word In Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/)

- solves: `longest_word_in_dictionary`
- Pattern: a word is only reachable if every prefix of it is itself a complete word.

### 4. [Replace Words](https://leetcode.com/problems/replace-words/)

- solves: `replace_words`
- Pattern: walk the trie from each word's start and stop at the first end-of-word marker.

### 5. [Implement Trie II (Prefix Tree)](https://leetcode.com/problems/implement-trie-ii-prefix-tree/)

- solves: `TrieII`
- Pattern: nodes track word counts and prefix counts to support insert, count, and erase.

### 6. [Short Encoding Of Words](https://leetcode.com/problems/short-encoding-of-words/)

- solves: `minimum_length_encoding`
- Pattern: insert reversed words into a suffix trie; only leaf words contribute to the encoding.

## Word Dictionary And Wildcard Search

`word_dictionary_problems.py` — trie search extended to wildcards, near-miss
matching, and prefix-by-prefix suggestion collection.

### 7. [Design Add And Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

- solves: `WordDictionary`
- Pattern: DFS branches into every child when the pattern character is a wildcard.

### 8. [Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/)

- solves: `MagicDictionary`
- Pattern: DFS search that must change exactly one character to reach a stored word.

### 9. [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/)

- solves: `search_suggestions`
- Pattern: walk the trie one character at a time, collecting the smallest matches at each prefix.

### 10. [Stream Of Characters](https://leetcode.com/problems/stream-of-characters/)

- solves: `StreamChecker`
- Pattern: build the trie on reversed words, then check backward from the newest character.

### 11. [Camelcase Matching](https://leetcode.com/problems/camelcase-matching/)

- solves: `camel_match`
- Pattern: match each query against the pattern trie, allowing extra lowercase but never extra uppercase.

### 12. [Prefix And Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/)

- solves: `WordFilter`
- Pattern: index each word by combined suffix#prefix keys so a single trie answers both filters.

### 13. [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/)

- solves: `AutocompleteSystem`
- Pattern: trie nodes store historical query frequencies, ranked as the user types each character.

## Trie Plus DFS

`trie_dfs_problems.py` — a trie combined with DFS or backtracking over a
larger search space, pruning on dead prefixes.

### 14. [Word Search II](https://leetcode.com/problems/word-search-ii/)

- solves: `find_words`
- Pattern: build one trie of all target words, then DFS the board while pruning on dead prefixes.

### 15. [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)

- solves: `palindrome_pairs`
- Pattern: trie of reversed words plus palindrome checks on the remaining substring.

### 16. [Concatenated Words](https://leetcode.com/problems/concatenated-words/)

- solves: `find_all_concatenated_words`
- Pattern: trie or hash set of words plus DFS/DP to check if a word splits into other words.

### 17. [Word Squares](https://leetcode.com/problems/word-squares/)

- solves: `word_squares`
- Pattern: prefix trie feeds backtracking that builds the grid row by row under column constraints.

### 18. [Maximum XOR Of Two Numbers In An Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

- solves: `find_maximum_xor`
- Pattern: binary trie of bits, greedily choosing the opposite bit at each level to maximize XOR.

### 19. [Maximum XOR With an Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)

- solves: `maximize_xor`
- Pattern: bit-trie with offline sorted queries, inserting values under an upper-bound limit.

### 20. [Longest Common Suffix Queries](https://leetcode.com/problems/longest-common-suffix-queries/)

- solves: `string_indices`
- Pattern: suffix trie of reversed words where each node caches the best (shortest, smallest-index) word.
