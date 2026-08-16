from problem_set.jump_game_problems import (
    can_jump,
    can_reach,
    can_reach_end,
    jump,
    min_jumps,
    minimum_jumps,
)


def test_can_jump_reachable():
    assert can_jump([2, 3, 1, 1, 4]) is True


def test_can_jump_unreachable():
    assert can_jump([3, 2, 1, 0, 4]) is False


def test_can_jump_single_index():
    assert can_jump([0]) is True


def test_can_jump_empty():
    assert can_jump([]) is True


def test_jump_normal():
    assert jump([2, 3, 1, 1, 4]) == 2


def test_jump_single_index():
    assert jump([0]) == 0


def test_jump_already_at_end_with_zeros():
    assert jump([1, 1, 1, 1]) == 3


def test_jump_large_first_step():
    assert jump([5, 1, 1, 1, 1]) == 1


def test_can_reach_true():
    assert can_reach([4, 2, 3, 0, 3, 1, 2], 5) is True


def test_can_reach_false():
    assert can_reach([4, 2, 3, 0, 3, 1, 2], 3) is False


def test_can_reach_start_is_zero_value():
    assert can_reach([3, 0, 2, 1, 2], 2) is True


def test_can_reach_single_element():
    assert can_reach([0], 0) is True


def test_min_jumps_uses_teleports():
    assert min_jumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]) == 3


def test_min_jumps_single_element():
    assert min_jumps([7]) == 0


def test_min_jumps_same_value_ends():
    assert min_jumps([7, 6, 9, 6, 9, 6, 9, 7]) == 1


def test_can_reach_end_reachable():
    assert can_reach_end("011010", 2, 3) is True


def test_can_reach_end_blocked():
    assert can_reach_end("01101110", 2, 3) is False


def test_minimum_jumps_normal():
    assert minimum_jumps([14, 4, 18, 1, 15], 3, 15, 9) == 3


def test_minimum_jumps_unreachable():
    assert minimum_jumps([8, 3, 16, 6, 12, 20], 15, 13, 11) == -1


def test_minimum_jumps_backwards_helps():
    assert minimum_jumps([1, 6, 2, 14, 5, 17, 4], 16, 9, 7) == 2
