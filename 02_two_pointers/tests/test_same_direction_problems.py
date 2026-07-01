from problem_set.same_direction_problems import (
    move_zeroes,
    remove_duplicates,
    remove_element,
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
