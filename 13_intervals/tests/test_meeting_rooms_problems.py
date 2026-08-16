from problem_set.meeting_rooms_problems import (
    MyCalendar,
    MyCalendarThree,
    MyCalendarTwo,
    can_attend_meetings,
    full_bloom_flowers,
    max_events,
    min_groups,
    min_interval,
    min_meeting_rooms,
    most_booked_room,
)


def test_can_attend_meetings_empty():
    assert can_attend_meetings([]) is True


def test_can_attend_meetings_no_overlap():
    assert can_attend_meetings([[0, 30], [35, 40]]) is True


def test_can_attend_meetings_true():
    assert can_attend_meetings([[7, 10], [2, 4]]) is True


def test_can_attend_meetings_false():
    assert can_attend_meetings([[0, 30], [5, 10], [15, 20]]) is False


def test_min_meeting_rooms_empty():
    assert min_meeting_rooms([]) == 0


def test_min_meeting_rooms_single_meeting():
    assert min_meeting_rooms([[1, 5]]) == 1


def test_min_meeting_rooms_normal():
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2


def test_min_meeting_rooms_back_to_back():
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1


def test_most_booked_room_normal():
    assert most_booked_room(2, [[0, 10], [1, 5], [2, 7], [3, 4]]) == 0


def test_most_booked_room_single_room():
    assert most_booked_room(1, [[1, 10]]) == 0


def test_my_calendar_accepts_non_overlapping():
    calendar = MyCalendar()
    assert calendar.book(10, 20) is True
    assert calendar.book(20, 30) is True


def test_my_calendar_rejects_overlap():
    calendar = MyCalendar()
    assert calendar.book(10, 20) is True
    assert calendar.book(15, 25) is False


def test_my_calendar_two_allows_double_book():
    calendar = MyCalendarTwo()
    assert calendar.book(10, 20) is True
    assert calendar.book(50, 60) is True
    assert calendar.book(10, 40) is True


def test_my_calendar_two_rejects_triple_book():
    calendar = MyCalendarTwo()
    calendar.book(10, 20)
    calendar.book(50, 60)
    calendar.book(10, 40)
    assert calendar.book(5, 15) is False
    assert calendar.book(5, 10) is True


def test_my_calendar_three_tracks_max_k_booking():
    calendar = MyCalendarThree()
    assert calendar.book(10, 20) == 1
    assert calendar.book(50, 60) == 1
    assert calendar.book(10, 40) == 2
    assert calendar.book(5, 15) == 3
    assert calendar.book(5, 10) == 3


def test_max_events_one_per_day():
    assert max_events([[1, 2], [2, 3], [3, 4]]) == 3


def test_max_events_with_duplicate_window():
    assert max_events([[1, 2], [2, 3], [3, 4], [1, 2]]) == 4


def test_min_groups_overlapping():
    assert min_groups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]) == 3


def test_min_groups_disjoint():
    assert min_groups([[1, 3], [5, 6], [8, 10], [11, 13]]) == 1


def test_min_interval_normal():
    assert min_interval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]) == [3, 3, 1, 4]


def test_min_interval_with_gap():
    intervals = [[2, 3], [2, 5], [1, 8], [20, 25]]
    assert min_interval(intervals, [2, 19, 5, 22]) == [2, -1, 4, 6]


def test_full_bloom_flowers_normal():
    flowers = [[1, 6], [3, 7], [9, 12], [4, 13]]
    assert full_bloom_flowers(flowers, [2, 3, 7, 11]) == [1, 2, 2, 2]


def test_full_bloom_flowers_repeated_queries():
    assert full_bloom_flowers([[1, 10], [3, 3]], [3, 3, 2]) == [2, 2, 1]
