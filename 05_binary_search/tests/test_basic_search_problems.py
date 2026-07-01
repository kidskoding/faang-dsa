from problem_set.basic_search_problems import (
    search,
    search_insert,
    search_matrix,
    search_matrix_ii,
)


def test_search_found_middle():
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4


def test_search_found_first():
    assert search([-1, 0, 3, 5, 9, 12], -1) == 0


def test_search_not_found():
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1


def test_search_empty():
    assert search([], 5) == -1


def test_search_single_found():
    assert search([5], 5) == 0


def test_search_single_missing():
    assert search([5], 3) == -1


def test_search_insert_found():
    assert search_insert([1, 3, 5, 6], 5) == 2


def test_search_insert_middle_gap():
    assert search_insert([1, 3, 5, 6], 2) == 1


def test_search_insert_end():
    assert search_insert([1, 3, 5, 6], 7) == 4


def test_search_insert_beginning():
    assert search_insert([1, 3, 5, 6], 0) == 0


def test_search_insert_empty():
    assert search_insert([], 5) == 0


def test_search_matrix_found():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert search_matrix(matrix, 3) is True


def test_search_matrix_not_found():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert search_matrix(matrix, 13) is False


def test_search_matrix_single_cell():
    assert search_matrix([[5]], 5) is True


def test_search_matrix_empty():
    assert search_matrix([], 1) is False


def test_search_matrix_ii_found():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert search_matrix_ii(matrix, 5) is True


def test_search_matrix_ii_not_found():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert search_matrix_ii(matrix, 20) is False


def test_search_matrix_ii_empty():
    assert search_matrix_ii([], 1) is False
