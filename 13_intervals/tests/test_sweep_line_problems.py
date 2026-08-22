from problem_set.sweep_line_problems import (
    RangeModule,
    amount_painted,
    car_pooling,
    corp_flight_bookings,
    employee_free_time,
    falling_squares,
    get_skyline,
    intersection_size_two,
    maximum_population,
    number_of_points,
    split_painting,
)


def test_employee_free_time_empty():
    assert employee_free_time([]) == []


def test_employee_free_time_normal():
    schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
    assert employee_free_time(schedule) == [[3, 4]]


def test_employee_free_time_no_gaps():
    schedule = [[[1, 5]], [[2, 3]], [[4, 6]]]
    assert employee_free_time(schedule) == []


def test_car_pooling_empty_trips():
    assert car_pooling([], 5) is True


def test_car_pooling_fits_capacity():
    assert car_pooling([[2, 1, 5], [3, 3, 7]], 4) is True


def test_car_pooling_exceeds_capacity():
    assert car_pooling([[2, 1, 5], [3, 3, 7]], 3) is False


def test_car_pooling_dropoff_frees_capacity():
    assert car_pooling([[3, 0, 2], [3, 2, 5]], 3) is True


def test_range_module_add_and_query():
    module = RangeModule()
    module.add_range(10, 20)
    assert module.query_range(10, 14) is True
    assert module.query_range(13, 21) is False


def test_range_module_remove_range():
    module = RangeModule()
    module.add_range(10, 20)
    module.remove_range(14, 16)
    assert module.query_range(10, 14) is True
    assert module.query_range(13, 17) is False
    assert module.query_range(16, 20) is True


def test_range_module_query_empty():
    module = RangeModule()
    assert module.query_range(1, 5) is False


def test_maximum_population_earliest_year_wins():
    assert maximum_population([[1993, 1999], [2000, 2010]]) == 1993


def test_maximum_population_overlapping_lives():
    logs = [[1950, 1961], [1960, 1971], [1970, 1981]]
    assert maximum_population(logs) == 1960


def test_number_of_points_overlapping():
    assert number_of_points([[3, 6], [1, 5], [4, 7]]) == 7


def test_number_of_points_disjoint():
    assert number_of_points([[1, 3], [5, 8]]) == 7


def test_corp_flight_bookings_normal():
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    assert corp_flight_bookings(bookings, 5) == [10, 55, 45, 25, 25]


def test_corp_flight_bookings_single_flight():
    assert corp_flight_bookings([[1, 2, 10], [2, 2, 15]], 2) == [10, 25]


def test_split_painting_overlapping_segments():
    assert split_painting([[1, 4, 5], [4, 7, 7], [1, 7, 9]]) == [[1, 4, 14], [4, 7, 16]]


def test_split_painting_partial_overlap():
    segments = [[1, 7, 9], [6, 8, 15], [8, 10, 7]]
    assert split_painting(segments) == [[1, 6, 9], [6, 7, 24], [7, 8, 15], [8, 10, 7]]


def test_get_skyline_normal():
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    assert get_skyline(buildings) == [
        [2, 10],
        [3, 15],
        [7, 12],
        [12, 0],
        [15, 10],
        [20, 8],
        [24, 0],
    ]


def test_intersection_size_two_chain():
    assert intersection_size_two([[1, 3], [3, 7], [8, 9]]) == 5


def test_intersection_size_two_nested():
    assert intersection_size_two([[1, 3], [1, 4], [2, 5], [3, 5]]) == 3


def test_falling_squares_stacking():
    assert falling_squares([[1, 2], [2, 3], [6, 1]]) == [2, 5, 5]


def test_falling_squares_no_overlap():
    assert falling_squares([[100, 100], [200, 100]]) == [100, 100]


def test_amount_painted_overlapping():
    assert amount_painted([[1, 4], [4, 7], [5, 8]]) == [3, 3, 1]


def test_amount_painted_out_of_order():
    assert amount_painted([[1, 4], [5, 8], [4, 7]]) == [3, 3, 1]


def test_get_skyline_single_building():
    assert get_skyline([[0, 2, 3]]) == [[0, 3], [2, 0]]


def test_get_skyline_nested_building():
    assert get_skyline([[0, 10, 5], [2, 4, 3]]) == [[0, 5], [10, 0]]
