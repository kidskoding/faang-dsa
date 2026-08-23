from problem_set.in_place_mutation_problems import (
    merge,
    pancake_sort,
    rearrange_array,
    remove_duplicates_ii,
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


def _apply_flips(arr: list[int], flips: list[int]) -> list[int]:
    out = arr[:]
    for k in flips:
        out[:k] = out[:k][::-1]
    return out


def test_remove_duplicates_ii_keeps_at_most_two():
    nums = [1, 1, 1, 2, 2, 3]
    k = remove_duplicates_ii(nums)

    assert k == 5
    assert nums[:k] == [1, 1, 2, 2, 3]


def test_remove_duplicates_ii_longer():
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = remove_duplicates_ii(nums)

    assert k == 7
    assert nums[:k] == [0, 0, 1, 1, 2, 3, 3]


def test_remove_duplicates_ii_single_element():
    nums = [1]
    k = remove_duplicates_ii(nums)

    assert k == 1
    assert nums[:k] == [1]


def test_rearrange_array_alternates_signs():
    assert rearrange_array([3, 1, -2, -5, 2, -4]) == [3, -2, 1, -5, 2, -4]


def test_rearrange_array_shortest():
    assert rearrange_array([-1, 1]) == [1, -1]


def test_pancake_sort_normal():
    arr = [3, 2, 4, 1]
    assert _apply_flips(arr, pancake_sort(arr)) == [1, 2, 3, 4]


def test_pancake_sort_already_sorted():
    arr = [1, 2, 3]
    assert _apply_flips(arr, pancake_sort(arr)) == [1, 2, 3]


def test_pancake_sort_two_swapped():
    arr = [2, 1, 3]
    assert _apply_flips(arr, pancake_sort(arr)) == [1, 2, 3]
