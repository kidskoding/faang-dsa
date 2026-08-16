from problem_set.k_way_merge_problems import (
    ListNode,
    Twitter,
    employee_free_time,
    k_smallest_pairs,
    kth_smallest,
    merge_k_lists,
    nth_super_ugly_number,
    smallest_range,
)


def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    curr = dummy
    for value in values:
        curr.next = ListNode(value)
        curr = curr.next
    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def test_merge_k_lists_normal():
    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    assert to_list(merge_k_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_merge_k_lists_empty_input():
    assert merge_k_lists([]) is None


def test_merge_k_lists_with_empty_lists():
    assert to_list(merge_k_lists([None, build_list([1]), None])) == [1]


def test_smallest_range_normal():
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    assert smallest_range(nums) == [20, 24]


def test_smallest_range_single_list():
    assert smallest_range([[1, 2, 3]]) == [1, 1]


def test_smallest_range_all_same_value():
    assert smallest_range([[1, 1], [1, 1]]) == [1, 1]


def test_twitter_feed_most_recent_first():
    twitter = Twitter()
    twitter.post_tweet(1, 5)
    assert twitter.get_news_feed(1) == [5]
    twitter.follow(1, 2)
    twitter.post_tweet(2, 6)
    assert twitter.get_news_feed(1) == [6, 5]
    twitter.unfollow(1, 2)
    assert twitter.get_news_feed(1) == [5]


def test_twitter_feed_caps_at_ten():
    twitter = Twitter()
    for tweet_id in range(15):
        twitter.post_tweet(1, tweet_id)
    feed = twitter.get_news_feed(1)
    assert len(feed) == 10
    assert feed[0] == 14


def test_twitter_feed_empty_when_no_posts():
    twitter = Twitter()
    assert twitter.get_news_feed(1) == []


def test_employee_free_time_normal():
    schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
    assert employee_free_time(schedule) == [[3, 4]]


def test_employee_free_time_no_gaps():
    schedule = [[[1, 5]], [[2, 6]]]
    assert employee_free_time(schedule) == []


def test_employee_free_time_single_employee():
    schedule = [[[1, 2], [4, 5], [7, 8]]]
    assert employee_free_time(schedule) == [[2, 4], [5, 7]]


def test_k_smallest_pairs_normal():
    assert k_smallest_pairs([1, 7, 11], [2, 4, 6], 3) == [[1, 2], [1, 4], [1, 6]]


def test_k_smallest_pairs_with_duplicates():
    assert k_smallest_pairs([1, 1, 2], [1, 2, 3], 2) == [[1, 1], [1, 1]]


def test_k_smallest_pairs_empty_input():
    assert k_smallest_pairs([], [1, 2], 3) == []


def test_kth_smallest_normal():
    assert kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13


def test_kth_smallest_first():
    assert kth_smallest([[1, 2], [3, 4]], 1) == 1


def test_nth_super_ugly_number_normal():
    assert nth_super_ugly_number(12, [2, 7, 13, 19]) == 32


def test_nth_super_ugly_number_first_is_one():
    assert nth_super_ugly_number(1, [2, 3, 5]) == 1
