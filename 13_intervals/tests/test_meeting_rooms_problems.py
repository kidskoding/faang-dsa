from problem_set.meeting_rooms_problems import (
    MyCalendar,
    MyCalendarTwo,
    MyCalendarThree,
    can_attend_meetings,
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
