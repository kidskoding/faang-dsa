from problem_set.knapsack_problems import (
    can_partition,
    change,
    coin_change,
    combination_sum4,
    find_max_form,
    find_target_sum_ways,
)


def test_can_partition_empty():
    assert can_partition([]) is True


def test_can_partition_normal_true():
    assert can_partition([1, 5, 11, 5]) is True


def test_can_partition_normal_false():
    assert can_partition([1, 2, 3, 5]) is False


def test_can_partition_single_element():
    assert can_partition([1]) is False


def test_find_target_sum_ways_normal():
    assert find_target_sum_ways([1, 1, 1, 1, 1], 3) == 5


def test_find_target_sum_ways_single_zero_target():
    assert find_target_sum_ways([1], 1) == 1


def test_find_target_sum_ways_no_way():
    assert find_target_sum_ways([1], 2) == 0


def test_coin_change_normal():
    assert coin_change([1, 2, 5], 11) == 3


def test_coin_change_impossible():
    assert coin_change([2], 3) == -1


def test_coin_change_zero_amount():
    assert coin_change([1], 0) == 0


def test_coin_change_empty_coins():
    assert coin_change([], 7) == -1


def test_change_normal():
    assert change(5, [1, 2, 5]) == 4


def test_change_no_combination():
    assert change(3, [2]) == 0


def test_change_zero_amount():
    assert change(0, [1, 2, 3]) == 1


def test_change_empty_coins():
    assert change(0, []) == 1


def test_combination_sum4_counts_orderings():
    assert combination_sum4([1, 2, 3], 4) == 7


def test_combination_sum4_unreachable():
    assert combination_sum4([9], 3) == 0


def test_find_max_form_normal():
    assert find_max_form(["10", "0001", "111001", "1", "0"], 5, 3) == 4


def test_find_max_form_tight_budget():
    assert find_max_form(["10", "0", "1"], 1, 1) == 2
