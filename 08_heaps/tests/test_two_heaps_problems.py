from problem_set.two_heaps_problems import (
    MedianFinder,
    find_maximized_capital,
    median_sliding_window,
)


def test_median_finder_odd_count():
    finder = MedianFinder()
    finder.add_num(1)
    finder.add_num(2)
    finder.add_num(3)
    assert finder.find_median() == 2


def test_median_finder_even_count():
    finder = MedianFinder()
    finder.add_num(1)
    finder.add_num(2)
    assert finder.find_median() == 1.5


def test_median_finder_single_value():
    finder = MedianFinder()
    finder.add_num(5)
    assert finder.find_median() == 5


def test_find_maximized_capital_normal():
    assert find_maximized_capital(2, 0, [1, 2, 3], [0, 1, 1]) == 4


def test_find_maximized_capital_no_affordable_project():
    assert find_maximized_capital(1, 0, [5], [1]) == 0


def test_find_maximized_capital_single_project():
    assert find_maximized_capital(1, 0, [1], [0]) == 1


def test_median_sliding_window_normal():
    result = median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
    assert result == [1, -1, -1, 3, 5, 6]


def test_median_sliding_window_size_one():
    assert median_sliding_window([1, 2, 3], 1) == [1, 2, 3]


def test_median_sliding_window_even_window():
    result = median_sliding_window([1, 2, 3, 4], 2)
    assert result == [1.5, 2.5, 3.5]
