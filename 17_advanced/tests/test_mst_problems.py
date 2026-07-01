from problem_set.mst_problems import (
    min_cost_connect_points,
    min_cost_connecting_cities,
    min_cost_to_supply_water,
)


def test_min_cost_connect_points_normal():
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    assert min_cost_connect_points(points) == 20


def test_min_cost_connect_points_two_points():
    assert min_cost_connect_points([[0, 0], [1, 1]]) == 2


def test_min_cost_connect_points_single_point():
    assert min_cost_connect_points([[3, 3]]) == 0


def test_min_cost_connecting_cities_normal():
    connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
    assert min_cost_connecting_cities(3, connections) == 6


def test_min_cost_connecting_cities_disconnected():
    connections = [[1, 2, 3], [3, 4, 4]]
    assert min_cost_connecting_cities(4, connections) == -1


def test_min_cost_connecting_cities_single_city():
    assert min_cost_connecting_cities(1, []) == 0


def test_min_cost_to_supply_water_normal():
    wells = [1, 2, 2]
    pipes = [[1, 2, 1], [2, 3, 1]]
    assert min_cost_to_supply_water(3, wells, pipes) == 3


def test_min_cost_to_supply_water_no_pipes_needed():
    assert min_cost_to_supply_water(2, [1, 1], []) == 2


def test_min_cost_to_supply_water_single_house():
    assert min_cost_to_supply_water(1, [5], []) == 5
