from problem_set.stack_problems import (
    MinStack,
    calculate,
    calculate_ii,
    decode_string,
    eval_rpn,
    is_valid,
)


def test_is_valid_empty_string():
    assert is_valid("") is True


def test_is_valid_single_pair():
    assert is_valid("()") is True


def test_is_valid_mixed_brackets_true():
    assert is_valid("()[]{}") is True


def test_is_valid_nested_true():
    assert is_valid("{[]}") is True


def test_is_valid_unmatched_closing_false():
    assert is_valid("(]") is False


def test_is_valid_unclosed_opening_false():
    assert is_valid("(()") is False


def test_min_stack_tracks_running_minimum():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.get_min() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.get_min() == -2


def test_min_stack_single_element():
    stack = MinStack()
    stack.push(5)
    assert stack.top() == 5
    assert stack.get_min() == 5


def test_eval_rpn_addition_subtraction():
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9


def test_eval_rpn_division_truncates_toward_zero():
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6


def test_eval_rpn_single_token():
    assert eval_rpn(["42"]) == 42


def test_decode_string_simple_repeat():
    assert decode_string("3[a]2[bc]") == "aaabcbc"


def test_decode_string_nested():
    assert decode_string("3[a2[c]]") == "accaccacc"


def test_decode_string_no_brackets():
    assert decode_string("abc") == "abc"


def test_calculate_ii_mixed_precedence():
    assert calculate_ii("3+2*2") == 7


def test_calculate_ii_division_truncates():
    assert calculate_ii(" 3/2 ") == 1


def test_calculate_ii_single_number():
    assert calculate_ii("42") == 42


def test_calculate_with_parentheses():
    assert calculate("(1+(4+5+2)-3)+(6+8)") == 23


def test_calculate_simple_addition():
    assert calculate("1 + 1") == 2


def test_calculate_leading_negative():
    assert calculate("-(2+3)") == -5
