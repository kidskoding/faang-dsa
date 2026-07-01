from problem_set.bitwise_basics_problems import (
    count_bits,
    hamming_weight,
    is_power_of_four,
    is_power_of_two,
    reverse_bits,
)


def test_hamming_weight_zero():
    assert hamming_weight(0) == 0


def test_hamming_weight_single_bit():
    assert hamming_weight(1) == 1


def test_hamming_weight_normal():
    assert hamming_weight(11) == 3


def test_hamming_weight_all_ones_byte():
    assert hamming_weight(255) == 8


def test_count_bits_zero():
    assert count_bits(0) == [0]


def test_count_bits_normal():
    assert count_bits(5) == [0, 1, 1, 2, 1, 2]


def test_count_bits_power_of_two():
    assert count_bits(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1]


def test_reverse_bits_all_zero():
    assert reverse_bits(0) == 0


def test_reverse_bits_all_ones():
    assert reverse_bits(0xFFFFFFFF) == 0xFFFFFFFF


def test_reverse_bits_normal():
    assert reverse_bits(0b00000010100101000001111010011100) == 0b00111001011110000010100101000000


def test_is_power_of_two_true():
    assert is_power_of_two(16) is True


def test_is_power_of_two_false():
    assert is_power_of_two(18) is False


def test_is_power_of_two_zero():
    assert is_power_of_two(0) is False


def test_is_power_of_two_one():
    assert is_power_of_two(1) is True


def test_is_power_of_two_negative():
    assert is_power_of_two(-4) is False


def test_is_power_of_four_true():
    assert is_power_of_four(16) is True


def test_is_power_of_four_false_power_of_two():
    assert is_power_of_four(8) is False


def test_is_power_of_four_zero():
    assert is_power_of_four(0) is False


def test_is_power_of_four_one():
    assert is_power_of_four(1) is True


def test_is_power_of_four_negative():
    assert is_power_of_four(-4) is False
