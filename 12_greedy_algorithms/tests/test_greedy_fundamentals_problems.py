from problem_set.greedy_fundamentals_problems import (
    assign_cookies,
    can_complete_circuit,
    lemonade_change,
    max_profit,
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
