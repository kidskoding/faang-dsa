from problem_set.interval_basics_problems import (
    find_min_arrow_shots,
    have_conflict,
    interval_intersection,
    partition_labels,
    summary_ranges,
)


def test_summary_ranges_empty():
    assert summary_ranges([]) == []


def test_summary_ranges_single():
    assert summary_ranges([5]) == ["5"]


def test_summary_ranges_normal():
    assert summary_ranges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]


def test_summary_ranges_all_consecutive():
    assert summary_ranges([1, 2, 3, 4]) == ["1->4"]


def test_find_min_arrow_shots_empty():
    assert find_min_arrow_shots([]) == 0


def test_find_min_arrow_shots_single_balloon():
    assert find_min_arrow_shots([[1, 2]]) == 1


def test_find_min_arrow_shots_normal():
    assert find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2


def test_find_min_arrow_shots_no_overlap():
    assert find_min_arrow_shots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4


def test_interval_intersection_empty_first_list():
    assert interval_intersection([], [[1, 5]]) == []


def test_interval_intersection_empty_second_list():
    assert interval_intersection([[1, 5]], []) == []


def test_interval_intersection_normal():
    first_list = [[0, 2], [5, 10], [13, 23], [24, 25]]
    second_list = [[1, 5], [8, 12], [15, 24], [25, 26]]
    expected = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    assert interval_intersection(first_list, second_list) == expected


def test_interval_intersection_no_overlap():
    assert interval_intersection([[1, 2]], [[3, 4]]) == []


def test_have_conflict_touching_at_boundary():
    assert have_conflict(["01:15", "02:00"], ["02:00", "03:00"]) is True


def test_have_conflict_overlapping():
    assert have_conflict(["01:00", "02:00"], ["01:20", "03:00"]) is True


def test_have_conflict_disjoint():
    assert have_conflict(["10:00", "11:00"], ["14:00", "15:00"]) is False


def test_partition_labels_normal():
    assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]


def test_partition_labels_single_part():
    assert partition_labels("eccbbbbdec") == [10]
