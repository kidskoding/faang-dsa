from problem_set.basic_search_problems import (
    ArrayReader,
    find_peak_grid,
    guess_number,
    h_index,
    search,
    search_insert,
    search_matrix,
    search_matrix_ii,
    search_unknown_size,
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


def test_guess_number_finds_target():
    def guess(num: int) -> int:
        return 0 if num == 6 else (-1 if num > 6 else 1)

    assert guess_number(10, guess) == 6


def test_guess_number_single_candidate():
    assert guess_number(1, lambda num: 0) == 1


def test_guess_number_at_upper_bound():
    def guess(num: int) -> int:
        return 0 if num == 10 else (-1 if num > 10 else 1)

    assert guess_number(10, guess) == 10


class _ListReader(ArrayReader):
    """Concrete stand-in; get returns 2^31 - 1 past the end, as the problem states."""

    def __init__(self, values: list[int]) -> None:
        self.values = values

    def get(self, index: int) -> int:
        return self.values[index] if 0 <= index < len(self.values) else 2**31 - 1


def test_find_peak_grid_two_by_two():
    assert find_peak_grid([[1, 4], [3, 2]]) in ([0, 1], [1, 0])


def test_find_peak_grid_three_by_three():
    assert find_peak_grid([[10, 20, 15], [21, 30, 14], [7, 16, 32]]) in ([1, 1], [2, 2])


def test_find_peak_grid_single_cell():
    assert find_peak_grid([[1]]) == [0, 0]


def test_h_index_normal():
    assert h_index([0, 1, 3, 5, 6]) == 3


def test_h_index_few_papers():
    assert h_index([1, 2, 100]) == 2


def test_h_index_no_citations():
    assert h_index([0]) == 0


def test_h_index_single_well_cited_paper():
    assert h_index([100]) == 1


def test_search_unknown_size_found():
    assert search_unknown_size(_ListReader([-1, 0, 3, 5, 9, 12]), 9) == 4


def test_search_unknown_size_missing():
    assert search_unknown_size(_ListReader([-1, 0, 3, 5, 9, 12]), 2) == -1


def test_search_unknown_size_single_element():
    assert search_unknown_size(_ListReader([5]), 5) == 0
