from __future__ import annotations


class TrieNode:
    # Shared node for the trie-basics problems in this file.
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_word: bool = False


class Trie:
    # Problem 1: Implement Trie (Prefix Tree)
    # Key idea: children map plus an end-of-word marker.

    def __init__(self) -> None:
        # Time:
        # Space:
        pass

    def insert(self, word: str) -> None:
        # Time:
        # Space:
        pass

    def search(self, word: str) -> bool:
        # Time:
        # Space:
        pass

    def starts_with(self, prefix: str) -> bool:
        # Time:
        # Space:
        pass


class MapSumNode:
    # Node for Map Sum Pairs.
    def __init__(self) -> None:
        self.children: dict[str, MapSumNode] = {}
        self.value: int = 0


class MapSum:
    # Problem 2: Map Sum Pairs
    # Key idea: trie nodes carry a running value sum for every prefix.

    def __init__(self) -> None:
        # Time:
        # Space:
        pass

    def insert(self, key: str, val: int) -> None:
        # Time:
        # Space:
        pass

    def sum(self, prefix: str) -> int:
        # Time:
        # Space:
        pass


def longest_word_in_dictionary(words: list[str]) -> str:
    # Problem 3: Longest Word In Dictionary
    # Key idea: a word is only reachable if every prefix of it is itself a complete word.
    # Time:
    # Space:

    pass


def replace_words(dictionary: list[str], sentence: str) -> str:
    # Problem 4: Replace Words
    # Key idea: walk the trie from each word's start and stop at the first
    # end-of-word marker to find its shortest root.
    # Time:
    # Space:

    pass
