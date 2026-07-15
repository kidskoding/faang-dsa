from problem_set.gcd_lcm_problems import (
    common_factors,
    fraction_to_decimal,
    gcd_of_strings,
)


def test_fraction_to_decimal_terminating():
    assert fraction_to_decimal(1, 2) == "0.5"


def test_fraction_to_decimal_repeating():
    assert fraction_to_decimal(2, 3) == "0.(6)"


def test_fraction_to_decimal_integer_result():
    assert fraction_to_decimal(4, 2) == "2"


def test_fraction_to_decimal_negative():
    assert fraction_to_decimal(-1, 2) == "-0.5"


def test_fraction_to_decimal_zero_numerator():
    assert fraction_to_decimal(0, 5) == "0"


def test_fraction_to_decimal_long_repeat():
    assert fraction_to_decimal(1, 6) == "0.1(6)"


def test_gcd_of_strings_clean_divisor():
    assert gcd_of_strings("ABCABC", "ABC") == "ABC"


def test_gcd_of_strings_smaller_divisor():
    assert gcd_of_strings("ABABAB", "ABAB") == "AB"


def test_gcd_of_strings_no_common():
    assert gcd_of_strings("LEET", "CODE") == ""


def test_common_factors_normal():
    assert common_factors(12, 6) == 4


def test_common_factors_coprime_ish():
    assert common_factors(25, 30) == 2


def test_common_factors_equal():
    assert common_factors(1, 1) == 1
