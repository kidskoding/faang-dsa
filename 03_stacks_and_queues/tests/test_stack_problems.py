from problem_set.stack_problems import (
    FreqStack,
    MinStack,
    calculate,
    calculate_ii,
    count_of_atoms,
    decode_string,
    eval_rpn,
    is_valid,
    longest_valid_parentheses,
    min_remove_to_make_valid,
    remove_duplicates,
    remove_duplicates_ii,
    simplify_path,
    validate_stack_sequences,
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


def test_remove_duplicates_normal():
    assert remove_duplicates("abbaca") == "ca"


def test_remove_duplicates_inner_pair():
    assert remove_duplicates("azxxzy") == "ay"


def test_simplify_path_trailing_slash():
    assert simplify_path("/home/") == "/home"


def test_simplify_path_above_root():
    assert simplify_path("/../") == "/"


def test_simplify_path_double_slash():
    assert simplify_path("/home//foo/") == "/home/foo"


def test_simplify_path_dots():
    assert simplify_path("/a/./b/../../c/") == "/c"


def test_min_remove_to_make_valid_extra_close():
    assert min_remove_to_make_valid("lee(t(c)o)de)") == "lee(t(c)o)de"


def test_min_remove_to_make_valid_leading_close():
    assert min_remove_to_make_valid("a)b(c)d") == "ab(c)d"


def test_min_remove_to_make_valid_removes_everything():
    assert min_remove_to_make_valid("))((") == ""


def test_validate_stack_sequences_valid():
    assert validate_stack_sequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) is True


def test_validate_stack_sequences_invalid():
    assert validate_stack_sequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) is False


def test_remove_duplicates_ii_no_removal():
    assert remove_duplicates_ii("abcd", 2) == "abcd"


def test_remove_duplicates_ii_cascading():
    assert remove_duplicates_ii("deeedbbcccbdaa", 3) == "aa"


def test_remove_duplicates_ii_pairs():
    assert remove_duplicates_ii("pbbcggttciiippooaais", 2) == "ps"


def test_count_of_atoms_simple():
    assert count_of_atoms("H2O") == "H2O"


def test_count_of_atoms_with_group():
    assert count_of_atoms("Mg(OH)2") == "H2MgO2"


def test_count_of_atoms_nested_groups():
    assert count_of_atoms("K4(ON(SO3)2)2") == "K4N2O14S4"


def test_freq_stack_pops_most_frequent_then_most_recent():
    stack = FreqStack()
    for value in [5, 7, 5, 7, 4, 5]:
        stack.push(value)

    assert stack.pop() == 5
    assert stack.pop() == 7
    assert stack.pop() == 5
    assert stack.pop() == 4


def test_longest_valid_parentheses_partial():
    assert longest_valid_parentheses("(()") == 2


def test_longest_valid_parentheses_normal():
    assert longest_valid_parentheses(")()())") == 4


def test_longest_valid_parentheses_empty():
    assert longest_valid_parentheses("") == 0
