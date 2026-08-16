from problem_set.subset_masks_problems import (
    can_partition_k_subsets,
    distribute_cookies,
    max_students,
    max_xor_of_two_numbers,
    shortest_path_length,
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


def test_can_partition_k_subsets_possible():
    assert can_partition_k_subsets([4, 3, 2, 3, 5, 2, 1], 4) is True


def test_can_partition_k_subsets_impossible():
    assert can_partition_k_subsets([1, 2, 3, 4], 3) is False


def test_shortest_path_length_star_graph():
    assert shortest_path_length([[1, 2, 3], [0], [0], [0]]) == 4


def test_shortest_path_length_branching_tree():
    assert shortest_path_length([[1], [0, 2, 4], [1, 3], [2], [1, 5], [4]]) == 6


def test_max_students_normal():
    seats = [
        ["#", ".", "#", "#", ".", "#"],
        [".", "#", "#", "#", "#", "."],
        ["#", ".", "#", "#", ".", "#"],
    ]
    assert max_students(seats) == 4


def test_max_students_narrow_room():
    seats = [[".", "#"], ["#", "#"], ["#", "."], ["#", "#"], [".", "#"]]
    assert max_students(seats) == 3


def test_distribute_cookies_two_children():
    assert distribute_cookies([8, 15, 10, 20, 8], 2) == 31


def test_distribute_cookies_three_children():
    assert distribute_cookies([6, 1, 3, 2, 2, 4, 1, 2], 3) == 7
