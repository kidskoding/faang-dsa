from collections import deque

from problem_set.multi_pattern_problems import (
    LFUCache,
    LRUCache,
    SnapshotArray,
    StockPrice,
    TreeNode,
    WeightedRandomPicker,
    alien_order,
    busiest_servers,
    constrained_subset_sum,
    count_range_sum,
    count_subgraphs_for_each_diameter,
    find_ladders,
    find_words,
    job_scheduling,
    longest_dup_substring,
    max_envelopes,
    max_number,
    max_result,
    max_sum_submatrix,
    max_value,
    median_sliding_window,
    min_camera_cover,
    odd_even_jumps,
    rob,
    sort_items,
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


def test_count_subgraphs_for_each_diameter_path():
    assert count_subgraphs_for_each_diameter(4, [[1, 2], [2, 3], [2, 4]]) == [3, 4, 0]


def test_count_subgraphs_for_each_diameter_two_nodes():
    assert count_subgraphs_for_each_diameter(2, [[1, 2]]) == [1]


def test_count_subgraphs_for_each_diameter_star():
    assert count_subgraphs_for_each_diameter(3, [[1, 2], [2, 3]]) == [2, 1]


def build_tree(values: list[int | None]) -> TreeNode | None:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root


def is_valid_item_order(n: int, group: list[int], before_items: list[list[int]], order: list[int]) -> bool:
    """Any order satisfying the constraints is accepted, so check those directly."""
    if sorted(order) != list(range(n)):
        return False
    position = {item: i for i, item in enumerate(order)}
    for item, befores in enumerate(before_items):
        if any(position[b] > position[item] for b in befores):
            return False
    seen_groups: list[int] = []
    for item in order:
        g = group[item]
        if g == -1 or (seen_groups and seen_groups[-1] == g):
            continue
        if g in seen_groups:
            return False
        seen_groups.append(g)
    return True


def test_count_range_sum_normal():
    assert count_range_sum([-2, 5, -1], -2, 2) == 3


def test_count_range_sum_single_zero():
    assert count_range_sum([0], 0, 0) == 1


def test_median_sliding_window_odd_window():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    assert median_sliding_window(nums, 3) == [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]


def test_median_sliding_window_with_repeats():
    nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
    assert median_sliding_window(nums, 3) == [2, 3, 3, 3, 2, 3, 2]


def test_lfu_cache_evicts_least_frequent():
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)

    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_find_words_normal():
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    assert sorted(find_words(board, ["oath", "pea", "eat", "rain"])) == ["eat", "oath"]


def test_find_words_no_match():
    assert find_words([["a", "b"], ["c", "d"]], ["abcb"]) == []


def test_max_envelopes_normal():
    assert max_envelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3


def test_max_envelopes_all_identical():
    assert max_envelopes([[1, 1], [1, 1], [1, 1]]) == 1


def test_max_value_two_events():
    assert max_value([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2) == 7


def test_max_value_one_big_event_wins():
    assert max_value([[1, 2, 4], [3, 4, 3], [2, 3, 10]], 2) == 10


def test_constrained_subset_sum_normal():
    assert constrained_subset_sum([10, 2, -10, 5, 20], 2) == 37


def test_constrained_subset_sum_all_negative():
    assert constrained_subset_sum([-1, -2, -3], 1) == -1


def test_constrained_subset_sum_skips_negatives():
    assert constrained_subset_sum([10, -2, -10, -5, 20], 2) == 23


def test_job_scheduling_normal():
    assert job_scheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]) == 120


def test_job_scheduling_longer():
    start = [1, 2, 3, 4, 6]
    end = [3, 5, 10, 6, 9]
    assert job_scheduling(start, end, [20, 20, 100, 70, 60]) == 150


def test_max_sum_submatrix_normal():
    assert max_sum_submatrix([[1, 0, 1], [0, -2, 3]], 2) == 2


def test_max_sum_submatrix_single_row():
    assert max_sum_submatrix([[2, 2, -1]], 3) == 3


def test_odd_even_jumps_normal():
    assert odd_even_jumps([10, 13, 12, 14, 15]) == 2


def test_odd_even_jumps_more_starts():
    assert odd_even_jumps([2, 3, 1, 1, 4]) == 3


def test_odd_even_jumps_descending_helps():
    assert odd_even_jumps([5, 1, 3, 4, 2]) == 3


def test_snapshot_array_reads_old_snapshot():
    array = SnapshotArray(3)
    array.set(0, 5)

    assert array.snap() == 0
    array.set(0, 6)
    assert array.get(0, 0) == 5


def test_snapshot_array_unset_index_is_zero():
    array = SnapshotArray(2)
    snap_id = array.snap()

    assert array.get(1, snap_id) == 0


def test_stock_price_tracks_current_and_extremes():
    stock = StockPrice()
    stock.update(1, 10)
    stock.update(2, 5)

    assert stock.current() == 5
    assert stock.maximum() == 10


def test_stock_price_corrects_a_record():
    stock = StockPrice()
    stock.update(1, 10)
    stock.update(2, 5)
    stock.update(1, 3)

    assert stock.maximum() == 5
    assert stock.minimum() == 3


def test_busiest_servers_single_busiest():
    assert busiest_servers(3, [1, 2, 3, 4, 5], [5, 2, 3, 3, 3]) == [1]


def test_busiest_servers_first_server():
    assert busiest_servers(3, [1, 2, 3, 4], [1, 2, 1, 2]) == [0]


def test_busiest_servers_all_tied():
    assert busiest_servers(3, [1, 2, 3], [10, 12, 11]) == [0, 1, 2]


def test_sort_items_respects_groups_and_dependencies():
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    before_items = [[], [6], [5], [6], [3, 6], [], [], []]
    order = sort_items(8, 2, group[:], before_items)

    assert is_valid_item_order(8, group, before_items, order)


def test_sort_items_cycle_returns_empty():
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    before_items = [[], [6], [5], [6], [3], [], [4], []]

    assert sort_items(8, 2, group[:], before_items) == []


def test_max_number_normal():
    assert max_number([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5) == [9, 8, 6, 5, 3]


def test_max_number_uses_all_digits():
    assert max_number([6, 7], [6, 0, 4], 5) == [6, 7, 6, 0, 4]


def test_max_number_interleaves():
    assert max_number([3, 9], [8, 9], 3) == [9, 8, 9]


def test_rob_skips_children():
    assert rob(build_tree([3, 2, 3, None, 3, None, 1])) == 7


def test_rob_takes_children_instead():
    assert rob(build_tree([3, 4, 5, 1, 3, None, 1])) == 9


def test_min_camera_cover_one_camera():
    assert min_camera_cover(build_tree([0, 0, None, 0, 0])) == 1


def test_min_camera_cover_two_cameras():
    assert min_camera_cover(build_tree([0, 0, None, 0, None, 0, None, None, 0])) == 2


def test_weighted_random_picker_single_weight():
    picker = WeightedRandomPicker([1])

    assert all(picker.pick_index() == 0 for _ in range(50))


def test_weighted_random_picker_respects_weights():
    picker = WeightedRandomPicker([1, 3])
    draws = [picker.pick_index() for _ in range(20000)]

    assert set(draws) == {0, 1}
    assert 0.70 < draws.count(1) / len(draws) < 0.80
