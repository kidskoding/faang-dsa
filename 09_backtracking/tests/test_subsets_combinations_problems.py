from problem_set.subsets_combinations_problems import (
    combination_sum,
    combination_sum2,
    combination_sum3,
    combine,
    count_vowel_strings,
    subsets,
    subsets_with_dup,
)


def to_sorted_sets(result: list[list[int]]) -> list[tuple[int, ...]]:
    return sorted(tuple(sorted(group)) for group in result)


def test_subsets_empty():
    assert subsets([]) == [[]]


def test_subsets_single_element():
    assert to_sorted_sets(subsets([1])) == sorted([(), (1,)])


def test_subsets_normal():
    assert to_sorted_sets(subsets([1, 2, 3])) == to_sorted_sets([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])


def test_subsets_with_dup_normal():
    assert to_sorted_sets(subsets_with_dup([1, 2, 2])) == to_sorted_sets([[], [1], [2], [1, 2], [2, 2], [1, 2, 2]])


def test_subsets_with_dup_all_same():
    assert to_sorted_sets(subsets_with_dup([2, 2])) == to_sorted_sets([[], [2], [2, 2]])


def test_combine_normal():
    assert to_sorted_sets(combine(4, 2)) == to_sorted_sets([[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])


def test_combine_k_equals_n():
    assert combine(2, 2) == [[1, 2]]


def test_combination_sum_normal():
    assert to_sorted_sets(combination_sum([2, 3, 6, 7], 7)) == to_sorted_sets([[2, 2, 3], [7]])


def test_combination_sum_no_solution():
    assert combination_sum([5], 3) == []


def test_combination_sum2_normal():
    assert to_sorted_sets(combination_sum2([10, 1, 2, 7, 6, 1, 5], 8)) == to_sorted_sets([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])


def test_combination_sum2_no_solution():
    assert combination_sum2([2], 1) == []


def test_combination_sum3_normal():
    assert to_sorted_sets(combination_sum3(3, 7)) == to_sorted_sets([[1, 2, 4]])


def test_combination_sum3_no_solution():
    assert combination_sum3(9, 1) == []


def test_count_vowel_strings_length_one():
    assert count_vowel_strings(1) == 5


def test_count_vowel_strings_length_two():
    assert count_vowel_strings(2) == 15


def test_count_vowel_strings_long():
    assert count_vowel_strings(33) == 66045
