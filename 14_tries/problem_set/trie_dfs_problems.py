from __future__ import annotations


class WordSearchNode:
    # Node for Word Search II.
    def __init__(self) -> None:
        self.children: dict[str, WordSearchNode] = {}
        self.word: str | None = None


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    # Problem 9: Word Search II
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
    # Problem 10: Palindrome Pairs
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
    # Problem 11: Concatenated Words
    # Key idea: trie or hash set of words plus DFS/DP to check if a word
    # splits into other words.
    # Time:
    # Space:

    raise NotImplementedError
