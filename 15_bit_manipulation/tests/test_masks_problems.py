from problem_set.masks_problems import get_sum, min_flips, range_bitwise_and


def test_get_sum_normal():
    assert get_sum(1, 2) == 3


def test_get_sum_with_carry():
    assert get_sum(2, 3) == 5


def test_get_sum_zero():
    assert get_sum(0, 0) == 0


def test_get_sum_negative():
    assert get_sum(-2, 3) == 1


def test_get_sum_both_negative():
    assert get_sum(-5, -7) == -12


def test_range_bitwise_and_same_value():
    assert range_bitwise_and(5, 5) == 5


def test_range_bitwise_and_normal():
    assert range_bitwise_and(5, 7) == 4


def test_range_bitwise_and_includes_zero():
    assert range_bitwise_and(0, 1) == 0


def test_range_bitwise_and_wide_range():
    assert range_bitwise_and(1, 2147483647) == 0


def test_min_flips_zero_flips_needed():
    assert min_flips(2, 6, 5) == 3


def test_min_flips_already_equal():
    assert min_flips(4, 2, 7) == 1


def test_min_flips_all_zero():
    assert min_flips(1, 2, 3) == 0
