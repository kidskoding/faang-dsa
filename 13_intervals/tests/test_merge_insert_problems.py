from problem_set.merge_insert_problems import (
    SummaryRanges,
    erase_overlap_intervals,
    insert,
    merge,
    remove_covered_intervals,
)


def test_merge_empty():
    assert merge([]) == []


def test_merge_single_interval():
    assert merge([[1, 3]]) == [[1, 3]]


def test_merge_normal():
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_merge_touching_intervals():
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]


def test_insert_into_empty():
    assert insert([], [5, 7]) == [[5, 7]]


def test_insert_no_overlap():
    assert insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 4]) == [
        [1, 2],
        [3, 5],
        [6, 7],
        [8, 10],
        [12, 16],
    ]


def test_insert_merges_overlap():
    assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]


def test_erase_overlap_intervals_empty():
    assert erase_overlap_intervals([]) == 0


def test_erase_overlap_intervals_no_overlap():
    assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4]]) == 0


def test_erase_overlap_intervals_normal():
    assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1


def test_summary_ranges_stream_single_value():
    ranges = SummaryRanges()
    ranges.add_num(1)
    assert ranges.get_intervals() == [[1, 1]]


def test_summary_ranges_stream_merges_consecutive():
    ranges = SummaryRanges()
    for value in (1, 3, 7, 2, 6):
        ranges.add_num(value)
    assert ranges.get_intervals() == [[1, 3], [6, 7]]


def test_summary_ranges_stream_bridges_gap():
    ranges = SummaryRanges()
    for value in (1, 3, 7, 2, 6):
        ranges.add_num(value)
    ranges.add_num(4)
    assert ranges.get_intervals() == [[1, 4], [6, 7]]


def test_remove_covered_intervals_normal():
    assert remove_covered_intervals([[1, 4], [3, 6], [2, 8]]) == 2


def test_remove_covered_intervals_nested():
    assert remove_covered_intervals([[1, 4], [2, 3]]) == 1
