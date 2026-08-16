from problem_set.rotated_array_problems import (
    find_min_rotated,
    find_min_rotated_ii,
    peak_index_in_mountain_array,
    search_rotated,
    search_rotated_ii,
)


def test_search_rotated_found_right_half():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_search_rotated_found_left_half():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 5) == 1


def test_search_rotated_not_found():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_search_rotated_empty():
    assert search_rotated([], 5) == -1


def test_search_rotated_single_found():
    assert search_rotated([1], 1) == 0


def test_search_rotated_single_missing():
    assert search_rotated([1], 0) == -1


def test_search_rotated_no_rotation():
    assert search_rotated([1, 2, 3, 4, 5], 4) == 3


def test_find_min_rotated_middle_pivot():
    assert find_min_rotated([4, 5, 6, 7, 0, 1, 2]) == 0


def test_find_min_rotated_no_rotation():
    assert find_min_rotated([1, 2, 3, 4, 5]) == 1


def test_find_min_rotated_single():
    assert find_min_rotated([1]) == 1


def test_find_min_rotated_two_elements():
    assert find_min_rotated([2, 1]) == 1


def test_find_min_rotated_small_rotation():
    assert find_min_rotated([3, 1, 2]) == 1


def test_search_rotated_ii_found_with_duplicates():
    assert search_rotated_ii([2, 5, 6, 0, 0, 1, 2], 0) is True


def test_search_rotated_ii_not_found_with_duplicates():
    assert search_rotated_ii([2, 5, 6, 0, 0, 1, 2], 3) is False


def test_search_rotated_ii_empty():
    assert search_rotated_ii([], 1) is False


def test_search_rotated_ii_single_found():
    assert search_rotated_ii([1], 1) is True


def test_search_rotated_ii_all_same_missing():
    assert search_rotated_ii([1, 1, 1, 1], 2) is False


def test_find_min_rotated_ii_with_duplicates():
    assert find_min_rotated_ii([2, 2, 2, 0, 1]) == 0


def test_find_min_rotated_ii_no_rotation():
    assert find_min_rotated_ii([1, 1, 1]) == 1


def test_find_min_rotated_ii_single():
    assert find_min_rotated_ii([1]) == 1


def test_find_min_rotated_ii_all_duplicates():
    assert find_min_rotated_ii([2, 2, 2, 2]) == 2


def test_peak_index_in_mountain_array_minimal():
    assert peak_index_in_mountain_array([0, 1, 0]) == 1


def test_peak_index_in_mountain_array_longer_descent():
    assert peak_index_in_mountain_array([0, 2, 1, 0]) == 1


def test_peak_index_in_mountain_array_late_peak():
    assert peak_index_in_mountain_array([3, 4, 5, 1]) == 2
