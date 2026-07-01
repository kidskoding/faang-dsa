from problem_set.heap_basics_problems import (
    KthLargest,
    k_closest_points,
    kth_largest_element,
    last_stone_weight,
    meeting_rooms_ii,
)


def test_kth_largest_element_normal():
    assert kth_largest_element([3, 2, 1, 5, 6, 4], 2) == 5


def test_kth_largest_element_with_duplicates():
    assert kth_largest_element([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


def test_kth_largest_element_single():
    assert kth_largest_element([1], 1) == 1


def test_last_stone_weight_normal():
    assert last_stone_weight([2, 7, 4, 1, 8, 1]) == 1


def test_last_stone_weight_all_destroyed():
    assert last_stone_weight([2, 2]) == 0


def test_last_stone_weight_single():
    assert last_stone_weight([5]) == 5


def test_last_stone_weight_empty():
    assert last_stone_weight([]) == 0


def test_k_closest_points_normal():
    result = k_closest_points([[1, 3], [-2, 2]], 1)
    assert result == [[-2, 2]]


def test_k_closest_points_all_points():
    points = [[3, 3], [5, -1], [-2, 4]]
    result = k_closest_points(points, 2)
    assert sorted(result) == sorted([[3, 3], [-2, 4]])


def test_k_closest_points_single():
    assert k_closest_points([[0, 1]], 1) == [[0, 1]]


def test_kth_largest_stream_basic():
    kth = KthLargest(3, [4, 5, 8, 2])
    assert kth.add(3) == 4
    assert kth.add(5) == 5
    assert kth.add(10) == 5
    assert kth.add(9) == 8
    assert kth.add(4) == 8


def test_kth_largest_stream_empty_initial():
    kth = KthLargest(1, [])
    assert kth.add(-3) == -3
    assert kth.add(-2) == -2


def test_meeting_rooms_ii_normal():
    assert meeting_rooms_ii([[0, 30], [5, 10], [15, 20]]) == 2


def test_meeting_rooms_ii_no_overlap():
    assert meeting_rooms_ii([[7, 10], [2, 4]]) == 1


def test_meeting_rooms_ii_empty():
    assert meeting_rooms_ii([]) == 0


def test_meeting_rooms_ii_single():
    assert meeting_rooms_ii([[1, 5]]) == 1
