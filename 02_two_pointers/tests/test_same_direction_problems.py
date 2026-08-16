from problem_set.same_direction_problems import (
    find_duplicate,
    interval_intersection,
    longest_mountain,
    move_zeroes,
    num_subarray_bounded_max,
    num_subarray_product_less_than_k,
    partition_labels,
    remove_duplicates,
    remove_element,
    subarrays_with_k_distinct,
)


def test_remove_element_empty():
    nums: list[int] = []
    assert remove_element(nums, 5) == 0


def test_remove_element_single_match():
    nums = [5]
    k = remove_element(nums, 5)
    assert k == 0


def test_remove_element_single_no_match():
    nums = [3]
    k = remove_element(nums, 5)
    assert k == 1
    assert nums[:k] == [3]


def test_remove_element_normal():
    nums = [3, 2, 2, 3]
    k = remove_element(nums, 3)
    assert k == 2
    assert sorted(nums[:k]) == [2, 2]


def test_remove_duplicates_empty():
    nums: list[int] = []
    assert remove_duplicates(nums) == 0


def test_remove_duplicates_single():
    nums = [1]
    k = remove_duplicates(nums)
    assert k == 1
    assert nums[:k] == [1]


def test_remove_duplicates_no_dupes():
    nums = [1, 2, 3]
    k = remove_duplicates(nums)
    assert k == 3
    assert nums[:k] == [1, 2, 3]


def test_remove_duplicates_with_dupes():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    assert k == 5
    assert nums[:k] == [0, 1, 2, 3, 4]


def test_move_zeroes_empty():
    nums: list[int] = []
    move_zeroes(nums)
    assert nums == []


def test_move_zeroes_single_zero():
    nums = [0]
    move_zeroes(nums)
    assert nums == [0]


def test_move_zeroes_normal():
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    assert nums == [1, 3, 12, 0, 0]


def test_move_zeroes_no_zeroes():
    nums = [1, 2, 3]
    move_zeroes(nums)
    assert nums == [1, 2, 3]


def test_find_duplicate_normal():
    assert find_duplicate([1, 3, 4, 2, 2]) == 2


def test_find_duplicate_repeat_is_first_value():
    assert find_duplicate([3, 1, 3, 4, 2]) == 3


def test_partition_labels_normal():
    assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]


def test_partition_labels_single_part():
    assert partition_labels("eccbbbbdec") == [10]


def test_longest_mountain_normal():
    assert longest_mountain([2, 1, 4, 7, 3, 2, 5]) == 5


def test_longest_mountain_flat():
    assert longest_mountain([2, 2, 2]) == 0


def test_longest_mountain_minimum():
    assert longest_mountain([0, 1, 0]) == 3


def test_num_subarray_product_less_than_k_normal():
    assert num_subarray_product_less_than_k([10, 5, 2, 6], 100) == 8


def test_num_subarray_product_less_than_k_zero_k():
    assert num_subarray_product_less_than_k([1, 2, 3], 0) == 0


def test_num_subarray_bounded_max_normal():
    assert num_subarray_bounded_max([2, 1, 4, 3], 2, 3) == 3


def test_num_subarray_bounded_max_wider_range():
    assert num_subarray_bounded_max([2, 9, 2, 5, 6], 2, 8) == 7


def test_interval_intersection_normal():
    first = [[0, 2], [5, 10], [13, 23], [24, 25]]
    second = [[1, 5], [8, 12], [15, 24], [25, 26]]

    assert interval_intersection(first, second) == [
        [1, 2],
        [5, 5],
        [8, 10],
        [15, 23],
        [24, 24],
        [25, 25],
    ]


def test_interval_intersection_empty_second():
    assert interval_intersection([[1, 3], [5, 9]], []) == []


def test_subarrays_with_k_distinct_normal():
    assert subarrays_with_k_distinct([1, 2, 1, 2, 3], 2) == 7


def test_subarrays_with_k_distinct_three():
    assert subarrays_with_k_distinct([1, 2, 1, 3, 4], 3) == 3
