from problem_set.weighted_shortest_paths_problems import (
    calc_equation,
    find_cheapest_price,
    find_the_city,
    has_path,
    max_probability,
    min_cost,
    minimum_cost,
    minimum_effort_path,
    minimum_obstacles,
    network_delay_time,
    second_minimum_time,
    shortest_distance,
    swim_in_water,
)


def test_calc_equation_normal_case():
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    assert calc_equation(equations, values, queries) == [6.0, 0.5, -1.0, 1.0, -1.0]


def test_calc_equation_no_queries_answerable():
    assert calc_equation([["a", "b"]], [1.0], [["c", "d"]]) == [-1.0]


def test_network_delay_time_normal_case():
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]

    assert network_delay_time(times, 4, 2) == 2


def test_network_delay_time_unreachable_node():
    assert network_delay_time([[1, 2, 1]], 2, 2) == -1


def test_network_delay_time_single_node():
    assert network_delay_time([], 1, 1) == 0


def test_find_cheapest_price_normal_case():
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]

    assert find_cheapest_price(3, flights, 0, 2, 1) == 200


def test_find_cheapest_price_no_valid_route():
    assert find_cheapest_price(3, [[0, 1, 100]], 0, 2, 1) == -1


def test_minimum_effort_path_normal_case():
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]

    assert minimum_effort_path(heights) == 2


def test_minimum_effort_path_single_cell():
    assert minimum_effort_path([[5]]) == 0


def test_max_probability_normal_case():
    edges = [[0, 1], [1, 2], [0, 2]]
    succ_prob = [0.5, 0.5, 0.2]

    assert max_probability(3, edges, succ_prob, 0, 2) == 0.25


def test_max_probability_no_path():
    assert max_probability(3, [[0, 1]], [0.5], 0, 2) == 0.0


def test_has_path_true():
    maze = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
    ]

    assert has_path(maze, [0, 4], [4, 4]) is True


def test_has_path_false():
    maze = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
    ]

    assert has_path(maze, [0, 4], [3, 2]) is False


def test_shortest_distance_normal_case():
    maze = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
    ]

    assert shortest_distance(maze, [0, 4], [4, 4]) == 12


def test_shortest_distance_unreachable():
    maze = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
    ]

    assert shortest_distance(maze, [0, 4], [3, 2]) == -1


def test_find_the_city_normal_case():
    edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]

    assert find_the_city(4, edges, 4) == 3


def test_find_the_city_all_reachable_picks_highest_index():
    edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]

    assert find_the_city(5, edges, 2) == 0


def test_minimum_obstacles_normal_case():
    grid = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]

    assert minimum_obstacles(grid) == 2


def test_minimum_obstacles_no_obstacles():
    assert minimum_obstacles([[0, 0], [0, 0]]) == 0


def test_min_cost_normal_case():
    grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]

    assert min_cost(grid) == 3


def test_min_cost_no_changes_needed():
    assert min_cost([[1, 1], [1, 1]]) == 0


def test_swim_in_water_normal_case():
    assert swim_in_water([[0, 2], [1, 3]]) == 3


def test_swim_in_water_single_cell():
    assert swim_in_water([[0]]) == 0


def test_minimum_cost_normal_case():
    edges = [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]]
    passing_fees = [5, 1, 2, 20, 20, 3]

    assert minimum_cost(30, edges, passing_fees) == 11


def test_minimum_cost_no_valid_route():
    assert minimum_cost(5, [[0, 1, 10]], [0, 5]) == -1


def test_second_minimum_time_normal_case():
    edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]

    assert second_minimum_time(5, edges, 3, 5) == 13


def test_second_minimum_time_two_nodes():
    assert second_minimum_time(2, [[1, 2]], 3, 2) == 11
