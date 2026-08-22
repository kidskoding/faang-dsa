from problem_set.greedy_fundamentals_problems import (
    assign_cookies,
    bag_of_tokens_score,
    can_complete_circuit,
    can_place_flowers,
    connect_sticks,
    find_maximized_capital,
    furthest_building,
    lemonade_change,
    max_profit,
    maximum_units,
    min_add_to_make_valid,
    min_deletions,
    min_refuel_stops,
    remove_duplicate_letters,
    remove_k_digits,
    reorganize_string,
    schedule_course,
    two_city_sched_cost,
    wiggle_max_length,
)


def test_assign_cookies_normal():
    assert assign_cookies([1, 2, 3], [1, 1]) == 1


def test_assign_cookies_all_satisfied():
    assert assign_cookies([1, 2], [1, 2, 3]) == 2


def test_assign_cookies_empty_children():
    assert assign_cookies([], [1, 2, 3]) == 0


def test_assign_cookies_empty_cookies():
    assert assign_cookies([1, 2, 3], []) == 0


def test_lemonade_change_success():
    assert lemonade_change([5, 5, 5, 10, 20]) is True


def test_lemonade_change_failure():
    assert lemonade_change([5, 5, 10, 10, 20]) is False


def test_lemonade_change_single_five():
    assert lemonade_change([5]) is True


def test_lemonade_change_empty():
    assert lemonade_change([]) is True


def test_max_profit_multiple_transactions():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 7


def test_max_profit_monotonic_decreasing():
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_max_profit_single_day():
    assert max_profit([5]) == 0


def test_max_profit_empty():
    assert max_profit([]) == 0


def test_can_complete_circuit_solvable():
    assert can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3


def test_can_complete_circuit_impossible():
    assert can_complete_circuit([2, 3, 4], [3, 4, 3]) == -1


def test_can_complete_circuit_single_station():
    assert can_complete_circuit([5], [4]) == 0


def test_can_complete_circuit_empty():
    assert can_complete_circuit([], []) == -1


def test_can_place_flowers_one_fits():
    assert can_place_flowers([1, 0, 0, 0, 1], 1) is True


def test_can_place_flowers_two_do_not_fit():
    assert can_place_flowers([1, 0, 0, 0, 1], 2) is False


def test_maximum_units_partial_box():
    assert maximum_units([[1, 3], [2, 2], [3, 1]], 4) == 8


def test_maximum_units_full_truck():
    assert maximum_units([[5, 10], [2, 5], [4, 7], [3, 9]], 10) == 91


def test_min_add_to_make_valid_extra_close():
    assert min_add_to_make_valid("())") == 1


def test_min_add_to_make_valid_all_open():
    assert min_add_to_make_valid("(((") == 3


def test_min_add_to_make_valid_already_valid():
    assert min_add_to_make_valid("()") == 0


def test_wiggle_max_length_fully_wiggly():
    assert wiggle_max_length([1, 7, 4, 9, 2, 5]) == 6


def test_wiggle_max_length_monotonic():
    assert wiggle_max_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2


def test_bag_of_tokens_score_trades_down():
    assert bag_of_tokens_score([100, 200, 300, 400], 200) == 2


def test_two_city_sched_cost_normal():
    assert two_city_sched_cost([[10, 20], [30, 200], [400, 50], [30, 20]]) == 110


def test_two_city_sched_cost_six_people():
    costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
    assert two_city_sched_cost(costs) == 1859


def test_remove_k_digits_normal():
    assert remove_k_digits("1432219", 3) == "1219"


def test_remove_k_digits_strips_leading_zero():
    assert remove_k_digits("10200", 1) == "200"


def test_remove_k_digits_removes_everything():
    assert remove_k_digits("10", 2) == "0"


def test_remove_duplicate_letters_normal():
    assert remove_duplicate_letters("cbacdcbc") == "acdb"


def test_reorganize_string_possible():
    result = reorganize_string("aab")

    assert sorted(result) == sorted("aab")
    assert all(result[i] != result[i + 1] for i in range(len(result) - 1))


def test_reorganize_string_impossible():
    assert reorganize_string("aaab") == ""


def test_min_deletions_already_unique():
    assert min_deletions("aab") == 0


def test_min_deletions_normal():
    assert min_deletions("aaabbbcc") == 2


def test_min_deletions_longer():
    assert min_deletions("ceabaacb") == 2


def test_connect_sticks_three():
    assert connect_sticks([2, 4, 3]) == 14


def test_connect_sticks_four():
    assert connect_sticks([1, 8, 3, 5]) == 30


def test_connect_sticks_single():
    assert connect_sticks([5]) == 0


def test_furthest_building_runs_out_of_bricks():
    assert furthest_building([4, 2, 7, 6, 9, 14, 12], 5, 1) == 4


def test_furthest_building_uses_ladders_on_big_gaps():
    assert furthest_building([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2) == 7


def test_find_maximized_capital_two_projects():
    assert find_maximized_capital(2, 0, [1, 2, 3], [0, 1, 1]) == 4


def test_find_maximized_capital_three_projects():
    assert find_maximized_capital(3, 0, [1, 2, 3], [0, 1, 2]) == 6


def test_min_refuel_stops_normal():
    assert min_refuel_stops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]) == 2


def test_schedule_course_normal():
    assert schedule_course([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]) == 3


def test_bag_of_tokens_score_cannot_play_any():
    assert bag_of_tokens_score([100], 50) == 0


def test_bag_of_tokens_score_single_affordable_token():
    assert bag_of_tokens_score([100], 200) == 1


def test_remove_duplicate_letters_already_unique():
    assert remove_duplicate_letters("abc") == "abc"


def test_remove_duplicate_letters_simple_repeat():
    assert remove_duplicate_letters("bcabc") == "abc"


def test_min_refuel_stops_no_stations_needed():
    assert min_refuel_stops(1, 1, []) == 0


def test_min_refuel_stops_unreachable():
    assert min_refuel_stops(100, 1, [[10, 100]]) == -1


def test_schedule_course_single_course_fits():
    assert schedule_course([[1, 2]]) == 1


def test_schedule_course_none_fit():
    assert schedule_course([[3, 2], [4, 3]]) == 0
