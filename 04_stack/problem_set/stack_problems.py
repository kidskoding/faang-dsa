class MinStack:
    # Problem 2: Min Stack
    # Key idea: track the running minimum alongside each push.

    def __init__(self) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def push(self, val: int) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def pop(self) -> None:
        # Time:
        # Space:
        raise NotImplementedError

    def top(self) -> int:
        # Time:
        # Space:
        raise NotImplementedError

    def get_min(self) -> int:
        # Time:
        # Space:
        raise NotImplementedError


def is_valid(s: str) -> bool:
    # Problem 1: Valid Parentheses
    # Key idea: push opening brackets, pop and match on a closing bracket.
    # Time:
    # Space:

    raise NotImplementedError


def eval_rpn(tokens: list[str]) -> int:
    # Problem 6: Evaluate Reverse Polish Notation
    # Key idea: push operands, pop two and apply the operator when one appears.
    # Time:
    # Space:

    raise NotImplementedError


def decode_string(s: str) -> str:
    # Problem 7: Decode String
    # Key idea: stack of (count, partial string) to resolve nested k[...] brackets.
    # Time:
    # Space:

    raise NotImplementedError


def calculate_ii(s: str) -> int:
    # Problem 8: Basic Calculator II
    # Key idea: stack resolves */ immediately, leaves +/- terms for a final sum.
    # Time:
    # Space:

    raise NotImplementedError


def calculate(s: str) -> int:
    # Problem 18: Basic Calculator
    # Key idea: stack holds sign and running result across nested parentheses.
    # Time:
    # Space:

    raise NotImplementedError
