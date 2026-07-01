from problem_set.xor_problems import (
    missing_number,
    single_number,
    single_number_ii,
    single_number_iii,
)


def test_single_number_normal():
    assert single_number([4, 1, 2, 1, 2]) == 4


def test_single_number_single_element():
    assert single_number([1]) == 1


def test_single_number_negative_values():
    assert single_number([-1, -1, -2]) == -2


def test_single_number_ii_normal():
    assert single_number_ii([2, 2, 3, 2]) == 3


def test_single_number_ii_single_element():
    assert single_number_ii([99]) == 99


def test_single_number_ii_larger_group():
    assert single_number_ii([0, 1, 0, 1, 0, 1, 99]) == 99


def test_single_number_iii_normal():
    assert sorted(single_number_iii([1, 2, 1, 3, 2, 5])) == [3, 5]


def test_single_number_iii_two_elements():
    assert sorted(single_number_iii([-1, 0])) == [-1, 0]


def test_missing_number_normal():
    assert missing_number([3, 0, 1]) == 2


def test_missing_number_missing_last():
    assert missing_number([0, 1]) == 2


def test_missing_number_missing_first():
    assert missing_number([1, 2]) == 0


def test_missing_number_single_element_missing():
    assert missing_number([1]) == 0


def test_missing_number_empty():
    assert missing_number([]) == 0
