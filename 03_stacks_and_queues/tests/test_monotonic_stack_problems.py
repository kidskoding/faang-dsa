from problem_set.monotonic_stack_problems import (
    StockSpanner,
    asteroid_collision,
    car_fleet,
    daily_temperatures,
    find132pattern,
    largest_rectangle_area,
    maximal_rectangle,
    next_greater_element,
    next_greater_elements,
    remove_duplicate_letters,
    remove_k_digits,
    sub_array_ranges,
    sum_subarray_mins,
    trap,
)


def test_stock_spanner_increasing_prices():
    spanner = StockSpanner()
    assert spanner.next(100) == 1
    assert spanner.next(80) == 1
    assert spanner.next(60) == 1
    assert spanner.next(70) == 2
    assert spanner.next(60) == 1
    assert spanner.next(75) == 4
    assert spanner.next(85) == 6


def test_stock_spanner_single_call():
    spanner = StockSpanner()
    assert spanner.next(50) == 1


def test_daily_temperatures_normal_case():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ]


def test_daily_temperatures_empty():
    assert daily_temperatures([]) == []


def test_daily_temperatures_single_element():
    assert daily_temperatures([50]) == [0]


def test_daily_temperatures_strictly_decreasing():
    assert daily_temperatures([80, 70, 60]) == [0, 0, 0]


def test_next_greater_element_normal_case():
    assert next_greater_element([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]


def test_next_greater_element_empty_nums1():
    assert next_greater_element([], [1, 2, 3]) == []


def test_next_greater_element_no_greater_found():
    assert next_greater_element([2], [3, 2, 1]) == [-1]


def test_next_greater_elements_circular_case():
    assert next_greater_elements([1, 2, 1]) == [2, -1, 2]


def test_next_greater_elements_single_element():
    assert next_greater_elements([5]) == [-1]


def test_next_greater_elements_empty():
    assert next_greater_elements([]) == []


def test_asteroid_collision_normal_case():
    assert asteroid_collision([5, 10, -5]) == [5, 10]


def test_asteroid_collision_all_destroyed():
    assert asteroid_collision([8, -8]) == []


def test_asteroid_collision_single_asteroid():
    assert asteroid_collision([5]) == [5]


def test_asteroid_collision_empty():
    assert asteroid_collision([]) == []


def test_remove_k_digits_normal_case():
    assert remove_k_digits("1432219", 3) == "1219"


def test_remove_k_digits_removes_all_digits():
    assert remove_k_digits("10", 2) == "0"


def test_remove_k_digits_single_digit_remove_zero():
    assert remove_k_digits("9", 0) == "9"


def test_largest_rectangle_area_normal_case():
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10


def test_largest_rectangle_area_single_bar():
    assert largest_rectangle_area([4]) == 4


def test_largest_rectangle_area_empty():
    assert largest_rectangle_area([]) == 0


def test_largest_rectangle_area_all_same_height():
    assert largest_rectangle_area([3, 3, 3]) == 9


def test_trap_normal_case():
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_trap_empty():
    assert trap([]) == 0


def test_trap_single_bar():
    assert trap([4]) == 0


def test_trap_no_trapped_water():
    assert trap([1, 2, 3, 4]) == 0


def test_car_fleet_normal():
    assert car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3


def test_car_fleet_single_car():
    assert car_fleet(10, [3], [3]) == 1


def test_car_fleet_all_merge():
    assert car_fleet(100, [0, 2, 4], [4, 2, 1]) == 1


def test_remove_duplicate_letters_normal():
    assert remove_duplicate_letters("bcabc") == "abc"


def test_remove_duplicate_letters_keeps_needed_larger_letter():
    assert remove_duplicate_letters("cbacdcbc") == "acdb"


def test_find132pattern_increasing_has_none():
    assert find132pattern([1, 2, 3, 4]) is False


def test_find132pattern_present():
    assert find132pattern([3, 1, 4, 2]) is True


def test_find132pattern_with_negatives():
    assert find132pattern([-1, 3, 2, 0]) is True


def test_sum_subarray_mins_normal():
    assert sum_subarray_mins([3, 1, 2, 4]) == 17


def test_sum_subarray_mins_larger():
    assert sum_subarray_mins([11, 81, 94, 43, 3]) == 444


def test_sub_array_ranges_normal():
    assert sub_array_ranges([1, 2, 3]) == 4


def test_sub_array_ranges_with_duplicates():
    assert sub_array_ranges([1, 3, 3]) == 4


def test_sub_array_ranges_with_negatives():
    assert sub_array_ranges([4, -2, -3, 4, 1]) == 59


def test_maximal_rectangle_normal():
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]

    assert maximal_rectangle(matrix) == 6


def test_maximal_rectangle_all_zero():
    assert maximal_rectangle([["0"]]) == 0


def test_maximal_rectangle_single_one():
    assert maximal_rectangle([["1"]]) == 1
