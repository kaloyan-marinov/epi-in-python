"""
A string is said to be an arithmetical expression in Reverse Polish Notation (RPN) if:

    (1) it is a single digit or a sequence of digits, prefixed with an optional "-"
        (e.g. "6", "123", "-42"), or

    (2) it is of the form "A, B, o", where
        A and B are RPN expressions and
        "o" is one of +, -, *, /

For example, the following strings satisfy those rules:

    1729
    3,4,+,2,*,1,+
    1,1,+,-2,*
    -641,6,/,28,/

An RPN can be evaluated uniquely to an integer,
which is determined [iteratively] according to above-described rules,
with division being integer division.
"""


from typing import List


def evaluate(expression: str) -> int:
    """
    The `expression` represents a string in Reverse Polish Notation.

    Assume that the operands to division are always positive.

    Compute the integer that the `expression` evaluates to.

    For example, if the `expression` is
        3,4,+,2,*,1,+
    this function should return the value of (3 + 4) * 2 + 1 = 15

    time:  O(n)
           where n := len(expression)
    """

    operator_symbol_2_function = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x // y,
    }

    integers: List[int] = []
    for token in expression.split(","):
        if token not in operator_symbol_2_function:
            integers.append(int(token))
        else:
            # NB: The order of defining & using `a` and `b` is important!
            b = integers.pop()
            a = integers.pop()
            r = operator_symbol_2_function[token](a, b)

            integers.append(r)

    return integers[0]
