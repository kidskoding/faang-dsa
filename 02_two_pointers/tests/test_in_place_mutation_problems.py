from problem_set.in_place_mutation_problems import (
    merge,
    rotate,
    sort_colors,
    wiggle_sort,
)


def test_merge_both_empty():
    nums1: list[int] = []
    nums2: list[int] = []
    merge(nums1, 0, nums2, 0)
    assert nums1 == []


def test_merge_second_empty():
    nums1 = [1, 2, 3]
    nums2: list[int] = []
    merge(nums1, 3, nums2, 0)
    assert nums1 == [1, 2, 3]


def test_merge_first_empty():
    nums1 = [0, 0, 0]
    nums2 = [1, 2, 3]
    merge(nums1, 0, nums2, 3)
    assert nums1 == [1, 2, 3]


def test_merge_normal():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_sort_colors_empty():
    nums: list[int] = []
    sort_colors(nums)
    assert nums == []


def test_sort_colors_single():
    nums = [1]
    sort_colors(nums)
    assert nums == [1]


def test_sort_colors_normal():
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_sort_colors_already_sorted():
    nums = [0, 1, 2]
    sort_colors(nums)
    assert nums == [0, 1, 2]


def test_rotate_normal():
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_rotate_with_negatives():
    nums = [-1, -100, 3, 99]
    rotate(nums, 2)
    assert nums == [3, 99, -1, -100]


def test_rotate_k_larger_than_length():
    nums = [1, 2]
    rotate(nums, 3)
    assert nums == [2, 1]


def test_wiggle_sort_alternates():
    nums = [1, 5, 1, 1, 6, 4]
    wiggle_sort(nums)

    assert sorted(nums) == [1, 1, 1, 4, 5, 6]
    assert all(nums[i] < nums[i + 1] if i % 2 == 0 else nums[i] > nums[i + 1] for i in range(len(nums) - 1))


def test_wiggle_sort_odd_length():
    nums = [1, 5, 1, 1, 6, 4, 3]
    wiggle_sort(nums)

    assert sorted(nums) == [1, 1, 1, 3, 4, 5, 6]
    assert all(
        nums[i] < nums[i + 1] if i % 2 == 0 else nums[i] > nums[i + 1]
        for i in range(len(nums) - 1)
    )


def test_wiggle_sort_two_elements():
    nums = [2, 1]
    wiggle_sort(nums)

    assert nums == [1, 2]


def test_wiggle_sort_single_element():
    nums = [7]
    wiggle_sort(nums)

    assert nums == [7]
