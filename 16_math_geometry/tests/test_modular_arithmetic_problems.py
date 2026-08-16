from problem_set.modular_arithmetic_problems import (
    add_strings,
    can_win_nim,
    convert_to_title,
    count_primes,
    int_to_roman,
    is_happy,
    is_palindrome,
    multiply,
    my_pow,
    my_sqrt,
    nth_ugly_number,
    num_squares,
    plus_one,
    rand10,
    reverse,
    title_to_number,
    trailing_zeroes,
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


def test_plus_one_no_carry():
    assert plus_one([1, 2, 3]) == [1, 2, 4]


def test_plus_one_single_carry():
    assert plus_one([9]) == [1, 0]


def test_plus_one_cascading_carry():
    assert plus_one([9, 9]) == [1, 0, 0]


def test_is_palindrome_true():
    assert is_palindrome(121) is True


def test_is_palindrome_negative():
    assert is_palindrome(-121) is False


def test_is_palindrome_trailing_zero():
    assert is_palindrome(10) is False


def test_add_strings_normal():
    assert add_strings("11", "123") == "134"


def test_add_strings_with_carry():
    assert add_strings("456", "77") == "533"


def test_add_strings_zeros():
    assert add_strings("0", "0") == "0"


def test_reverse_positive():
    assert reverse(123) == 321


def test_reverse_negative():
    assert reverse(-123) == -321


def test_reverse_trailing_zero():
    assert reverse(120) == 21


def test_reverse_overflow_returns_zero():
    assert reverse(1534236469) == 0


def test_count_primes_below_ten():
    assert count_primes(10) == 4


def test_count_primes_zero():
    assert count_primes(0) == 0


def test_count_primes_two():
    assert count_primes(2) == 0


def test_trailing_zeroes_none():
    assert trailing_zeroes(3) == 0


def test_trailing_zeroes_one():
    assert trailing_zeroes(5) == 1


def test_trailing_zeroes_many():
    assert trailing_zeroes(30) == 7


def test_multiply_single_digits():
    assert multiply("2", "3") == "6"


def test_multiply_multi_digit():
    assert multiply("123", "456") == "56088"


def test_multiply_by_zero():
    assert multiply("0", "52") == "0"


def test_int_to_roman_large():
    assert int_to_roman(3749) == "MMMDCCXLIX"


def test_int_to_roman_normal():
    assert int_to_roman(58) == "LVIII"


def test_int_to_roman_subtractive():
    assert int_to_roman(1994) == "MCMXCIV"


def test_nth_ugly_number_tenth():
    assert nth_ugly_number(10) == 12


def test_nth_ugly_number_first():
    assert nth_ugly_number(1) == 1


def test_num_squares_three_terms():
    assert num_squares(12) == 3


def test_num_squares_two_terms():
    assert num_squares(13) == 2


def test_num_squares_perfect_square():
    assert num_squares(1) == 1


def test_rand10_stays_in_range():
    assert all(1 <= rand10() <= 10 for _ in range(200))


def test_rand10_covers_the_range():
    assert len({rand10() for _ in range(2000)}) == 10
