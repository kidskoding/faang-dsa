from problem_set.word_dictionary_problems import (
    MagicDictionary,
    StreamChecker,
    WordDictionary,
    search_suggestions,
)


def test_word_dictionary_exact_and_wildcard_search():
    word_dictionary = WordDictionary()
    word_dictionary.add_word("bad")
    word_dictionary.add_word("dad")
    word_dictionary.add_word("mad")

    assert word_dictionary.search("pad") is False
    assert word_dictionary.search("bad") is True
    assert word_dictionary.search(".ad") is True
    assert word_dictionary.search("b..") is True


def test_word_dictionary_search_empty():
    word_dictionary = WordDictionary()
    assert word_dictionary.search("a") is False


def test_word_dictionary_all_wildcards():
    word_dictionary = WordDictionary()
    word_dictionary.add_word("ab")
    assert word_dictionary.search("..") is True
    assert word_dictionary.search("...") is False


def test_magic_dictionary_one_character_swap():
    magic_dictionary = MagicDictionary()
    magic_dictionary.build_dict(["hello", "leetcode"])

    assert magic_dictionary.search("hello") is False
    assert magic_dictionary.search("hhllo") is True
    assert magic_dictionary.search("hell") is False
    assert magic_dictionary.search("leetcoded") is False


def test_magic_dictionary_empty_dictionary():
    magic_dictionary = MagicDictionary()
    magic_dictionary.build_dict([])
    assert magic_dictionary.search("hello") is False


def test_search_suggestions_normal():
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    search_word = "mouse"
    expected = [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
    ]
    assert search_suggestions(products, search_word) == expected


def test_search_suggestions_no_matches():
    products = ["havana"]
    search_word = "tatiana"
    assert search_suggestions(products, search_word) == [[] for _ in search_word]


def test_stream_checker_matches_suffix():
    stream_checker = StreamChecker(["cd", "f", "kl"])
    results = [stream_checker.query(letter) for letter in "abcdefghijkl"]
    expected = [
        False, False, False, True, False, True,
        False, False, False, False, False, True,
    ]
    assert results == expected


def test_stream_checker_single_letter_word():
    stream_checker = StreamChecker(["a"])
    assert stream_checker.query("a") is True
    assert stream_checker.query("b") is False
    assert stream_checker.query("a") is True
