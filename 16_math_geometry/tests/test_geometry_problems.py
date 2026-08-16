from problem_set.geometry_problems import (
    compute_area,
    is_rectangle_cover,
    is_rectangle_overlap,
    is_self_crossing,
    k_closest,
    largest_triangle_area,
    max_points,
    min_area_rect,
    outer_trees,
    rectangle_area,
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


def test_largest_triangle_area_normal():
    assert largest_triangle_area([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]) == 2.0


def test_largest_triangle_area_three_points():
    assert largest_triangle_area([[1, 0], [0, 0], [0, 1]]) == 0.5


def test_compute_area_overlapping():
    assert compute_area(-3, 0, 3, 4, 0, -1, 9, 2) == 45


def test_compute_area_identical_rectangles():
    assert compute_area(-2, -2, 2, 2, -2, -2, 2, 2) == 16


def test_k_closest_single_point():
    assert k_closest([[1, 3], [-2, 2]], 1) == [[-2, 2]]


def test_k_closest_two_points():
    assert sorted(k_closest([[3, 3], [5, -1], [-2, 4]], 2)) == sorted([[3, 3], [-2, 4]])


def test_is_self_crossing_true():
    assert is_self_crossing([2, 1, 1, 2]) is True


def test_is_self_crossing_spiral_out():
    assert is_self_crossing([1, 2, 3, 4]) is False


def test_is_self_crossing_square():
    assert is_self_crossing([1, 1, 1, 1]) is True


def test_outer_trees_normal():
    trees = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
    result = outer_trees(trees)

    assert sorted(result) == sorted([[1, 1], [2, 0], [2, 4], [3, 3], [4, 2]])


def test_outer_trees_collinear():
    result = outer_trees([[1, 2], [2, 2], [4, 2]])

    assert sorted(result) == sorted([[1, 2], [2, 2], [4, 2]])


def test_is_rectangle_cover_exact():
    rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
    assert is_rectangle_cover(rectangles) is True


def test_is_rectangle_cover_with_gap():
    rectangles = [[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]
    assert is_rectangle_cover(rectangles) is False


def test_rectangle_area_overlapping():
    assert rectangle_area([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]) == 6


def test_rectangle_area_takes_modulo():
    assert rectangle_area([[0, 0, 1000000000, 1000000000]]) == 49
