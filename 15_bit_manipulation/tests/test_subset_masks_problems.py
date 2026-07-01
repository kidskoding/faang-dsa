from problem_set.subset_masks_problems import (
    max_xor_of_two_numbers,
    subsets,
    total_hamming_distance,
)


def test_subsets_empty_input():
    assert subsets([]) == [[]]


def test_subsets_single_element():
    result = {tuple(sorted(s)) for s in subsets([1])}
    assert result == {(), (1,)}


def test_subsets_normal():
    result = {tuple(sorted(s)) for s in subsets([1, 2, 3])}
    expected = {
        (),
        (1,),
        (2,),
        (3,),
        (1, 2),
        (1, 3),
        (2, 3),
        (1, 2, 3),
    }
    assert result == expected


def test_total_hamming_distance_normal():
    assert total_hamming_distance([4, 14, 2]) == 6


def test_total_hamming_distance_single_element():
    assert total_hamming_distance([5]) == 0


def test_total_hamming_distance_identical_values():
    assert total_hamming_distance([7, 7, 7]) == 0


def test_max_xor_of_two_numbers_normal():
    assert max_xor_of_two_numbers([3, 10, 5, 25, 2, 8]) == 28


def test_max_xor_of_two_numbers_two_elements():
    assert max_xor_of_two_numbers([0, 1]) == 1


def test_max_xor_of_two_numbers_zeros():
    assert max_xor_of_two_numbers([0, 0]) == 0
