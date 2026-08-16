from problem_set.divide_and_conquer_problems import (
    beautiful_array,
    closest_pair,
    diff_ways_to_compute,
    find_median_sorted_arrays,
    get_skyline,
    max_sub_array,
)


def test_diff_ways_to_compute_single_number():
    assert diff_ways_to_compute("2") == [2]


def test_diff_ways_to_compute_normal():
    assert sorted(diff_ways_to_compute("2-1-1")) == [0, 2]


def test_diff_ways_to_compute_mixed_operators():
    assert sorted(diff_ways_to_compute("2*3-4*5")) == sorted([-34, -14, -10, -10, 10])


def test_get_skyline_single_building():
    assert get_skyline([[0, 2, 3]]) == [[0, 3], [2, 0]]


def test_get_skyline_overlapping_buildings():
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    expected = [
        [2, 10],
        [3, 15],
        [7, 12],
        [12, 0],
        [15, 10],
        [20, 8],
        [24, 0],
    ]
    assert get_skyline(buildings) == expected


def test_get_skyline_empty():
    assert get_skyline([]) == []


def test_closest_pair_two_points():
    assert closest_pair([[0, 0], [3, 4]]) == 5.0


def test_closest_pair_normal():
    points = [[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]
    assert closest_pair(points) == 1.4142135623730951


def test_closest_pair_duplicate_points():
    assert closest_pair([[1, 1], [1, 1], [5, 5]]) == 0.0


def test_beautiful_array_single():
    assert beautiful_array(1) == [1]


def test_beautiful_array_is_permutation():
    n = 6
    result = beautiful_array(n)
    assert sorted(result) == list(range(1, n + 1))


def test_beautiful_array_no_arithmetic_triple():
    result = beautiful_array(8)
    values = {v: i for i, v in enumerate(result)}
    for a in range(1, 9):
        for b in range(a + 1, 9):
            c = 2 * b - a
            if c in values:
                assert not (values[a] < values[b] < values[c])


def test_max_sub_array_normal():
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_sub_array_all_negative():
    assert max_sub_array([-1]) == -1


def test_find_median_sorted_arrays_odd_total():
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0


def test_find_median_sorted_arrays_even_total():
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
