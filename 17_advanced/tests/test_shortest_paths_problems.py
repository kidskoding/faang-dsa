from problem_set.shortest_paths_problems import (
    count_paths,
    find_cheapest_price,
    find_the_city,
)


def test_find_cheapest_price_within_stops():
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    assert find_cheapest_price(3, flights, 0, 2, 1) == 200


def test_find_cheapest_price_no_route():
    flights = [[0, 1, 100]]
    assert find_cheapest_price(3, flights, 0, 2, 1) == -1


def test_find_cheapest_price_direct_is_cheapest():
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 100]]
    assert find_cheapest_price(3, flights, 0, 2, 0) == 100


def test_count_paths_single_shortest():
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
    assert count_paths(7, roads) == 4


def test_count_paths_single_node():
    assert count_paths(1, []) == 1


def test_count_paths_two_equal_routes():
    roads = [[0, 1, 1], [0, 2, 1], [1, 3, 1], [2, 3, 1]]
    assert count_paths(4, roads) == 2


def test_find_the_city_prefers_farthest_threshold():
    edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    assert find_the_city(4, edges, 4) == 3


def test_find_the_city_tiebreak_largest_index():
    edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
    assert find_the_city(5, edges, 2) == 0


def test_find_the_city_minimal_graph():
    assert find_the_city(2, [[0, 1, 1]], 1) in (0, 1)
