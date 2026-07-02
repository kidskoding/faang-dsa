from __future__ import annotations


class WordDictionaryNode:
    # Node for Design Add And Search Words Data Structure.
    def __init__(self) -> None:
        self.children: dict[str, WordDictionaryNode] = {}
        self.is_word: bool = False


class WordDictionary:
    # Problem 5: Design Add And Search Words Data Structure
    # Key idea: DFS branches into every child when the pattern character is a wildcard.

    def __init__(self) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def add_word(self, word: str) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        # Time:
        # Space:
        raise NotImplementedError


class MagicDictionaryNode:
    # Node for Implement Magic Dictionary.
    def __init__(self) -> None:
        self.children: dict[str, MagicDictionaryNode] = {}
        self.is_word: bool = False


class MagicDictionary:
    # Problem 6: Implement Magic Dictionary
    # Key idea: DFS search that must change exactly one character to reach a
    # stored word.

    def __init__(self) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def build_dict(self, dictionary: list[str]) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def search(self, search_word: str) -> bool:
        # Time:
        # Space:
        raise NotImplementedError


def search_suggestions(products: list[str], search_word: str) -> list[list[str]]:
    # Problem 7: Search Suggestions System
    # Key idea: walk the trie one character at a time, collecting the smallest
    # matches at each prefix.
    # Time:
    # Space:

    raise NotImplementedError


class StreamCheckerNode:
    # Node for Stream Of Characters.
    def __init__(self) -> None:
        self.children: dict[str, StreamCheckerNode] = {}
        self.is_word: bool = False


class StreamChecker:
    # Problem 8: Stream Of Characters
    # Key idea: build the trie on reversed words, then check backward from the
    # newest character.

    def __init__(self, words: list[str]) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def query(self, letter: str) -> bool:
        # Time:
        # Space:
        raise NotImplementedError
