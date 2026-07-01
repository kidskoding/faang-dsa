from problem_set.modular_arithmetic_problems import (
    can_win_nim,
    convert_to_title,
    is_happy,
    my_pow,
    my_sqrt,
    title_to_number,
)


def test_my_pow_positive_exponent():
    assert my_pow(2.0, 10) == 1024.0


def test_my_pow_negative_exponent():
    assert my_pow(2.0, -2) == 0.25


def test_my_pow_zero_exponent():
    assert my_pow(2.0, 0) == 1.0


def test_my_pow_base_one():
    assert my_pow(1.0, 100) == 1.0


def test_my_sqrt_perfect_square():
    assert my_sqrt(4) == 2


def test_my_sqrt_rounds_down():
    assert my_sqrt(8) == 2


def test_my_sqrt_zero():
    assert my_sqrt(0) == 0


def test_my_sqrt_one():
    assert my_sqrt(1) == 1


def test_can_win_nim_multiple_of_four():
    assert can_win_nim(4) is False


def test_can_win_nim_not_multiple_of_four():
    assert can_win_nim(5) is True


def test_can_win_nim_one_stone():
    assert can_win_nim(1) is True


def test_is_happy_true():
    assert is_happy(19) is True


def test_is_happy_false():
    assert is_happy(2) is False


def test_is_happy_one():
    assert is_happy(1) is True


def test_title_to_number_single_letter():
    assert title_to_number("A") == 1


def test_title_to_number_double_letter():
    assert title_to_number("AB") == 28


def test_title_to_number_zz():
    assert title_to_number("ZY") == 701


def test_convert_to_title_single_letter():
    assert convert_to_title(1) == "A"


def test_convert_to_title_double_letter():
    assert convert_to_title(28) == "AB"


def test_convert_to_title_z():
    assert convert_to_title(26) == "Z"
