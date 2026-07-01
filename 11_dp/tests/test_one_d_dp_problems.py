from problem_set.one_d_dp_problems import (
    climbing_stairs,
    min_cost_climbing_stairs,
    num_decodings,
    rob,
    rob_ii,
)


def test_climbing_stairs_base_cases():
    assert climbing_stairs(1) == 1
    assert climbing_stairs(2) == 2


def test_climbing_stairs_normal():
    assert climbing_stairs(5) == 8


def test_min_cost_climbing_stairs_normal():
    assert min_cost_climbing_stairs([10, 15, 20]) == 15


def test_min_cost_climbing_stairs_alternating():
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


def test_min_cost_climbing_stairs_two_steps():
    assert min_cost_climbing_stairs([0, 0]) == 0


def test_rob_empty():
    assert rob([]) == 0


def test_rob_single():
    assert rob([5]) == 5


def test_rob_normal():
    assert rob([1, 2, 3, 1]) == 4


def test_rob_alternating_better():
    assert rob([2, 7, 9, 3, 1]) == 12


def test_rob_ii_single():
    assert rob_ii([5]) == 5


def test_rob_ii_two_houses():
    assert rob_ii([1, 2]) == 2


def test_rob_ii_normal():
    assert rob_ii([2, 3, 2]) == 3


def test_rob_ii_larger():
    assert rob_ii([1, 2, 3, 1]) == 4


def test_num_decodings_empty():
    assert num_decodings("") == 0


def test_num_decodings_single_digit():
    assert num_decodings("2") == 1


def test_num_decodings_normal():
    assert num_decodings("12") == 2


def test_num_decodings_with_zero():
    assert num_decodings("06") == 0


def test_num_decodings_leading_invalid():
    assert num_decodings("0") == 0
