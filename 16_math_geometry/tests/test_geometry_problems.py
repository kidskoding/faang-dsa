from problem_set.geometry_problems import (
    is_rectangle_overlap,
    max_points,
    min_area_rect,
    valid_square,
)


def test_valid_square_true():
    assert valid_square([0, 0], [1, 1], [1, 0], [0, 1]) is True


def test_valid_square_false_not_square():
    assert valid_square([0, 0], [1, 1], [1, 0], [0, 12]) is False


def test_valid_square_duplicate_points():
    assert valid_square([0, 0], [0, 0], [1, 0], [0, 1]) is False


def test_is_rectangle_overlap_true():
    assert is_rectangle_overlap([0, 0, 2, 2], [1, 1, 3, 3]) is True


def test_is_rectangle_overlap_false_touching_edge():
    assert is_rectangle_overlap([0, 0, 1, 1], [1, 0, 2, 1]) is False


def test_is_rectangle_overlap_false_disjoint():
    assert is_rectangle_overlap([0, 0, 1, 1], [2, 2, 3, 3]) is False


def test_min_area_rect_normal():
    points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
    assert min_area_rect(points) == 4


def test_min_area_rect_no_rectangle():
    points = [[1, 1], [1, 3], [3, 1]]
    assert min_area_rect(points) == 0


def test_min_area_rect_empty():
    assert min_area_rect([]) == 0


def test_max_points_collinear():
    points = [[1, 1], [2, 2], [3, 3]]
    assert max_points(points) == 3


def test_max_points_single_point():
    assert max_points([[0, 0]]) == 1


def test_max_points_vertical_line():
    points = [[1, 1], [1, 2], [1, 3], [2, 5]]
    assert max_points(points) == 3
