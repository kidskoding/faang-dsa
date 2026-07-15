from problem_set.multi_pattern_problems import (
    LRUCache,
    alien_order,
    find_ladders,
    longest_dup_substring,
    max_result,
)


def test_lru_cache_eviction_sequence():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_lru_cache_update_existing():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(1, 10)
    assert cache.get(1) == 10


def test_alien_order_normal_case():
    assert alien_order(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"


def test_alien_order_invalid_ordering():
    assert alien_order(["z", "x", "z"]) == ""


def test_find_ladders_normal_case():
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

    result = find_ladders("hit", "cog", word_list)

    assert sorted(tuple(path) for path in result) == sorted(
        tuple(path)
        for path in [
            ["hit", "hot", "dot", "dog", "cog"],
            ["hit", "hot", "lot", "log", "cog"],
        ]
    )


def test_find_ladders_no_path():
    assert find_ladders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == []


def test_longest_dup_substring_normal():
    assert longest_dup_substring("banana") == "ana"


def test_longest_dup_substring_none():
    assert longest_dup_substring("abcd") == ""


def test_max_result_normal():
    assert max_result([1, -1, -2, 4, -7, 3], 2) == 7


def test_max_result_large_jumps():
    assert max_result([10, -5, -2, 4, 0, 3], 3) == 17


def test_max_result_all_negative_middle():
    assert max_result([1, -5, -20, 4, -1, 3, -6, -3], 2) == 0
