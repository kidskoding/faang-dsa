from problem_set.monotonic_stack_problems import (
    StockSpanner,
    asteroid_collision,
    daily_temperatures,
    largest_rectangle_area,
    next_greater_element,
    next_greater_elements,
    remove_k_digits,
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
