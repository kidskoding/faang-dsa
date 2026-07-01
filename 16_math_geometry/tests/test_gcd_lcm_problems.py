from problem_set.gcd_lcm_problems import fraction_to_decimal


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
