from problem_set.prefix_sum_problems import (
    NumArray,
    NumMatrix,
    check_subarray_sum,
    subarray_sum,
    subarrays_div_by_k,
)


def test_num_array_sum_range_normal():
    num_array = NumArray([-2, 0, 3, -5, 2, -1])
    assert num_array.sum_range(0, 2) == 1
    assert num_array.sum_range(2, 5) == -1
    assert num_array.sum_range(0, 5) == -3


def test_num_array_sum_range_single_element():
    num_array = NumArray([7])
    assert num_array.sum_range(0, 0) == 7


def test_subarray_sum_normal():
    assert subarray_sum([1, 1, 1], 2) == 2


def test_subarray_sum_negative_numbers():
    assert subarray_sum([1, -1, 0], 0) == 3


def test_subarray_sum_no_match():
    assert subarray_sum([1, 2, 3], 100) == 0


def test_subarray_sum_single_element():
    assert subarray_sum([5], 5) == 1


def test_check_subarray_sum_true():
    assert check_subarray_sum([23, 2, 4, 6, 7], 6) is True


def test_check_subarray_sum_false():
    assert check_subarray_sum([23, 2, 6, 4, 7], 13) is False


def test_check_subarray_sum_zero_sum_pair():
    assert check_subarray_sum([23, 2, 6, 4, 7], 6) is True


def test_num_matrix_sum_region_normal():
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]
    num_matrix = NumMatrix(matrix)
    assert num_matrix.sum_region(2, 1, 4, 3) == 8
    assert num_matrix.sum_region(1, 1, 2, 2) == 11
    assert num_matrix.sum_region(1, 2, 2, 4) == 12


def test_num_matrix_sum_region_single_cell():
    num_matrix = NumMatrix([[5]])
    assert num_matrix.sum_region(0, 0, 0, 0) == 5


def test_subarrays_div_by_k_normal():
    assert subarrays_div_by_k([4, 5, 0, -2, -3, 1], 5) == 7


def test_subarrays_div_by_k_single_element_divisible():
    assert subarrays_div_by_k([5], 5) == 1


def test_subarrays_div_by_k_no_match():
    assert subarrays_div_by_k([1, 2, 3], 100) == 0
