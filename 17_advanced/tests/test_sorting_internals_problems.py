from problem_set.sorting_internals_problems import (
    largest_number,
    sort_array,
    wiggle_sort,
)


def test_sort_array_empty():
    assert sort_array([]) == []


def test_sort_array_single():
    assert sort_array([1]) == [1]


def test_sort_array_normal():
    assert sort_array([5, 2, 3, 1]) == [1, 2, 3, 5]


def test_sort_array_duplicates():
    assert sort_array([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]


def test_sort_array_already_sorted():
    assert sort_array([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_largest_number_normal():
    assert largest_number([10, 2]) == "210"


def test_largest_number_all_zeros():
    assert largest_number([0, 0]) == "0"


def test_largest_number_single():
    assert largest_number([5]) == "5"


def test_largest_number_mixed_lengths():
    assert largest_number([3, 30, 34, 5, 9]) == "9534330"


def test_wiggle_sort_single():
    nums = [1]
    wiggle_sort(nums)
    assert nums == [1]


def test_wiggle_sort_normal():
    nums = [1, 5, 1, 1, 6, 4]
    wiggle_sort(nums)
    for i in range(1, len(nums) - 1, 2):
        assert nums[i - 1] < nums[i] > nums[i + 1]


def test_wiggle_sort_with_duplicates():
    nums = [1, 3, 2, 2, 3, 1]
    wiggle_sort(nums)
    for i in range(1, len(nums) - 1, 2):
        assert nums[i - 1] < nums[i] > nums[i + 1]
