from __future__ import annotations


class WordSearchNode:
    # Node for Word Search II.
    def __init__(self) -> None:
        self.children: dict[str, WordSearchNode] = {}
        self.word: str | None = None


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    # Problem 14: Word Search II
    # Key idea: build one trie of all target words, then DFS the board while
    # pruning on dead prefixes.
    # Time:
    # Space:

    raise NotImplementedError


class PalindromePairNode:
    # Node for Palindrome Pairs.
    def __init__(self) -> None:
        self.children: dict[str, PalindromePairNode] = {}
        self.word_index: int | None = None
        self.palindrome_suffix_indices: list[int] = []


def palindrome_pairs(words: list[str]) -> list[list[int]]:
    # Problem 15: Palindrome Pairs
    # Key idea: trie of reversed words plus palindrome checks on the remaining
    # substring.
    # Time:
    # Space:

    raise NotImplementedError


class ConcatenatedWordNode:
    # Node for Concatenated Words.
    def __init__(self) -> None:
        self.children: dict[str, ConcatenatedWordNode] = {}
        self.is_word: bool = False


def find_all_concatenated_words(words: list[str]) -> list[str]:
    # Problem 16: Concatenated Words
    # Key idea: trie or hash set of words plus DFS/DP to check if a word
    # splits into other words.
    # Time:
    # Space:

    raise NotImplementedError


class WordSquareNode:
    # Node for Word Squares.
    def __init__(self) -> None:
        self.children: dict[str, WordSquareNode] = {}
        self.indices: list[int] = []


def word_squares(words: list[str]) -> list[list[str]]:
    # Problem 17: Word Squares
    # Key idea: prefix trie feeds backtracking that builds the grid row by row
    # under column constraints.
    # Time:
    # Space:

    raise NotImplementedError


class MaximumXorNode:
    # Binary-bit node for Maximum XOR Of Two Numbers In An Array.
    def __init__(self) -> None:
        self.children: dict[int, MaximumXorNode] = {}


def find_maximum_xor(nums: list[int]) -> int:
    # Problem 18: Maximum XOR Of Two Numbers In An Array
    # Key idea: binary trie of bits, greedily choosing the opposite bit at each
    # level to maximize XOR.
    # Time:
    # Space:

    raise NotImplementedError


def maximize_xor(nums: list[int], queries: list[list[int]]) -> list[int]:
    # Problem 19: Maximum XOR With an Element From Array
    # Key idea: bit-trie with offline sorted queries, inserting values under an
    # upper-bound limit.
    # Time:
    # Space:

    raise NotImplementedError


class SuffixQueryNode:
    # Node for Longest Common Suffix Queries.
    def __init__(self) -> None:
        self.children: dict[str, SuffixQueryNode] = {}
        self.best_index: int = -1


def string_indices(words_container: list[str], words_query: list[str]) -> list[int]:
    # Problem 20: Longest Common Suffix Queries
    # Key idea: suffix trie of reversed words where each node caches the best
    # (shortest, smallest-index) word.
    # Time:
    # Space:

    raise NotImplementedError
