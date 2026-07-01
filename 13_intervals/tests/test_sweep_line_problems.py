from problem_set.sweep_line_problems import (
    RangeModule,
    car_pooling,
    employee_free_time,
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
