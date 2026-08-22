from problem_set.kadane_problems import (
    k_concatenation_max_sum,
    max_absolute_sum,
    max_product_subarray,
    max_profit,
    max_subarray,
    max_subarray_sum_circular,
    max_turbulence_size,
    maximum_sum,
)


def test_max_subarray_normal():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_subarray_all_negative():
    assert max_subarray([-3, -1, -2]) == -1


def test_max_subarray_single_element():
    assert max_subarray([5]) == 5


def test_max_profit_normal():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5


def test_max_profit_no_profit():
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_max_profit_single_price():
    assert max_profit([5]) == 0


def test_max_profit_empty():
    assert max_profit([]) == 0


def test_max_product_subarray_normal():
    assert max_product_subarray([2, 3, -2, 4]) == 6


def test_max_product_subarray_negative_flip():
    assert max_product_subarray([-2, 0, -1]) == 0


def test_max_product_subarray_single_element():
    assert max_product_subarray([-5]) == -5


def test_max_subarray_sum_circular_non_wrapping():
    assert max_subarray_sum_circular([1, -2, 3, -2]) == 3


def test_max_subarray_sum_circular_wraps():
    assert max_subarray_sum_circular([5, -3, 5]) == 10


def test_max_subarray_sum_circular_all_negative():
    assert max_subarray_sum_circular([-3, -2, -3]) == -2


def test_max_subarray_sum_circular_wraps_by_one():
    assert max_subarray_sum_circular([3, -1, 2, -1]) == 4


def test_max_absolute_sum_negative_run_wins():
    assert max_absolute_sum([1, -3, 2, 3, -4]) == 5


def test_max_absolute_sum_longer():
    assert max_absolute_sum([2, -5, 1, -4, 3, -2]) == 8


def test_max_absolute_sum_all_positive():
    assert max_absolute_sum([1, 2, 3]) == 6


def test_max_turbulence_size_normal():
    assert max_turbulence_size([9, 4, 2, 10, 7, 8, 8, 1, 9]) == 5


def test_max_turbulence_size_monotonic():
    assert max_turbulence_size([4, 8, 12, 16]) == 2


def test_max_turbulence_size_single():
    assert max_turbulence_size([100]) == 1


def test_k_concatenation_max_sum_positive_total():
    assert k_concatenation_max_sum([1, 2], 3) == 9


def test_k_concatenation_max_sum_non_positive_total():
    assert k_concatenation_max_sum([1, -2, 1], 5) == 2


def test_k_concatenation_max_sum_all_negative():
    assert k_concatenation_max_sum([-1, -2], 7) == 0


def test_maximum_sum_deletes_one_negative():
    assert maximum_sum([1, -2, 0, 3]) == 4


def test_maximum_sum_deletion_not_enough():
    assert maximum_sum([1, -2, -2, 3]) == 3


def test_maximum_sum_all_negative():
    assert maximum_sum([-1, -1, -1, -1]) == -1


def test_maximum_sum_deletes_from_the_middle():
    assert maximum_sum([2, 1, -2, -5, -2]) == 3
