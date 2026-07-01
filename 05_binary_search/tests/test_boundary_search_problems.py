from problem_set.boundary_search_problems import (
    TimeMap,
    find_closest_elements,
    find_peak_element,
    first_bad_version,
    search_range,
)


def _bad_version_factory(first_bad: int):
    def is_bad_version(version: int) -> bool:
        return version >= first_bad

    return is_bad_version


def test_first_bad_version_middle():
    assert first_bad_version(5, _bad_version_factory(4)) == 4


def test_first_bad_version_first():
    assert first_bad_version(5, _bad_version_factory(1)) == 1


def test_first_bad_version_last():
    assert first_bad_version(5, _bad_version_factory(5)) == 5


def test_first_bad_version_single():
    assert first_bad_version(1, _bad_version_factory(1)) == 1


def test_search_range_found():
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]


def test_search_range_not_found():
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]


def test_search_range_empty():
    assert search_range([], 0) == [-1, -1]


def test_search_range_single_found():
    assert search_range([5], 5) == [0, 0]


def test_search_range_single_missing():
    assert search_range([5], 3) == [-1, -1]


def test_search_range_all_same():
    assert search_range([2, 2, 2, 2], 2) == [0, 3]


def test_find_peak_element_middle():
    result = find_peak_element([1, 2, 3, 1])
    assert result == 2


def test_find_peak_element_descending():
    result = find_peak_element([3, 2, 1])
    assert result == 0


def test_find_peak_element_ascending():
    result = find_peak_element([1, 2, 3])
    assert result == 2


def test_find_peak_element_single():
    assert find_peak_element([1]) == 0


def test_find_peak_element_two_elements():
    result = find_peak_element([1, 2])
    assert result == 1


def test_find_closest_elements_middle_window():
    assert find_closest_elements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]


def test_find_closest_elements_left_edge():
    assert find_closest_elements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]


def test_find_closest_elements_right_edge():
    assert find_closest_elements([1, 2, 3, 4, 5], 4, 6) == [2, 3, 4, 5]


def test_find_closest_elements_k_equals_length():
    assert find_closest_elements([1, 2, 3], 3, 2) == [1, 2, 3]


def test_find_closest_elements_single_element():
    assert find_closest_elements([1], 1, 5) == [1]


def test_time_map_get_exact_and_earlier_timestamp():
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)
    assert time_map.get("foo", 1) == "bar"
    assert time_map.get("foo", 3) == "bar"


def test_time_map_get_before_first_set():
    time_map = TimeMap()
    time_map.set("foo", "bar", 5)
    assert time_map.get("foo", 2) == ""


def test_time_map_get_latest_before_timestamp():
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)
    time_map.set("foo", "bar2", 4)
    assert time_map.get("foo", 4) == "bar2"
    assert time_map.get("foo", 5) == "bar2"
    assert time_map.get("foo", 3) == "bar"


def test_time_map_get_missing_key():
    time_map = TimeMap()
    assert time_map.get("missing", 1) == ""
