from problem_set.in_place_mutation_problems import merge, sort_colors


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
