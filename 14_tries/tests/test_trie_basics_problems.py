from problem_set.trie_basics_problems import (
    MapSum,
    Trie,
    longest_word_in_dictionary,
    replace_words,
)


def test_trie_insert_and_search():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.starts_with("app") is True


def test_trie_search_empty_trie():
    trie = Trie()
    assert trie.search("anything") is False
    assert trie.starts_with("a") is False


def test_trie_multiple_words_share_prefix():
    trie = Trie()
    trie.insert("car")
    trie.insert("cat")
    assert trie.search("car") is True
    assert trie.search("cat") is True
    assert trie.search("ca") is False
    assert trie.starts_with("ca") is True
    assert trie.starts_with("ca t") is False


def test_map_sum_single_key():
    map_sum = MapSum()
    map_sum.insert("apple", 3)
    assert map_sum.sum("ap") == 3
    assert map_sum.sum("apple") == 3
    assert map_sum.sum("b") == 0


def test_map_sum_overwrite_key():
    map_sum = MapSum()
    map_sum.insert("apple", 3)
    map_sum.insert("app", 2)
    assert map_sum.sum("ap") == 5
    map_sum.insert("apple", 10)
    assert map_sum.sum("ap") == 12


def test_longest_word_in_dictionary_normal():
    words = ["w", "wo", "wor", "worl", "world"]
    assert longest_word_in_dictionary(words) == "world"


def test_longest_word_in_dictionary_no_valid_chain():
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    assert longest_word_in_dictionary(words) == "apple"


def test_longest_word_in_dictionary_empty():
    assert longest_word_in_dictionary([]) == ""


def test_replace_words_normal():
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    assert replace_words(dictionary, sentence) == "the cat was rat by the bat"


def test_replace_words_no_matching_root():
    dictionary = ["a", "b", "c"]
    sentence = "aadsfasf absbs bbab cadsfafs"
    assert replace_words(dictionary, sentence) == "a a b c"


def test_replace_words_shortest_root_wins():
    dictionary = ["cat", "ca"]
    sentence = "cattle"
    assert replace_words(dictionary, sentence) == "ca"
