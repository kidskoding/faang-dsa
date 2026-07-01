from problem_set.kadane_problems import max_product_subarray, max_profit, max_subarray


def test_max_subarray_normal():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_subarray_all_negative():
    assert max_subarray([-3, -1, -2]) == -1


def test_max_subarray_single_element():
    assert max_subarray([5]) == 5


def test_max_profit_normal():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5


def test_max_profit_no_profit():
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_max_profit_single_price():
    assert max_profit([5]) == 0


def test_max_profit_empty():
    assert max_profit([]) == 0


def test_max_product_subarray_normal():
    assert max_product_subarray([2, 3, -2, 4]) == 6


def test_max_product_subarray_negative_flip():
    assert max_product_subarray([-2, 0, -1]) == 0


def test_max_product_subarray_single_element():
    assert max_product_subarray([-5]) == -5
