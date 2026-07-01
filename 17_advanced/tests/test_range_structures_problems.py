from problem_set.range_structures_problems import (
    NumArray,
    NumMatrix,
    count_range_sum,
    count_smaller,
)


def test_num_array_sum_range():
    num_array = NumArray([1, 3, 5])
    assert num_array.sum_range(0, 2) == 9


def test_num_array_update_then_sum():
    num_array = NumArray([1, 3, 5])
    num_array.update(1, 2)
    assert num_array.sum_range(0, 2) == 8


def test_num_array_single_element():
    num_array = NumArray([7])
    assert num_array.sum_range(0, 0) == 7


def test_num_matrix_sum_region():
    matrix = [[3, 0, 1, 4], [5, 6, 3, 2], [1, 2, 0, 1], [4, 3, 4, 6]]
    num_matrix = NumMatrix(matrix)
    assert num_matrix.sum_region(2, 1, 4 - 1, 3) == 8


def test_num_matrix_update_then_sum_region():
    matrix = [[3, 0, 1, 4], [5, 6, 3, 2], [1, 2, 0, 1], [4, 3, 4, 6]]
    num_matrix = NumMatrix(matrix)
    num_matrix.update(3, 2, 2)
    assert num_matrix.sum_region(2, 1, 4 - 1, 3) == 10


def test_num_matrix_single_cell():
    num_matrix = NumMatrix([[5]])
    assert num_matrix.sum_region(0, 0, 0, 0) == 5


def test_count_smaller_normal():
    assert count_smaller([5, 2, 6, 1]) == [2, 1, 1, 0]


def test_count_smaller_sorted_ascending():
    assert count_smaller([1, 2, 3]) == [0, 0, 0]


def test_count_smaller_empty():
    assert count_smaller([]) == []


def test_count_range_sum_normal():
    assert count_range_sum([-2, 5, -1], -2, 2) == 3


def test_count_range_sum_single_element():
    assert count_range_sum([0], 0, 0) == 1


def test_count_range_sum_no_valid_ranges():
    assert count_range_sum([10, 20], -5, 5) == 0
