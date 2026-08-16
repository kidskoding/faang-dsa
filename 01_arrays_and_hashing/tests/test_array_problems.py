from problem_set.array_problems import (
    RandomizedSet,
    find_duplicates,
    first_missing_positive,
    next_permutation,
    rotate,
    set_zeroes,
)


def test_rotate_normal():
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_rotate_k_greater_than_length():
    nums = [1, 2, 3]
    rotate(nums, 4)
    assert nums == [3, 1, 2]


def test_rotate_single_element():
    nums = [1]
    rotate(nums, 5)
    assert nums == [1]


def test_rotate_empty():
    nums = []
    rotate(nums, 0)
    assert nums == []


def test_set_zeroes_normal():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


def test_set_zeroes_single_element():
    matrix = [[0]]
    set_zeroes(matrix)
    assert matrix == [[0]]


def test_set_zeroes_multiple_zeroes():
    matrix = [[0, 1, 2], [3, 4, 5], [0, 6, 7]]
    set_zeroes(matrix)
    assert matrix == [[0, 0, 0], [0, 4, 5], [0, 0, 0]]


def test_find_duplicates_normal():
    assert find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]


def test_find_duplicates_single_element():
    assert find_duplicates([1]) == []


def test_find_duplicates_empty():
    assert find_duplicates([]) == []


def test_first_missing_positive_normal():
    assert first_missing_positive([3, 4, -1, 1]) == 2


def test_first_missing_positive_all_present():
    assert first_missing_positive([1, 2, 0]) == 3


def test_first_missing_positive_disjoint():
    assert first_missing_positive([7, 8, 9]) == 1


def test_first_missing_positive_empty():
    assert first_missing_positive([]) == 1


def test_first_missing_positive_single_element():
    assert first_missing_positive([1]) == 2


def test_randomized_set_insert_and_remove():
    randomized_set = RandomizedSet()
    assert randomized_set.insert(1) is True
    assert randomized_set.insert(1) is False
    assert randomized_set.remove(1) is True
    assert randomized_set.remove(1) is False


def test_randomized_set_get_random_returns_inserted_value():
    randomized_set = RandomizedSet()
    randomized_set.insert(42)
    assert randomized_set.get_random() == 42


def test_randomized_set_remove_missing_value():
    randomized_set = RandomizedSet()
    assert randomized_set.remove(99) is False


def test_next_permutation_middle():
    nums = [1, 2, 3]
    next_permutation(nums)
    assert nums == [1, 3, 2]


def test_next_permutation_last_wraps_to_first():
    nums = [3, 2, 1]
    next_permutation(nums)
    assert nums == [1, 2, 3]


def test_next_permutation_with_duplicates():
    nums = [1, 1, 5]
    next_permutation(nums)
    assert nums == [1, 5, 1]


def test_next_permutation_single():
    nums = [1]
    next_permutation(nums)
    assert nums == [1]
