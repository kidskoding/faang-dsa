from problem_set.interval_greedy_problems import (
    candy,
    erase_overlap_intervals,
    find_min_arrow_shots,
    least_interval,
    num_rescue_boats,
    partition_labels,
    reconstruct_queue,
)


def test_erase_overlap_intervals_normal():
    assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1


def test_erase_overlap_intervals_no_overlap():
    assert erase_overlap_intervals([[1, 2], [2, 3]]) == 0


def test_erase_overlap_intervals_single():
    assert erase_overlap_intervals([[1, 2]]) == 0


def test_erase_overlap_intervals_empty():
    assert erase_overlap_intervals([]) == 0


def test_partition_labels_normal():
    assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]


def test_partition_labels_all_unique():
    assert partition_labels("abcd") == [1, 1, 1, 1]


def test_partition_labels_single_char():
    assert partition_labels("a") == [1]


def test_partition_labels_empty():
    assert partition_labels("") == []


def test_candy_normal():
    assert candy([1, 0, 2]) == 5


def test_candy_flat_ratings():
    assert candy([1, 1, 1]) == 3


def test_candy_increasing():
    assert candy([1, 2, 3]) == 6


def test_candy_single_child():
    assert candy([5]) == 1


def test_candy_empty():
    assert candy([]) == 0


def test_reconstruct_queue_normal():
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    expected = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    assert reconstruct_queue(people) == expected


def test_reconstruct_queue_single_person():
    assert reconstruct_queue([[6, 0]]) == [[6, 0]]


def test_reconstruct_queue_empty():
    assert reconstruct_queue([]) == []


def test_find_min_arrow_shots_normal():
    assert find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2


def test_find_min_arrow_shots_no_overlap():
    assert find_min_arrow_shots([[1, 2], [3, 4], [5, 6]]) == 3


def test_find_min_arrow_shots_single_balloon():
    assert find_min_arrow_shots([[1, 2]]) == 1


def test_find_min_arrow_shots_empty():
    assert find_min_arrow_shots([]) == 0


def test_num_rescue_boats_normal():
    assert num_rescue_boats([3, 2, 2, 1], 3) == 3


def test_num_rescue_boats_all_pair():
    assert num_rescue_boats([3, 5, 3, 4], 5) == 4


def test_num_rescue_boats_single_person():
    assert num_rescue_boats([5], 5) == 1


def test_num_rescue_boats_empty():
    assert num_rescue_boats([], 5) == 0


def test_least_interval_needs_idle():
    assert least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8


def test_least_interval_no_idle_needed():
    assert least_interval(["A", "A", "A", "B", "B", "B"], 0) == 6


def test_least_interval_single_task_type():
    assert least_interval(["A", "A", "A"], 2) == 7


def test_least_interval_empty():
    assert least_interval([], 2) == 0
