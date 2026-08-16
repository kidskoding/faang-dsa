from problem_set.heap_hards_problems import (
    get_skyline,
    kth_smallest_matrix_sum,
    max_performance,
    min_refuel_stops,
    mincost_to_hire_workers,
    network_delay_time,
    schedule_course,
    swim_in_water,
    trap_rain_water,
)


def test_trap_rain_water_normal():
    height_map = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
    assert trap_rain_water(height_map) == 4


def test_trap_rain_water_deep_basin():
    height_map = [
        [3, 3, 3, 3, 3],
        [3, 2, 2, 2, 3],
        [3, 2, 1, 2, 3],
        [3, 2, 2, 2, 3],
        [3, 3, 3, 3, 3],
    ]
    assert trap_rain_water(height_map) == 10


def test_mincost_to_hire_workers_normal():
    assert round(mincost_to_hire_workers([10, 20, 5], [70, 50, 30], 2), 5) == 105.0


def test_mincost_to_hire_workers_three_workers():
    cost = mincost_to_hire_workers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3)
    assert round(cost, 5) == 30.66667


def test_swim_in_water_small_grid():
    assert swim_in_water([[0, 2], [1, 3]]) == 3


def test_swim_in_water_larger_grid():
    grid = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6],
    ]
    assert swim_in_water(grid) == 16


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


def test_get_skyline_adjacent_same_height():
    assert get_skyline([[0, 2, 3], [2, 5, 3]]) == [[0, 3], [5, 0]]


def test_max_performance_two_engineers():
    assert max_performance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2) == 60


def test_max_performance_three_engineers():
    assert max_performance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3) == 68


def test_min_refuel_stops_normal():
    assert min_refuel_stops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]) == 2


def test_min_refuel_stops_unreachable():
    assert min_refuel_stops(100, 1, [[10, 100]]) == -1


def test_min_refuel_stops_no_stop_needed():
    assert min_refuel_stops(1, 1, []) == 0


def test_kth_smallest_matrix_sum_normal():
    assert kth_smallest_matrix_sum([[1, 3, 11], [2, 4, 6]], 5) == 7


def test_kth_smallest_matrix_sum_last():
    assert kth_smallest_matrix_sum([[1, 3, 11], [2, 4, 6]], 9) == 17


def test_schedule_course_normal():
    courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    assert schedule_course(courses) == 3


def test_schedule_course_single():
    assert schedule_course([[1, 2]]) == 1


def test_schedule_course_none_fit():
    assert schedule_course([[3, 2], [4, 3]]) == 0


def test_network_delay_time_reaches_all():
    assert network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2


def test_network_delay_time_unreachable():
    assert network_delay_time([[1, 2, 1]], 2, 2) == -1
