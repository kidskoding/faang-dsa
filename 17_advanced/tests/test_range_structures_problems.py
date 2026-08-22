from problem_set.range_structures_problems import (
    FenwickTree,
    MyCalendarThree,
    NumArray,
    NumMatrix,
    count_range_sum,
    count_smaller,
    reverse_pairs,
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


def test_fenwick_tree_prefix_and_range_sums():
    tree = FenwickTree(5)
    tree.update(0, 1)
    tree.update(2, 3)

    assert tree.prefix_sum(2) == 4
    assert tree.range_sum(1, 2) == 3
    assert tree.range_sum(0, 4) == 4


def test_fenwick_tree_starts_empty():
    tree = FenwickTree(3)

    assert tree.prefix_sum(2) == 0


def test_reverse_pairs_normal():
    assert reverse_pairs([1, 3, 2, 3, 1]) == 2


def test_reverse_pairs_more():
    assert reverse_pairs([2, 4, 3, 5, 1]) == 3


def test_my_calendar_three_tracks_max_overlap():
    calendar = MyCalendarThree()

    assert calendar.book(10, 20) == 1
    assert calendar.book(50, 60) == 1
    assert calendar.book(10, 40) == 2
    assert calendar.book(5, 15) == 3
    assert calendar.book(5, 10) == 3
    assert calendar.book(25, 55) == 3


def test_my_calendar_three_disjoint_bookings_stay_at_one():
    calendar = MyCalendarThree()

    assert calendar.book(10, 20) == 1
    assert calendar.book(30, 40) == 1


def test_my_calendar_three_touching_intervals_do_not_overlap():
    calendar = MyCalendarThree()

    assert calendar.book(10, 20) == 1
    assert calendar.book(20, 30) == 1


def test_my_calendar_three_triple_overlap():
    calendar = MyCalendarThree()
    calendar.book(10, 20)
    calendar.book(15, 25)

    assert calendar.book(12, 18) == 3
