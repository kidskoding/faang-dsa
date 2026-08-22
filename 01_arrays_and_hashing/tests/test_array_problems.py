from problem_set.array_problems import (
    RandomizedSet,
    find_duplicate,
    find_duplicates,
    first_missing_positive,
    increasing_triplet,
    maximum_swap,
    next_permutation,
    rotate,
    rotate_image,
    set_zeroes,
    sort_colors,
    spiral_order,
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


def test_sort_colors_mixed():
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_sort_colors_one_of_each():
    nums = [2, 0, 1]
    sort_colors(nums)
    assert nums == [0, 1, 2]


def test_sort_colors_single():
    nums = [0]
    sort_colors(nums)
    assert nums == [0]


def test_sort_colors_no_twos():
    nums = [1, 1, 0, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1]


def test_find_duplicate_normal():
    assert find_duplicate([1, 3, 4, 2, 2]) == 2


def test_find_duplicate_repeat_is_first_value():
    assert find_duplicate([3, 1, 3, 4, 2]) == 3


def test_find_duplicate_two_elements():
    assert find_duplicate([1, 1]) == 1


def test_find_duplicate_all_same():
    assert find_duplicate([2, 2, 2, 2, 2]) == 2


def test_spiral_order_square():
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_spiral_order_wide():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert spiral_order(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


def test_spiral_order_single_cell():
    assert spiral_order([[7]]) == [7]


def test_spiral_order_two_by_two():
    assert spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]


def test_rotate_image_three_by_three():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_image(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


def test_rotate_image_two_by_two():
    matrix = [[1, 2], [3, 4]]
    rotate_image(matrix)
    assert matrix == [[3, 1], [4, 2]]


def test_rotate_image_single_cell():
    matrix = [[1]]
    rotate_image(matrix)
    assert matrix == [[1]]


def test_increasing_triplet_sorted():
    assert increasing_triplet([1, 2, 3, 4, 5]) is True


def test_increasing_triplet_descending():
    assert increasing_triplet([5, 4, 3, 2, 1]) is False


def test_increasing_triplet_out_of_order():
    assert increasing_triplet([2, 1, 5, 0, 4, 6]) is True


def test_increasing_triplet_all_equal():
    assert increasing_triplet([1, 1, 1]) is False


def test_maximum_swap_normal():
    assert maximum_swap(2736) == 7236


def test_maximum_swap_already_maximal():
    assert maximum_swap(9973) == 9973


def test_maximum_swap_repeated_digits():
    assert maximum_swap(1993) == 9913


def test_maximum_swap_uses_the_last_occurrence():
    assert maximum_swap(98368) == 98863
