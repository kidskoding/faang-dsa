from problem_set.search_on_answer_problems import (
    arrange_coins,
    find_duplicate,
    find_kth_number,
    find_median_sorted_arrays,
    kth_smallest,
    max_distance,
    min_days,
    min_eating_speed,
    min_speed_on_time,
    my_sqrt,
    ship_within_days,
    smallest_distance_pair,
    smallest_divisor,
    split_array,
)


def test_my_sqrt_perfect_square():
    assert my_sqrt(4) == 2


def test_my_sqrt_rounds_down():
    assert my_sqrt(8) == 2


def test_my_sqrt_zero():
    assert my_sqrt(0) == 0


def test_my_sqrt_one():
    assert my_sqrt(1) == 1


def test_min_eating_speed_basic():
    assert min_eating_speed([3, 6, 7, 11], 8) == 4


def test_min_eating_speed_exact_pile_count():
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30


def test_min_eating_speed_generous_hours():
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23


def test_min_eating_speed_single_pile():
    assert min_eating_speed([5], 1) == 5


def test_ship_within_days_basic():
    assert ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15


def test_ship_within_days_one_day():
    assert ship_within_days([3, 2, 2, 4, 1, 4], 1) == 16


def test_ship_within_days_one_per_day():
    assert ship_within_days([1, 2, 3, 1, 1], 4) == 3


def test_ship_within_days_single_package():
    assert ship_within_days([7], 1) == 7


def test_split_array_basic():
    assert split_array([7, 2, 5, 10, 8], 2) == 18


def test_split_array_single_group():
    assert split_array([1, 2, 3, 4, 5], 1) == 15


def test_split_array_groups_equal_length():
    assert split_array([1, 4, 4], 3) == 4


def test_split_array_single_element():
    assert split_array([5], 1) == 5


def test_find_median_sorted_arrays_odd_total():
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0


def test_find_median_sorted_arrays_even_total():
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5


def test_find_median_sorted_arrays_one_empty():
    assert find_median_sorted_arrays([], [1]) == 1.0


def test_find_median_sorted_arrays_both_single():
    assert find_median_sorted_arrays([2], [3]) == 2.5


def test_arrange_coins_partial_last_row():
    assert arrange_coins(5) == 2


def test_arrange_coins_normal():
    assert arrange_coins(8) == 3


def test_arrange_coins_single():
    assert arrange_coins(1) == 1


def test_min_speed_on_time_generous_hour():
    assert min_speed_on_time([1, 3, 2], 6) == 1


def test_min_speed_on_time_fractional_hour():
    assert min_speed_on_time([1, 3, 2], 2.7) == 3


def test_min_speed_on_time_impossible():
    assert min_speed_on_time([1, 3, 2], 1.9) == -1


def test_smallest_divisor_normal():
    assert smallest_divisor([1, 2, 5, 9], 6) == 5


def test_smallest_divisor_tight_threshold():
    assert smallest_divisor([44, 22, 33, 11, 1], 5) == 44


def test_find_duplicate_normal():
    assert find_duplicate([1, 3, 4, 2, 2]) == 2


def test_find_duplicate_repeat_is_first_value():
    assert find_duplicate([3, 1, 3, 4, 2]) == 3


def test_min_days_single_flower_bouquets():
    assert min_days([1, 10, 3, 10, 2], 3, 1) == 3


def test_min_days_impossible():
    assert min_days([1, 10, 3, 10, 2], 3, 2) == -1


def test_min_days_adjacent_requirement():
    assert min_days([7, 7, 7, 7, 12, 7, 7], 2, 3) == 12


def test_max_distance_normal():
    assert max_distance([1, 2, 3, 4, 7], 3) == 3


def test_max_distance_two_baskets():
    assert max_distance([5, 4, 3, 2, 1, 1000000000], 2) == 999999999


def test_kth_smallest_normal():
    assert kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13


def test_kth_smallest_single_cell():
    assert kth_smallest([[-5]], 1) == -5


def test_find_kth_number_square_table():
    assert find_kth_number(3, 3, 5) == 3


def test_find_kth_number_last_entry():
    assert find_kth_number(2, 3, 6) == 6


def test_smallest_distance_pair_zero_distance():
    assert smallest_distance_pair([1, 3, 1], 1) == 0


def test_smallest_distance_pair_all_equal():
    assert smallest_distance_pair([1, 1, 1], 2) == 0


def test_smallest_distance_pair_largest_gap():
    assert smallest_distance_pair([1, 6, 1], 3) == 5
