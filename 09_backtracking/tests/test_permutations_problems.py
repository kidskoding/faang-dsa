from problem_set.permutations_problems import (
    partition,
    permute,
    permute_unique,
    restore_ip_addresses,
)


def to_sorted_lists(result: list[list]) -> list[tuple]:
    return sorted(tuple(group) for group in result)


def test_permute_single_element():
    assert permute([1]) == [[1]]


def test_permute_normal():
    assert to_sorted_lists(permute([1, 2, 3])) == to_sorted_lists(
        [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]
    )


def test_permute_unique_all_same():
    assert permute_unique([1, 1]) == [[1, 1]]


def test_permute_unique_normal():
    assert to_sorted_lists(permute_unique([1, 1, 2])) == to_sorted_lists(
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    )


def test_partition_single_char():
    assert partition("a") == [["a"]]


def test_partition_normal():
    assert to_sorted_lists(partition("aab")) == to_sorted_lists(
        [["a", "a", "b"], ["aa", "b"]]
    )


def test_partition_no_palindromic_split_needed():
    assert partition("") == [[]]


def test_restore_ip_addresses_normal():
    assert sorted(restore_ip_addresses("25525511135")) == sorted(
        ["255.255.11.135", "255.255.111.35"]
    )


def test_restore_ip_addresses_too_short():
    assert restore_ip_addresses("1") == []


def test_restore_ip_addresses_all_zeros():
    assert restore_ip_addresses("0000") == ["0.0.0.0"]
