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


def camel_match(queries: list[str], pattern: str) -> list[bool]:
    # Problem 9: Camelcase Matching
    # Key idea: match each query against the pattern trie, allowing extra
    # lowercase but never extra uppercase.
    # Time:
    # Space:

    pass


class WordFilterNode:
    # Node for Prefix And Suffix Search.
    def __init__(self) -> None:
        self.children: dict[str, WordFilterNode] = {}
        self.weight: int = -1


class WordFilter:
    # Problem 10: Prefix And Suffix Search
    # Key idea: index each word by combined suffix#prefix keys so a single trie
    # answers both filters.

    def __init__(self, words: list[str]) -> None:
        # Time:
        # Space:
        pass

    def f(self, prefix: str, suffix: str) -> int:
        # Time:
        # Space:
        pass


class AutocompleteNode:
    # Node for Design Search Autocomplete System.
    def __init__(self) -> None:
        self.children: dict[str, AutocompleteNode] = {}
        self.counts: dict[str, int] = {}


class AutocompleteSystem:
    # Problem 11: Design Search Autocomplete System
    # Key idea: trie nodes store historical query frequencies, ranked as the
    # user types each character.

    def __init__(self, sentences: list[str], times: list[int]) -> None:
        # Time:
        # Space:
        pass

    def input(self, c: str) -> list[str]:
        # Time:
        # Space:
        pass
