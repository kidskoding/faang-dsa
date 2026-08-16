from problem_set.backtracking_basics_problems import (
    count_arrangement,
    generate_parentheses,
    letter_case_permutation,
    letter_combinations,
    max_unique_split,
)


def test_letter_combinations_empty():
    assert letter_combinations("") == []


def test_letter_combinations_single_digit():
    assert sorted(letter_combinations("2")) == sorted(["a", "b", "c"])


def test_letter_combinations_two_digits():
    assert sorted(letter_combinations("23")) == sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])


def test_generate_parentheses_single_pair():
    assert sorted(generate_parentheses(1)) == ["()"]


def test_generate_parentheses_two_pairs():
    assert sorted(generate_parentheses(2)) == sorted(["(())", "()()"])


def test_generate_parentheses_three_pairs():
    assert sorted(generate_parentheses(3)) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])


def test_count_arrangement_single():
    assert count_arrangement(1) == 1


def test_count_arrangement_normal():
    assert count_arrangement(2) == 2


def test_count_arrangement_larger():
    assert count_arrangement(4) == 8


def test_letter_case_permutation_letters_and_digits():
    assert sorted(letter_case_permutation("a1b2")) == sorted(["a1b2", "a1B2", "A1b2", "A1B2"])


def test_letter_case_permutation_single_letter():
    assert sorted(letter_case_permutation("3z4")) == ["3Z4", "3z4"]


def test_letter_case_permutation_no_letters():
    assert letter_case_permutation("12") == ["12"]


def test_max_unique_split_normal():
    assert max_unique_split("ababccc") == 5


def test_max_unique_split_short():
    assert max_unique_split("aba") == 2


def test_max_unique_split_all_same():
    assert max_unique_split("aa") == 1
